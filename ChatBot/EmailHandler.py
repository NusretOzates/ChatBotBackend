import json
from django.contrib.auth.models import User
# todo: send out an email to request-opening-person --> standardemail: requesthandler@daimler.com
# todo: send out an email to request-handling-person --> pull e-mail from database (user.profile.email)
# todo: Format for Email:
"""
    Sehr geehrter Herr/Frau Hatip (User.last_name.capitalize())

    hiermit bestätigen wir den Eingang Ihres Supporttickets. Das Ticket mit der Kennnummer 2838332 (ticket.ID) wird sobald wie möglich bearbeitet.

    Ihr Anliegen: Berechtigung (intent + objekt --> premade messages), Programm: SAP, Rechte: X, Y, Z
    Ihre User-ID: HATIPSE (User.userID)

    Das Ticket wird sobald wie möglich von unserem Support Team bearbeitet. Die übliche Bearbeitungszeit beträgt 2-3 Werktage. Falls Sie bis dahin keine
    Nachricht von unserem Team erhalten haben, können Sie sich per E-Mail erneut an support@mercedes.com (managingRecipient) wenden.

    Vielen Dank für Ihre Geduld.


    Mit freundlichen Grüßen

    Chatbotcan

"""


class EmailHandler:
        def __init__(self,ticket):
                print("Hallo")
