# Write a class vector representing a vector of n dimension.
# Overload the + and * operator which calculates the sum and the dot product of them.


class Vector:
    def __init__(self,vec):
        self.vec=vec

    def __str__(self):
        str1=""
        index=0
        for i in self.vec:
            str1 += f" (a{index}) {i}  +"
            index +=1
        return str1[:-1]

    def __add__(self,vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)


    def __mul__(self,vec2):
        sum=0
        for i in range(len(self.vec)):
            sum+=self.vec[i] * vec2.vec[i]
        return sum





V1=Vector([1,4,6])
V2=Vector([1,6,9])
print(V1+V2)
print(V1*V2)




