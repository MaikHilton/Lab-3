def substitution(word):
    substitutions = {'i': 'і', 'a': 'а', 'o': 'о'}
    
    substitutions_found = []

    for latin, cyrillic in substitutions.items():
        if latin in word:
            substitutions_found.append(f"латинська '{latin}' замість кириличної '{cyrillic}'")

    if substitutions_found:
        print("У слові є підміна:")
        for substitution in substitutions_found:
            print(substitution)
        return True
    else:
        print("Підміна відсутня.")
        return False

word = "Іван"
result = substitution(word)  
print(result)
