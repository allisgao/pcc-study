# coding=utf-8

from survey import AnonymousSurvey

# 定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# show question and store the answer
my_survey.show_question()
print("Enter q to exit\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# show results
print("\nThank you to everyone who participated in my survey!")
my_survey.show_results()
