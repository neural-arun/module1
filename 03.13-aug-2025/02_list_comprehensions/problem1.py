"""
given a list of patient ages create a list showing which patients are adults
age >= 18 with True/False.
"""
patient_ages = [67,89,65,12,34,21,11,12,10,15,16]

adult_patients = [ages for ages in patient_ages if ages >= 18 ]
print(adult_patients)


