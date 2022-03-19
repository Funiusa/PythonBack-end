# PythonBack-end

Exercise 00: Blockchain

Correct lines are 32 characters long
They start with exactly 5 zeroes, so e.g. line starting with 6 zeroes is NOT
considered correct

So, for the example above your script should print:

00000254b208c0f43409d8dc00439896
0000085a34260d1c84e89865c210ceb4
0000071f49cffeaea4184be3d507086v

Your code should accept the number of lines as an argument, like this:
~$ cat data_hashes_10lines.txt | python blocks.py 10
This way the program when stop when it processed 10 lines.

Exercise 01: Decypher

It should be launchable like this:
~$ python decipher.py "Have you delivered eggplant pizza at restored keep?"
and print out the answer as a single word without spaces.

Exercise 02: Track and Capture
So, as an input your code is given a 2d "image" as text, five characters over
three lines, like this:

*d&t*
**h**
*l*!*

If a given pattern is not 3x5, then 'Error' word should be printed instead.
