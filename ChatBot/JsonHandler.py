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

    def setupParameters(self, json):
        self.message = json["chat"]
        self.ismultiple = json["multiple"]
        self.answer = json["answer"]

    def getResult(self):
        if self.ismultiple:
            return self.multiple()
        else:
            return self.chat()

    def multiple(self):
        handler = MultipleChoiceHandler(self.message, self.answer)
        return handler.necessary

    def chat(self):
        response = self.client.message(self.message)
        x = str(response)
        response = ast.literal_eval(x)
        self.chatHandler.setupParameters(response, self.message)

        return self.chatHandler.getResult()
