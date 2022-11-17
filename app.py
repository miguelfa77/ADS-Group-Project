
#Introduction function introduces the user to the app.
def Introduction():
  print("Welcome to Noted - The marketplace for your notes at IE University, BBADBA, Year 2.")
  #Asks the user if it wants to upload or find notes
  print("\nEnter U to upload notes:\nEnter F to find notes:\nEnter Q to Quit:")

#notesFinder function (takes availableNotes as input) returns 
#Finder needs to input course 
def NotesFinder(availableNotes):
    print("\nAvailable courses: ")
    
#notesUploader function to upload notes link.
def NotesUploader():
    #return UploadedNotes

#NotesStorage all notes
def NotesStorage(UploadedNotes,DefaultNotes):
    #returns availableNotes


#PreExistingNotes stores default notes
def PreExistingNotes():
    #creates availableNotes course: NotesTitle,NotesLink
    availableNotes = {}

    availableNotes["Algorithms and Data Structures"] = ["Algorithms and Data Structures Notes", "https://docs.google.com/document/d/1yhn4FexW91B4uUPILZaIinKlN8kviWodLRo7t6Mq_ig/edit?usp=sharing"]
    availableNotes["Marketing"] = ["Marketing Management Notes", "https://docs.google.com/document/d/1Q4stCUyCwlASZlxDthlFPlJ4liHGbeDlrUC94-O_n2Q/edit?usp=sharing"]
    availableNotes["Mathematics"] = ["Mathematics Notes", ""]
    availableNotes["Probability and Statistics"] = ["Probability and Statistics Notes", ""]
    availableNotes["Building Powerful Relationships"] = ["Building Powerful Relationships Notes", ""]
    availableNotes["Programming"] = ["Programming", ""]
    
    return availableNotes
#This main function calls the rest of the functions
def main():
    Introduction()
