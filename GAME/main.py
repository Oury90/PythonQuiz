from data import results_data
from brand_question import QuizBrand
from quiz import Quiz


question_bank = []

for question in results_data:
    question_text = question["question"]
    answer_text = question["correct_answer"]
    new_question = QuizBrand(question_text, answer_text)
    question_bank.append(new_question)

quiz = Quiz(question_bank)

while quiz.looping_question():
    quiz.ask_question()

print(f"Your final score is: {quiz.score}/{quiz.current_number}")
