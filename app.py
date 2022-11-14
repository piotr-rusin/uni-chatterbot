import dotenv

dotenv.load_dotenv()

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

from integrations.google_sheets import google_sheets

sheet_id = "1GgfvAsHorqf4Z7X7IexQ0iDitnHOeRUfz2bUo1JnZQw"

chatbot = ChatBot('Mr Bot')

trainer = ListTrainer(chatbot)
trainer.train([row[0] for row in google_sheets.get_values(sheet_id, "data!A1:A1000")['values']])

while True:
    print(chatbot.get_response(input("> ")))
