zander_length = float(input("Enter the length of the zander in centimeters: "))

if zander_length >= 42:
    print("Congratulations! You can keep the zander.")
else:
    below_limit = 42 - zander_length
    print(f"The zander is below the size limit. Release it back into the lake. It is {below_limit} centimeters below the limit.")
