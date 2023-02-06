# -*- coding: utf-8 -*-
"""bus.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jHC0A3diHQRA4ln2fUgT_FfAh8DBQTyc
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

train = pd.read_csv('/content/drive/MyDrive/bus/train.csv')
test = pd.read_csv('/content/drive/MyDrive/bus/test.csv')
submission = pd.read_csv('/content/drive/MyDrive/bus/submission_제출양식.csv')

train.head()

test.head()

submission.head()

train.shape

"""id 기준 0~210456까지 총 210457개의 row와 14개의 칼럼이 존재한다."""

train.info()

"""- id : 해당 데이터의 고유한 ID
- date : 버스 운행 날짜
- route_id : 버스 노선 ID
- vh_id : 버스 ID
- route_nm : 버스 노선 실제 번호
- now_latitude : 현재 정류소의 위도
- now_longtitude : 현재 정류소의 경도
- now_station : 현재 정류소 이름
- now_arrive_time : 현재 정류장에 도착한 시간
- distance : 현재 정류장에서 다음 정류장까지 실제 이동한 거리
- next_station : 다음 정류소 이름
- next_latitude : 다음 정류서의 위도
- next_longtitude : 다음 정류소의 경도
- next_arrive_time : target, 다음 정류장에 도착할때 까지 걸린 시간(초)


"""

train.isnull().sum()

# 결측치는 존재하지 않는다.

test.isnull().sum()

train.route_id.unique()

test.route_id.unique()

train.route_id.nunique()

test.route_id.nunique()

"""총 21 개의 루트가 존재한다.


"""

train.vh_id.unique()

test.vh_id.nunique()

train.vh_id.nunique()

"""train : 총 104대의 버스가 존재한다.<br>
test : 총 100대의 버스가 존재한다.


"""

train.route_nm.unique()

train.route_nm.nunique()

"""route_nm이 route_id 보다 더 보기 편한 것 같다."""

train.now_station.nunique()

test.now_station.nunique()

"""train : 348개의 정류소가 존재한다.
test : 349개의 정류소가 존재한다.
"""

# 왜 차이가 날까?
# 제주 한라 대학교가 없다.

train[train['now_station']=='제주한라대학교(종점)']

train.now_station.unique()

train.now_station.value_counts()

test.now_station.value_counts()

# 기준이어서 시 단위로 끊어진 것 같다.
train.now_arrive_time.value_counts()

plt.figure(figsize=(25,4))
sns.countplot(data = train, x= "now_arrive_time")

plt.figure(figsize=(25,4))
sns.countplot(data=test,x="now_arrive_time")

# 00시가 test data에서는 존재하지 않는다.

plt.figure(figsize=(25,4))
sns.countplot(data = train,x = "distance")


# 거리가 뚜렷한 경향이 보이지는 않지만 distance가 큰 정류장은 작아보인다.

train.next_station.value_counts()

test.next_station.value_counts()

"""next station은 test data에서 또 하나가 적다.
아마 전경대 입구가 아닐까......?
"""

test[test['next_station']=='전경대 입구']

# 전경대 입구가 없다.

train.next_arrive_time.value_counts()

plt.figure(figsize=(25,4))
sns.countplot(data=train, x="next_arrive_time")

train = train.sort_values(by='next_arrive_time')

train['next_arrive_time'].describe()

"""이상치로 보이는 값들은 좀 없앨 필요가 있어 보인다.
이상치를 어떻게 판별할 수 있을까?
"""
