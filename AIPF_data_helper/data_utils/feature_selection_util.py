import pandas as pd

def get_skb_score(data : pd.DataFrame = None):
    ret : pd.DataFrame = None
    return ret

def filter_skb_result(data : pd.DataFrame = None, data_ti : pd.DataFrame = None, skb_score : pd.DataFrame = None, cutoff_dict : dict(str, float) = None)
    ret : pd.DataFrame = None
    
    skb_cutoff = cutoff_dict['skb_cutoff']
    
    return ret

def get_ranksum(data : pd.DataFrame = None, target_name : str = None):
    ret : pd.DataFrame = None
    
    xgb_rank = get_xgb_rank(data)
    lasso_rank = get_lasso_rank(data)
    corr_rank = get_corr_rank(data)
    
    # merge results
    
    # calc ranksum
    
    return ret

def get_xgb_rank(data : pd.DataFrame = None):
    ret : pd.DataFrame = None
    return ret

def get_lasso_rank(data : pd.DataFrame = None):
    ret : pd.DataFrame = None
    return ret

def get_corr_rank(data : pd.DataFrame = None):
    ret : pd.DataFrame = None
    return ret

def lead_lag_analysis(data : pd.DataFrame = None, ranksum_result : pd.DataFrame = None, shift_len : int = None):
    ret : pd.DataFrame = None
    return ret