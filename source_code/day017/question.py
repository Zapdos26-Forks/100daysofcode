class Question:

    def __init__(self, q_text, q_answer):
        self.__text = q_text
        self.__answer = q_answer

    @property
    def text(self):
        return self.__text

    @property
    def answer(self):
        return self.__answer
