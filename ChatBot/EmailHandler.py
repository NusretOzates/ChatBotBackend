import json
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
# todo: send out an email to request-opening-person --> standardemail: requesthandler@daimler.com
# todo: send out an email to request-handling-person --> pull e-mail from database (user.profile.email)
# todo: Format for Email:
from django.core.mail import send_mail
import ChatBot.models as models

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
        def __init__(self,ticket,user):
                self.user = user
                self.sendEmail(ticket,self.user)
        def sendEmail(self,ticket,user):
                print("Test1")
                user2 = user
                #user2 = models.User.objects.get(username = "admin")
                emessage = "Sehr geehrter Herr/Frau " + user2.last_name.capitalize() + "\n\n" \
                "hiermit bestätigen wir den Eingang Ihres Supporttickets. Das Ticket mit der Kennnummer " + ticket.ticketID + " "\
                "wird sobald wie möglich bearbeitet.\n\nIhr Anliegen: " + ticket.intent + ", Programm: " + ticket.application + ", Beantragte Rechte: " + ticket.requestedPermissions + ", Grund: "+ ticket.reasoning + "\n" \
                "Ihre User-ID: "+ user2.username.upper() +"\n\nDas Ticket wird sobald wie möglich von unserem Support Team bearbeitet. Die übliche " \
                "Bearbeitungszeit beträgt 2-3 Werktage. Falls Sie bis dahin keine Rückmeldung von unserem Team erhalten haben, können Sie sich per E-Mail " \
                "erneut an support@mercedes.com wenden.\nDies ist eine automatisch generierte E-Mail. Bitte antworten Sie NICHT auf diese E-Mail\n\nVielen Dank für Ihre Geduld\n\n\n" \
                "Mit freundlichen Grüßen\n\n" \
                "Chatbotcan"
                send_mail(subject="Ihr Ticket mit der ID " + ticket.ticketID + " wird bearbeitet.", message=emessage , from_email="hatipdev@gmail.com", recipient_list = [user2.email], fail_silently=False)
