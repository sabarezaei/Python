from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for q in question_data:
    question = q["text"]
    answer = q["answer"]
    new_question = Question(question_text = question, question_answer = answer)
    question_bank. append(new_question)
    

quiz = QuizBrain(question_bank)
while quiz.more_questions:
    quiz .next_question()