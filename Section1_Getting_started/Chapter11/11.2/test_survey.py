# coding=utf-8

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """specific test for AnonymousSurvey"""
    def test_store_single_response(self):
        """test single answer which can be stored properly"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('Chinese')

        self.assertIn('Chinese', my_survey.responses)

    def test_store_three_responses(self):
        """ test 3 answers which can be stored properly"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Chinese']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)


unittest.main()












