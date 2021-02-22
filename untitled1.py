# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:08:46 2020

@author: Gurudas
"""
import random

capitals = {'alabama':'monto','alaska':'jun','arizona':'phoenix','arkansas':'little rock','california':'sacra',
            'colorado':'denver','connecticut':'hartford','delaware':'dover'}

states = list(capitals.keys())

random.shuffle(states)

for quizNum in range(2):
    quizFile = open('quiz_file_%s'%(quizNum+1))
    