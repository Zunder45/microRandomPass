length = 5 
itr = 1 

en_alph = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L" ,"M", "N", "O", "P", "Q", "R", "S", "T", "V", "X", "Y", "Z" ]
char = ["`","~","!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","}","[","]","\\","\|",":",";","\"","\'","<",">",",",".","?","/"]

onlyNum = False
onlySymAlph = False
onlyChar = False
allChar = False

def allChar():
    global onlyNum, onlySymAlph, onlyChar 
    onlyNum = onlySymAlph = onlyChar = True

