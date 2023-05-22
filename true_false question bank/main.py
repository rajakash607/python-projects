from data import question_data
from question_model import Question
from quiz_brain import Quiz_brain

question_bank = []
for question in question_data:
    new = Question(question["text"], question["answer"])
    question_bank.append(new)

quiz = Quiz_brain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()
