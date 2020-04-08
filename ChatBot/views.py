from django.shortcuts import render
from django.shortcuts import HttpResponse
from wit import Wit
import ast
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

response = {}

intent = ""
message = ""

vergessenesElement = ""
zustand = ""
contact = ""
objekt = ""


@csrf_exempt
def ChatBotMessage(request):
    global message
    global intent
    global response

    actualText = json.loads(request.body)
    client = Wit('HFLSFMYE7ZZCYSHSFAAWMGDAEJ237CWO')
    message = actualText["chat"]

    resp = client.message(message)
    x = str(resp)
    y = ast.literal_eval(x)
    response = y

    # Wie werden Funktionen benutzen.
    switcher = {
        "sonstiges": sonstiges,
        "zuruecksetzen": zuruecksetzen,
        "begruessung": begruessung,
        "anmeldeprobleme": anmeldeprobleme
    }

    # intent = y["entities"]["intent"][0]["value"]
    if y.get("entities").get("intent") is None:

        x = {
            "antwort": "Ich kann Sie nicht verstehen",
            "message": message
        }
        return HttpResponse(json.dumps(x))
    else:
        intent = y.get("entities").get("intent")[0].get("value")
        antwort = switcher[intent]

        z = json.dumps(antwort())

        return HttpResponse(z)


def zuruecksetzen():
    global vergessenesElement

    if "vergessenesElement" in response.get("entities"):
        vergessenesElement = response.get("entities").get("vergessenesElement")[0].get("value")

    if vergessenesElement != "":
        antwort = "Um Ihr %s zurückzusetzen, folgen Sie folgenden Anweisungen unter www.mercedes.com.tr/%s-zurucksetzen" % (
            vergessenesElement, vergessenesElement)
    else:
        antwort = "Um Ihr %s zurückzusetzen, folgen Sie folgenden Anweisungen unter www.mercedes.com.tr/%s-zurucksetzen" % (
            objekt, objekt)
    x = {
        "antwort": antwort,
        "message": message
    }
    return x


def sonstiges():
    global objekt
    global zustand
    global contact
    global vergessenesElement

    antwort = "Ich habe Sie nicht verstanden"

    x = {
        "antwort": antwort,
        "message": message
    }

    if "objekt" in response.get("entities"):
        objekt = response.get("entities").get("objekt")[0].get("value")
        antwort = "Was für ein Problem haben Sie mit ihren %s" % (objekt)
        x = {
            "antwort": antwort,
            "message": message
        }
    if "vergessenesElement" in response.get("entities"):
        vergessenesElement = response.get("entities").get("vergessenesElement")[0].get("value")
        antwort = "Was für ein Problem haben Sie mit ihren %s" % (vergessenesElement)
        x = {
            "antwort": antwort,
            "message": message
        }
    if "zustand" in response.get("entities") and objekt != "":
        zustand = response.get("entities").get("zustand")[0].get("value")

        antwort = "Ist dein %s %s?" % (objekt, zustand)
        x = {
            "antwort": antwort,
            "message": message
        }

    if "contact" in response.get("entities"):
        contact = response.get("entities").get("contact")[0].get("value")

    return x


def begruessung():
    antwort = "Hallo! Wie kann ich Ihnen helfen?"
    x = {
        "antwort": antwort,
        "message": message
    }
    return x


def anmeldeprobleme():
    antwort = ""


@csrf_exempt
def registeruser(request):
    user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    user.last_name = 'Lennon'
    user.save()


def loginchat(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.

    else:
        # Return an 'invalid login' error message.
        ...
