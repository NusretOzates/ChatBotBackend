import json


class ChatHandler:
    intent = ""
    response = ''
    message = ''

    vergessenesElement = ""
    zustand = ""
    objekt = ""

    def setupParameters(self, response, message):
        self.response = response
        self.message = message

    def getResult(self):
        # Wie werden Funktionen benutzen.
        switcher = {
            "sonstiges": self.sonstiges,
            "zuruecksetzen": self.zuruecksetzen,
            "begruessung": self.begruessung,
            "anmeldeproblem": self.anmeldeprobleme,
            "cleanupWorkspace": self.cleanup,
            "entsperren": self.entsperren
        }

        # Get intent from self.response
        if self.response.get("entities").get("intent") is None:
            # We don't know the user intent
            x = {
                "antwort": "Ich kann Sie nicht verstehen",
                "message": self.message
            }
            return json.dumps(x)
        else:
            self.intent = self.response.get("entities").get("intent")[0].get("value")
            # Necessary function to use intent
            antwort = switcher[self.intent]

            # Result of intent
            return json.dumps(antwort())

    def cleanup(self):

        antwort = ''
        if "objekt" in self.response.get("entities"):
            self.objekt = self.response.get("entities").get("objekt")[0].get("value")
            if self.objekt == "Client":
                # Todo did it work button?
                antwort = "Führen Sie einen Workspace cleanup durch"
            else:
                # todo : Button Yes No
                antwort = "Ich habe Sie nicht verstanden. Haben Sie ein Problem mit dem Client? "

            x = {
                "antwort": antwort,
                "message": self.message
            }
            return x

        return {
            "antwort": "Ich habe Sie nicht verstanden.",
            "message": self.message
        }

    # User wants to change Username or Password
    def zuruecksetzen(self):

        if "vergessenesElement" in self.response.get("entities"):
            self.vergessenesElement = self.response.get("entities").get("vergessenesElement")[0].get("value")
            antwort = "Um Ihr %s zurückzusetzen, folgen Sie folgenden Anweisungen unter www.mercedes.com.tr/%s-zurucksetzen" % (
                self.vergessenesElement, self.vergessenesElement)

        else:
            antwort = "Um Ihr %s zurückzusetzen, folgen Sie folgenden Anweisungen unter www.mercedes.com.tr/%s-zurucksetzen" % (
                self.objekt, self.objekt)

        x = {
            "antwort": antwort,
            "message": self.message
        }
        return x

    def entsperren(self):

        if "objekt" in self.response.get("entities"):
            self.objekt = self.response.get("entities").get("objekt")[0].get("value")
            antwort = "Um Ihr Konto zu entsperren, wenden Sie sich an Technical Support"

            x = {
                "antwort": antwort,
                "message": self.message
            }
            return x

    def sonstiges(self):

        antwort = "Ich habe Sie nicht verstanden"

        x = {
            "antwort": antwort,
            "message": self.message
        }

        if "objekt" in self.response.get("entities"):
            self.objekt = self.response.get("entities").get("objekt")[0].get("value")
            antwort = "Was für ein Problem haben Sie mit ihren %s" % (self.objekt)
            x = {
                "antwort": antwort,
                "message": self.message
            }
        if "vergessenesElement" in self.response.get("entities"):
            self.vergessenesElement = self.response.get("entities").get("vergessenesElement")[0].get("value")
            antwort = "Was für ein Problem haben Sie mit ihren %s" % (self.vergessenesElement)
            x = {
                "antwort": antwort,
                "message": self.message
            }
        if "zustand" in self.response.get("entities") and self.objekt != "":
            self.zustand = self.response.get("entities").get("zustand")[0].get("value")

            antwort = "Ist dein %s %s?" % (self.objekt, self.zustand)
            x = {
                "antwort": antwort,
                "message": self.message
            }
        return x

    def begruessung(self):
        antwort = "Hallo! Wie kann ich Ihnen helfen?"
        x = {
            "antwort": antwort,
            "message": self.message
        }
        return x

    def anmeldeprobleme(self):
        antwort = ""
