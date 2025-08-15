# med bot mini diagnos
symptom = input("Kya aapko fever hai? (yes/no): ").strip().lower()
if symptom == "yes":
    temp = float(input("Aap apna temperature celcius mein bataye: "))
    if temp >= 101:
        print("Aapko high fever hai , agar aapne paracetamol kha liye hai to paani pijiye aur rest kijiye.  ")
        print("agar aapne paracetamol nhi khaye to turant abhi doctor ke paas jaye.")
    elif temp < 101 :
        print("aap paani pijiye aur rest kijiye")