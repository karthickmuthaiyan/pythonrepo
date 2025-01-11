"""            
class edureka:
    domain="DS"
    def __init__(self,name):
        self.name=name

ob1=edureka("Karthick");
ob2=edureka("Muthaiyan");

print(ob1.domain);
print(ob2.domain)
ob1.domain="CS"
print(ob1.domain);
print(ob1.name)
print(ob2.name)


#Echo last 3 letters of the word
import sys

def echo(text: str, repetitions: int = 3) :
    #Imitate a real-world echo
    echoes = [text[-i:].lower() for i in range(repetitions, 0, -1)]
    return "\n".join(echoes + ["."])

if __name__ == "__main__":
    text = " ".join(sys.argv[1:])
    print(echo(text))
"""
class Rectangle: 
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def getarea(self):
        print(self.length*self.width, "is area of rectangle")
    
class Square(Rectangle):
    def __init__(self, side):
        self.side=side
        ##Rectangle.__init__(self,side,side)
    def getarea(self):
        print(self.side*self.side," is the area of the square")

s=Square(4)
s.getarea()
s=Rectangle(4,8)
s.getarea()
