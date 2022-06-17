# pre_diagnosis
<br>

## 1. 프로젝트
2022년도 1학기 의료정보소프트웨어특강 내 IC-PBL과제로 수행된 프로젝트입니다.

## 2. 프로그램
고령환자를 위한 예진 서비스를 웹페이지 형태로 제공하는 프로그램입니다.

## 3. 폴더 및 파일 구성
- `chart_gen`: 저장된 예진 데이터를 차트화 시켜주는 파이썬 프로그램
  * `form.xlsx`: 차트 form
  * `main.py`: 차트화 시키는 파이썬 프로그램
  * `requirements.txt`: 해당 프로그램 실행을 위한 요구사항
- `project_final`: 전체 프로그램을 구성하는 django project 폴더
- `home`: 홈 화면을 구성하는 django app 폴더
  * `static/home`: html 구성에 필요한 이미지, css, js 파일
  * `templates/home template`: 홈 화면 html template
- `question`: 질문 페이지를 구성하는 django app 폴더
  * `static/question`: html 구성에 필요한 이미지, css, js 파일
  * `templates/question template`: 홈 화면 html template
## 4. 실행환경
`python==3.9.7`  
`django==5.1.3`  
`certifi==2022.5.18.1`  
`et-xmlfile==1.1.0`  
`openpyxl==3.0.10`  
`wincertstore==0.2`  
## 5. 사용방법
- 프로젝트 폴더(pre_diagnosis) 내에서 django 실행
```bash
#migration 진행 (이미 진행했다면 skip)
>python manage.py migrate
  
#admin 계정 생성
>python manage.py createuser
  
#서버 실행
>python manage.py runserver
```
- 홈페이지 주소 입력 후 사용가능
## 6. 주의사항
현재 각 페이지 내 설명 영상은 유튜브 영상 링크로 연결되어 있습니다.  
해당 영상이 비공개 처리 시 사용 불가 할 수 있습니다.
로컬 영상으로 수정 가능합니다.
---