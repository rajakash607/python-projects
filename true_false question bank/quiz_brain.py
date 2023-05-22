class Quiz_brain:
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.q_number < len(self.q_list)

    def next_question(self):
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        user_input = input(
            f"Q.{self.q_number}: {current_question.q_text}. (True/False): ")
        self.check_answer(user_input, current_question.answer)

    def check_answer(self, user_input, correct_answer):
        if user_input.lower() == correct_answer.lower():
            print(f"You got it right!")
            self.score += 1
        else:
            print(f"Thats wrong!")

        print(f"The correct answer was: {correct_answer}")
        print(f"Current score: {self.score}/{self.q_number} \n")
