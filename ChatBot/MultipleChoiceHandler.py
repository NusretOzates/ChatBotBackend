class MultipleChoiceHandler:

    def __init__(self, identifier, answer, user):
        self.identifier = identifier
        self.user = user
        self.switcher = {
            "ClientFehler": self.clientfehler
        }
        self.necessary = self.switcher[identifier](answer)

    def clientfehler(self, answer):
        print("Hello Sedat")
