class Question:

    def __init__(self, q_text, q_answer):
        self._text = q_text
        self._answer = q_answer

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, d):
        self._text = d

    @property
    def answer(self):
        return self._answer
