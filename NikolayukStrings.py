#HT_2_1
str_1 = 'rythm rough rush shake than'
print('str_1 = ' + str_1.replace('a', '') + '\nдлина = ' + str(len(str_1)))
#HT_2_2
str_1 = 'rythm (rough rush shake) than'
print(str_1[0:str_1.find('(')] + str_1[str_1.find(')')+1:])
#HT_2_3
str_1 = 'rythm rough rush shake than'
print(str_1.count('t'))
#HT_2_4
str_1 = 'rythm rough rush shake than'
print(str_1[0:str_1.find('h')]
      + str_1[str_1.find('h'):str_1.rfind('h')+1][::-1]
      + str_1[-2:])
#HT_2_5
str_1 = 'rythm rough rush shake than'
str_1 = str_1.replace('h', 'H', str_1.find('h'))
str_1 = str_1.replace('H', 'h', 1)
print(str_1)