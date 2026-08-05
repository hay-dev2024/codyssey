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

    def get_number_input(self, message, minimum, maximum):
        while True:
            user_input = input(message).strip()

            if user_input == "":
                print("입력이 비어 있습니다. 다시 입력하세요.")
                continue

            if not user_input.isdigit():
                print("숫자를 입력하세요.")
                continue

            number = int(user_input)
            if number < minimum or number > maximum:
                print(str(minimum) + "부터 " + str(maximum) + "까지 입력하세요.")
                continue

            return number

    def get_text_input(self, message):
        while True:
            text = input(message).strip()
            if text == "":
                print("입력이 비어 있습니다. 다시 입력하세요.")
                continue
            return text

    def play_quizzes(self):
        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
            return

        correct_count = 0
        for number in range(len(self.quizzes)):
            print("\n[ 문제 " + str(number + 1) + " ]")
            quiz = self.quizzes[number]
            quiz.show_question()
            answer = self.get_number_input("정답 번호를 입력하세요: ", 1, 4)

            if quiz.is_correct(answer):
                print("정답입니다!")
                correct_count += 1
            else:
                print("오답입니다. 정답은 " + str(quiz.answer) + "번입니다.")

        score = int(correct_count / len(self.quizzes) * 100)
        print("\n[ 결과 ]")
        print("전체 문제 수: " + str(len(self.quizzes)))
        print("맞힌 문제 수: " + str(correct_count))
        print("점수: " + str(score) + "점")

        if self.best_score is None or score > self.best_score:
            self.best_score = score
            self.save_state()
            print("최고 점수가 갱신되었습니다.")

    def add_quiz(self):
        print("\n[ 퀴즈 추가 ]")
        question = self.get_text_input("문제를 입력하세요: ")
        choices = []

        for number in range(4):
            choice = self.get_text_input(
                "선택지 " + str(number + 1) + "을 입력하세요: "
            )
            choices.append(choice)

        answer = self.get_number_input("정답 번호를 입력하세요: ", 1, 4)
        self.quizzes.append(Quiz(question, choices, answer))
        self.save_state()
        print("퀴즈가 추가되었습니다.")
