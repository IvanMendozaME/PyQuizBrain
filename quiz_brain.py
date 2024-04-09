class QuizBrain():
    def __init__(self, question_list) -> None:
        self.question_number = -1
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number+1 < len(self.question_list)
           
    def next_question(self):
        self.question_number +=1
        answer = input(f"Q.{self.question_number+1} {self.question_list[self.question_number].text} (True/False)?: ")
        self.check_answer(self.question_list[self.question_number].answer,answer)

    def check_answer(self, Answer, UserAnswer):
        
        if Answer.lower() == UserAnswer.lower():
            print("You got it right")
            self.score +=1
        else:
            print("That's wrong")
        print(f"The correct answer is {Answer}")
        print(f"Your score is {self.score}/{self.question_number+1}")

        
    
    