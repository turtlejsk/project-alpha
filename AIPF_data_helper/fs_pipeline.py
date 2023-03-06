import logging
import multiprocessing
import pandas as pd
import data_utils.preprocessing_util as prep
import data_utils.common_util as comm
import data_utils.feature_selection_util as fs
import datetime as dt

# 전처리 파이프라인

# ranksum 파일 저장 경로
path_fs = ''

dt_format = '%Y-%m-%d'
run_date = '2023-03-06'

target_name = 'USDKRW'
data_start_date = '2015-01-01'
data_end_date = run_date
data_range =  pd.date_range(start = data_start_date, end = data_end_date, freq = 'b').strftime(dt_format)
today_real = dt.datetime.today().strftime(dt_format)

target = comm.get_target(target_name)

logging.info('전처리 시작')
target_files : list[str] = ['INT_DAILY', 'INT_DMPT']

date_dict = dict(str, str)
date_dict['miss_start_date'] = ''
date_dict['miss_end_date'] = ''
date_dict['data_start_date'] = data_start_date
date_dict['data_end_date'] = data_end_date

cutoff_dict : dict(str, float)
cutoff_dict['miss_cutoff'] = 0
cutoff_dict['mod_cutoff'] = 0
cutoff_dict['skew_cutoff'] = 0
cutoff_dict['kurt_cutoff'] = 0
cutoff_dict['skb_cutoff'] = 0
args_list = []

for target_file in target_files:
    args = dict()
    args['path_file'] = ''
    args['freq'] = ''
    args['date_dict'] = date_dict
    args['cutoff_dict'] = cutoff_dict
    args_list.append(args)

pool = multiprocessing.pool()
preprocess_results : list[pd.DataFrame] = pool.map(prep.preprocess, args_list)

df_whole = pd.DataFrame(index = data_range)
# 전처리 결과 병합
for result in preprocess_results:
    df_whole = pd.merge(df_whole, result, left_index = True, right_index = True, how = 'outer')

# 변수 별로 어떤 파생변수 만들어야하는지 구분할 수 있도록 해주는 DataFrame
feat_src_map = pd.DataFrame()

df_whole, df_ti = prep.generate_ti(df_whole, feat_src_map)

df_whole_ti = pd.merge(df_whole, df_ti, left_index = True, right_index = True, how = 'outer')
df_whole_log = prep.log_trans(df_whole_ti, cutoff_dict)

df_whole_rm_outl = prep.remove_outlier_secondary(df_whole_log)
df_whole_scaled = prep.scale_daily(df_whole_rm_outl, run_date)


df_scaled_org = df_whole_scaled.loc[:,df_whole.columns]
df_scaled_ti = df_whole_scaled.loc[:,df_whole_ti.columns]

shift_len_list = [20, 60, 120]
for shift_len in shift_len_list:
    target_shift = target.shift(-shift_len)
    df_scaled_org_with_target = pd.merge(df_scaled_org, target_shift, left_index = True, right_index = True, how = 'left')
    skb_score = fs.get_skb_score(df_scaled_org_with_target)
    
    df_skb_result = fs.filter_skb_result(df_scaled_org, df_scaled_ti, skb_score, cutoff_dict)
    df_skb_result_with_target = pd.merge(df_skb_result, target_shift, left_index = True, right_index = True, how = 'left')
    
    ranksum_result = fs.get_ranksum(df_skb_result_with_target, target_name)
    df_rs = df_skb_result_with_target.loc[:,ranksum_result]
    df_leadlag_result = fs.lead_lag_analysis(df_rs, ranksum_result, shift_len)