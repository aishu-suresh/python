a=input("enter the string:");
v=0
c=0
c=0
d=0
w=0
for i in a:
    if(i=='a')or(i=='e')or(i=='i')or(i=='0')or(i=='u'):
        v=v+1
    elif i.isdigit():
        d=d+1
    elif i.isalpha():
        c=c+1
    elif i.isspace():
        w=w+1
        print("count of vowels",v)
        print("count of consonant",c)
        print("count of digit",d)
        print("count of space",w)
