# Moment 백엔드
## 서비스 소개
네이버 지도 위에 여러분의 인생에서 가장 소중했던 순간들을 핀으로 남겨보세요!

해시태그와 카테고리를 활용해서 모아볼 수도 있어요!
## 장고 앱 구성
### main
프로젝트 메인 페이지 전반의 기능 수행

- mainpage : 로그인 되어 있으면 mainpage.html, 아니면 service.html 반환
- signup : signup.html
### account
회원 로그인, 가입 기능 등

- signupProc : 회원가입 처리용 url
- loginProc : 로그인 처리용 url
- logout : 로그아웃 처리용 url

### board
게시판 기능, 해시태그, 카테고리 기능

- create : 글쓰기 페이지 post_form.html
- read : 글읽기 페이지 post_detail.html

## 팀
세종대학교 멋사 7기 - 컨트롤즤
- [백지오](https://www.github.com/skyil7)
- [송지원](https://github.com/SongJi-Won)
- [임서정](https://github.com/sjytis14)
- [천이수](https://github.com/leesoo7595)
