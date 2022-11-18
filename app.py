import time
import hashlib
import re

#Introduction function introduces the user to the app.
def Introduction(loggedIn):
  print("Welcome to Noted - The marketplace for your notes at IE University, BBADBA, Year 2.")
  time.sleep(1)
  print("Please sign up/log in (For your security passwords will be encrypted)")
  time.sleep(1)
  #Login Process. Loops until logged in.
  while loggedIn != 1:
    UserIdentification()
  #Asks the user if it wants to upload or find notes
  UserPick = str(input("\nEnter U to upload notes or F to find notes or Q to Quit:")).upper().strip()
  return UserPick

#Sign up/Login Process
def UserIdentification():
    loggedIn = 0
    while loggedIn != 1:
        print("********** Login System **********")
        print("1.Signup")
        print("2.Login")
        print("3.Exit")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            SignUp()
        elif ch == 2:
            LogIn(loggedIn)
            return loggedIn
        elif ch == 3:
            break
        else:
            print("Wrong Choice!")
    return loggedIn

#Sign Up Process (Encryption)
def SignUp():
    #input email, password, confirmationPassword
    email = input("Enter email address (Use IE address): ")
    EmailVerification()
    password = input("Enter password: ")
    confPassword = input("Confirm password: ")
    #if passwords match, encode() from str to byte acceptable for hashing
    if confPassword == password:
        encoded = password.encode()
        #hash to hexidecimal notation and create HashedPassword
        HashedPassword = hashlib.blake2b(encoded).hexdigest()
        #open file with writing option as f, store email and HashedPassword
        with open("NotedCredentials.txt", "w") as f:
            f.write(email + "\n")
            f.write(HashedPassword)
            f.close()
            print("You have successfully registered your Noted account!\n")
            time.sleep(3)
    else:
        print("Password is not same as above! \n")

#Login Process
def LogIn(loggedIn):
    #prompt for email/password, encode() from byt to str and unhash into authenUnhash
    email = input("Enter email: ")
    password = input("Enter password: ")
    encodedPswrd = password.encode()
    HashedPswrd = hashlib.blake2b(encodedPswrd).hexdigest()
    #open file in reading, store in StoredEmail and storedPassword var. close file
    with open("NotedCredentials.txt", "r") as f:
        storedEmail, storedPassword = f.read().split("\n")
        f.close()
        #if input email is same as stored and unhash is same as storedPassword, login.
        if email == storedEmail and HashedPswrd == storedPassword:
            print("Logged in to Noted Successfully!")
            time.sleep(3)
            loggedIn == 1
        else:
            print("Login failed! \n")

def EmailVerification(email):
  regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
  ie = "ie"
  if re.fullmatch(regex, email):
    if ie in email:
      print("Email Valid\n")
      return True
    else:
      print("Email address valid but not from IE. Use IE address\n")
      email = input("Enter email address (Use IE address): ")
  else:
    if email == "Q" or email == "q":
      return False
    else:
      print("Invalid Email\n")
      email = input("Enter email address (Use IE address): ")

#notesFinder function (takes availableNotes as input) returns title and link
def NotesFinder(availableNotes):
  print("\nHere are the available courses: \n")
  #Creates availableCourses list 
  availableCourses = []
  #append the keys to the availableCourses list
  for key in availableNotes.keys():
    availableCourses.append(availableNotes[key])
  print(availableCourses)
  print()

  #User inputs chosenCourse.
  chosenCourse = input("Choose a course from the list: ").title().strip()
  while chosenCourse not in availableCourses:
    print("Sorry, course not available in our database. \nTry again!")
    time.sleep(0.5)
    chosenCourse = input("Choose your course: ").title().strip()
  else:
    chosenChapter = int(input("What chapter do you need? Chapter:"))
    print()
    print(f"Congratulations!\nClick on the link below to access your notes!\n{availableNotes[chosenCourse][chosenChapter-1]}")
    
    #notesUploader function to upload notes link.
def NotesUploader():
    Maths = {['Chapter1',
              'https://docs.google.com/document/d/1yhn4FexW91B4uUPILZaIinKlN8kviWodLRo7t6Mq_ig/edit?usp=sharing']}

    Economics = {["Economics Chapter 1", "link"]}

    German = {["German Chapter 1", "link"], ["German Chapter 2", "link"], ["German Chapter 3", "link"]}

    Algorithms = {["Algorithms Chapter 1", "link"], ["Algorithms Chapter 1", "link"], ["Algorithms Chapter 1", "link"]}

    subject = input("What subject are your notes from? ")
    title = input("What chapter are your notes on? ")
    link = input("Upload here the link of your notes: ")

    if subject == 'Maths':
        Maths[title] = link
        print("Thanks for sharing your notes!")
    if subject == 'Economics':
        Economics[title] = link
        print("Thanks for sharing your notes!")
    if subject == 'German':
        German[title] = link
        print("Thanks for sharing your notes!")
    if subject == 'Algorithms':
        Algorithms[title] = link
        print("Thanks for sharing your notes!")
    else:
        print("Sorry, the course you have selected is not included in our app")

NotesUploader()


#PreExistingNotes stores default notes
def PreExistingNotes():
    #creates availableNotes course: NotesTitle,NotesLink
    availableNotes = {}

    availableNotes["Mathematics"] = [["Math Chapter 1", "https://docs.google.com/document/d/1yhn4FexW91B4uUPILZaIinKlN8kviWodLRo7t6Mq_ig/edit?usp=sharing"], 
                                    ["Math Chapter 2", "link"], 
                                    ["Math Chapter 3", "link"]]
    availableNotes["Marketing Management"] = [["Marketing Management Chapter 1","link"], 
                                              ["Marketing Management Chapter 2","link"], 
                                              ["Marketing Management Chapter 3","link"]]
    availableNotes["Probability and Statistics"] = [["Probability and Statistics Chapter 1","link"], 
                                                    ["Probability and Statistics Chapter 2","link"], 
                                                    ["Probability and Statistics Chapter 3","link"]]
    availableNotes["Algorithms and Data Structures"] = [["Algorithms and Data Structures Chapter 1","link"], 
                                                        ["Algorithms and Data Structures Chapter 2","link"], 
                                                        ["Algorithms and Data Structures Chapter 3","link"]]
    availableNotes["Programming"] = [["Programming Chapter 1", "link"], 
                                    ["Programming Chapter 2", "link"], 
                                    ["Programming Chapter 3", "link"]]
    
    availableNotes["Building Powerful Relationships"] = [["Building Powerful Relationships Chapter 1", "link"], 
                                                        ["Building Powerful Relationships Chapter 2", "link"], 
                                                        ["Building Powerful Relationships Chapter 3", "link"]]
    return availableNotes

#UserOption is the logic. It takes the step the user selected. Find, Upload or Quit
def UserOption(UserPick, availableNotes):     
    while UserPick != "U" and UserPick != "F":
        if UserPick == "Q":
            print("Exiting Program...")
            time.sleep(0.5)
            break
        else:
            print("Wrong Letter. Restarting Program.\nLoading...")
            time.sleep(5)
            Introduction()
    if UserPick == "U":
        NotesUploader(availableNotes)
    elif UserPick == "F":
        NotesFinder(availableNotes)

        

#This main function calls the rest of the functions
def main():
    Introduction()
    availableNotes = PreExistingNotes()
    UserOption(availableNotes)
   
main() 

        
