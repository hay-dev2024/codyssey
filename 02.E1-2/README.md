# Linux 퀴즈 게임

Python으로 만든 터미널 기반 Linux 기초 퀴즈 게임입니다. Linux의 자주 쓰는 명령어를 문제로 풀면서 기초 내용을 복습할 수 있습니다. 처음 배우는 사람이 바로 연습할 수 있어 Linux를 주제로 선정했습니다.

## 실행 방법

Python 3.10 이상이 필요합니다.

```bash
cd 02.E1-2
python3 main.py
```

## 기능

- 기본 Linux 퀴즈 5개 제공
- 모든 퀴즈를 순서대로 풀고 100점 기준 점수 확인
- 직접 만든 퀴즈 추가
- 등록된 퀴즈 목록 확인
- 최고 점수 저장 및 확인
- 잘못된 입력, Ctrl+C, EOF 입력을 안전하게 처리

## 파일 구조

```text
02.E1-2/
├── main.py       # 프로그램 시작과 안전 종료 처리
├── quiz.py       # Quiz 클래스
├── quiz_game.py  # 메뉴와 게임 기능을 담은 QuizGame 클래스
├── state.json    # 퀴즈와 최고 점수 데이터
├── README.md
└── .gitignore
```

## state.json

데이터 파일 경로는 `02.E1-2/state.json`입니다. 프로그램은 이 파일에 사용자가 추가한 퀴즈와 최고 점수를 저장하므로, 프로그램을 다시 실행해도 데이터가 유지됩니다.

주요 필드는 다음과 같습니다.

```json
{
    "quizzes": [
        {
            "question": "문제",
            "choices": ["선택지 1", "선택지 2", "선택지 3", "선택지 4"],
            "answer": 1
        }
    ],
    "best_score": null
}
```

- `quizzes`: 문제, 선택지 4개, 정답 번호를 저장합니다.
- `best_score`: 지금까지의 가장 높은 점수입니다. 아직 푼 적이 없으면 `null`입니다.
