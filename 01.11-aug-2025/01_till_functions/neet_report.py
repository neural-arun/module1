"""
build a function that takes a list of students NEET marks and returns 
a report (number of pass/fail students)
"""

def neet_report():
    marks_list = [123,234,657,456,245,667,715,718,719,455,667,122,22,222]

    passed_students = 0
    failed_students = 0
    for marks in marks_list:
        if marks >= 600:
            passed_students += 1

        elif marks < 600:
            failed_students += 1

    

    return  {"Number of Passed students in Neet " : passed_students ,
          "Number of failed students in NEET exam " : failed_students}

print(neet_report())