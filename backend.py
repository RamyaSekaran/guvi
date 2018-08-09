alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

s=[]
count=0
ct=0
import random

for i in range(6):
    y=random.choice(alphabet)
    s.append(y)

print(s)
for i in range(6):
    for j in range(i+1,6):
        if s[i]==s[j]:
            count=count+1
print(count)
print(s)
inp=[]
guess=20
inp1=inp
same=0
diff=0
print("Hey! Welcome to the F22Labs Game")
print("There is a 6 letter word selected by me,can you guess the word? (in Capital letters)")
while same!=6 and guess>0:
    same=0
    diff=0

    inp=input();
    while(len(inp)>6 or len(inp)<6):
        print("Enter the Word with a length of 6 characters")
        inp=input()
    for i in range(6):
        for j in range(i+1,6):
            if s[i]==s[j]:
                ct=ct+1
    for i in range(6):
        if s[i]==inp[i]:
            same=same+1
        else:
            for j in range(6):
                if s[i]==inp[j]:
                    diff=diff+1
                    break
    if ct==count:
        print("\nNumber of characters that are correct but are in the wrong place are ",diff-ct)
        print("Number of characters that are correct and are in the correct place are",same)
    else:
        print("\nNumber of characters that are correct but are in the wrong place are ",diff)
        print("Number of characters that are correct and are in the correct place are",same)

    if same==6:
        print("Congratulations!! You found the string!!")
        break;
    guess=guess-1
    if guess==0:
        print("Game has ended")
        break;
    print("Guesses the remaining:",guess)
    print("Please try again \n")
    print("Guess the word ")
