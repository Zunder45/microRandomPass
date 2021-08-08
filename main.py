import random as r
import argparse

length = 5 

en_alph = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L" ,"M", "N", "O", "P", "Q", "R", "S", "T", "V", "X", "Y", "Z" ]
char = ["`","~","!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","}","[","]","\\","\|",":",";","\"","\'","<",">",",",".","?","/"]

def rand_word():
    res = ""

    if r.randint(0,1) == 0:
        return en_alph[r.randint(0,len(en_alph)-1)].lower()
    else:
        return en_alph[r.randint(0,len(en_alph)-1)]
    

def rand_num():
    return r.randint(0,10)

def rend_char():
    return str(char[r.randint(0,len(char))])

rand_func = {
    1: rand_num,
    2: rand_word,
    3: rend_char
}


def rand_func_select():
    return r.randint(1,len(rand_func))
def rand():
    res = ""
    i = 0
    while i <= int(length):
        res += str(rand_func[rand_func_select()]())
        i += 1
    print(res)


def pars():
    parser = argparse.ArgumentParser()

    parser.add_argument("-l",help="length", type=int)


    arg = parser.parse_args()

    if arg.l != None:
        global length
        length = arg.l
    




def main():
    pars()
    rand()


main()




