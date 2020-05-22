import json


# 0 -> Multiple degil  1 -> Ja nein 2 -> checkbox

class ChatHandler:
    profile = ''

    def setupParameters(self, user):
        self.profile = user.profile

    def getResult(self):
        # Wie werden Funktionen benutzen.
        switcher = {
            "sonstiges": self.sonstiges,
            "zuruecksetzen": self.zuruecksetzen,
            "begruessung": self.begruessung,
            "anmeldeproblem": self.anmeldeprobleme,
            "cleanupWorkspace": self.cleanup,
            "entsperren": self.entsperren,
            "berechtigung": self.berechtigung
        }

        # Get intent from self.response
        if self.profile.response.get("entities").get("intent") is None:
            # We don't know the user intent
            x = {
                "antwort": "Ich kann Sie nicht verstehen",
                "message": self.profile.message,
                "isMultiple": 0
            }
            return json.dumps(x)
        else:
            self.profile.intent = self.profile.response.get("entities").get("intent")[0].get("value")
            self.profile.save()
            # Necessary function to use intent
            antwort = switcher[self.profile.intent]

            # Result of intent
            return json.dumps(antwort())

    def berechtigung(self):

        antwort = ''

        if 'applikation' in self.profile.response.get('entities'):

            self.profile.application = self.profile.response.get('entities').get('application')[0].get('value')
            self.profile.save()
            antwort = "Welche Berechtigungen benötigen sie für " + self.profile.application + " ?"
            x = {
                "antwort": antwort,
                "message": self.profile.message,
                "isMultiple": 2
            }
            return x

        elif self.profile.application != "":
            antwort = "Welche Berechtigungen benötigen sie für " + self.profile.application + " ?"
            x = {
                "antwort": antwort,
                "message": self.profile.message,
                "isMultiple": 2
            }
            return x
        else:

            antwort = 'Auf Welche Applikation mochten sie zugreifen'
            x = {
                "antwort": antwort,
                "message": self.profile.message,
                "isMultiple": 0
            }
            return x

    def cleanup(self):

        antwort = ''
        if "objekt" in self.profile.response.get("entities"):
            self.profile.objekt = self.profile.response.get("entities").get("objekt")[0].get("value")
            self.profile.save()
            if self.profile.objekt == "Client":
                # Todo did it work button?
                antwort = "Führen Sie einen Workspace cleanup durch"
            else:
                # todo : Button Yes No
                antwort = "Ich habe Sie nicht verstanden. Haben Sie ein Problem mit dem Client?"

            x = {
                "antwort": antwort,
                "message": self.profile.message,
                "isMultiple": 1
            }
            return x

        return {
            "antwort": "Ich habe Sie nicht verstanden.",
            "message": self.profile.message,
            "isMultiple": 0
        }

    # User wants to change Username or Password
    def zuruecksetzen(self):
        antwort = "Ich kann sie nicht verstehen"
        print(self.profile.objekt)

        if "objekt" in self.profile.response.get("entities"):
            self.profile.objekt = self.profile.response.get("entities").get("objekt")[0].get("value")
            self.profile.save()

            antwort = "Um Ihr %s zurückzusetzen, folgen Sie folgenden Anweisungen unter " \
                      "www.mercedes.com.tr/%s-zurucksetzen" % (
                          self.profile.objekt, self.profile.objekt)

        # Eger objekt yoksa ne diyecegiz?
        elif self.profile.objekt != "":

            antwort = "Um Ihr %s zurückzusetzen, folgen Sie folgenden Anweisungen unter " \
                      "www.mercedes.com.tr/%s-zurucksetzen" % (
                          self.profile.objekt, self.profile.objekt)

        else:
            antwort = 'Ich habe Sie nicht verstanden'

        x = {
            "antwort": antwort,
            "message": self.profile.message,
            "isMultiple": 0
        }
        return x

    def entsperren(self):

        if "objekt" in self.profile.response.get("entities"):
            self.profile.objekt = self.profile.response.get("entities").get("objekt")[0].get("value")
            self.profile.save()
            antwort = "Um Ihr Konto zu entsperren, wenden Sie sich an Technical Support"

            x = {
                "antwort": antwort,
                "message": self.profile.message,
                "isMultiple": 0
            }
            return x

    def sonstiges(self):

        antwort = "Ich habe Sie nicht verstanden"

        x = {
            "antwort": antwort,
            "message": self.profile.message,
            "isMultiple": 0
        }

        if 'applikation' in self.profile.response.get("entities"):
            self.profile.application = self.profile.response.get("entities").get("applikation")[0].get("value")
            self.profile.save()
            self.berechtigung()

        if "objekt" in self.profile.response.get("entities"):
            self.profile.objekt = self.profile.response.get("entities").get("objekt")[0].get("value")
            self.profile.save()

            antwort = "Was für ein Problem haben Sie mit ihren %s" % self.profile.objekt
            x = {
                "antwort": antwort,
                "message": self.profile.message,
                "isMultiple": 0
            }
        if "zustand" in self.profile.response.get("entities") and self.profile.objekt != "":
            self.profile.zustand = self.profile.response.get("entities").get("zustand")[0].get("value")
            self.profile.save()

            antwort = "Ist dein %s %s?" % (self.profile.objekt, self.profile.zustand)
            x = {
                "antwort": antwort,
                "message": self.profile.message,
                "isMultiple": 0
            }
        return x

    def begruessung(self):
        antwort = "Hallo! Wie kann ich Ihnen helfen?"
        x = {
            "antwort": antwort,
            "message": self.profile.message,
            "isMultiple": 0
        }
        return x

    def anmeldeprobleme(self):
        antwort = ""
