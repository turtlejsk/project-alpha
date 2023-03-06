import pandas as pd
import glob

def map_varmeta(data : pd.DataFrame = None, var_meta : pd.DataFrame = None):
    ret = None
    return ret

# 추후 DB 테이블에서 조회하는 방식으로 변경 가능
def get_file_version(path_root : str = None, date : str = None, filename : str = None):
    ret : str = None
    
    all_files = glob.glob(f'{path_root}{filename}*')
    
    return ret

def get_org_varname(feature_name : str = None):
    ret : str = None
    return ret

def get_ranksum(path_fs : str = None, date : str = None, shift : int = None):
    ret = pd.DataFrame = None
    
    # 추후 DB 테이블에서 조회하는 방식으로 변경 가능
    version = get_file_version(path_fs, date, 'RANKSUM')
    
    return ret