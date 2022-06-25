# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import time

def QAndA():
    question = open("Question.txt", "r+")
    questions = []
    answer = open("Answer.txt", "r+")
    answers = []
    for line in question.readlines():
        line = line.strip()
        if len(line) > 0:
            questions.append(line)
    for line in answer.readlines():
        line = line.strip()
        if len(line) > 0:
            answers.append(line)
    print(answers)
    print(questions)
    print("Hi")
    time.sleep(1)
    print("I'm the Q&A server~")
    asking = input("What's your question?")
    sequence = 0
    for q in questions:
        if q == asking:
            print("Oh!\nI know!")
            time.sleep(1)
            print(answers[sequence])
            return 0
        else:
            sequence = sequence+1
    time.sleep(2)
    print("Ummm, It's a tough one!\nI bet you know the answer!")
    newanswer = input("The answer: ")
    answer.writelines(newanswer+"\n")
    question.writelines(asking+"\n")
    answer.close()
    question.close()





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    QAndA()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
