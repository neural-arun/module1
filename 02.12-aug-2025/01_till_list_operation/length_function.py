name = "Arun"
print(len(name))
neet_marks = {2022 : 368 , 2023 : 469 , 2024 : 535 , 2025 : 400} # summary of 4 years , fucked up.
print(len(neet_marks))

# typecasting 

age = 21
age_str = str(age)
print(f"My name is Arun Yadav & i am {age} years old")

# string operations examples

# string concatenation
first_name = "Arun"
last_name = "Yadav"

full_name = first_name + " " + last_name
print(full_name)
print(len(full_name))

email = "arunyadav149413@gmail.com"
print("Username:",email[:15])
print(email.upper())

date = "Name: Arun , Marks: 98 , Subject: Biology"
data = date.replace("Arun" , "Dr. Arun")
parts = data.split(" , ")
print(parts) 

num = 67.898
new_num = int(num)  # decimal ke baad vali cheezein loose hongi
print(new_num)

