# The game() function in a program let's a user to play a game and returns the score as an integer.
# You need to read a file "HiScore.txt" which is either blank or contains the previous hi-score.
# So, WAP to update the highscore when games breaks the hi-score. 


def game():
    
    return 94


score=game()
with open("D:\Python Learning\Chapter10_File_InputOutput\\hi-score.txt") as fil:
    hiscore= fil.read()

if hiscore=="":
        with open("D:\Python Learning\Chapter10_File_InputOutput\\hi-score.txt","w") as fil:
            fil.write(str(score))

elif int(hiscore)<score:
    with open("D:\Python Learning\Chapter10_File_InputOutput\\hi-score.txt","w") as fil:
        fil.write(str(score))



