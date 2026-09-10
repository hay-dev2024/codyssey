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
