class ISE:
    def stddetail(self,usn,name,age,marks):
        #local variable
        self.usn=usn
        self.name=name
        self.age=age
        self.marks=marks
        print("the usn {},name {},age:{} and marks:{}".format (self.usn,self.name,self.age,self.marks))
s1=ISE()
s1.stddetail('is01','alen','25','99')
s2=ISE()
s2.stddetail('is02','mosk','29','89')
#polymorphisum-overloading
'''
1.operator overloading
2.method overloading
'''
#operator overloading 
#'+' string(concatination),integer(adding)
#string
n1='10'
n2='20'
print(n1+n2)
a='alen'
b='mosk'
print(a+b)

#integer
n1=10
n2=30
print(n1+n2)

#"*" datatypes(replication),integers(multiplication)
l=[10,20]
print(l*3)
#integer
l=10
m=20
print(l*m)

#method overloading
def add():
    n1=10
    n2=30
    summ = n1+n2
    print("sum is ",summ)
add()

def add(a,b):
    print(a-b)

add(30,10)

#over riding
class parent:
    a=10
    def display(self):
        print("parent property")
class child(parent):
    a=10
    def display(self):
        print("child property")

c=child()
print(c.a)
c.display()


