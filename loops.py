"""fruits=["apple","banana","grapes"]
print((len(fruits)))
for i in (range(len(fruits))):
    print(fruits[i]);
    
a=int(input("enter a number"));
if (a < 13):
    print("too small");
elif(a>13):
    print("too big");
elif(a ==13):
    print("right answer");

    
count=1
for i in range(10):
    print(str(i)*i);
    
    for j in range(0,i):
        count+=1;
print(count);"""

for j in range(1,11):
    if(j==4):
        continue
    print(j);