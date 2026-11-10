
# freelance hire in roorkee 

freelance = {}
print (" welcome in freelance hire in roorkee ")

while True:
     print("===MENU===")
     print("1. MALE ")
     print("2. FEMALE  ")
     print("3. TEAM ")
     print("4. EXIT")

     choice = int(input(" enter your choice "))

#1 . MALE 
     
     if ( choice==1):
      name = input(" Entr your name  ") 
      date = input(" enter your sechudule ")  
      number = input(" enter your mobile number ")
      location = input(" enter your loaction ")
      budget = input(" enter your budget ")
      time = input(" enter your time ")
      category = input(" cameraman , videoeditor , socialmedia Manger , etc. ")

      print(f" { name} thanks for enter your details under 24 hours creator contact you ")

#2. FEMALE
    
     elif ( choice==2 ):
        name = input(" enter your name  ")
        date = input(" enter your date")
        locaction = input(" enter your location")
        girlcategory = input(" enter your girl category , ex= kalli,gorri,savlli")
        number = input(" enter your mobile number")
        budget = input(" enter your budget ")

        print(" thanks for visting under 24 hours will contact you ")

# TEAM 
     elif ( choice==3):
        name = input(" enter your name ")
        location = input(" enter your loaction ")
        date = input(" enter your date ")
        number = input (" enter your number ")
        budget = input (" enter your budget ")

        print(" thanks for enter your details team will bi contact you")

#4  EXIT 

     elif (choice==4):
      print(" thanks for visit this website love you ")
      break

     else: print(" non sense hai kya sahi option select chutiye")



