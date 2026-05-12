import requests
import html

class Question:
    def __init__(self, category, questionStr, correctAnswerFlag):
        self.category = category
        self.questionStr = questionStr
        self.correctAnswerFlag = correctAnswerFlag

class Quiz:
    def __init__(self, numQuestions):
        self.apiUrl = "https://opentdb.com/api.php?difficulty=easy&type=boolean&amount="
        self.numQuestions = numQuestions
        self.questionsList = []
        self.loadQuestions (numQuestions)

    def loadQuestions (self, numQuestions):
        response = requests.get (self.apiUrl + str (numQuestions))
        # {'response_code': 0, 'results': [{'type': 'boolean', 'difficulty': 'easy', 'category': 'Geography', 'question': 'Bosnia and Herzegovina is a country located in the Baltic region in Europe.', 'correct_answer': 'False', 'incorrect_answers': ['True']}, {'type': 'boolean', 'difficulty': 'easy', 'category': 'General Knowledge', 'question': 'The National Animal of Scotland is the Unicorn.', 'correct_answer': 'True', 'incorrect_answers': ['False']}, {'type': 'boolean', 'difficulty': 'easy', 'category': 'Science &amp; Nature', 'question': 'A plant that has a life cycle for more than a year is known as an annual.', 'correct_answer': 'False', 'incorrect_answers': ['True']}, {'type': 'boolean', 'difficulty': 'easy', 'category': 'General Knowledge', 'question': 'Adolf Hitler was born in Australia. ', 'correct_answer': 'False', 'incorrect_answers': ['True']}, {'type': 'boolean', 'difficulty': 'easy', 'category': 'Mythology', 'question': 'In the Greek Mythology, the god of war is called Mars.', 'correct_answer': 'False', 'incorrect_answers': ['True']}, {'type': 'boolean', 'difficulty': 'easy', 'category': 'Geography', 'question': 'Africa is a country.', 'correct_answer': 'False', 'incorrect_answers': ['True']}, {'type': 'boolean', 'difficulty': 'easy', 'category': 'General Knowledge', 'question': 'Romanian belongs to the Romance language family, shared with French, Spanish, Portuguese and Italian. ', 'correct_answer': 'True', 'incorrect_answers': ['False']}, {'type': 'boolean', 'difficulty': 'easy', 'category': 'Vehicles', 'question': 'The full English name of the car manufacturer BMW is Bavarian Motor Works', 'correct_answer': 'True', 'incorrect_answers': ['False']}, {'type': 'boolean', 'difficulty': 'easy', 'category': 'Politics', 'question': 'In 2016, the United Kingdom voted to stay in the EU.', 'correct_answer': 'False', 'incorrect_answers': ['True']}, {'type': 'boolean', 'difficulty': 'easy', 'category': 'General Knowledge', 'question': 'Dihydrogen Monoxide was banned due to health risks after being discovered in 1983 inside swimming pools and drinking water.', 'correct_answer': 'False', 'incorrect_answers': ['True']}]}
        if response.ok:
            data = response.json ()
            results = data ["results"]
            for q in results:
                category = q["category"]
                questionType = q ["type"]
                difficulty = q ["difficulty"]
                questionStr = q ["question"]
                questionStr = html.unescape (q["question"])
                print (questionStr)
                correctAnswerFlag = q ["correct_answer"].lower () in ["true", "1", "yes"]
                qObj = Question (category, questionStr, correctAnswerFlag)
                self.questionsList.append (qObj)

    def startQuiz (self):
        print ("\n Welcome in Quiz")
        numCorrectUserAnswers = 0
        n = 0
        numQuestion = len (self.questionsList)

        while n<numQuestion :
            q = self.questionsList [n]
            print ("Quesion Number: " + str(n+1) + " " + q.questionStr)
            n+=1
            answer = input ("Give correct answer as yes or no: ")
            answerBool = False
            if answer == "yes":
                answerBool = True
            if answerBool == q.correctAnswerFlag:
                print ("Correct")
                numCorrectUserAnswers += 1
            else:
                print ("Not correct")
        
        print ("Number of correct answers: ", numCorrectUserAnswers, " from: ", len (self.questionsList), "questions")


quiz = Quiz (10)
quiz.startQuiz ()