class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def show_question(self):
        print(self.question)
        for number in range(4):
            print(str(number + 1) + ". " + self.choices[number])

    def is_correct(self, user_answer):
        return user_answer == self.answer
