# Bitly bruteforce script
This script first creates all possible two-letter combinations. Then the program tests if there's a working link behind that Bitly url. The program will write the found urls on a file that can be utilized after.

This script is based on the mathematically proven fact that there are only 26^2=676 possible combinations of two-letter strings (with no numbers or special characters). That's why we can store all of them in just one array with ease.

You need the following Python library:
 - eventlet
 
 
