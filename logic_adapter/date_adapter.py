from datetime import datetime

from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter


class DateAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        return self.process(statement).confidence

    def process(self, input_statement, additional_response_selection_parameters=None):
        if "dzien" in input_statement.text \
                or "dzień" in input_statement.text \
                or "dzisiaj" in input_statement.text \
                or "data" in input_statement.text:
            now = datetime.now().strftime('%Y-%m-%d')
            statement = Statement(text="Dzisiaj jest {}.".format(now))
            statement.confidence = 1
        else:
            statement = Statement(text="")
            statement.confidence = 0

        return statement
