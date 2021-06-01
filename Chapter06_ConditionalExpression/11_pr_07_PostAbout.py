# WAP to find out whether a given post is talking about "someone" or not Enter in any case format. 


post=input("Enter Your Post Here  : ")
cpost=post.lower()


if("someone" in cpost):
    print("The Entered Post Has something to tell about someone.")

else:
    print("There is nothing to talk about Someone in the post.")

