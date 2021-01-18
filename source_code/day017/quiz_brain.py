class QuizBrain:

    def __init__(self, q_list):
        self.__question_number = 0
        self.__score = 0
        self.__question_list = q_list

    @property
    def question_number(self):
        return self.__question_number

    @property
    def score(self):
        return self.__score

    def still_has_questions(self):
        return self.__question_number < len(self.__question_list)

    def next_question(self):
        current_question = self.__question_list[self.__question_number]
        self.__question_number += 1
        user_answer = input(
            f"Q.{self.__question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.__score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(
            f"Your current score is: {self.__score}/{self.__question_number}")
        print("\n")
