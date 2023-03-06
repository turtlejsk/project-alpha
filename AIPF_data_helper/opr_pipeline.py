import logging
import multiprocessing
import pandas as pd
import data_utils.preprocessing_util as prep
import data_utils.common_util as comm
import datetime as dt

# 전처리 파이프라인

# ranksum 파일 저장 경로
path_fs = ''

dt_format = '%Y-%m-%d'
run_date = '2023-03-06'

data_start_date = '2015-01-01'
data_end_date = run_date
data_range =  pd.date_range(start = data_start_date, end = data_end_date, freq = 'b').strftime(dt_format)

today_real = dt.datetime.today().strftime(dt_format)


logging.info('전처리 시작')
target_files : list[str] = ['INT_DAILY', 'INT_DMPT']

args_list = []

for target_file in target_files:
    args = dict()
    args['path_file'] = ''
    args['freq'] = ''
    
    date_dict = dict(str, str)
    date_dict['miss_start_date'] = ''
    date_dict['miss_end_date'] = ''
    date_dict['data_start_date'] = data_start_date
    date_dict['data_end_date'] = data_end_date
    
    args['date_dict'] = date_dict
    
    cutoff_dict : dict(str, float)
    cutoff_dict['miss_cutoff'] = 0
    cutoff_dict['mod_cutoff'] = 0
    
    args['cutoff_dict'] = cutoff_dict
    args_list.append(args)

pool = multiprocessing.pool()
preprocess_results : list[pd.DataFrame] = pool.map(prep.preprocess, args_list)

rs_20 = comm.get_ranksum(path_fs, run_date, 20)
rs_60 = comm.get_ranksum(path_fs, run_date, 60)
rs_120 = comm.get_ranksum(path_fs, run_date, 120)

df_whole = pd.DataFrame(index = data_range)
# 전처리 결과 병합
for result in preprocess_results:
    imp = [] # 당일 배치에 필요한 중요변수만 가져오기
    result_rs = result.loc[:, imp]
    df_whole = pd.merge(df_whole, result_rs, left_index = True, right_index = True, how = 'outer')

# 변수 별로 어떤 파생변수 만들어야하는지 구분할 수 있도록 해주는 DataFrame
feat_src_map = pd.DataFrame()

df_whole, df_ti = prep.generate_ti(df_whole, feat_src_map)


