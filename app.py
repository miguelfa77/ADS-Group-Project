
import time

#Introduction function introduces the user to the app.
def Introduction():
  print("Welcome to Noted - The marketplace for your notes at IE University, BBADBA, Year 2.")
  #Asks the user if it wants to upload or find notes
  UserPick = str(input("\nEnter U to upload notes or F to find notes or Q to Quit:")).upper().strip()
  return UserPick

#notesFinder function (takes availableNotes as input) returns NotesTitle and NotesLink
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
