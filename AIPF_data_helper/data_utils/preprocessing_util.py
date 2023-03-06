import pandas as pd
import multiprocessing
import sys
import os

# 1차 전처리 - preprocess()
## 전달 인
## 결측치와 최빈값 비중으로 데이터 필터링
## 기간과 cutoff 인자로 전달
## miss = 0.3, mod = 0.4
## miss_start_date = today - timedelta(260)
## miss_end_date = today - timedelta(30)

## 특수문자 제거
## numeric 변환
## 데이터 중복 제거
## OHLC 데이터 있는 경우(Investing.com) CLOSE만 남기고 제거
## 날짜 표준화

def preprocess(
    path_file : str = None,
    freq : str = None,
    date_dict : dict(str, str) = None,
    cutoff_dict : dict(str, float) = None,
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
    ret : pd.DataFrame = None
    return ret

def clean_data(data : pd.DataFrame = None):
    '''
    """_summary_

    Returns:
        _type_: _description_
    """    '''
    ret : pd.DataFrame = None
    return ret

def make_bizdate(data : pd.DataFrame = None):
    ret : pd.DataFrame = None
    return ret

def summerize_data(data : pd.DataFrame = None):
    ret : pd.DataFrame= None
    ret_eda : pd.DataFrame = None
    
    return ret, ret_eda

def filter_missmod(data : pd.DataFrame = None, cutoff_dict : dict(str, float) = None):
    ret : pd.DataFrame = None
    return ret

def remove_outlier(data : pd.DataFrame = None, cutoff_dict : dict(str, float) = None):
    ret : pd.DataFrame= None
    ret_log : pd.DataFrame = None
    return ret, ret_log
