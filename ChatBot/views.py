import json

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import ChatBot.models as models
from rest_framework.status import (
    HTTP_200_OK
)

from ChatBot.EmailHandler import EmailHandler
from ChatBot.JsonHandler import JsonHandler

response = {}


@csrf_exempt
@api_view(["POST"])
def ChatBotMessage(request):
    user = request.user
    # print(user.username)
    # Get message from Vue
    jsonHandler = JsonHandler()
    actualText = json.loads(request.body)
    jsonHandler.setupParameters(actualText, user)

    return HttpResponse(jsonHandler.getResult())


@csrf_exempt
def registeruser(request):
    user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    user.last_name = 'Lennon'
    user.save()


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def loginchat(request):
    # Get message from Vue
    actualText = json.loads(request.body)
    username = actualText['username']
    password = actualText['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key},
                        status=HTTP_200_OK)
    else:
        # Return an 'invalid login' error message.
        return Response({'message': "Username or password is false"},
                        status=HTTP_200_OK)

@api_view(["GET"])
@permission_classes((AllowAny,))
def test(request):
    EmailHandler(models.Ticket.objects.get(ticketID="25555"))
    return Response({'message': "Successfully executed TEST block"},
                    status=HTTP_200_OK)
