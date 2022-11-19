import time
import hashlib
import re
import sys


# Sign up/Login Process
def UserIdentification():
    # repeat sign up and login until login or exit. If login, break. If exit, exit the whole program.
    while True:
        print("********** Login System **********")
        print("1.Signup")
        print("2.Login")
        print("3.Exit")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            SignUp()
        elif ch == 2:
            LogIn()
            break
        elif ch == 3:
            sys.exit()


# Sign Up Process (Encryption)
def SignUp():
    # input email, password, confirmationPassword
    email = input("Enter email address (Use IE address): ")
    EmailVerification(email)
    password = input("Enter password: ")
    confPassword = input("Confirm password: ")
    # if passwords match, encode() from str to byte acceptable for hashing
    if confPassword == password:
        encoded = password.encode()
        # hash to hexidecimal notation and create HashedPassword
        HashedPassword = hashlib.blake2b(encoded).hexdigest()
        # open file with writing option as f, store email and HashedPassword
        with open("NotedCredentials.txt", "w") as f:
            f.write(email + "\n")
            f.write(HashedPassword)
            f.close()
            print("You have successfully registered your Noted account!\n")
            time.sleep(3)
    else:
        print("Password is not same as above! \n")


# Login Process
def LogIn():
    # prompt for email/password, encode() from byt to str and unhash into authenUnhash
    email = input("Enter email: ")
    password = input("Enter password: ")
    encodedPswrd = password.encode()
    HashedPswrd = hashlib.blake2b(encodedPswrd).hexdigest()
    # open file in reading, store in StoredEmail and storedPassword var. close file
    with open("NotedCredentials.txt", "r") as f:
        storedEmail, storedPassword = f.read().split("\n")
        f.close()
        # if input email is same as stored and unhash is same as storedPassword, login.
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


# notesFinder function (takes availableNotes as input) returns title and link
def NotesFinder(availableNotes):
    print("\nHere are the available courses: \n")
    # Creates availableCourses list
    availableCourses = [key for key in availableNotes.keys()]
    # append the keys to the availableCourses list
    print(availableCourses)
    print()

    # User inputs chosenCourse.
    chosenCourse = input("Choose a course from the list: ")
    chosenCourse.title().strip()
    while chosenCourse != "":
         if chosenCourse in availableCourses:
                 Notes = availableNotes.get(chosenCourse)
                 print()
                 print(Notes)
                 break
         else:
             print("Sorry, course not available in our database. \nTry again!")
             time.sleep(0.5)
             chosenCourse = input("Choose your course: ").title().strip()


# notesUploader function to upload notes link.
def NotesUploader(availableCourses, availableNotes):
    print()
    print(availableCourses)
    print()

    try: 
        NotesSubject = input("¿What subject are your notes from?:")
        print()
        NotesTitle = input("¿What is the topic of your notes?:")
        print()
        NotesChapter = input("What is the chapter of your notes? <insert 'Chapter' and chapter number> ")
        print()
        NotesLink = input("Upload here the link of your notes:")

        while NotesSubject in availableCourses:
            if NotesSubject=="Mathematics" or "mathematics":
              availableNotes[NotesSubject] += [NotesTitle, NotesChapter, NotesLink]
            elif NotesSubject =="Marketing Management" or "marketing management":
                availableNotes[NotesSubject] += [NotesTitle, NotesChapter, NotesLink]
            elif NotesSubject =="Probability and Statistics" or "probability and statistics":
                availableNotes[NotesSubject] += [NotesTitle, NotesChapter, NotesLink]
            elif NotesSubject == "Algorithms and Data Structures" or "algorithms and data structures":
                availableCourses[NotesSubject] += [NotesTitle, NotesChapter, NotesLink]
            elif NotesSubject=="Programming" or "programming":
                availableNotes[NotesSubject] += [NotesTitle, NotesChapter, NotesLink]
            elif NotesSubject=="Building Powerful Relationships" or "building powerful relationships":
                availableNotes[NotesSubject] += [NotesTitle, NotesChapter, NotesLink]
            elif NotesSubject == "Entrepeneurship & Innovation" or "entrepeneurship & innovation":
                availableNotes[NotesSubject] += [NotesTitle, NotesChapter, NotesLink]
            else:
                print("Sorry, but you might have done a typing error")
                NotesSubject = input("¿What subject are your notes from?:")
                print()
                NotesTitle = input("¿What is the topic of your notes?:")
                print()
                NotesChapter = input("What is the chapter of your notes? <insert 'Chapter' and chapter number> ")
                print()
                NotesLink = input("Upload here the link of your notes:")

                return availableNotes
            
    except NotesSubject not in availableCourses:
            print("Sorry, but you might have done a typing error")
            NotesSubject = input("¿What subject are your notes from?:")
            print()
            NotesTitle = input("¿What is the topic of your notes?:")
            print()
            NotesChapter = input("What is the chapter of your notes? <insert 'Chapter' and chapter number> ")
            print()
            NotesLink = input("Upload here the link of your notes:")

# PreExistingNotes stores default notes
def PreExistingNotes():
    # creates availableNotes course: NotesTitle,NotesLink
    availableNotes = {}

    availableNotes["Mathematics"] = [["Systems", "Chapter 1"
                                      "https://docs.google.com/document/d/12Ubhr_Qw6aduMykVtbFCFLA2O32Ea7GKoVDsgV6UxIk/edit?usp=sharing"],
                                     ["Matrices", "Chapter 2", "https://docs.google.com/document/d/15ZSeOGDLVm8Hk2SmcJpTo9UfzhBzMs6D6fF3z_rlIA0/edit"],
                                     ["Vector Spaces", "Chapter 3", "https://docs.google.com/document/d/1uWV-CGrSXkPSCxgyRNrwALwwYsq6wudeTDjH1kXQvjU/edit"]]

    availableNotes["Marketing Management"] = [["Products and Services", "Chapter 1", "https://docs.google.com/document/d/1Qc6WegomqqfSwYfXYDbm1vW49R9NZhdDYhlZo3YupHs/edit?usp=sharing"],
                                              ["New Product Development", "Chapter 2", "https://docs.google.com/document/d/1WQLcSCfxibARMOn_3pAqXLERRtgFY5SZB99c4AinynQ/edit?usp=sharing"],
                                              ["Branding", "Chapter 3", "https://docs.google.com/document/d/1o8B3k4wHHSkmPj2US5JwdTDx8ojvxKwl_zjBNkmmUJs/edit?usp=sharing"]]

    availableNotes["Probability and Statistics"] = [["Intro to Multivariate Statistical Analysis", "Chapter 1", "https://docs.google.com/document/d/1ZQhx4tAdSH6MXkJpAv7kF8MUgdlUtigxdZISMj26h7U/edit?usp=sharing"],
                                                    ["Data Assessment & Evaluation", "Chapter 2", "https://docs.google.com/document/d/1D7Qwv-V5_IxhNbUMacHrRFVt9YK0R1MvIxnSdKmKbNE/edit?usp=sharing"],
                                                    ["Principal Component Analysis & Cluster Analysis", "Chapter 3", "https://docs.google.com/document/d/1vmcHfTepUkzRaSMc2XJyiX2F9BAL7bfMy4Ie2wHFLS0/edit?usp=sharing"]]

    availableNotes["Algorithms and Data Structures"] = [["Search Algorithms and Runtime", "Chapter 1", "https://docs.google.com/document/d/1FOHSX94IUOzNZOTHKXbh1_UWNOPGggIpDuHl-mk2n2c/edit?usp=sharing"],
                                                        ["Arrays, Linked Lists, Selection Sort", "Chapter 2", "https://docs.google.com/document/d/1CjwUiTdTwAkIRgWVChepRSpYsn6vZs0OQD7UhVDRWqw/edit?usp=sharing"],
                                                        ["Recursion", "Chapter 3", "https://docs.google.com/document/d/1Q_mljP1nIlDqOiOsI705-APOTynLBEfuHBb4OiQJkEk/edit?usp=sharing"]]

    availableNotes["Programming"] = [["Graphical User Interfaces", "Chapter 1", "https://docs.google.com/document/d/1yor2mDXPRguValGf0yzSPeXm8S-rFfyBWn-Qv90plII/edit?usp=sharing"],
                                     ["Definite Loops and Math Library", "Chapter 2", "https://docs.google.com/document/d/1YE9or8ywDPmi4lb8I7nNGCt8LDLZFgg7nx3iRhBK2Tk/edit?usp=sharing"],
                                     ["Visualiaing Data with Pandas", "Chapter 3", "https://docs.google.com/document/d/1fe86PO-CoqiWopSMlFVX1o1dK_6Uv5JXCXIPH5CAY0o/edit?usp=sharing"]]

    availableNotes["Building Powerful Relationships"] = [["7 Basic Communication Skills", "Chapter 1", "7 basic communication skills.docx"],
                                                         ["Pathos, Ethos and Logos","Chapter 2", "https://www.ted.com/talks/danish_dhamani_how_i_overcame_my_fear_of_public_speaking"],
                                                         ["How to do your own Ted Talk", "Chapter 3", "https://www.wix.com/wordsmatter/blog/2020/12/ethos-pathos-logos/"]]

    availableNotes["Entrepeneurship & Innovation"] = [["Dynamics", "Chapter 1", "https://docs.google.com/document/d/1sCO9ZETyAv7-KcTT1FH4RJ-4MKLuRaIfRCR4LHCgVT4/edit?usp=sharing"],
                                                         ["Entrepeneurial Mindset","Chapter 2", "https://docs.google.com/document/d/1qmJthzBIkogUv96gADBsKkCM-RXG7xDT2C3oi3-qb3Y/edit?usp=sharing"],
                                                         ["How Do Ideas Emerge", "Chapter 3", "https://docs.google.com/document/d/1rkHMd6d56zUfmg7qer3G2Tq2G--uN7213GwArAJwt7U/edit?usp=sharing"]]
    
    return availableNotes

def repeat(availableCourses, availableNotes):
    UserPick = input("\nEnter U to upload notes or F to find notes or Q to Quit:")
    UserPick.upper().strip()

    while UserPick != "U" and UserPick != "F":
        if UserPick == "Q" or UserPick == "":
            print("Exiting Program...")
            time.sleep(3)
            break
        else:
            print("Wrong Letter. Restarting Program.\nLoading...")
            time.sleep(5)

    if UserPick == "U":
        NotesUploader(availableCourses, availableNotes)
        repeat(availableCourses, availableNotes)
    elif UserPick == "F":
        NotesFinder(availableNotes)
        repeat(availableCourses, availableNotes)


def main():
    print("Welcome to Noted - The marketplace for your notes at IE University, BBADBA, Year 2.")
    time.sleep(1)
    print("Please sign up/log in (For your security passwords will be encrypted)")
    time.sleep(1)
    # Check Credentials
    UserIdentification()
    availableNotes = PreExistingNotes()
    availableCourses = [key for key in availableNotes.keys()]
    # Asks the user if it wants to upload or find notes
    repeat(availableCourses, availableNotes)

main()
