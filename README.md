# Moment 백엔드
## 장고 앱 구성
### main
프로젝트 메인 페이지 전반의 기능 수행

- mainpage : 로그인 되어 있으면 mainpage.html, 아니면 service.html 반환
- signup : signup.html
게시판 기능, 해시태그, 카테고리 기능
### account
회원 로그인, 가입 기능 등

- signupProc : 회원가입 처리용 url
- loginProc : 로그인 처리용 url
- logout : 로그아웃 처리용 url

### board
- create : 글쓰기 페이지 post_form.html