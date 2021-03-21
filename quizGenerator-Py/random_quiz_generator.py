import random

capitals={'Argentina':'Buenos Aires',
'Australia':'Canberra',
'Austria':'Vienna',
'Bangladesh':'Dhaka',
'Belarus':'Minsk',
'Belgium':'Brussels',
'Brazil':'Brasilia',
'Brunei':'Bandar Seri Begawan',
'Cambodia':'Phnom Penh',
'Canada':'Ottawa',
'Central African Republic':'Bangui',
'Chile':'Santiago',
'China':'Beijing',
'Colombia':'Bogota',
'Costa Rica':'San Jose',
'Croatia':'Zagreb',
'Cuba':'Havana',
'Czech Republic':'Prague',
'Denmark':'Copenhagen',
'East Timor':'Dili',
'Ecuador':'Quito',
'Egypt':'Cairo',
'Vietnam':'Hanoi',
'United Arab Emirates (UAE)':'Adu Dhabi',
'France':'Paris',
'Germany':'Berlin',
'Greece':'Athens',
'Singapore':'Singapore',
'Hungary':'Budapest',
'Iceland':'Reykjavik',
'India':'New Delhi',
'Indonesia':'Jakarta',
'Iran':'Tehran',
'Iraq':'Baghdad',
'Ireland':'Dublin',
'Italy':'Rome',
'Japan':'Tokyo',
'Laos':'Vientiane',
'Malaysia':'Kuala Lumpur',
'Mexico':'Mexico City',
'Myanmar':'Nay Pi Taw',
'Netherlands':'Amsterdam',
'New Zealand':'Wellington',
'North Korea':'Pyongyang',
'Philippines':'Manila',
'Poland':'Warsaw',
'Portugal':'Lisbon',
'Russia':'Moscow',
'South Korea':'Seoul',
'Spain':'Madrid',
'Thailand':'Bangkok',
'Turkey':'Ankara',
'Ukraine':'Kiev',
'United Kingdom':'London'}

#Generate 35 quiz files.
for quizNumber in range(35):
    #Create the quiz and answer key files.
    quizFile=open('capitalsquiz%s.txt'%(quizNumber+1),'w')
    answerKeyFile=open('capitalsquiz_answer%s.txt'%(quizNumber+1),'w')
    
    #Write out the header for the quiz.
    quizFile.write('Name:\n\nClass:\n\nDate:\n\n')
    quizFile.write((' '*20)+'State Captitals Quiz (Form %s)'%(quizNumber+1))
    quizFile.write('\n\n')

    #Shuffle the order of the capitals.
    capital=list(capitals.keys())
    random.shuffle(capital)

    #Loop through all 54 capitals, making a question for each.
    questionNumber=0
    for questionNumber in range(54):

        #Get right and wrong answer.
        correctAnswer=capitals[capital[questionNumber]]
        wrongAnswer=list(capitals.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswer=random.sample(wrongAnswer,3)
        answerOptions=wrongAnswer+[correctAnswer]
        random.shuffle(answerOptions)

        #Write the question and the answer options to the quiz file.
        quizFile.write('%s. What is the capital of %s?\n'%(questionNumber+1,capital[questionNumber]))

        for i in range(4):
            quizFile.write('    %s. %s\n'%('ABCD'[i],answerOptions[i]))
        quizFile.write('\n')

        #Write answer key to a file.
        answerKeyFile.write('%s. %s\n'%(questionNumber+1,'ABCD'[answerOptions.index(correctAnswer)]))

    quizFile.close()
    answerKeyFile.close()