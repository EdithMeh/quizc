from argparse import Namespace

import json
from quizc.console.quiz_ui_handler import *
from quizc.model.quiz import MyEncoder
from quizc.utils.Constans import path


class Menu(object):
    MENU_PROMPT = "> "

    def __init__(self):
        self.car = ""
        self.quiz = None
        self.quiz_answers = None

    def show_main_menu(self):
        print("""
Quizc - A command quiz utility
======================================
1. Create quiz
2. Fill quiz
3. Show quiz
4. Load quiz
5. Exit
======================================
        """)

    def createQuiz(self):
        self.quiz = QuizUIHandler.create_quiz()
        json = MyEncoder().encode(self.quiz)
        f = open(path+self.quiz.title+".json", "w")
        f.write(json)
        f.close()
        return False

    def fillQuiz(self):
        if self.quiz is None:
            print("No quiz available, you must create first a quiz")
        else:
            self.quiz_answers = QuizUIHandler.fill_quiz(self.quiz)
        return False

    def showQuiz(self):
        if self.quiz_answers is None:
            print("No filled quiz available, you must create first a quiz")
        else:
            QuizUIHandler.show_quiz(self.quiz_answers)
        return False

    def loadQuiz(self):
        print("Name of saved quiz: ")
        try:
            f = open(path+'INJSON.json', )
            data = json.load(f)
            jtopy = json.dumps(data)
            self.quiz = json.loads(jtopy)
            f.close()
        except:
            print("file not found")
        return False

    def exit(self):
        return True

    def process(self):
        self.show_main_menu()
        option = input(self.MENU_PROMPT)
        switcher = {
            "1": self.createQuiz,
            "2": self.fillQuiz,
            "3": self.showQuiz,
            "4": self.loadQuiz,
            "5": self.exit
        }
        # Get the function from switcher dictionary
        func = switcher.get(option, lambda: print("Invalid option"))
        should_exit = func()
        return should_exit
