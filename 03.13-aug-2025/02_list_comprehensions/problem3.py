question_marks = [("Question1" , 1),("Question2" , 2),("Question3" , 3),("Question4" , 4),
                  ("Question5" , 5),("Question6" , 6),("Question7" , 7),("Question8" , 8),
                  ("Question9" , 9),("Question10" , 10),("Question11" , 11),("Question12" , 12),]

# do not forget parenthesis aroun comprehension target
question_marks_more_than_5 = [(question.lower() , mark) for question , mark in question_marks 
                              if mark >= 5 ]

print(question_marks_more_than_5)