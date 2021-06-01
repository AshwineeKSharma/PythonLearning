def increment(num):
    
    try:
        return int(num)+1


    except:
        raise ValueError("Is there Something Wrong?")



a=increment(32)
print(a)
b=increment("haga")
print(b)




