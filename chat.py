from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


# Create Chatbot Instance with name Pendlebottom

chatbot = ChatBot('Mr. Pendlebottom')

conversation = [
    'Hi',
    'Hello',
    'How are you doing?',
    "I'm doing great.",
    "Great to hear!",
    'I need your assistance regarding my order',
    'Please, Provide me with your order id',
    'I have a complaint.',
    'Please elaborate your concern',
    'How long it will take to receive an order?',
    'An order takes 3-5 Business days to get delivered.',
    'Okay thanks',
    'No Problem! Have a Good Day!'
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)


