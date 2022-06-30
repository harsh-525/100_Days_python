from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    question_bank.append(Question(i['question'], i['correct_answer']))

new_quiz = QuizBrain(question_bank)

while new_quiz.still_has_questions():
    new_quiz.next_question()

print(f"You completed the Quiz!\nYour Final score is: {new_quiz.score}/{new_quiz.question_no}")
