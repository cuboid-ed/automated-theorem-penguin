# logical equivalences
# "logical sandbox" for now


#statement = input("input: ")
statement = "ㄱqΛㄱ(ㄱ(aⅤq)ΛpΛㄱ((pΛq)Ⅴs)Λp)Λㄱ(s→q)Λㄱ((aⅤ(aΛb))Λ(pⅤq)Ⅴ(pΛq)Λ(pⅤs)Λ(pⅤk))"
statement = "ㄱqΛㄱ(ㄱ(aⅤq)ΛpΛㄱ((pΛq)Ⅴs)Λp)Λㄱ(s→q)Λㄱ((aⅤ(aΛb))Λ(pⅤq)Ⅴ(pΛq)Λ(pⅤs)Λ(pⅤk))"
statement = ?ㄱqΛㄱ(ㄱ(aⅤq)ΛpΛㄱ((pΛq)Ⅴs)Λp)Λㄱ(s→q)Λㄱ((aⅤ(aΛb))Λ(pⅤq)Ⅴ(pΛq)Λ(pⅤs)Λ(pⅤk))"
#statement = "ㄱ(aΛbⅤc)"
print(statement) # checking 

#logical equivalences
double_negation = False 

# implementing the double negation
if "ㄱㄱ" in statement:
    double_negation = True


# check if negation can be pushed in 
push_negation = False 
if "ㄱ(" in statement:
    push_negation = True
    print("Negation can be pushed in")
    
# recognize each place that can get negated
negatable_statements = []
negatable_statements_start = []
negatable_start = 0 
negatable = ""
negation_char = False
store_negated_part = False
parenthesies = []
endNegation = ""
for i in range(0, len(statement)):
    char = statement[i]
    
    if char == "(" and negation_char == True:
        parenthesies.append("ㄱ(")
        #negation_char = False # turning it off so nested doesn't get impacted 
    elif char == "(":
        parenthesies.append("(")

    if negation_char == True and char == "(": # start storing
        negatable_start = i + 1 # where the negatable starts 
        store_negated_part = True
        negation_char = False
        negatable = ""
        
    if char == ")":
        endNegation = parenthesies.pop()
    #print(parenthesies, char, endNegation) #checking 
    
    if store_negated_part == True and char == ")" and endNegation == "ㄱ(": # ended collection 
        negatable = negatable + char
        negatable_statements.append(negatable)
        store_negated_part = False
        negatable = ""
        negatable_statements_start.append(negatable_start)
        endNegation = ""
        #print("added") #checking 
    elif store_negated_part == True: # add it to the character 
        negatable = negatable + char
    '''
    if negation_char == True and not(char == "("): # get out of can negate mode 
        negation_char = False
        store_negated_part = False
    '''

    if char == "ㄱ": # start negation mode 
        negation_char = True 

print(negatable_statements)
print(negatable_statements_start)

# Dropping negatables with conditionals 
negatable_statements_andOr = []
negatable_statements_start_andOr = []
for j in range(0, len(negatable_statements)):
    negatable = negatable_statements[j]
    if not(("↔" in negatable) or ("→" in negatable)):
        negatable_statements_andOr.append(negatable)
        negatable_statements_start_andOr.append(negatable_statements_start[j])
print(negatable_statements_andOr) #checking 
print(negatable_statements_start_andOr) #checking 

# not really a step, but removing the parenthesies at the start and end
for i in range(0, len(negatable_statements_andOr)):
    negatable_statements_andOr[i] = negatable_statements_andOr[i][1:-1]
print(negatable_statements_andOr)

print("\n")
print("\n")

# Separate into sections that would let it get a "ㄱ"
# like in 'aⅤq' -> 'a', 'Ⅴ', 'q'
negatable_statements_andOr_separted = []
for k in range(0, len(negatable_statements_andOr)):
    negatable = negatable_statements_andOr[k]

    sections = []

    # get things inside parenthesies first
    parenthesies = [] 
    inside = "" 
    for l in range(0, len(negatable)):
        char = negatable[l]

        # if there is an end to a section
        if ((char == "Λ") or (char == "Ⅴ")) and (len(parenthesies) == 0):
            sections.append(inside)
            sections.append(char)
            inside = ""
        else:
            inside = inside + char
            
        # controlling parenthesies list 
        if char == "(": 
            parenthesies.append("(")  
        elif char == ")":
            parenthesies.pop() 

        #print(parenthesies, "inside", inside) # checking
    # last section
    sections.append(inside)
    negatable_statements_andOr_separted.append(sections)

print(negatable_statements_andOr_separted, "Separate into sections that would let it get a 'ㄱ'")
print("\n")
print("\n")

### Allocate a "ㄱ"  to each section
# check if order of operations of "Λ" before "Ⅴ" needs to be applied
for k in range(0, len(negatable_statements_andOr_separted)):
    negatable = negatable_statements_andOr_separted[k]

    if ("Λ" in negatable) and ("Ⅴ" in negatable):
        print(negatable, "negatable") 

        negatable_and_before_or = []
        inside_and = False
        and_part = ""
        for i in range(0, len(negatable)):
            part = negatable[i]

            if (inside_and == False) and (part == "Λ"): # start the and statement 
                inside_and = True
                and_part = "(" + negatable[i - 1] + "Λ"
                del negatable_and_before_or[-1]
            elif (inside_and == True) and (part == "Ⅴ"): # end since encountered an or
                inside_and = False
                and_part = and_part + ")" # last parenthesies 
                negatable_and_before_or.append(and_part)
                and_part = ""
                negatable_and_before_or.append("Ⅴ") # don't forget to add the or 
            elif inside_and == True:
                and_part = and_part + part
            else:
                negatable_and_before_or.append(part)
            print("inside_and", inside_and, "and_part", and_part)
        # add the last section if it wasn't stopped by an or
        if (and_part != ""):
            and_part = and_part + ")" # last parenthesies
            negatable_and_before_or.append(and_part)
        negatable_statements_andOr_separted[k] = negatable_and_before_or

print(negatable_statements_andOr_separted)

# make sure the allocate demorgan's law once and only once
for k in range(0, len(negatable_statements_andOr_separted)):
    negatable = negatable_statements_andOr_separted[k]
        
    
    for l in range(0, len(negatable)):
        section = negatable[l]






















