# function returning a diagnosis suggestion bases on symptoms

def suggest_diagnosis(symptoms):
    if "fever" in symptoms and "rash" in symptoms:
        return "Possible :Dengue ya measles"
    
    elif "cough" in symptoms and "fever" in symptoms:
        return "Possible : Flu ya covid 19"
    
    else:
        return "Zarurat hai : better symptoms ki!"
    
sym_list = ["fever" , "cough"]

print(suggest_diagnosis(sym_list))