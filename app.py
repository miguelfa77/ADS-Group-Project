import pandas as pd
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
            SignUp(emailValidity=False)
        elif ch == 2:
            LogIn()
            break
        elif ch == 3:
            sys.exit()


# Sign Up Process (Encryption)
def SignUp(emailValidity):
    # input email (loop until emailValidity is True), password, confirmationPassword
    while emailValidity is not True:
        email = input("Enter email address (Use IE address): ")
        emailValidity = EmailVerification(email, emailValidity)
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
    # prompt for email/password, encode() from str to byt and hash into authenUnhash
    email = input("Enter email: ")
    password = input("Enter password: ")
    encodedPswrd = password.encode()
    HashedPswrd = hashlib.blake2b(encodedPswrd).hexdigest()
    # open file in reading, store in StoredEmail and storedPassword var. close file
    with open("NotedCredentials.txt", "r") as f:
        storedEmail, storedPassword = f.read().split("\n")
        f.close()
        # if input email is same as stored and hash is same as storedPassword, login.
        if email == storedEmail and HashedPswrd == storedPassword:
            print("Logged in to Noted Successfully!")
            time.sleep(3)
        else:
            print("Login failed! \n")
            time.sleep(5)
            sys.exit()


def EmailVerification(email, emailValidity):
    #regex is accepted email format
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    ie = "ie"
    # if email is valid (also IE email) change emailValidity to True and return
    if re.fullmatch(regex, email):
        if ie in email:
            emailValidity = True
            print("Email Valid!\n")
            return emailValidity
    #if not from ie or not valid emailValidity remains as False
        else:
            print("Email address valid but not from IE. Use IE address in order to sign up!\n")
            return emailValidity
    else:
        print("Invalid Email.\n")
        return emailValidity


# notesFinder function (takes availableNotes as input) returns title and link
def NotesFinder(availableNotes):
    print("\nHere are the available courses: \n")
    # Creates availableCourses list
    # append the keys to the availableCourses list
    availableCourses = [key for key in availableNotes.keys()]
    print(availableCourses)
    print()

    # User inputs chosenCourse.
    chosenCourse = input("Choose a course from the list: ")
    chosenCourse.title().strip()
    #if chosenCourse is not empty and is in availableCourses get availableNotes values and store as notes.
    #puts notes(title, chapter and link) into data frame(df) and print
    while chosenCourse != "":
        if chosenCourse in availableCourses:
            notes = availableNotes.get(chosenCourse)
            df = pd.DataFrame(notes, columns=["Title", "Chapter", "Link"])
            print(df)
            break
    #else loop prompt
    else:
        print("Sorry, course not available in our database. \nTry again!")
        time.sleep(0.5)
        chosenCourse = input("Choose your course: ").title().strip()


# notesUploader function to upload notes link.
def NotesUploader(availableCourses, availableNotes):
    print()
    print(availableCourses)
    print()

    #prompt for subject, NotesTitle, NotesChapter, NotesLink
    subject = input("What subject are your notes from?:")
    NotesTitle = input("What is the title of your notes?:")
    NotesChapter = input("What Chapter are your notes from?: write <Chapter> and the number:")
    NotesLink = input("Upload here the link of your notes:")

    # if input subjects is not a 2nd year 1st semester BBADBA course, reprompt
    if subject in availableNotes:
        availableNotes[subject] += [[NotesTitle, NotesChapter, NotesLink]]
        notes = availableNotes.get(subject)
        df = pd.DataFrame(notes, columns=["Title", "Chapter", "Link"])
        print(df)
    else:
        print(
            "Sorry, the course you entered is not included in Noted. Please try again (capitalize the first letter of each word).")
        time.sleep(1)
        subject = input("What subject are your notes from?:")
        NotesTitle = input("What is the title of your notes?:")
        NotesChapter = input("What Chapter are your notes from?: write <Chapter> and the number:")
        NotesLink = input("Upload here the link of your notes:")
     # if inputed subject is in database, add to availableNotes (database) and print in table format as data frame


# PreExistingNotes stores default notes
def PreExistingNotes():
    # creates availableNotes course: NotesTitle, NotesChapter, NotesLink
    availableNotes = {}

    availableNotes["Mathematics"] = [["Systems", "Chapter 1",
                                      "https://docs.google.com/document/d/12Ubhr_Qw6aduMykVtbFCFLA2O32Ea7GKoVDsgV6UxIk/edit?usp=sharing"],
                                     ["Matrices", "Chapter 2",
                                      "https://docs.google.com/document/d/15ZSeOGDLVm8Hk2SmcJpTo9UfzhBzMs6D6fF3z_rlIA0/edit"],
                                     ["Vector Spaces", "Chapter 3",
                                      "https://docs.google.com/document/d/1uWV-CGrSXkPSCxgyRNrwALwwYsq6wudeTDjH1kXQvjU/edit"]]

    availableNotes["Marketing Management"] = [["Products and Services", "Chapter 1",
                                               "https://docs.google.com/document/d/1Qc6WegomqqfSwYfXYDbm1vW49R9NZhdDYhlZo3YupHs/edit?usp=sharing"],
                                              ["New Product Development", "Chapter 2",
                                               "https://docs.google.com/document/d/1WQLcSCfxibARMOn_3pAqXLERRtgFY5SZB99c4AinynQ/edit?usp=sharing"],
                                              ["Branding", "Chapter 3",
                                               "https://docs.google.com/document/d/1o8B3k4wHHSkmPj2US5JwdTDx8ojvxKwl_zjBNkmmUJs/edit?usp=sharing"]]

    availableNotes["Probability and Statistics"] = [["Intro to Multivariate Statistical Analysis", "Chapter 1",
                                                     "https://docs.google.com/document/d/1ZQhx4tAdSH6MXkJpAv7kF8MUgdlUtigxdZISMj26h7U/edit?usp=sharing"],
                                                    ["Data Assessment & Evaluation", "Chapter 2",
                                                     "https://docs.google.com/document/d/1D7Qwv-V5_IxhNbUMacHrRFVt9YK0R1MvIxnSdKmKbNE/edit?usp=sharing"],
                                                    ["Principal Component Analysis & Cluster Analysis", "Chapter 3",
                                                     "https://docs.google.com/document/d/1vmcHfTepUkzRaSMc2XJyiX2F9BAL7bfMy4Ie2wHFLS0/edit?usp=sharing"]]

    availableNotes["Algorithms and Data Structures"] = [["Search Algorithms and Runtime", "Chapter 1",
                                                         "https://docs.google.com/document/d/1FOHSX94IUOzNZOTHKXbh1_UWNOPGggIpDuHl-mk2n2c/edit?usp=sharing"],
                                                        ["Arrays, Linked Lists, Selection Sort", "Chapter 2",
                                                         "https://docs.google.com/document/d/1CjwUiTdTwAkIRgWVChepRSpYsn6vZs0OQD7UhVDRWqw/edit?usp=sharing"],
                                                        ["Recursion", "Chapter 3",
                                                         "https://docs.google.com/document/d/1Q_mljP1nIlDqOiOsI705-APOTynLBEfuHBb4OiQJkEk/edit?usp=sharing"]]

    availableNotes["Programming"] = [["Graphical User Interfaces", "Chapter 1",
                                      "https://docs.google.com/document/d/1yor2mDXPRguValGf0yzSPeXm8S-rFfyBWn-Qv90plII/edit?usp=sharing"],
                                     ["Definite Loops and Math Library", "Chapter 2",
                                      "https://docs.google.com/document/d/1YE9or8ywDPmi4lb8I7nNGCt8LDLZFgg7nx3iRhBK2Tk/edit?usp=sharing"],
                                     ["Visualiaing Data with Pandas", "Chapter 3",
                                      "https://docs.google.com/document/d/1fe86PO-CoqiWopSMlFVX1o1dK_6Uv5JXCXIPH5CAY0o/edit?usp=sharing"]]

    availableNotes["Building Powerful Relationships"] = [
        ["7 Basic Communication Skills", "Chapter 1", "https://docs.google.com/document/d/1M1F1bGdX8bwjP8RLppvCMeMsNKzVE0HRQukOiGFr5DE/edit?usp=sharing"],
        ["Pathos, Ethos and Logos", "Chapter 2",
         "https://www.ted.com/talks/danish_dhamani_how_i_overcame_my_fear_of_public_speaking"],
        ["How to do your own Ted Talk", "Chapter 3",
         "https://www.wix.com/wordsmatter/blog/2020/12/ethos-pathos-logos/"]]

    availableNotes["Entrepreneurship & Innovation"] = [["Dynamics", "Chapter 1",
                                                       "https://docs.google.com/document/d/1sCO9ZETyAv7-KcTT1FH4RJ-4MKLuRaIfRCR4LHCgVT4/edit?usp=sharing"],
                                                      ["Entrepeneurial Mindset", "Chapter 2",
                                                       "https://docs.google.com/document/d/1qmJthzBIkogUv96gADBsKkCM-RXG7xDT2C3oi3-qb3Y/edit?usp=sharing"],
                                                      ["How Do Ideas Emerge", "Chapter 3",
                                                       "https://docs.google.com/document/d/1rkHMd6d56zUfmg7qer3G2Tq2G--uN7213GwArAJwt7U/edit?usp=sharing"]]

    return availableNotes

#repeat prompts for U(Upload), F(Find) or Q(Quit) as UserPick and caps it.
def repeat(availableCourses, availableNotes):
    UserPick = input("\nEnter U to upload notes \nF to find notes \nQ to Quit \nChoose an option:")
    UserPick.upper().strip()

    #if Q or types nothing, quit. 
    while UserPick != "U" and UserPick != "F":
        if UserPick == "Q" or UserPick == "":
            print("Exiting Program...")
            time.sleep(3)
            break
        else:
            print("Wrong Letter. Restarting Program.\nLoading...")
            time.sleep(5)

    #if U run NotesUploader, if F run NotesFinder. Prompts again after Upload or Find.
    if UserPick == "U":
        NotesUploader(availableCourses, availableNotes)
        repeat(availableCourses, availableNotes)
    elif UserPick == "F":
        NotesFinder(availableNotes)
        repeat(availableCourses, availableNotes)


def main():
    #Welcomes user
    print("Welcome to Noted - The marketplace for your notes at IE University, BBADBA, Year 2.")
    time.sleep(1)
    print("Please sign up/log in (For your security passwords will be encrypted)")
    time.sleep(1)
    # Check Credentials
    UserIdentification()
    #PreExistingNotes returns availableNotes
    availableNotes = PreExistingNotes()
    availableCourses = [key for key in availableNotes.keys()]
    # Runs the prompt for user choice
    repeat(availableCourses, availableNotes)


main()
    

