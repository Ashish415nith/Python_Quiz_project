from User import Examiner,Candidate

e1=Examiner("Honey singh",420)
print(e1)
e1.addQuestion("gk","easy")
e1.addQuestion("sports","medium")
e1.addQuestion("Python","difficult")
e1.displayAllQuestions()

c1=Candidate("Babu mann",111)
print(c1)
c1.viewTopics()
c1.run_test()
