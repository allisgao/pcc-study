# coding=utf-8


import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """ specify to AnonymousSurvey-class's test"""

    def setUp(self):
        """
        create an object surveyed and a group of answers, for testing-methon using
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Chinese', 'English', 'American-English']

    def test_store_single_response(self):
        """test if single response can be stored properly"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """ test if three responses can be stored properly"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()




