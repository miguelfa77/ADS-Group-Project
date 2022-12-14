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

Login System:
  1. User Identification function prompts user to choose between sign-up(1), login(2) or quit(3).
  2. Sign up function prompts for email, password, confirmation password. It hashes the password and stores it in a file called NotedCredentials.txt along      with the email. It loops until email is proved to be valid.
  3. Email Verifiation verifies the email to prove that it is valid (must be in email format and be an IE email).
  4. Login function prompts for email and password. It hashes the password and checks if it matches with the stored email and password.

Now, the user will be asked to choose from the following:

  1. Input "U" to upload their notes
  2. Input "F" to find other people's notes
  3. Input "Q" to quit the program
  
  The user will be prompted with these options after every time the upload or look for notes in   our program
  
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

1. Hash Tables --> Has been used in order to store the association between courses (key) and their given notes (value).
2. Python list --> Used to create AvailableCourses, for the users to choose from
 
 
And the following algorithms:
1. Hashing --> Encrypting strings by transforming them into bytes and applying a hash function. (used hashlib library to hash passwords)
2. Insertion
3. Searching
4. Backtracking -->Eliminating solutions that fail to meet the criteria (password and email verification)

Structure:

The program follows a stack data structure. Whenever a function is invoked then the calling function is pushed into the stack and the function called is executed. Once the called function completes its execution and returns then then the calling function is popped from the stack and executed.
The function call is made from the main() function, to the rest of the functions inside main().
??



# Credits
Jorge Rodriguez

Miguel Ferrer

Pablo Stoclet

Alvaro De Castro

Adolfo Topham

Carlos Junquera
