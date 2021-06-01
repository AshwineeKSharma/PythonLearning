# WAP to Detect the spam comment where a spam comment is defined as a text containing following Keywords:
# "Make a lot of money" "Buy Now" "Subscribe This" "Click This"

comm=input("Enter the text : ")
spam=False

if("make a lot of money" in comm):
    spam=True
elif("buy now" in comm):
    spam=True
elif("subscribe this" in comm):
    spam=True
elif("click this" in comm):
    spam=True

else:
    spam=False


if(spam):
    print("The Text You Entered is Spam")

else:
    print("The Text You Entered is not Spam")






