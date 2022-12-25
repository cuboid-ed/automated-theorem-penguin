# logical equivalences
# "logical sandbox" for now


statement = input("input: ")

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
for i in range(0, len(statement)):
    char = statement[i]
    
    if store_negated_part == True and char == ")": # ended collection 
        negatable_statements.append(negatable)
        store_negated_part = False
        negatable = ""
        negatable_statements_start.append(negatable_start)
    elif store_negated_part == True: # add it to the character 
        negatable = negatable + char
    
    if negation_char == True and char == "(": # start storing
        negatable_start = i + 1 # where the negatable starts 
        store_negated_part = True
        negation_char = False
        negatable = ""
    elif negation_char == True and not(char == "("): # get out of can negate mode 
        negation_char = False
        store_negated_part = False

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
