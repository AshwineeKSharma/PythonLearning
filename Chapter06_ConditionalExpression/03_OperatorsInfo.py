# An operator in a programming language is a symbol 
# that tells the compiler or interpreter to perform 
# specific mathematical, relational or logical
# operation and produce final result. 


# Mathematical operators are used to perform mathematical operations.  e.g. : +  -   /   *


# Relational operator are used to identify / evaluate conditions e.g. :   <=, >=, ==, !=


# A logical operator is a symbol or word used to connect two or more 
# expressions such that the value of the compound expression produced 
# depends only on that of the original expressions and on the meaning 
# of the operator. Common logical operators include AND, OR, and NOT.



age=int(input("Enter your Age : "))

#----- AND Operator conditions both true then result also true---------
if(age>23 and age<60):
    print("Yes!! You are an Adult and are elegible to work.")

else:
    print("We are sorry to say no to you.")


#----- OR operation condition if one true then result will always be true.----


if(age>23 or age<60):
    print("Yes!! You are an Adult and are elegible to work.  OR Example.")

else:
    print("We are sorry to say no to you.  OR Example.")