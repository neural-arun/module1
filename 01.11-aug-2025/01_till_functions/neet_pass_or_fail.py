# function to check neet pass or fail

def neet_score_checker(score):
    if score >= 137:
        print("Congrats! , Aap neet mein paas ho gye")
        print("Good luck for your future!")
    elif score < 137 :
        print("sorry! , you have failed the examination , Try again next time.")
        print("Good luck")
    else:
        print("Wrong input detected!")

neet_score_checker(146)
neet_score_checker(133)