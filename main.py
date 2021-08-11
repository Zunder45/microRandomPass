import random as r
import argparse
import rand, var


def pars(): 
    parser = argparse.ArgumentParser()

    parser.add_argument("-l","--length",help="length", type=int)
    parser.add_argument("-i","--iteration",type=int)
    parser.add_argument("-n","--num",action="store_const", const="True")
    parser.add_argument("-c","--char",action="store_const", const="True")
    parser.add_argument("-a","--alph",action="store_const", const="True")

    arg = parser.parse_args()

    if arg.iteration !=  None:
        var.itr = arg.iteration

    if arg.length != None:
        var.length = arg.length
    if not any((arg.num,arg.char,arg.alph)):
        var.allChar()
    else:
        if arg.num != None:
            var.onlyNum = True
        if arg.char != None:
            var.onlyChar = True
        if arg.alph != None:
            var.onlySymAlph = True

    # print(var.onlyNum, var.onlyChar, var.onlyStr)

    
    

def main():
    pars()
    i = 0
    while i < var.itr: 
        rand.rand_main()
        i += 1


main()




