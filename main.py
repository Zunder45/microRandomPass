"""
-----------
    1.0
-----------
    -h - Помощь
    -l - Длина пароля
    -i - Количество паролей
    -n - Цифры
    -a - Маленькие буквы
    -A - Большие букыв
    -c - Симвалы
"""



import conf
import sys, random

def getValArg():
    args = sys.argv

    valsArgs = {
        "len": 8,
        "itr": 1,
        "num": False,
        "chr": False,
        "aup": False,
        "adw": False,
    }
    if "-h" in args:
        printHelp()
        exit()

    if len(args) == 1:
        valsArgs = {
            "len": 8,
            "itr": 1,
            "num": True,
            "chr": True,
            "aup": True,
            "adw": True,
        }
        return valsArgs

    if "-l" in args:
        if args.index("-l") + 1 < len(args):
            valsArgs["len"] = args[args.index("-l") + 1]
    if "-i" in args:
        if args.index("-i") + 1 < len(args):
            valsArgs["itr"] = args[args.index("-i") + 1]
    if "-n" in args:
        valsArgs["num"] = True
    if "-c" in args:
        valsArgs["chr"] = True
    if "-a" in args:
        valsArgs["adw"] = True
    if "-A" in args:
        valsArgs["aup"] = True

    return valsArgs

def printHelp():
    print(__doc__)

def getPasswd(args):
    
    passwdListChar = []

    listArgForGen = []

    if args["num"] == True:
        listArgForGen.append("num")
    if args["chr"] == True:
        listArgForGen.append("chr")
    if args["adw"] == True:
        listArgForGen.append("adw")
    if args["aup"] == True:
        listArgForGen.append("aup")
    
    for i in range(int(args['itr'])):
        strPass = ""
        for j in range(int(args['len'])):
            start = random.choice(listArgForGen)

            if start == "num":
                strPass += str(random.randrange(0,10))
            elif start == "adw":
                strPass += str(random.choice(conf.lett)).lower()
            elif start == "aup":
                strPass += random.choice(conf.lett).upper()    
            elif start == "chr":
                strPass += random.choice(conf.char)
            
        passwdListChar.append(strPass)

    return passwdListChar


def main():
    passList = getPasswd(getValArg())

    for p in passList:
        print(p)


if __name__ == "__main__":
    main()





