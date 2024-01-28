gender = input("Enter your biological gender (male/female): ").lower()
hemoglobin = float(input("Enter your hemoglobin value (g/l): "))

if gender == "female":
    if 117 <= hemoglobin <= 155:
        print("Your hemoglobin level is normal.")
    elif hemoglobin < 117:
        print("Your hemoglobin level is low.")
    else:
        print("Your hemoglobin level is high.")
elif gender == "male":
    if 134 <= hemoglobin <= 167:
        print("Your hemoglobin level is normal.")
    elif hemoglobin < 134:
        print("Your hemoglobin level is low.")
    else:
        print("Your hemoglobin level is high.")
else:
    print("Invalid gender input.")
