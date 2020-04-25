from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
chatbot = ChatBot("Ron Obvious")
trainer = ChatterBotCorpusTrainer(chatbot)
 
trainer.train(
 "chatterbot.corpus.english"
)
