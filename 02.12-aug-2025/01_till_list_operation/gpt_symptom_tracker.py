# Start with an empty list to store patient symptoms
symptoms = []

print("Enter patient's symptoms. Type 'done' when you are finished.")

# This loop will run forever until we 'break' out of it
while True:
    # Get input from the user and convert it to lowercase
    new_symptom = input("Enter a symptom: ").lower()

    # If the user types 'done', exit the loop
    if new_symptom == 'done':
        break
    # To avoid adding empty entries if the user just hits Enter
    elif new_symptom:
        symptoms.append(new_symptom)

# --- Removing Duplicates ---
# Convert the list to a set to automatically remove duplicates,
# then convert it back to a list.
if symptoms:
    unique_symptoms = list(set(symptoms))
    print("\n--- Final List of Symptoms (Duplicates Removed) ---")
    print(unique_symptoms)
else:
    print("\nNo symptoms were entered.")