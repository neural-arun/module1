# using global , nonlocal , aur return
attempts = 0

def quiz():
    global attempts
    answer = "heart"
    attempts += 1

    def hint(reveal):
        nonlocal answer
        if reveal:
            print("Hint: ye organ poori body mein blood pump karta hai!")

        else:
            print("No Hint")

    user_guess = input("Which organ pumps blood for body?: ").strip().lower()
    if user_guess == answer:
        print("Correct answer!")
    else:
        hint(True)
        print("Incorrect attempts: ", attempts)
        print("Play again!")
quiz()