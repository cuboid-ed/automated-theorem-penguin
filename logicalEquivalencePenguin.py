# logical equivalences
# "logical sandbox" for now


#statement = input("input: ")
statement = "ㄱqΛㄱ(ㄱ(aⅤq)ΛpΛㄱ((pΛq)Ⅴs)Λp)Λㄱ(s→q)Λㄱ((aⅤ(aΛb))Λ(pⅤq)Λ(pΛq))"
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
print(negatable_statements_andOr)
print(negatable_statements_start_andOr)

# not really a step, but removing the parenthesies at the start and end
for i in range(0, len(negatable_statements_andOr)):
    negatable_statements_andOr[i] = negatable_statements_andOr[i][1:-1]
print(negatable_statements_andOr)

print("\n")
print("\n")

# Separate into sections that would let it get a "ㄱ"
# like in 'aⅤq' -> 'a', 'q'
for k in range(0, len(negatable_statements_andOr)):
    negatable = negatable_statements_andOr[k]

    sections = []

    # get things inside parenthesies first
    parenthesies = []
    bird = ""
    inside = ""
    inside_parenthesies = False 
    for l in range(0, len(negatable)):
        char = negatable[l]

        if inside_parenthesies == True:
            inside = inside + char

        if char == "(":
            inside_parenthesies = True
            parenthesies.append("(")
            sections.append(bird)
            bird = ""
        elif char == ")":
            parenthesies.pop()
            if 
               sections.append(bird)
               inside_parenthesies = False
               inside = ""

        if inside_parenthesies == False:
            bird = bird + char

        print(parenthesies, "bird", bird, "inside", inside)

    print(sections, "sections")
