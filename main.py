from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
a = 0
question_bank = []
for i in question_data:
     question = Question(i['text'],i['answer'] )
     question_bank.append(question)

Quiz_Brain = QuizBrain(question_bank)
while Quiz_Brain.still_has_questions():
    Score, QN = Quiz_Brain.next_question()

print("You have completed the quiz")
print(f"Your final score was: {Quiz_Brain.score}/{Quiz_Brain.question_number}")