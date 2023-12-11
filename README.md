# Final Project Report

* Student Name: milson chhantyal
* Github Username milsonchhantyal
* Semester: fall 2023
* Course: CS5001



## Description 
General overview of the project, what you did, why you did it, etc. 

I made a hangman game for my final project that inculdes 3 different topics the user can pick from. I wanted to make something that people could play so I decided on making the minigame hangman. I also wanted there to be muiltple topics that people could choose from so they have options on the genere they want to guess. It started with a list of words for colors then I made one for animals and one for countires. Out of these 3 topics there are at least 10 words each that the user cn guess from each topic. The user gets 6 attempts/guesses, the more they guess wrong the more parts of the hangman appear.

## Key Features
Highlight some key features of this project that you want to show off/talk about/focus on. 

One of the key highlights of this project is the display of "_" on the console. The function update_display allows the user to see where the correct letter they guessed is placed on the word. This is useful beacuse it gives a hint of what the word is and it keeps track of the correct letters the user has guessed. Another key feature is the ASCII art of the hangman. The visual representation of the hangman is an important factor to the game so adding it to this project was a priority. If the user guesses a wrong letter a part of the hangman art is displayed. Since there are 6 attempts at guessing correctly the hangman art has 6 stages where it gradually appears as the attempts decrease.

## Guide
How do we run your project? What should we do to see it in action? - Note this isn't installing, this is actual use of the project.. If it is a website, you can point towards the gui, use screenshots, etc talking about features.

To run the project, users simply need to execute the Python script. The program will prompt them to choose a topic (Colors, Animals, or Countries) and then guide them through the Hangman game, allowing them to guess the hidden word.

## Installation Instructions
If we wanted to run this project locally, what would we need to do?  If we need to get API key's include that information, and also command line startup commands to execute the project. If you have a lot of dependencies, you can also include a requirements.txt file, but make sure to include that we need to run `pip install -r requirements.txt` or something similar.

To run the project you just have to make sure Python is installed.

## Code Review
Go over key aspects of code in this section. Both link to the file, include snippets in this report (make sure to use the [coding blocks](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)).  Grading wise, we are looking for that you understand your code and what you did. 

The main part of the code is in hangman.py. It imports 2 files, hangman_drawings.py and topics_file.py. Within hangman.py there are multiple functions that work together to create the game. For example, choose_topic_menu is a function that presents users with 3 topics that they can choose from to play the game. Once the topic is chosen choose_topic_menu is used in initalize_game where a random word is picked from the topic the user has chosen. Each function is important to the overall game because they all have a role to play in the hangman game.

### Major Challenges
Key aspects could include pieces that your struggled on and/or pieces that you are proud of and want to show off.

I was struggling for a while with def get_valid_guess because I couldnt figure out a way to exlude options that werent letters without manually writing them in, but then I remembered in one of the homeworks we used .isalpha() which was perfect for this function becausae it looks through a string for alphabetical letters and returns True only if the string contains all alphabetical letters.

## Example Runs
Explain how you documented running the project, and what we need to look for in your repository (text output from the project, small videos, links to videos on youtube of you running it, etc)

For the example run I played a runthrough of the game myself and documented it under "example_run.py" which is a saved file in the repository. 

## Testing
How did you test your code? What did you do to make sure your code was correct? If you wrote unit tests, you can link to them here. If you did run tests, make sure you document them as text files, and include them in your submission. 

> _Make it easy for us to know you *ran the project* and *tested the project* before you submitted this report!_

I tested the code through doctests to make sure it was passing the tests. Throughout the processs I would run the code after every couple of lines to make sure it was running smoothly, and if there were any errors I would use that as feedback on what I needed to fix. The test is under "testing.py" in the repository.

## Missing Features / What's Next
Focus on what you didn't get to do, and what you would do if you had more time, or things you would implement in the future. 

I think one feature that would be great for this project is having a little fact about the hidden word once its revealed. For example, if the word was giraffe there could be a fun fact about giraffes once the user guessed the word or if the user ran out of attempts. I would also like it to add a score tracker for players who are more competitive. I feel like having a score that goes up by 1 when the user wins and down by 1 when the user loses would be a nice touch. The score wouldnt go to the negatives though, 0 would be the lowest. I was also playing around with Tkinter because I feel like having a GUI would make the game more enjoyable. Although I wasnt able to figure out how to fully incorparate my game with Tkinter, I would like to use more of it in the future because I feel like there are so many possiblites with it.

## Final Reflection
Write at least a paragraph about your experience in this course. What did you learn? What do you need to do to learn more? Key takeaways? etc.

I feel like throughout this course I've gained a deeper understanding of Python programming and software development concepts. Having to practice my coding ability continually provided practical experience in applying the knowledge I learned. For example, this project pushed me to use multiple modules and lessons from this semester to make a final project and it also helped me realize how much I've learned in just 1 semester. I was able to incorprate lessons all the way from week 1 with the ASCII art and more recent lessons as well with methods and loops. Moving forward I think I want to continue exploring advanced topics in programming like Tkinter because I feell ike the interface part of the program is one of the most rewarding aspects since theres a visual with the code your creating. I feel like this course has been instrumental in giving a strong foundation into computer science and a robust experience in learning how to think like a computer scientist. 
