# 프로젝트 소개

순수 HTML, CSS, JavaScript로 만든 반응형 개인 포트폴리오 웹사이트입니다. 사용자 이벤트가 상태를 바꾸고 DOM을 다시 그리는 흐름을 작은 기능 단위로 확인할 수 있습니다.

## 사용 기술

- HTML5
- CSS3
- JavaScript
- GitHub REST API
- GitHub Pages

## 실행 방법

1. VS Code에서 `index.html`을 엽니다.
2. Live Server 확장 기능의 **Open with Live Server**를 실행합니다.
3. 브라우저에서 표시된 로컬 주소를 엽니다.

## 주요 기능

- 모바일 우선 반응형 디자인과 햄버거 메뉴
- 메뉴와 CTA의 부드러운 스크롤
- 300px 이후 표시되는 Scroll Top 버튼
- 60px 이후 변경되는 Navigation 스타일
- 다크 모드 및 localStorage를 이용한 테마 유지
- `IntersectionObserver` 기반 스크롤 애니메이션
- Contact 폼의 실시간 입력 검증과 제출 검증
- GitHub API 기반 프로젝트 카드 렌더링
- API 로딩, 성공, 오류/재시도, 빈 상태 UI

## 프로젝트 구조

```text
B1-1/
├── index.html
├── css/
│   └── style.css
├── js/
│   └── main.js
├── images/
│   └── profile.svg
└── README.md
```

## JavaScript 상태/렌더링 흐름

- **다크 모드:** 버튼 click → theme 상태 결정 → `data-theme` 변경 → CSS 변수로 화면 변경 → localStorage 저장
- **GitHub API:** API 호출 → 로딩 메시지 → 성공/빈 상태의 프로젝트 DOM 렌더링 또는 오류 메시지와 재시도 버튼 표시
- **Form Validation:** input/submit → 필드 유효성 검사 → 오류 상태 결정 → 각 입력 필드 근처의 오류 메시지 DOM 업데이트

## 기준값

- Scroll Top 버튼 표시: **300px**
- Navigation 스타일 변경: **60px**
- IntersectionObserver threshold: **0.2**
- 반응형 breakpoint: **768px / 1024px**

## GitHub API

사용 API: `https://api.github.com/users/hay-dev2024/repos`

인증 없는 GitHub API는 rate limit이 있을 수 있습니다. 요청 오류(403 포함)가 발생하면 오류 UI와 다시 시도 버튼을 표시합니다.

## 배포 URL

GitHub Pages 배포 후 실제 주소로 바꿔 주세요.

`[GitHub Pages 배포 URL을 여기에 입력]`

## 스크린샷

GitHub Pages 배포 및 검증 후 아래 스크린샷을 추가해 주세요.

- Desktop 화면
- Mobile 화면
- Dark Mode 화면

## 필수 구현 체크리스트

완료 표시는 코드와 정적 검증으로 확인한 항목입니다. 실제 브라우저 및 배포 환경이 필요한 항목은 확인 전까지 비워 둡니다.

### 프로젝트 구조와 제한

- [x] 순수 HTML, CSS, JavaScript만 사용
- [x] 외부 프레임워크·라이브러리·웹 폰트 미사용
- [x] 보너스 기능(프로젝트 필터, 타이핑 효과, 실제 이메일 전송, 시스템 테마 감지) 미구현
- [x] `index.html`, `css/style.css`, `js/main.js`, `images/profile.svg`, `README.md` 구성
- [x] CSS 상대 경로 및 JavaScript `defer` 연결
- [x] 로컬 프로필 이미지와 의미 있는 `alt` 제공
- [x] 인라인 `style`, HTML `onclick`, JavaScript `var` 미사용

### 페이지와 인터랙션

- [x] `header`, `nav`, `main`, `section`, `article`, `footer` 시맨틱 태그 사용
- [x] Hero, About, Skills, Projects, Contact, Footer 영역 및 앵커 메뉴 제공
- [x] Hero CTA, 모바일 햄버거 메뉴, JavaScript 부드러운 스크롤 구현
- [x] 60px 헤더 스타일 변경 및 300px Scroll Top 버튼 구현
- [x] CSS 변수 기반 다크 모드와 localStorage 유지 구현
- [x] IntersectionObserver threshold 0.2 스크롤 애니메이션 구현
- [x] `querySelector`, `querySelectorAll`, `textContent`, `innerHTML`, `classList` 사용
- [x] click, submit, scroll, input 이벤트와 `preventDefault()` 사용
- [x] 화살표 함수, 템플릿 리터럴, 구조분해 할당, `map`, `forEach` 사용

### GitHub API와 Contact 폼

- [x] `fetch`, `async`/`await`, `try`/`catch`로 `hay-dev2024` API 요청
- [x] 프로젝트 로딩, 성공, 빈 목록, 오류·재시도 상태 UI 구현
- [x] 저장소 이름, 설명, 언어, star 수, 링크 동적 렌더링
- [x] Contact 이름·이메일·메시지 빈 값 및 이메일 형식 검증
- [x] 입력 중 오류 갱신, 제출 차단, 정상 입력 성공 메시지 구현
- [x] 실제 이메일 전송 미구현

### CSS와 문서

- [x] `:root`와 `[data-theme="dark"]` CSS 변수 정의
- [x] 내비게이션 Flexbox와 `repeat(auto-fit, minmax(...))` 프로젝트 Grid 적용
- [x] 모바일 우선 레이아웃과 768px·1024px 브레이크포인트 적용
- [x] hover, transition, box-shadow 적용
- [x] README에 실행법, 상태→렌더링 흐름, 기준값, API 제약, 배포·스크린샷 안내 작성

### 사용자 확인 및 배포

- [ ] Desktop / Tablet / Mobile 브라우저 화면 확인
- [ ] 실제 GitHub API 로딩·성공·오류·재시도·빈 상태 확인
- [ ] Contact 폼의 빈 값·이메일 형식·정상 제출 확인
- [ ] 다크 모드 새로고침 유지 확인
- [ ] GitHub에 push
- [ ] GitHub Pages 활성화 및 README 배포 URL 반영
- [ ] 배포 환경 재검증 및 Desktop / Mobile / Dark Mode 스크린샷 추가
