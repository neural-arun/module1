# ek list banao jo patients ke symptoms store kare. usaer se input leke symptoms add karo aur agar 
# user done bol de to sypmtoms print karo 

symptoms = ["fever" , "cough" ,"headache"]
number_of_symptoms = int(input("Enter number of symptoms you want to add(1/2/3/4/5): "))
def add_symptoms():
    print("You can type 'done' if there are no symptoms to add")
    new_symptom = input("Enter new Symptom: ").lower()
    global symptoms
    if new_symptom == "done":
        print("Thanks for Adding new symptoms")

    else:
        symptoms.append(new_symptom)
    return symptoms
if number_of_symptoms == 1:
    add_symptoms()
elif number_of_symptoms == 2:
    add_symptoms()
    add_symptoms()
elif number_of_symptoms == 3:
    add_symptoms()
    add_symptoms()
    add_symptoms()
elif number_of_symptoms == 4:
    add_symptoms()
    add_symptoms()
    add_symptoms()
    add_symptoms()
elif number_of_symptoms == 5:
    add_symptoms()
    add_symptoms()
    add_symptoms()
    add_symptoms()
    add_symptoms()
else:
    print("You can only add only upto 5 symptoms at once")
print(symptoms)

    