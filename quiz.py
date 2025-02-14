class Quiz:
    def __init__(self, q_text):
        self.q_question = q_text
        self.current_number = 0
        self.score = 0

    def looping_question(self):
        return len(self.q_question) > self.current_number
    def ask_question(self):
        current_question = self.q_question[self.current_number]
        self.current_number += 1
        user_answer = input(f"Q-{self.current_number}: {current_question.question} ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user, right_answer):
        if user.lower() == right_answer.lower():
            self.score += 1
            print("You got right")
        else:
            print("You are wrong")
        print(f"The answer is: {right_answer}")
        print(f"Your current score is {self.score}/{self.current_number}")
        print("\n")