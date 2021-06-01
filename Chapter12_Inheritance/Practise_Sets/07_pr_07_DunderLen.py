
class Vector:
    def __init__(self,vec):
        self.vec=vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k  "

    
    def __len__(self):
        return len(self.vec)




V1=Vector([1,4,6,5])
V2=Vector([1,6,9])
print(V1)
print(V2)
print(len(V1))
print(len(V2))

if(len(V1)!=len(V2)):
    print("The length of Vector 1 and Vector 2 varies So, Operations can't be done")

else:
    print("You can perform the Required Operations")

    





