from django.shortcuts import render
from django.shortcuts import HttpResponse
from wit import Wit
import ast
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def ChatBotMessage(request):

    text = request.POST["chat"]
    client = Wit('HFLSFMYE7ZZCYSHSFAAWMGDAEJ237CWO')
    resp = client.message(text)
    x = str(resp)
    y = ast.literal_eval(x)

    intent = y["entities"]["intent"][0]["value"]
    subValue = y["entities"]["vergessenesElement"][0]["value"]


    switcher = {
        "zuruecksetzen" : "Um Ihr Passwort zurückzusetzen, folgen Sie folgenden Anweisungen unter www.mechatroniker.com.tr/pw-zurucksetzen",
        "begruessung" : "Hallo, ich bin Chatbotcan, wie kann ich Ihnen behilflich sein?",
        "anmeldeprobleme" : "Falls Sie Probleme mit dem Anmelden in das Intranet haben, benötigen Sie Ihre Daimler-Nutzerkennung, die Sie durch ein anderes Teammitglied erfahren können. Anschließend können Sie über www.mechatroniker.com.tr/pw-zurucksetzen Ihr Passwort zurücksetzen"
    }


    return HttpResponse(switcher[intent])
