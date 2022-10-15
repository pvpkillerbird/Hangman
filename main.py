import time
import random
file = open("words","r")
word_bank = []
for line in file:
    word_bank += line.split()
ans = (random.choice(word_bank))
t =len(ans)
bool = False
guesses = []
tries_left = random.randrange(6,8,1)
num = -1
key = ""
for i in range(t):
    key += "_"
#print(ans)
print("Welcome to hangman!")
time.sleep(1)

print("You will have to guess the word with 6 wrong tries allowed.\nOnly the first letter of your guess will be submitted.\n")
time.sleep(1)

print(key)
while not bool:
    state = True
    state_1 = False
    print("\n","\bGuesses used: ", guesses)
    print("Tries left= ", tries_left)
    letter = input("Choose a letter:").lower()
    x = letter[0]
    key_1=list(key)
    if len(letter) > 1:
        guesses.append(letter)
        if letter == ans:
            key = ans
        else:
            state = False
    else:
        guesses.append(x)
        for abc in ans:
            num += 1
            if x == abc:
                key_1[num] = x
                key="".join(key_1)
                state_1= True
            else:
                state = False
    if not state and not state_1:
        tries_left -= 1
    num= -1
    print(key)
    if key == ans:
        bool = True
        print("You won!")
    elif tries_left == 0:
        bool = True
        print("The answer was", ans, "\b! Try again.")

"""
if x == abc:
            print(abc, end="")
else:
            print("_", end="")
"""

file.close()
