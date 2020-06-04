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
        self.necessary = self.switcher[answer]()

        # begrundung / W,X

        # Benutzer user mochte W,X  fur applikation. begrundung : .

    def permission(self):
        print(self.answer)

        split = self.answer.split("/")
        begrundung = split[0].strip()
        permissions = split[1].strip()

        # todo: split the message up in requestedPermissions + reasoning --> save in user.profile.requestedPermissions & user.profile.reasoning
        # todo: Create "ticket" table:
        """
            ticket:
                id: int
                user_id: user.id
                intent: varchar
                application: varchar
                requestedPermissions: varchar
                reasoning: varchar
                ticketcreationdate: date
        """

        # todo: save the request accordingly as a ticket in the database
        """
            --> id: A_I
            --> user_id: user.profile.id
            --> intent: user.profile.intent
            --> application: user.profile.application
            --> requestedPermissions: user.profile.permissions
            --> reasoning: user.profile.reasoning
            --> ticketcreationdate: getTime(now)
        """
        x = {
            "antwort": "Wir haben Ihnen folgende Berechtigungen gegeben: " + self.answer + ". Es wurde ein Ticket mit folgender ID angelegt: (ticket.id).Nähere Details an Ihre hinterlegte Mail versendet.",
            "message": self.answer,
            "isMultiple": 0
        }
        emailcontent = x[0]

        return x

    def clientfehler(self):

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
