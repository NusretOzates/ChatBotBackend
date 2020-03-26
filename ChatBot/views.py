from django.shortcuts import render
from django.shortcuts import HttpResponse
from MachineLearning import sumNums
from wit import  Wit
import ast


# Create your views here.

def ChatBotMessage(request):

    client = Wit('HFLSFMYE7ZZCYSHSFAAWMGDAEJ237CWO')
    resp = client.message("Hello World")
    x = str(resp)
    y = ast.literal_eval(x)

    return HttpResponse(y["entities"])
