# API 설명
## post
- pub_date
    - Readonly
    - AutoNow
- text
    - 텍스트 내용
- lat, lang
    - 좌표 저장용 int
    
## user
- username
    - 로그인용 아이디
- first_name
    - 닉네임
- password
    - 말그대로
    
## API 링크들
### 회원가입
`/signup/`로 POST 요청을 해서 회원가입

제대로 가입되면 회원 정보가 response 됨

### OAUTH 애플리케이션 생성
`/o/applications/`로 접속하여 `confidential` 타입의 `Resource owner password-base`로 앱 생성후, 클라이언트 id와 secret key 발급받아 사용하면 됨!


### 토큰 발급
`/o/token/`으로 아래 포맷으로 데이터를 전송하면 토큰을 얻을 수 있음

```
x-www-from-urlencoded 
"client_id": "",
"client_secret": "",
"grant_type":"password",
"username": "USERNAME",
"password": "PW"
```