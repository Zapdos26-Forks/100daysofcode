from question import Question
from quiz_brain import QuizBrain
import json


if __name__ == '__main__':
    question_bank = []
    with open('data.json') as file:
        question_data = json.load(file)
    for question in question_data:
        new_question = Question(
            question["question"], question["correct_answer"])

        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()

    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")
