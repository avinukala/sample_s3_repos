'''a=8,10,9,7,6
print(type(a))
for i in a:
    print(i)


pranshu = ('James', 24, 'M')    
print(pranshu)
head= ("name=","age=","gender=")
i=0

for x in pranshu:
    print(head[i],x)
    i=i+1


emp={"eno":101,"ename":'kiran',"sal":50000}
#print(emp["eno"])
for i,j in emp.keys(),emp.values():
    print(i,j)



emp = {"eno": 101, "ename": 'kiran', "sal": 50000}

# Print the value associated with the key "eno"
print(emp["eno"])

# Iterate over keys and values
for key, value in zip(emp.keys(), emp.values()):
    print(key, value)


import collections    
d1=collections.OrderedDict()    
d1['A']=10    
d1['C']=12    
d1['B']=11    
d1['D']=13    
    
for k,v in d1.items():    
    print (k,v)  

from collections import defaultdict      
number = defaultdict(int)      
number['one'] = "avinash"      
number['two'] = 2      
print(number['one'])       
'''



'''
emp = {"eno": 101, "ename": 'kiran', "sal": 50000}



# Iterate over keys and values directly
for key in emp:
    value = emp[key]
    print("\"",key,"\"",":", value)




def add(a, b):
    return a + b

result = add(5, 3)  # result is 8
print(result)


add = lambda a, b: a + b
result = add(5, 3)  # result is 8
print(result)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(4)  # result is 120
print(result)
'''

#print 5 to 1 numbers using recrussion
def sum(n):
    if n==0:
        return 0
    else:
        return n+ sum(n-1)


result=sum(5)
print(result)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     