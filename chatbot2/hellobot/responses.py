from simple_chatbot.responses import GenericRandomResponse


class GreetingResponse(GenericRandomResponse):
    choices = ("Hey, how can I help you?",
               "Hey, How are you? How can I help you?")


class GoodbyeResponse(GenericRandomResponse):
    choices = ("See you later.",
               "Thanks for visiting.",
               "See ya! Have a nice day.")

class ProductResponse(GenericRandomResponse):
    choices = ("We Have Training Bench,Dumbbell Set,Barbell Set,Pull-Up Frame and Bar,Treadmill,Rowing Machine",
    " Things in our store are Training Bench,Dumbbell Set,Barbell Set,Pull-Up Frame and Bar,Treadmill,Rowing Machine and much more","You Buy Training Bench,Dumbbell Set,Barbell Set,Pull-Up Frame and Bar,Treadmill,Rowing Machine")    

class StoreResponse(GenericRandomResponse):
    choices = ("This is the store to buy all your home workout fitness equipment ",
    "This is a Fitness equipment Store","You can but all kinds of fitness equipments in this store") 

class PriceResponse(GenericRandomResponse):
    choices = ("The price of every product could be viewed on the product page.",
               "Prices of the products is mensioned in the project page.",
               "The product page shows the price of all the products.")              

class ContactResponse(GenericRandomResponse):
    choices = ("The contact information about the store is available in the contact page.",
               "Please look at the contact page to get in touch with the management .",
               "Contact information could be found in the contact information page.")  