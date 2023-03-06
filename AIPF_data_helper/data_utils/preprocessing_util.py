import pandas as pd
import multiprocessing
import sys
import os


'''
기조 전처리 - preprocess()
결측치와 최빈값 비중으로 데이터 필터링
기간과 cutoff 인자로 전달
miss = 0.3, mod = 0.4
miss_start_date = today - timedelta(260)
miss_end_date = today - timedelta(30)
특수문자 제거
numeric 변환
데이터 중복 제거
OHLC 데이터 있는 경우(Investing.com) CLOSE만 남기고 제거
날짜 표준화
'''
def preprocess(
    args : dict(str, object) = None
    ):
    """_summary_

    Args:
        path_file (str, optional): _description_. Defaults to None.
        freq (str, optional): _description_. Defaults to None.
        date_dict (dict, optional): _description_. Defaults to None.
        cutoff_dict (dict, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """    """
    """
    path_file : str = args['path_file']
    freq : str = args['freq']
    date_dict : dict(str, str) = args['date_dict']
    cutoff_dict : dict(str, float) = args['cutoff_dict']
    
    ret : pd.DataFrame = None
    
    data = pd.read_csv(path_file, index_col = 0)
    
    data_clean = clean_data(data)
    
    data_biz = make_bizdate(data_clean, freq)
    
    data_summ, data_eda = summerize_data(data_biz, date_dict)
    
    data_filtered = filter_missmod(data_summ, data_eda, cutoff_dict)
    
    data_outl = remove_outlier(data_filtered, cutoff_dict)
    
    ret = remove_missing(data_outl)
    
    return ret

def clean_data(data : pd.DataFrame = None):
    '''
    """
    _summary_ : DataFrame 내 모든 특수문자 제거

    Returns:
        _type_: _description_
    """    '''
    ret : pd.DataFrame = None
    return ret

def make_bizdate(data : pd.DataFrame = None):
    """
    _summary_ : DataFrame의 index를 영업일만 남기며, Daily 데이터가 아닌 경우 주말 데이터를 영업일로 이동시켜 데이터 누락을 방지하며 처리
    1. 영업일 기준으로 날짜 인덱스 생성 (biz_index)
    2. daily가 아닌 데이터(Q,M,W)에 대해서 주말 데이터를 가장 가까운 평일로 이동
    3. data의 column 별로(변수별로) 처리
    4. 토요일 -> 금요일, 일요일 -> 월요일로 데이터 이동
    5. 데이터 이동이 끝난 변수를 biz_index에 병합해 하나의 DataFrame으로 병합
    6. 일별 데이터의 경우 영업일만 남겨서 return
    
    Returns:
        _type_: _description_
    """    
    
    ret : pd.DataFrame = None
    return ret

def summerize_data(data : pd.DataFrame = None):
    """_summary_

    Args:
        data (pd.DataFrame, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """    
    
    ret : pd.DataFrame= None
    ret_eda : pd.DataFrame = None
    
    ### run EDA
    
    return ret, ret_eda

def filter_missmod(data : pd.DataFrame = None, data_eda : pd.DataFrame = None,  cutoff_dict : dict(str, float) = None):
    ret : pd.DataFrame = None
    return ret

'''
후속 전처리
'''

def remove_outlier(data : pd.DataFrame = None, cutoff_dict : dict(str, float) = None):
    ret : pd.DataFrame= None
    ret_log : pd.DataFrame = None
    
    return ret, ret_log

def remove_missing(data : pd.DataFrame = None):
    ret : pd.DataFrame = None
    
    data = data.interpolate()
    
    return ret

def generate_ti(data : pd.DataFrame = None, feat_src_map  : pd.DataFrame = None):
    ret : pd.DataFrame = None
    
    return data, ret