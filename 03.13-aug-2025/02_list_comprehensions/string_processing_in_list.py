# filter neet realted medical subjects starting with 'A' and convert to uppercase

subjects = ["Anatomy" , "Biology","Chemistry" , "Agriculture"]

filtered_subjects = [sub.upper() for sub in subjects if sub.startswith("A")]
print(filtered_subjects)