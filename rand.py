import random as r
import var




def rand_word():
    res = ""
    if r.randint(0,1) == 0: #0 - lower 1 - upper
        return  var.en_alph[r.randint(0,len(var.en_alph)-1)].lower()
    else:
        return  var.en_alph[r.randint(0,len(var.en_alph)-1)]
    
def rand_num():
    return r.randint(0,9)

def rend_char():
    return  var.char[r.randint(0,len(var.char)-1)]




rand_func = {
    1: lambda: rand_num() if var.onlyNum else False,
    2: lambda: rand_word() if var.onlySymAlph else False,
    3: lambda: rend_char() if var.onlyChar else False
}

def rand_func_select():
    test = str(rand_func[r.randint(1,len(rand_func))]())
    while(test == "False"):
        test = str(rand_func[r.randint(1,len(rand_func))]())
    return test
    

def rand_all():
    res = ""
    i = 0
    while i < var.length:
        res += str(rand_func[rand_func_select()]())
        i += 1
    print(res)

def rand_main():
    res = ""
    i = 0
    while i < var.length:
        # test = str(rand_func[rand_func_select()]())
        # while(test == "False"):
        #     test = str(rand_func[rand_func_select()]())
            
        res += rand_func_select()
        i += 1
    print(res)