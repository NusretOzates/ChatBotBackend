import ast

from wit import Wit

from ChatBot.ChatHandler import ChatHandler
from ChatBot.MultipleChoiceHandler import MultipleChoiceHandler


class JsonHandler:
    client = Wit('HFLSFMYE7ZZCYSHSFAAWMGDAEJ237CWO')
    chatHandler = ChatHandler()

    message = ""
    ismultiple = False
    answer = ""
    user = ''

    def setupParameters(self, json, user):
        self.message = json.get("chat")  # answer
        self.ismultiple = json.get("multiple")
        self.answer = json.get("answer")  # neye Ja nein
        self.user = user

        self.user.profile.message = self.message
        self.user.profile.save()

    def getResult(self):
        if self.ismultiple is not None and self.ismultiple:
            return self.multiple()
        else:
            return self.chat()

    def multiple(self):
        handler = MultipleChoiceHandler(self.message, self.answer, self.user)
        return handler.necessary

    def chat(self):
        response = self.client.message(self.message)
        x = str(response)
        response = ast.literal_eval(x)
        self.user.profile.response = response

        self.chatHandler.setupParameters(self.user)

        return self.chatHandler.getResult()
