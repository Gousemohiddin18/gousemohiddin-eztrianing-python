LIST :
    
L=[1,4,7.4,'sam']
L
[1, 4, 7.4, 'sam']
L[3]
'sam'
L[2:3]
[7.4]
L[2:4]
[7.4, 'sam']
L[0:]
[1, 4, 7.4, 'sam']
L[:-1]
[1, 4, 7.4]
L[::-1]
['sam', 7.4, 4, 1]

L=[1,4,1,1,6,4,1,2]
len(L)
8
L.count(1)
4
L.append(400)
L
[1, 4, 1, 1, 6, 4, 1, 2, 400]
L.extend([100,200,300])
L
[1, 4, 1, 1, 6, 4, 1, 2, 400, 100, 200, 300]
L.remove(1)
L
[4, 1, 1, 6, 4, 1, 2, 400, 100, 200, 300]
L.pop(-2)
200
L.pop(8)
100
L
[4, 1, 1, 6, 4, 1, 2, 400, 300]
L.sort()
L
[1, 1, 1, 2, 4, 4, 6, 300, 400]
L.reverse()
L
[400, 300, 6, 4, 4, 2, 1, 1, 1]

1) L=[0,1,2,3,4,5,6,7,8,9]
   for j in L:
     print(j)

= RESTART: C:/Users/PC-35/AppData/Local/Programs/Python/Python311/days 3 programe.py
0
1
2
3
4
5
6
7
8
9


2) L=[1.1,2.2,3.3,4.4,5.5]
   x=sum(L)
   print(x)
   avg=x/10
   print(avg)

= RESTART: C:/Users/PC-35/AppData/Local/Programs/Python/Python311/days 3 programe.py
16.5
1.65

3) L=[1,2,3,4,5,6]
   for i in L:
      if(i%2==0):
        print(i)

= RESTART: C:/Users/PC-35/AppData/Local/Programs/Python/Python311/days 3 programe.py
2
4
6

3) size=int(input("size :"))
   L=[]
   for i in range(size):
       ele=int(input("element :"))
       L.append(ele)
   print(L)
   for j in L:
       if(j%2==0):
           print(j)

= RESTART: C:/Users/PC-35/AppData/Local/Programs/Python/Python311/days 3 programe.py
size :5
element :1
element :2
element :3
element :4
element :5
[1, 2, 3, 4, 5]
2
4

n=list(map(int,input("enter").split()))
print(n)
x=1
y=0
for i in n:
    x=x*i
    y=y+i
if x<=750:
    print("prod",x)
else:
    print("sum",y)


===== RESTART: C:/Users/PC-35/AppData/Local/Programs/Python/Python311/g.py =====
enter756
[756]
sum 756


5) numbers=[elements for elements in "Great afternoon"]
   print(numbers)

   ===== RESTART: C:/Users/PC-35/AppData/Local/Programs/Python/Python311/g.py =====
['G', 'r', 'e', 'a', 't', ' ', 'a', 'f', 't', 'e', 'r', 'n', 'o', 'o', 'n']


6) L=["hyd","vizag","chennai","vijayawada"]
city = []
for n in L:
    if "v" in n:
        city.append(n)
print(city)


===== RESTART: C:/Users/PC-35/AppData/Local/Programs/Python/Python311/g.py =====
['vizag', 'vijayawada']


7)L1=[2**x for x in range(2,10)]
print(L1)


===== RESTART: C:/Users/PC-35/AppData/Local/Programs/Python/Python311/g.py =====
[4, 8, 16, 32, 64, 128, 256, 512]

8)L2=[a for a in range (100,201,20)]
print(L2)

===== RESTART: C:/Users/PC-35/AppData/Local/Programs/Python/Python311/g.py =====
[100, 120, 140, 160, 180, 200]

9)L3=[1,2,3,4,5,6]
L4=[i for i in L3 if (i<5)]
print(L4)

===== RESTART: C:/Users/PC-35/AppData/Local/Programs/Python/Python311/g.py =====
[1, 2, 3, 4]

SET :

10) s={1,2,3,4,5,6}
    s.add(7)


    s
    {1, 2, 3, 4, 5, 6, 7}

11)  s={1,2,3,4,5,6}
     s.update([8,9])

     s
     {1, 2, 3, 4, 5, 6, 8, 9}

     
12)  s={1,2,3,4,5,6}
     s.remove(3)

 ===== RESTART: C:/Users/PC-35/AppData/Local/Programs/Python/Python311/g.py =====
s
{1, 2, 4, 5, 6}


13)S1={1,2,3}
   S2={4,5,6,1,2}
   S1|S2

   ===== RESTART: C:/Users/PC-35/AppData/Local/Programs/Python/Python311/g.py =====
s
{1, 2, 4, 5, 6}

14) S1={1,2,3}
    S2={4,5,6,1,2}
    S1-S2 

S1
{1, 2, 3}

15)  S1={1,2,3}
     S2={4,5,6,1,2}
     S2-S1

     S2-S1
     {4, 5, 6}

16)  S1={1,2,3}
     S2={4,5,6,1,2}
     S2.issuperset(S1)

     S2.issuperset(S1)
False

17) s1={1,2,3,4,5,1,2,3,4,5}
    s2={1,2,3,4,5,6,7,8,9}
    s1^s2

    s1^s2
{6, 7, 8, 9}

TUPLE :

   t=(4,3,4,9.6,"ice cream")
   type(t)
   <class 'tuple'>
   t.count(4)
   2
   t.index(4)
   0

DICT :


    d={1:"one",2:"two"}
    d
    {1: 'one', 2: 'two'}
    type(d)
    <class 'dict'>
    d.keys()
    dict_keys([1, 2])
    d.values()
    dict_values(['one', 'two'])
    d.items()
    dict_items([(1, 'one'), (2, 'two')])

    d={'syl':'techno','chaaru':'meizu'}
    type(d)
    <class 'dict'>
    d.keys()
    dict_keys(['syl', 'chaaru'])
    d.values()
    dict_values(['techno', 'meizu'])
    d.get{"x"}
    

##disctionary-mapping :
    
    d={1:'a',2:'c'}
    d.setdefault(3,d)
    {1: 'a', 2: 'c', 3: {...}}















   

    

