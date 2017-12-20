#Calc App Version 0.1 Test
print("Welcome to the app! ")
print("")
Cont_1 = input("Press RETURN to continue: ")
print("")

#Get user login info
User_ID = input("Enter your User ID: ")
PassWD = input("Enter your Passcode: ")

#Verify User Details
if User_ID == "Adam":
  print("")
else:
  quit()

if PassWD == "password":
  print("Welcome", User_ID, "You are now logged in")
else:
  quit()


print("")

#Main Calc App

Used_Mins = int(input("Enter the amount of minutes you have used this month: "))
print("")

Total_Mins = (Used_Mins*0.1)
print("You need to pay", "£", Total_Mins, "this month")

