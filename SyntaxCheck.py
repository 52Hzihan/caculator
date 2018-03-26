class SymError(ValueError):
    pass

class Over(ValueError):
    pass

def SyntaxCheck(strlist):
    length = len(strlist)
    counter = 0
    factor_follow = {'+', '-', '*', '/', '^', ')'}
    for i, string in enumerate(strlist):
        if string.isdigit() is True or string.find('.') != -1:
            strlist[i] = 'num'
    sym = strlist[0]
    def getsym():
        nonlocal counter
        counter = counter + 1
        if counter >= length:
            raise SymError('incomplete expression')
        nonlocal sym 
        sym = strlist[counter]

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
        elif sym == 'sin' or sym == 'cos':
            getsym()
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


example1 = ['1', '+', 'sin', '(', '2', ')']
print(SyntaxCheck(example1))
