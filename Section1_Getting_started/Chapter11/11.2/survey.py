# coding=utf-8

class AnonymousSurvey():
    """ collect the anonymous-survey's response"""


    def __init__(self, question):
        """ store a question, and prepare for storage the answer"""
        self.question = question
        self.responses = []

    def show_question(self):
        """ show question"""
        print(self.question)

    def store_response(self, new_response):
        """ store single response"""
        self.responses.append(new_response)

    def show_results(self):
        """ show all collected results"""
        print("Survey results: ")
        for response in self.responses:
            print(' - ' + response)

"""
test = AnonymousSurvey("What's your name?")

print(test.question)

"""


