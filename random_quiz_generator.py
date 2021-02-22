# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 09:16:18 2020

@author: Gurudas

Random Quiz Generator 
"""
import random

# =============================================================================
# Step 1 : Storing the quiz data into the dictionary
# =============================================================================

capitals = {'alabama':'monto','alaska':'jun','arizona':'phoenix','arkansas':'little rock','california':'sacra',
            'colorado':'denver','connecticut':'hartford','delaware':'dover'}

# =============================================================================
# Step 2 : create the quiz file and shuffle the question order 
# =============================================================================

for quizNum in range(5):
    #create the quiz and answer key files
    quizFile = open('capitals_quiz%s.txt' %(quizNum + 1),'w')
    answerKeyFile = open('capitals_quizAnswers%s.txt'%(quizNum+1),'w')
    
    #writing the header of the quiz file
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' '*5) + 'State Capitals Quiz (Form %s)' %(quizNum + 1))
    quizFile.write('\n\n')
    
    #shuffling the keys of the capitals dictionary
    states = list(capitals.keys())
    random.shuffle(states)

# =============================================================================
# Step 3 : create the answer options 
# =============================================================================
    correctAnswer = capitals[states[quizNum]]
    wrongAnswers = list(capitals.values())
    del wrongAnswers[wrongAnswers.index(correctAnswer)]
    wrongAnswers = random.sample(wrongAnswers,3)
    answerOptions = wrongAnswers + [correctAnswer]
    random.shuffle(answerOptions)
    

# =============================================================================
# Step 4 : write the content to the quiz file and the answer key 
# =============================================================================

    
    #write questions and the answer options to the quiz file
    quizFile.write('%s. What is the captial of %s ?\n'%(quizNum + 1 , states[quizNum]))
    
    #write the answer options to the respective question 
    for option in range(4):
        quizFile.write('    %s. %s\n' %('ABCD'[option],answerOptions[option]))
    
    #new line for new question 
    quizFile.write('\n')
    
    #writing answer key to the file 
    answerKeyFile.write('%s. %s\n' %(quizNum+1,'ABCD'[answerOptions.index(correctAnswer)]))
    
 
# =============================================================================
# Step 5 : Closing the files
# =============================================================================

quizFile.close()
answerKeyFile.close()