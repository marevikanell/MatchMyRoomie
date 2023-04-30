# MatchMyRoomie

MatchMyRoomie aims to help you find the perfect Roommate!


# Table of Content 

1. Introduction 
2. Installation & Usage 
3. Further Improvements 
4. Credits 

# Introduction

This application was created for our Algorithms & Data Structures class. The project instructions were to create an application using at least of the algorithms that were learned during the course. 

MatchMyRoomie is an application that helps you find the ideal roommate based on a questionnaire. The application calculates the number of intersections between users and generates a max heap algorithm to match roommates based on shared interests and preferences. The questionnaire gathers information about users' lifestyle, habits, and preferences, and uses this information to determine which users are most compatible. Users can browse through their matches and contact potential roommates to find their perfect match.

# Limitation 

The algorithm is currently limited to displaying the perfect Roommate in the Area of the City of Madrid out of the pull of users on the platform.


# Installation 

To be able to run our program, make sure you have the following things installed:

Python programming language 

Libraries - In order to run our program, we make use of the following 3 libraries: heapq_max and pickle, heapq

To download the library type the following command
- pip install heapq_max 
- pip install pickle 
- pip install heapq

Now that we have the required libraries set up, open the file named app.py and run the program.

# Usage

After a user enters our platform, they will be welcomed and asked what steps they want to take: 

- Create an account 
- Log in 

The user will now have to enter their choice. After their choice is validated, the respective action will be carried out and the user will be asked more questions based on their choice

1. Creating an account: Our create account function has the purpose of enabling the user to create an account to find the perfect roomate 

      - **User input** : A username and a password, if the username already exist the         programm will ask the user to choose a valid username 
      - Once the user has created an account ,they are able log in and complete the           questionnaire to find compatible roommates.

2. Log into your account: Our main menu functions helps the user to navigate through the whole process 
      
      -It will start by displaying a list with all available options that the user          can choose from. The user will be asekd to choose one option by typing the            proper number on his/her keyboard
      
      - The login menu will be displayed with options such as updating your profile,         filling out the questionare and accsessing your matches.
      
     
      - **User Input** :These are the answers of the filled out questionaire of the user (the                                 questions have to be answered using the keyboard, they will be multiple                               choice)

      - **Output** : Depending on the option that the user typed, rommate options that best match the                      user's preferences will be displayed. If there is more than one match, all of                          them will be displayed accorind to priority. The users that share no                                  intersections will be filtered out. 


# Further Improvements











# Credits 

This project was created for our Algorithms and Data Structures course at IE University. The project was created by 

- VICTORIA VOLMAN
- NEAL LASOWSKI 
- MARIA EVRYDIKI KANELLOPOULOU
- JENNA HATEM SOBHY TIEBY
- RAKEL ÓSK SIGURÐARDÓTTIR



