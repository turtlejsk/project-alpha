import data_utils.feature_selection_util as fs


# 전처리 파이프라인

# 데이터 load - load_data()
# 주어진 파일 리스트에 맞게 데이터들 load
logging.info('전처리 시작')
file_list : list[str] = []

# file_list로 file_path_list 생성
file_path_list : list[str] = []
    
pool = multiprocessing.pool()
preprocess_results : list[pd.DataFrame] = pool.map(prep.preprocess, file_list)


