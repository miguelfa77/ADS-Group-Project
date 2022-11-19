import time
import hashlib
import re
import sys

#Sign up/Login Process
def UserIdentification():
    #repeat sign up and login until login or exit. If login, break. If exit, exit the whole program.
    while True:
        print("********** Login System **********")
        print("1.Signup")
        print("2.Login (If you already have an account)")
        print("3.Exit")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            SignUp()
        elif ch == 2:
            LogIn()
            break
        elif ch == 3:
            sys.exit()

#Sign Up Process (Encryption)
def SignUp():
    #input email, password, confirmationPassword
    email = input("Enter email address (Use IE address): ")
    EmailVerification(email)
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
def LogIn():
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
        else:
            print("Login failed! \n")
            time.sleep(5)
            sys.exit()

def EmailVerification(email):
  regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
  ie = "ie"
  if re.fullmatch(regex, email):
    if ie in email:
      print("Email Valid\n")
    else:
      print("Email address valid but not from IE. Use IE address next time\n")
  else:
    print("Invalid Email\n")


#notesFinder function (takes availableNotes as input) returns title and link
def NotesFinder(availableNotes):
  print("\nHere are the available courses: \n")
  #Creates availableCourses list 
  availableCourses = [key for key in availableNotes.keys()]
  #append the keys to the availableCourses list
  print(availableCourses)
  print()

  #User inputs chosenCourse.
  chosenCourse = input("Choose a course from the list: ")
  chosenCourse.title().strip()
  while chosenCourse not in availableCourses:
    print("Sorry, course not available in our database. \nTry again!")
    time.sleep(0.5)
    chosenCourse = input("Choose your course: ").title().strip()
  else:
    chosenChapter = int(input("What chapter do you need? Chapter:"))
    print()
    print(f"Congratulations!\nClick on the link below to access your notes!\n{availableNotes[chosenCourse][chosenChapter-1]}")
    
    #notesUploader function to upload notes link.
def NotesUploader(availableCourses, AvailableNotes):
    print()
    print(availableCourses)
    print()
    SubjectInput = input("What subject are your notes from?:")
    NotesTitle= input("What is the title of your notes?:")
    NotesLink = input("Upload here the link of your notes:")
    availableCourses[SubjectInput].append(NotesTitle,NotesLink)

    return AvailableNotes


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

#This main function calls the rest of the functions
def main():
    print("Welcome to Noted - The marketplace for your notes at IE University, BBADBA, Year 2.")
    time.sleep(1)
    print("Please sign up/log in (For your security passwords will be encrypted)")
    time.sleep(1)
    #Check Credentials
    UserIdentification()
    availableNotes = PreExistingNotes()
    #Asks the user if it wants to upload or find notes
    UserPick = input("\nEnter U to upload notes or F to find notes or Q to Quit:")
    UserPick.upper().strip()
    
   
    while UserPick != "U" and UserPick != "F":
        if UserPick == "Q":
            print("Exiting Program...")
            time.sleep(3)
            break
        else:
            print("Wrong Letter. Restarting Program.\nLoading...")
            time.sleep(5)
    if UserPick == "U":
        NotesUploader(availableNotes)
    elif UserPick == "F":
        NotesFinder(availableNotes)
   
main()  
        

    
    
    
    
    
 def NotesUploader(availableCourses):
    print()
    print(availableCourses)
    print()

    subject = input("¿What subject are your notes from?:")
    Titleofthenotes = input("¿What is the title of your notes?:")
    Linkofthenotes = input("Upload here the link of your notes:")

    if subject=="Mathematics" or "mathematics":
        availableCourses[subject]+= [[Titleofthenotes,Linkofthenotes]]
        print(availableCourses)
    elif subject =="Marketing Management" or "marketing management":
        availableCourses[subject] += [Titleofthenotes, Linkofthenotes]
        print(availableCourses)
    elif subject =="Probability and Statistics" or "probability and statistics":
        availableCourses[subject] += [Titleofthenotes, Linkofthenotes]
        print(availableCourses)
    elif subject == "Algorithms and Data Structures" or "algorithms and data structures":
        availableCourses[subject] += [Titleofthenotes, Linkofthenotes]
        print(availableCourses)
    elif subject=="Programming" or "programming":
        availableCourses[subject] += [Titleofthenotes, Linkofthenotes]
        print(availableCourses)
    elif subject=="Building Powerful Relationships" or "building powerful relationships":
        availableCourses[subject] += [Titleofthenotes, Linkofthenotes]
        print(availableCourses)
    else:
        print("Sorry, but you might have done a typing error")
