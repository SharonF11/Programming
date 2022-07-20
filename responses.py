from simple_chatbot.responses import GenericRandomResponse


class GreetingResponse(GenericRandomResponse):
    choices = ("Hey, how can I help you?",
               "Hey friend. How are you? How can I help you?")


class GoodbyeResponse(GenericRandomResponse):
    choices = ("See you later.",
               "Thanks for visiting.",
               "See ya! Have a nice day.")

class ProductResponse(GenericRandomResponse):
    choices = ("We Have Training Bench,Dumbbell Set,Barbell Set,Pull-Up Frame and Bar,Treadmill,Rowing Machine",
    " things in our store Training Bench,Dumbbell Set,Barbell Set,Pull-Up Frame and Bar,Treadmill,Rowing Machine","You Buy Training Bench,Dumbbell Set,Barbell Set,Pull-Up Frame and Bar,Treadmill,Rowing Machine")               