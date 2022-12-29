# adds parens for order of operations in logic 
'''
() paren
ㄱ not 
Λand 
Ⅴor 
→ implies
↔ biconditional 
'''


statement = input("input: ")
#statement = "ㄱ(aΛq)ΛㄱqΛㄱ(ㄱ(aⅤq)ΛpΛㄱ((pΛq)Ⅴs)Λp)Λㄱ(s→q)Λㄱ((aⅤ(aΛb))Λ(pⅤq)Ⅴ(pΛq)Λ(pⅤs)Λ(pⅤk))" 
#statement = "ㄱ(aΛbⅤc)"
print(statement) # checking 

def addParenForParen(operators, statement):
    '''
    separates string given a list of operators, statement, assuming all
    variables are 1 letter long
    operators = ['ㄱ', 'Λ', 'Ⅴ', '→', '↔']
    '''
    paren = []
    for i in 
    # controlling parenthesies list 
        if char == "(": 
            paren.append("(")  
        elif char == ")":
            paren.pop()

def addParenForOpearator(operator):
    ''' adds parenthesies for a given operator 
    '''
