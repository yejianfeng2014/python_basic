from survey import AnonymousSurvey


#定义一个问题，并创建一个表示调查的AnonymousSurvey对象

question = 'what language do you like ?'

my_survery = AnonymousSurvey(question)

#显示问题并存储答案
my_survery.show_questions()

print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survery.store_question(response)