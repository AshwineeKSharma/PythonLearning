# can you change the self parameter inside a class to something else say("example").
#-----> Yes We Can Change

# try changing self to "slf" or "example" and see the Effect.
# ------> It Works as self but is not a good Practise.





class Sample:
    def __init__(slf,name):
        slf.name=name




n=Sample("Ashwinee Kumar Sharma")
print(n.name)


