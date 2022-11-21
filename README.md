# Project - Noted

Noted - The class notes marketplace for all courses in BBADBA Year 2.

Noted Platform Description:
  
   - Users can find and access a database of notes from any 2nd year BBADBA course.  
   - Users can also upload notes from any 2nd year BBADBA course which then are added to the Noted notes database.

# Installation

In order to use Noted, make sure you have the following installed:
    
   - Python version no older than 3.6
   - Libraries: pandas, time, hashlib, re, sys
    


# Usage

When a user enters our application, they will be greeted with the following messages:

  1. Welcome to Noted - The marketplace for your notes at IE University, BBADBA, Year 2
  2. Please sign up/log in (For your security passwords will be encrypted)

To begin, the user will have to create an account by entering their IE email and their password (they will also have to confirm this password) by selecting option 1. After creating their Noted account, they will be asked to log in using the same email and password by selecting option 2.

If they already have an account, the user can skip directly to the log in option.

Now, the user will be asked to choose from the following:

  1. Input "U" to upload their notes
  2. Input "F" to find other people's notes
  3. Input "Q" to quit the program
  
  The user will be prompted with this options after every time the upload or look for notes in   our program
  
Uploading Notes:

  - The user will have to enter a course included in the displayed list of available courses
  - Then the title of their document
  - The chapter number of the course it pertains to
  - And finally the link to the actual document
  
  Output: The program will display a filtered dataframe of the previously chosen course (from the pandas library) with each row containing the title, chapter number,             and link to show that they have succesfully uploaded their document
  
Finding Notes:

  - The user will have to enter a course included in the displayed list of available courses
  
   Output: The program will display a filtered dataframe of the previously chosen course (from the pandas library) with each row containing the title, chapter number,            and link to show that they have succesfully uploaded their document


# Information About the Code
In order to run our program, we have used the following data structures:

1. Hash Tables - Has been used in order to store the association between courses (value) and their given notes (its key).
 
 
And the following algorithms:
1. Insertion
2. Deletion
3. Searching

Structure:
The program follows stack data structure. Whenever a function is invoked then the calling function is pushed into the stack and the function called is executed. Once the called function completes its execution and returns then then the calling function is popped from the stack and executed.




# Credits
Jorge Rodriguez

Miguel Ferrer

Pablo Stoclet

Alvaro De Castro

Adolfo Topham

Carlos Junquera
