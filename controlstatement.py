def voting():
    miaka = int(input("Enter your age:"))
    if miaka >= 18:
        print("You are eligible to vote")
    else:
        print("Sorry,You are not eligible to vote")
voting()

def checkingnumber():
    nambari = int(input("Enter your number:"))
    if nambari <0:
        print(f"{nambari} is a negative number")
    else:
        print(f"{nambari} is a positive number")
checkingnumber()

