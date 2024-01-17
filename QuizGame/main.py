from data import question_data
from question_model import Question
from quiz_brain import Brain

question_bank = []
gameplay = Brain(question_bank)
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

gameplay = Brain(question_bank)

while gameplay.still_has_question():
    gameplay.next_question()

print("You've completed the Quiz")
print(f"Your final score is: {gameplay.score}/{gameplay.question_number}")
