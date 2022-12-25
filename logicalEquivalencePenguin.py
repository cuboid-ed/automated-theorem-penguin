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
for char in statement:
    if char == "ㄱ":
        negation_char = True
    if negation_char = True and char == "(": # start storing 
        store_negated_part = True
    elif negation_char = True and not(char == "("): # get out of can negate mode 
        negation_char = False 
