class MultipleChoiceHandler:

    def __init__(self, message, answer, user):
        # Begrundung + permissions
        self.message = message
        self.user = user

        # Hangi soruya cevap verdigi
        self.answer = answer

        self.switcher = {
            "Welche Berechtigungen benötigen sie für " + user.profile.application + " ?": self.permission,
            "Ich habe Sie nicht verstanden. Haben Sie ein Problem mit dem Client?": self.clientfehler
        }
        self.necessary = self.switcher[message](answer)

        # begrundung / W,X

        # Benutzer user mochte W,X  fur applikation. begrundung : .

    def permission(self):
        print("Hello Sedat")

    def clientfehler(self):
        print("Hello Sedat")

        if self.message == "Ja":
            x = {
                "antwort": "Führen Sie einen Workspace cleanup durch",
                "message": self.answer,
                "isMultiple": 0
            }
            return x
        else:
            x = {
                "antwort": "Bitte spezifizieren Sie Ihr Problem.",
                "message": self.answer,
                "isMultiple": 0
            }
            return x
