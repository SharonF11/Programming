import imp

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainers

my bot = ChatBot (name='PyBot', read only=True,
logic adapters=
['chatterbot.logic.MathematicalEvaluation
"chatterbot. logic.BestMatch'])