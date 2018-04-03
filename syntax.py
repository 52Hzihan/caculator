class SymError(ValueError):
    pass

class Over(ValueError):
    pass

def SyntaxCheck(strlist):
    length = len(strlist)
    counter = 0
    lp = 0
    rp = 0
    factor_follow = {'+', '-', '*', '/', '^', ')'}
    strlistcopy = strlist.copy()
    for i, string in enumerate(strlistcopy):
        if string.isdigit() is True or string.find('.') != -1 or string == 'ans':
            strlistcopy[i] = 'num'
        elif string == '(':
            lp = lp + 1
        elif string == ')':
            rp = rp + 1
    if lp != rp:
        return length - 1
        
    sym = strlistcopy[0]

    def getsym():
        nonlocal counter
        counter = counter + 1
        if counter >= length:
            counter = counter - 1
            raise SymError('incomplete expression')
        nonlocal sym 
        sym = strlistcopy[counter]

    def testover():
        if counter == length - 1:
            raise Over('over')

    def factor():        
        if sym == 'num':
            testover()
            getsym()
        elif sym == '(':
            getsym()
            expression()
            if sym == ')':
                testover()
                getsym()
            else:
                raise SymError('incorrect symbol')
        elif sym == '-':
            getsym()
            factor()
        elif sym == 'sin' or sym == 'cos':
            getsym()
            if sym != '(':
                raise SymError('incorrect symbol')
            else:
                factor()
        else:
            raise SymError('incorrect symbol')
        if sym not in factor_follow:
            raise SymError('incorrect symbol')

    def exfactor():
        factor()
        while sym == '^':
            getsym()
            factor()
    
    def term():
        exfactor()
        while sym == '*' or sym == '/':
            getsym()
            exfactor()

    def expression():
        term()
        while sym == '+' or sym == '-':
            getsym()
            term()

    try:
        expression()
    except SymError:
        return counter
    except Over:
        return - 1
