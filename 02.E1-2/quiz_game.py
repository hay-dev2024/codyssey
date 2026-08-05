from quiz import Quiz


class QuizGame:
    def __init__(self):
        self.quizzes = self.create_default_quizzes()
        self.best_score = None

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
