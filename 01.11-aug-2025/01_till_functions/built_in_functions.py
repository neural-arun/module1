# enumerate 

prescriptions = [["Paracetamol", "Ibuprofen"], ["Amoxicillin"], ["Aspirin", "Paracetamol"]]
print(len(prescriptions))
for i ,med in enumerate(prescriptions):
    print(f"{i + 1} has {len(med)} medicines.")


for i in range(5):
    print(i , end=" ")

# Step-size usage (Medical batches roll numbers)
for roll in range(1001 ,1011 ,2):
    print(f"Roll Numbers are : {roll} ")

fruits = ["Apple", "Banana", "Mango"]

for i , fruit in enumerate(fruits):
    print(f"{i , fruit}")

specialities = ["Cardiology", "Neurology", "Orthopaedics"]

for i , speciality in enumerate(specialities , start=1):
    print(f" {i} : {speciality}")


# Enumerate with nested loop (NEET question options)


questions = [["A","B","C","D"] , ["TRUE" , "False"] , ["yes" , "no" , "maybe"]]
for q_ind ,options in enumerate(questions , start=1):
    print(f"Q{q_ind} options: ")
    for opt_index , opt in enumerate(options):
        print(f"option {opt_index+1} : {opt}")



