import pandas as pd


def get_skb_score(data : pd.DataFrame = None):
    ret : pd.DataFrame = None
    return ret


def get_ranksum(data : pd.DataFrame = None):
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