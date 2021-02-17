# Create your classes here
class Student(object):
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        answer = input("f{self.question} >")
        if answer == self.correct_answer:
            return True
        else:
            return False


class Exam(object):

    self.questions = []

    def __init__(self, name):
        self.name = name
        
    def add_question():
        self.questions.append(Question)



alberta_capital = Question("What is the capital of Alberta?", "Edmonton")
python_author = Question("Who is the author of Python?", "Guido Van Rossum")