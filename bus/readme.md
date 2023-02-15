# 제주도 버스 운행 시간 예측 프로젝트

### 개요
- 효율적인 배차를 위해 제주도 버스의 운행 시간을 예측해 봅시다.

### 과정
1. 데이터확인
2. Folium
3. Insight 추출
4. 모델링
5. 결과

### 데이터 확인
- id : 고유 id
- date : 버스 운행 날짜
- route_id : 버스 노선 ID
- vh_id : 버스 id
- route_nm : 버스 노선 실제 번호
- now_latitude : 현재 정류소의 위도
- now_longitude : 현재 정류소의 경도
- now_station : 현재 정류소 이름
- now_arrive_time : 현재 정류장에 도착한 시간
- distance : 현재 정류장에서 다음 정류장까지 실제 이동한 거리
- next_station : 다음 정류소 이름
- next_latitude : 다음 정류소의 위도
- next_longitude : 다음 정류소의 경도
- next_arrive_time : 다음 정류장에 도착할 때 까지 걸린 시간(단위:초)으로 답안 제출을 위해서 예측해야 되는 값
<br>
- 총 210457개의 row와 14개의 칼럼이 조재한다.
- 결측치는 존재하지 않는다.
- 총 21개의 루트가 존재한다.
- train 에는 총 104대의 버스가 존재한다.
- test 에는 총 100 대의 버스가 존재한다.

### Insight
- 노선에 따라 평균이 꽤 차이가 난다.
- 제일 시간이 오래 걸린 노선 : 405136521
- 제일 시간이 짧게 걸린 노선 : 405320122
- 노선을 folium으로 그려본다.
- distance가 뚜렷한 경향을 보이지는 않지만 distance가 클 수록 데이터가 줄어든다.
- next_arrive_time은 초기 값에 많은 데이터가 분포해있다.
- now_arrive_time에 '시'를 빼고 int 로 바꿔 모델링하기 편하게 바꿔준다.

### 모델링
- now_latitude, now_longitude, now_arrive_time, distance 만 넣어서 모델링했다.
- LinearRegression, RandomForestRegressor, LGBM 을 사용하여 모델링 한다.
### 결과
