from data import question_data
from question_model import Question
from quiz_brain import Brain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

brain = Brain(question_bank)
quiz_ui = QuizInterface(brain)

# print("You've completed the Quiz")
# print(f"Your final score is: {gameplay.score}/{gameplay.question_number}")
