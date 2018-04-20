# Bitly bruteforce script
This script creates all possible two-letter combinations and then checks if there's a Bitly link with that combination. If a working combination is found, it will be printed on a file.

This script is based on the mathematically proven fact that there are only 26^2=676 possible combinations of two-letter strings (with no numbers or special characters). That's why we can store all of them in just one array with ease.

You need the following Python library:
 - `eventlet`
 
It may be installed with `pip`

``` pip install eventlet ```
