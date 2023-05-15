import random
print("Welcome to my MCU quiz!")
num = input("How many Marvel Cinematic Universe movies have you watched?: ")
ans = input('Are you ready to play the Quiz ? (yes/no): ')
count = 0
count1 = 0
class Question:
    def __init__(self, questionText, answer, multipleChoice=None):
        self.questionText = questionText
        self.answer = answer
        self.multipleChoice = multipleChoice
    def __repr__(self):
        return '{'+ self.questionText +', '+ self.answer +'}'

quizQuestions = [
    Question("Question. What was the first Marvel Cinematic Universe Movie?: ","a" ,["(a) ironman ""(b) hulk ""(c) spider-man ""(d) captain america"]),
    Question("Question. When was Spider-Man Homecoming released?: ",'d' ,['(a) 2019 ''(b) 2015 ''(c) 2022 ''(d) 2017']),
    Question("Question. Who plays Natasha Romanoff and Black Widow?: ",'b' ,['(a) elizabeth olsen ''(b) scarlett johansson ''(c) zendaya ''(d) paul raud',]),
    Question("Question. Who is the king of Wakanda?: ",'a' ,['(a) tchalla ''(b) kilmonger ''(c) star lord ''(d) thanos']),
    Question("Question. How many infinity stones did Thanos have in Infinity War?: ",'c' ,['(a) 10 ''(b) 5 ''(c) 6 ''(d) 2']),
    Question("Question. How many Avengers movies are there?: ",'c' ,['(a) 23 ''(b) 30 ''(c) 4 ''(d) 12']),
    Question("Question. What is the Hulk's real name?: ",'b' ,['(a) mark rufallo ''(b) bruce banner ''(c) who is the hulk ''(d) jen']),
    Question("Question. Where is Spider-Man from?: ",'d' ,['(a) brooklyn ''(b) london ''(c) california ''(d) queens']),
    Question("Question. How many Thor movie's are there as of 2023?: ",'a' ,['(a) 4 ''(b) 3 ''(c) 1 ''(d) there are no thor movies']),
    Question("Question. What universe is Tony Stark's Iron Man from?: ",'b' ,['(a) 111 ''(b) 616 ''(c) there is only one universe ''(d) huh?']),
    Question("Question. What is Captain America's shield made out of?: ",'c' ,['(a) titanium ''(b) copper ''(c) vibranium ''(d) paper']),
    Question("Question. How many people have lifted Thor's hammer?: ",'d' ,['(a) only thor ''(b) 10 ''(c) 4 ''(d) 5'])
]
while ans.lower() == 'yes':
    numPlayer = int(input('Enter numbers of Players (1-2): '))
    while numPlayer == 1:
        playerName1 = input('Enter player name: ')
        for question in quizQuestions:
            random.shuffle(quizQuestions)
            print(question.questionText)
            #quizQuestions.remove(question)
            for choice in question.multipleChoice:
                print(choice)
                userInput = input('Answer: ')
            if userInput.lower() == question.answer.lower():
                count+=1
                print("That is correct! Your score is:",count)
            else:
                print("Sorry, the correct answer is", question.answer, ".")
        print('Your final score is: ',count)
        ans = input('Would you like to play again (yes/no): ')
        break
    if numPlayer == 2:
        playerName2 = input('Enter player 1 name: ')
        playerName3 = input('Enter player 2 name: ')
        for question in quizQuestions:
            random.shuffle(quizQuestions)
            print(question.questionText)
            for choice in question.multipleChoice:
               print(choice)
               userInput = input('Answer: ')
            if userInput.lower() == question.answer.lower():
                count+=1
                print("That is correct! Your score is:",count)
            else:
                print("Sorry, the correct answer is", question.answer, "." ,"Your score is:",count)
        print(playerName2,'your final score is:',count)
        print(playerName3, 'your turn')
        for question in quizQuestions:
            random.shuffle(quizQuestions)
            print(question.questionText)
            for choice in question.multipleChoice:
               print(choice)
               userInput = input('Answer: ')
            if userInput.lower() == question.answer.lower():
                count1+=1
                print("That is correct! Your score is:",count1)
            else:
                print("Sorry, the correct answer is", question.answer, "." ,"Your score is:",count1)
        print(playerName3,'your final score is: ',count1)
        if count1 == count:
            print("It's a draw!!")
        elif count1 > count:
            print(playerName3, 'won!!')
        elif count1 < count:
            print(playerName2, 'won!!')
        ans = input('Would you like to play again (yes/no): ')
        break
    else:
        print('Invalid. Try again!')
while ans == 'no':
    simulationPlay = input('Would you like to view how to play (yes/no): ')
    while simulationPlay.lower() == 'yes':
        print('******************************How to Play**************************')
        print('The game is simple, you are given a question')
        print('When was Ironman released?: ')
        print('')
        print('Your options will be displayed')
        print('(a) 2005','(b) 2000','(c) 2009','(d) 2008')
        print('')
        print('Your chosen answer will be displayed')
        print('Answer: c')
        print('')
        print('If your answer is correct, the following will be displayed')
        print("That is correct! Your score is: 1")
        print('')
        print('Answer: d')
        print('If your answer is incorrect,  the following will be displayed')
        print("Sorry, the correct answer is c. Your score is: 0")
        break
    while simulationPlay.lower() == 'no':
        print('Goodbye')
        break        
    break
