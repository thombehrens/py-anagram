# Anagram Coding Kata

[Here][1] is a link to the challenge

## [Version 1][2]

This was my first python script since college! I feel like I already understand python more now than I did then.

I learned the basics of `venv`, and of using Python in VS Code. I actually got to learn quite a bit about how debugging works in VS Code, since Salesforce development in VS Code doesn't have any good local debugging tools (only bad ones).

I _really_ like the syntax of Python. And I love how easy it is to get started.

The thing that tripped me up was learning to use `list.copy()` in order to duplicate a list - it took me about 30 minutes to figure out that when I was removing words from `valid_words`, I was also removing words from `words`, which was making my loop end before it had gone through every element and was throwing everything off.

This thing takes a long time to run. I am sure there are ways to do it more efficiently. I could get rid of `find_valid_words` and just do an n^2 nested for loop for the whole list... that would definitely look cleaner... I'll be interested to see if that runs faster.

Another thing that has thrown me off is needing to use the i+=1 loop iterator for the inner while loop. I am going to try to find way to get rid of that... I've either omitted it or put it at the wrong level of indentation a few times and the only way I realize it's stuck in an infinite loop is when the fans on my MacBook Air kick in.

I wonder if I can write this program (and using a dictionary this huge) in such a way that doesn't turn on my computer fans?

Execution times:
46.440101146698 seconds
48.45626997947693 seconds
48.42616391181946 seconds

[1]: https://codingdojo.org/kata/Anagram/
[2]: https://github.com/thombehrens/py-anagram/blob/master/anagram-v1.py
