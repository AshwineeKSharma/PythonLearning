# WAP to fill in a template given below with name and date

#    letter =  '''Dear <Name>, You are Selected!  <Date>'''

name=input("Enter Your Name : ")
date=input("Enter Date : ")


letter =  '''Dear <|NAME|>, 
 You are Selected!  
                            

 Date : <|DATE|>'''

letter=letter.replace("<|NAME|>", name)
letter=letter.replace("<|DATE|>", date)


print(letter)