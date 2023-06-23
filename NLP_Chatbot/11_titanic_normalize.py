# 076일차-실습-3-해답
# 수치데이터 활용실습
import pandas as pd
import numpy as np
"""1. 정규화를 수행하는 함수를 구현
min(), max() 메서드 이용 """
def normal(data): # 정규화 
    data = (data-data.min())/(data.max()-data.min())
    return data
#
def std(data): # 표준화 
    data2 = np.mean(data)   # 평균계산 
    data3 = np.std(data)    # 표준편차 계산 
    data_ret = (data - data2) / data3   # 표준화계산
    
    return data_ret
# 데이터를 읽어옵니다.
titanic = pd.read_csv('titanic.csv')
print('정규화 변환 전: \n',titanic['Fare'].head())

# normal 함수를 사용하여 정규화합니다.
Fare = normal(titanic['Fare'])
# 정규화 변환한 Fare 데이터를 출력합니다.
print('\n정규화변환 후: \n',Fare.head())

# normal 함수를 사용하여 표준화합니다.
Fare2 = std(titanic['Fare'])

# 표준화변환한 Fare 데이터를 출력합니다.
print('\n표준화 변환 후: \n',Fare2.head())