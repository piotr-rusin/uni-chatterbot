from datetime import datetime

from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter


class TimeAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        return self.process(statement).confidence

    def process(self, input_statement, additional_response_selection_parameters=None):
        if "godzina" in input_statement.text or "czas" in input_statement.text:
            now = datetime.now().strftime('%H:%M:%S')
            statement = Statement(text="Jest {}.".format(now))
            statement.confidence = 1
        else:
            statement = Statement(text="")
            statement.confidence = 0

        return statement
