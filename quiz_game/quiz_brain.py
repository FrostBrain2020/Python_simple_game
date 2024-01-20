class Brain:

    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

# TODO: asking the question
    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {question.text} (True/False)? ")
        correct_answer = self.question_list[self.question_number - 1].answer
        self.check_answer(correct_answer, user_answer)

# TODO: checking if answer is correct
    def check_answer(self, correct_answer, user_answer):
        print(f"correct: {correct_answer}, user: {user_answer}")
        if correct_answer.lower() == user_answer.lower():
            print("You got right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")

# TODO: checking if we're to the end of the quiz
    def still_has_question(self):
        return self.question_number < len(self.question_list)
