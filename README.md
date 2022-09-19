# PROJECTS FOR PYTHON3 PROGRAMMING COURSE ON COURSERA

## PR0JECT 1: sentiments.py
We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv which has the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet. We have also words that express positive sentiment and negative sentiment, in the files positive_words.txt and negative_words.txt.

Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. You will create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.
### STEP 1
To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.)

### STEP 2
Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered positive words. Use the list, positive_words to determine what words will count as positive. The function should return a positive integer - how many occurrences there are of positive words in the text. Note that all of the words in positive_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.

### STEP 3
Next, copy in your strip_punctuation function and define a function called get_neg which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered negative words. Use the list, negative_words to determine what words will count as negative. The function should return a positive integer - how many occurrences there are of negative words in the text. Note that all of the words in negative_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.

### STEP 4
Finally, copy in your previous functions and write code that opens the file project_twitter_data.csv which has the fake generated twitter data (the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet). Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. Copy the code from the code windows above, and put that in the top of this code window. Now, you will write code to create a csv file called resulting_data.csv, which contains the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall) for each tweet. The file should have those headers in that order. Remember that there is another component to this project. You will upload the csv file to Excel or Google Sheets and produce a graph of the Net Score vs Number of Retweets. Check Coursera for that portion of the assignment, if you’re accessing this textbook from Coursera.


## PROJECT 2: movie-rating.py
This project will take you through the process of mashing up data from two different APIs to make movie recommendations. The TasteDive API lets you provide a movie (or bands, TV shows, etc.) as a query input, and returns a set of related items. The OMDB API lets you provide a movie title as a query input and get back data about the movie, including scores from various review sites (Rotten Tomatoes, IMDB, etc.).

You will put those two together. You will use TasteDive to get related movies for a whole list of titles. You’ll combine the resulting lists of related movies, and sort them according to their Rotten Tomatoes scores (which will require making API calls to the OMDB API.)

To avoid problems with rate limits and site accessibility, we have provided a cache file with results for all the queries you need to make to both OMDB and TasteDive. Just use requests_with_caching.get() rather than requests.get(). If you’re having trouble, you may not be formatting your queries properly, or you may not be asking for data that exists in our cache. We will try to provide as much information as we can to help guide you to form queries for which data exists in the cache.
### STEP 1
Your first task will be to fetch data from TasteDive. The documentation for the API is at https://tastedive.com/read/api.

Define a function, called get_movies_from_tastedive. It should take one input parameter, a string that is the name of a movie or music artist. The function should return the 5 TasteDive results that are associated with that string; be sure to only get movies, not other kinds of media. It will be a python dictionary with just one key, ‘Similar’.

Try invoking your function with the input “Black Panther”.

HINT: Be sure to include only q, type, and limit as parameters in order to extract data from the cache. If any other parameters are included, then the function will not be able to recognize the data that you’re attempting to pull from the cache. Remember, you will not need an api key in order to complete the project, because all data will be found in the cache.
### STEP 2
Please copy the completed function from above into this active code window. Next, you will need to write a function that extracts just the list of movie titles from a dictionary returned by get_movies_from_tastedive. Call it extract_movie_titles.
### STEP 3
Please copy the completed functions from the two code windows above into this active code window. Next, you’ll write a function, called get_related_titles. It takes a list of movie titles as input. It gets five related movies for each from TasteDive, extracts the titles for all of them, and combines them all into a single list. Don’t include the same movie twice.
### STEP 4
Your next task will be to fetch data from OMDB. The documentation for the API is at https://www.omdbapi.com/

Define a function called get_movie_data. It takes in one parameter which is a string that should represent the title of a movie you want to search. The function should return a dictionary with information about that movie.

Again, use requests_with_caching.get(). For the queries on movies that are already in the cache, you won’t need an api key. You will need to provide the following keys: t and r. As with the TasteDive cache, be sure to only include those two parameters in order to extract existing data from the cache.
### STEP 5
Please copy the completed function from above into this active code window. Now write a function called get_movie_rating. It takes an OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer. For example, if given the OMDB dictionary for “Black Panther”, it would return 97. If there is no Rotten Tomatoes rating, return 0.
### STEP 6
Now, you’ll put it all together. Don’t forget to copy all of the functions that you have previously defined into this code window. Define a function get_sorted_recommendations. It takes a list of movie titles as an input. It returns a sorted list of related movie titles as output, up to five related movies for each input movie title. The movies should be sorted in descending order by their Rotten Tomatoes rating, as returned by the get_movie_rating function. Break ties in reverse alphabetic order, so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.# python-3-programming

## PROJECT 4: wheel-of-python.py

### INTRO
This project will take you through the process of implementing a simplified version of the game Wheel of Fortune. Here are the rules of our game:

There are num_human human players and num_computer computer players.
Every player has some amount of money ($0 at the start of the game)

Every player has a set of prizes (none at the start of the game)

The goal is to guess a phrase within a category. For example:
Category: Artist & Song

Phrase: Whitney Houston’s I Will Always Love You

Players see the category and an obscured version of the phrase where every alphanumeric character in the phrase starts out as hidden (using underscores: _):
Category: Artist & Song

Phrase: _______ _______'_ _ ____ ______ ____ ___

Note that case (capitalization) does not matter

During their turn, every player spins the wheel to determine a prize amount and:
If the wheel lands on a cash square, players may do one of three actions:
Guess any letter that hasn’t been guessed by typing a letter (a-z)
Vowels (a, e, i, o, u) cost $250 to guess and can’t be guessed if the player doesn’t have enough money. All other letters are “free” to guess

The player can guess any letter that hasn’t been guessed and gets that cash amount for every time that letter appears in the phrase

If there is a prize, the user also gets that prize (in addition to any prizes they already had)

If the letter does appear in the phrase, the user keeps their turn. Otherwise, it’s the next player’s turn

Example: The user lands on $500 and guesses ‘W’
There are three W’s in the phrase, so the player wins $1500

Guess the complete phrase by typing a phrase (anything over one character that isn’t ‘pass’)
If they are correct, they win the game

If they are incorrect, it is the next player’s turn

Pass their turn by entering 'pass'

If the wheel lands on “lose a turn”, the player loses their turn and the game moves on to the next player

If the wheel lands on “bankrupt”, the player loses their turn and loses their money but they keep all of the prizes they have won so far.

The game continues until the entire phrase is revealed (or one player guesses the complete phrase)

—
### STEP 1
We’re going to define a few useful methods for you:

getNumberBetween(prompt, min, max)) repeatedly asks the user for a number between min and max with the prompt prompt

spinWheel() simulates spinning the wheel and returns a dictionary with a random prize

getRandomCategoryAndPhrase() returns a tuple with a random category and phrase for players to guess

obscurePhrase(phrase, guessed) returns a tuple with a random category and phrase for players to guess

### STEP 2
Part A: WOFPlayer

We’re going to start by defining a class to represent a Wheel of Fortune player, called WOFPlayer. Every instance of WOFPlayer has three instance variables:

.name: The name of the player (should be passed into the constructor)

.prizeMoney: The amount of prize money for this player (an integer, initialized to 0)

.prizes: The prizes this player has won so far (a list, initialized to [])

Of these instance variables, only name should be passed into the constructor.

It should also have the following methods (note: we will exclude self in our descriptions):

.addMoney(amt): Add amt to self.prizeMoney

.goBankrupt(): Set self.prizeMoney to 0

.addPrize(prize): Append prize to self.prizes

.__str__(): Returns the player’s name and prize money in the following format:
Steve ($1800) (for a player with instance variables .name == 'Steve' and prizeMoney == 1800)

Part B: WOFHumanPlayer

Next, we’re going to define a class named WOFHumanPlayer, which should inherit from WOFPlayer (part A). This class is going to represent a human player. In addition to having all of the instance variables and methods that WOFPlayer has, WOFHumanPlayer should have an additional method:

.getMove(category, obscuredPhrase, guessed): Should ask the user to enter a move (using input()) and return whatever string they entered.

.getMove()’s prompt should be:

{name} has ${prizeMoney}

Category: {category}
Phrase:  {obscured_phrase}
Guessed: {guessed}

Guess a letter, phrase, or type 'exit' or 'pass':
For example:

Steve has $200

Category: Places
Phrase: _L___ER N____N_L P_RK
Guessed: B, E, K, L, N, P, R, X, Z

Guess a letter, phrase, or type 'exit' or 'pass':
The user can then enter:

'exit' to exit the game

'pass' to skip their turn

a single character to guess that letter

a complete phrase (a multi-character phrase other than 'exit' or 'pass') to guess that phrase

Note that .getMove() does not need to enforce anything about the user’s input; that will be done via the game logic that we define in the next ActiveCode window.

Part C: WOFComputerPlayer

Finally, we’re going to define a class named WOFComputerPlayer, which should inherit from WOFPlayer (part A). This class is going to represent a computer player.

Every computer player will have a difficulty instance variable. Players with a higher difficulty generally play “better”. There are many ways to implement this. We’ll do the following:

If there aren’t any possible letters to choose (for example: if the last character is a vowel but this player doesn’t have enough to guess a vowel), we’ll 'pass'

Otherwise, semi-randomly decide whether to make a “good” move or a “bad” move on a given turn (a higher difficulty should make it more likely for the player to make a “good” move)
To make a “bad” move, we’ll randomly decide on a possible letter.

To make a “good” move, we’ll choose a letter according to their overall frequency in the English language.

In addition to having all of the instance variables and methods that WOFPlayer has, WOFComputerPlayer should have:

Class variable

.SORTED_FREQUENCIES: Should be set to 'ZQXJKVBPYGFWMUCLDRHSNIOATE', which is a list of English characters sorted from least frequent ('Z') to most frequent ('E'). We’ll use this when trying to make a “good” move.

Additional Instance variable

.difficulty: The level of difficulty for this computer (should be passed as the second argument into the constructor after .name)

Methods

.smartCoinFlip(): This method will help us decide semi-randomly whether to make a “good” or “bad” move. A higher difficulty should make us more likely to make a “good” move. Implement this by choosing a random number between 1 and 10 using random.randint(1, 10) (see above) and returning False if that random number is greater than self.difficulty. If the random number is less than or equal to self.difficulty, return True.

.getPossibleLetters(guessed): This method should return a list of letters that can be guessed.
These should be characters that are in LETTERS ('ABCDEFGHIJKLMNOPQRSTUVWXYZ') but not in the guessed parameter.

Additionally, if this player doesn’t have enough prize money to guess a vowel (variable VOWEL_COST set to 250), then vowels (variable VOWELS set to 'AEIOU') should not be included

.getMove(category, obscuredPhrase, guessed): Should return a valid move.
Use the .getPossibleLetters(guessed) method described above.

If there aren’t any letters that can be guessed (this can happen if the only letters left to guess are vowels and the player doesn’t have enough for vowels), return 'pass'

Use the .smartCoinFlip() method to decide whether to make a “good” or a “bad” move
If making a “good” move (.smartCoinFlip() returns True), then return the most frequent (highest index in .SORTED_FREQUENCIES) possible character

If making a “bad” move (.smartCoinFlip() returns False), then return a random character from the set of possible characters (use random.choice())

## PROJECT 5 tic-tac-toe.py --from python course project on netacad

### Scenario
Your task is to write a simple program which pretends to play tic-tac-toe with the user. To make it all easier for you, we've decided to simplify the game. Here are our assumptions:

-the computer (i.e., your program) should play the game using 'X's;
-the user (e.g., you) should play the game using 'O's;
-the first move belongs to the computer − it always puts its first 'X' in the middle of the board;
-all the squares are numbered row by row starting with 1 (see the example session below for reference)
-the user inputs their move by entering the number of the square they choose − the number must be valid, i.e., it must be an integer, it must be greater than 0 and less than 10, and it cannot point to a field which is already occupied;
-the program checks if the game is over − there are four possible verdicts: the game should continue, the game ends with a tie, you win, or the computer wins;
-the computer responds with its move and the check is repeated;
-don't implement any form of artificial intelligence − a random field choice made by the computer is good enough for the game.
The example session with the program may look as follows:

+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move: 1
+-------+-------+-------+
|       |       |       |
|   O   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move: 8
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move: 4
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move: 7
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
You won!

### Requirements
Implement the following features:

-the board should be stored as a three-element list, while each element is another three-element list (the inner lists represent rows) so that all of the squares may be accessed using the following syntax:
```
board[row][column]
```

-each of the inner list's elements can contain 'O', 'X', or a digit representing the square's number (such a square is considered free)
-the board's appearance should be exactly the same as the one presented in the example.
-implement the functions defined for you in the editor


## Challenge test from Turing 

### Baseball Game

You are keeping score for a baseball game with strange rules. The game consists of several rounds, where
the scores of past rounds may affect future rounds' scores.
At the beginning of the game, you start with an empty record. You are given a list of strings ops , where ops[i] is the ith operation you must apply to the record and is one of the following:
1. An integer x - Record a new score of x .
2. "+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
3. "D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
4. "C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be
a previous score. Return the sum of all the scores on the record.
Example 1:
Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.
Example 2:
Input: ops = ["5","-2","4","C","D","9","+","+"]
Output: 27
Explanation:
"5" - Add 5 to the record, record is now [5].
"-2" - Add -2 to the record, record is now [5, -2].
"4" - Add 4 to the record, record is now [5, -2, 4].
"C" - Invalidate and remove the previous score, record is now [5, -2].
"D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
"9" - Add 9 to the record, record is now [5, -2, -4, 9].
"+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
"+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.
Example 3:
Input: ops = ["1"]
Output: 1
Constraints:
• 1 <= ops.length <= 1000
• ops[i] is "C" , "D" , "+" , or a string representing an integer in the range [-3 * 104, 3 * 104] .
• For operation "+" , there will always be at least two previous scores on the record.
• For operations "C" and "D" , there will always be at least one previous score on the record.




### Valid Parentheses

Given a string s containing just the characters '(' , ')' , '{' , '}' , '[' and ']' , determine if the input
string is valid.
An input string is valid if:
0. Open brackets must be closed by the same type of brackets.
0. Open brackets must be closed in the correct order.
Constraints:
• 1 <= s.length <= 104
• s consists of parentheses only '()[]{}' .
Example 1:
Input: s = "()"
Output: valid
Example 2:
Input: s = "()[]{}"
Output: valid
Example 3:
Input: s = "(]"
Output: invalid
Example 4:
Input: s = "([)]"
Output: invalid
Example 5:
Input: s = "{[]}"
Output: valid
