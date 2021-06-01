# create a clas C-2D Vector and use it to create another class representing 3D vector. 



class C2DVec:
    
    def __init__(self,i,j):             # Initializing the constructor
        self.icap=i
        self.jcap=j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"




class Vec3D(C2DVec):

        
    def __init__(self,i,j,k):             # Initializing the constructor
        super().__init__(i,j)
        self.kcap=k


    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"



v2d=C2DVec(1,3)
v3d=Vec3D(1,9,7)

print(v2d)
print(v3d)



