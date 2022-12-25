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
    
    if store_negated_part == True and char == ")":
        negatable_statements.append(negatable)
        store_negated_part = False
        negatable = ""
        negatable_statements_start.append(negatable_start)
    elif store_negated_part == True:
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
