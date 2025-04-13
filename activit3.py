ride=input("Which ride do you want to ride? Car/Bike :1/2")
if ride=="1":
    typ=input("Which type of car do you prefer Sedan/Suv/Sports: 1/2/3")
    if typ=="1":
        print("You have chosen a Sedan these are your options: Toyota,Porsche,Suzuki")
    elif typ=="2":
        print("You have chosen Suv these are your options : Volvo,Audi,BMW")
    else :
        print("You have chosen a Sports car these are your options :Mercedes ,Lamborghini,Bugatti")
else:
    typ=input("Which type of Bike do you prefer Scooter/Sports ")