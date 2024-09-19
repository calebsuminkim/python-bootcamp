class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}. {current_question.text} (True / False): ")
        self.check_answer(user_answer, current_question.answer)

    def next_question_trivia(self):     # Trivia 모드용. 단순히 질문 끝에 (True/False)만 지운 버전임
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}. {current_question.text}: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was : {correct_answer}.")
        print(f"Your current score is : {self.score} / {self.question_number}")
        print("\n")     # 문제간 공백을 위해

    def still_has_questions(self):  # 남아있는 질문이 있는지 체크
        if self.question_number < len(self.questions_list):
            return True
        else:                       # 질문이 끝에 다다르면 False
            return False
        # return self.question_number < len(self.questions_list) 만 써도 같은 동작이다(True/False리턴)
