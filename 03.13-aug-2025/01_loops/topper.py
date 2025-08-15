students = [("Arun" , 120) , ("Sarita" , 150) , ("uday" , 300) , ("sanni" , 40)]

topper_name = ""
top_mark = 0

for name , mark in students:
    if mark > top_mark:
        top_mark = mark
        topper_name = name

print(topper_name , top_mark)