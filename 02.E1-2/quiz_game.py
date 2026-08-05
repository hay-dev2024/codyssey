import json
import os

from quiz import Quiz


class QuizGame:
    def __init__(self):
        self.quizzes = self.create_default_quizzes()
        self.best_score = None
        self.state_file = os.path.join(os.path.dirname(__file__), "state.json")
        self.load_state()

    def create_default_quizzes(self):
        quizzes = []
        quizzes.append(Quiz(
            "현재 작업 중인 디렉터리의 경로를 확인하는 명령어는 무엇인가요?",
            ["pwd", "cd", "ls", "chmod"],
            1
        ))
        quizzes.append(Quiz(
            "다른 디렉터리로 이동할 때 사용하는 명령어는 무엇인가요?",
            ["pwd", "cd", "ls", "mkdir"],
            2
        ))
        quizzes.append(Quiz(
            "현재 디렉터리의 파일과 디렉터리 목록을 보는 명령어는 무엇인가요?",
            ["rm", "touch", "ls", "cp"],
            3
        ))
        quizzes.append(Quiz(
            "파일의 권한을 변경할 때 사용하는 명령어는 무엇인가요?",
            ["chmod", "cat", "mv", "grep"],
            1
        ))
        quizzes.append(Quiz(
            "Linux에서 디렉터리를 만드는 명령어는 무엇인가요?",
            ["rmdir", "mkdir", "file", "man"],
            2
        ))
        return quizzes

    def save_state(self):
        quiz_data = []
        for quiz in self.quizzes:
            quiz_data.append({
                "question": quiz.question,
                "choices": quiz.choices,
                "answer": quiz.answer
            })

        data = {
            "quizzes": quiz_data,
            "best_score": self.best_score
        }

        try:
            with open(self.state_file, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except OSError:
            print("상태 파일을 저장하지 못했습니다.")

    def load_state(self):
        if not os.path.exists(self.state_file):
            self.save_state()
            return

        try:
            with open(self.state_file, "r", encoding="utf-8") as file:
                data = json.load(file)

            quizzes = []
            for item in data["quizzes"]:
                quizzes.append(Quiz(
                    item["question"], item["choices"], item["answer"]
                ))
            self.quizzes = quizzes
            self.best_score = data["best_score"]
        except (OSError, json.JSONDecodeError, KeyError, TypeError):
            print("상태 파일을 읽을 수 없어 기본 퀴즈로 시작합니다.")
            self.quizzes = self.create_default_quizzes()
            self.best_score = None
            self.save_state()

    def show_quiz_list(self):
        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
            return

        print("\n[ 퀴즈 목록 ]")
        for number in range(len(self.quizzes)):
            print(str(number + 1) + ". " + self.quizzes[number].question)
