
class AnonymousSurvey():
    def __init__(self,question):
        self.question = question
        self.response = []

    def show_questions (self):
        '''显示调查问卷'''
        print(self.question)

    def store_question(self,new_responese):
        '''存储'''
        self.response.append(new_responese)
    def show_results(self):
        '''显示所有调查的答案'''
        print('answers')
        for a in self.response:
            print(a)

