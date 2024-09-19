from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from data_from_TDB import question_data_from_tdb    # Trivia DataBase 문제 목록

mode = input("Which questions would you like to go? Type 'Normal' or 'Trivia': ")
if mode == 'Normal':
    question_bank = []
    for q in question_data:
        question_bank.append(Question(q["text"], q["answer"]))

    quiz = QuizBrain(question_bank)
    while quiz.still_has_questions() is True:   # 질문이 남아있는 한 계속 질문을 던진다.
        quiz.next_question()

    print("You've completed the quiz.")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")
else:   # Trivia mode
    question_bank = []
    for q in question_data_from_tdb:
        question_bank.append(Question(q["question"], q["correct_answer"]))

    quiz = QuizBrain(question_bank)
    while quiz.still_has_questions() is True:
        quiz.next_question_trivia()

    print("You've completed the quiz.")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")