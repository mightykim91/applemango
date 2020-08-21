## 1. bing 크롤링으로 데이터 수집

* 사용되는 py파일 
  * bingfordata.py 
  * similarity_measure.py

* 입력값

  * ko_search = list(input("한글 음식명:").split()) 
    * 음식의 한글명
  * en_search = list(input("영어 음식명:").split())
    * 음식의 영문명(구글 번역기에 한글 검색후, 번역된 영어가 아닌 한글 그대로 읽은 영어로 사용)
  * stan_search = list(input("target image url:").split())
    * 유사도 판별을 위한 이미지 url 첨부

  띄어쓰기로 여러 음식 입력가능

* 과정

  1. bing.com에서 음식을 크롤링
     * 해당 음식 이미지데이터가 cnn_sample폴더에 있다면 pass
  2. 음식이미지의 url을 갖고옴
  3. 유사도 검증을 통해 filtering을 진행 (similarity_measure.py의 Similarity_Measurement함수)하여 최대한 음식 이미지 url과 유사한 이미지만 크롤링한다.
  4. 유사도 검증을 끝낸 이미지들을 수작업을 통해 이미지를 필터시킨다(글자, 사람 필터링을 돌려본 결과 시간이 너무 오래걸리고, 유사도 판단을 통해 한번 걸러진 데이터기때문에 수작업이 더 빠르다)
  5. 마지막으로 menu.py에 음식명을 추가한다.(필수!!)

* 결과값 

  * cnn_sample 폴더내에 음식별 이미지 사진이 있음 



## 2. cnn 학습 진행

* 참여하는 py파일 
  * cnn_train.py
* 입력값
  * ko_foods = list(input("음식명:").split())
* 과정
  1. 내가 학습시키고 싶은 이미지 데이터들을 학습시킴
  2. cnn_sample폴더내에서 음식명을 찾아 훈련을 시킴 => 속도 빠름

* 결과값 
  * 모델 bingforcnn.h5을 만들어냄

이미지 데이터가 수십만개가 아닌이상 cnn학습은 금방 끝냄



## 3.인스타 크롤링 + 이미지 예측

* 참여하는 py파일
  * insta.py , insta_modal.py, cnn_predict.py, server_select.py

* 입력값
  * plusUrl = input('식당명을 입력하세요 : ')
  * en_name = input('식당의 영어명을 입력하세요 : ')
  * irid = int(input('식당의 rid값을 입력하세요: '))
  * ko_search = list(input("음식명:").split())
    * 식당 이름과 json파일의 이름을 위한 식당의 영어이름도 작성한다.
    * 식당번호인 irid와 음식명 역시 직접 지정해준다.
    * 이때 음식명은 모델에 학습시킨 순서대로 해줘야한다.

* 과정
  1. 식당 이름을 기준으로 인스타 크롤링을 진행
  2. 우리 DB내 저장된 계정만 추출하기 위한 server_select.SELECT로 검증
  3. 검증된 계정만 insta_modal.py로 이동하여 해당 이미지 추출
  4. cnn_predict.Predict 에서 해당 이미지의 음식 유무를 판단 및 음식 종류를 분류
  5. person.person_filter에 이동하여 해당 이미지의 사람 유무를 판단
  6. 2 ~ 4번의 과정을 다 겪은 이미지만 json파일로 변환
* 결과값
  * 가게명을 기준으로 크롤링한 결과가 json파일로 변환되어 저장됨



## 4. DB에 INSERT 

* 참여하는 py파일 
  * server_insert.py
* 입력값
  * name = input('로드할 json 파일명을 작성해주세요: ')
    * insert할 json파일명을 입력값으로 넣는다.
* 과정
  1. DB와 연결한뒤, 해당 json 데이터를 instagrampictures테이블에 insert

* 결과값 
  * insert되고 끝남
