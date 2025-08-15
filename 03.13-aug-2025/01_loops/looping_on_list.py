patient_data = [{"name" : "anil" , "symptoms" : "fever"}
                , {"name" : "Arun" , "symptoms" : "fever"},
                {"name" : "Sarita" , "symptoms" : "fever"}]

fever_count = 0

for patient in patient_data:
    if patient["symptoms"] == "fever":
        fever_count += 1

    

print("Number of fever patients is:",fever_count) 