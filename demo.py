message = "Hello's Python" + str(11) + " world!"
print (message)
print (message.title())
print (message.upper())
print (message.lower())
print ( message + "!")
print ( 100**2 )

bicycles = ['trek', "a", 'cannondale', 'redline']
del bicycles[0]
print ( bicycles )
for item in bicycles:
    print ( item )
print ( max(bicycles) )
squares = [ [ 0 for col in range(1, 11) ] for row in range(1, 11) ]
print (squares)
for i in range(1,11):
    print (i)
dimensions = (200, 50)
dimensions1 = (200, 51)
print ( dimensions )
for item in dimensions:
    print ( item )
print ( dimensions1 == dimensions )
map1= {'aaa': 'aa1', 1: 3}
print ( map1 )
print ( map1[1] )
map2 = { 'aa' : 1 }
print ( map2 )
print ( map2['aa'] )
aaa = [ 1, 1 ]
aaa[1] = 2
print ( aaa[1] )
for key, value in map1.items():
    print (key)
    print (value)

# message = input("input: ")
# print ( message )

current_number = 1
while current_number <= 5:
    print(current_number)
    x = 1
    current_number += 1

print (x)

while_list = [ '111', '222' ]
while while_list:
    print(while_list)
    break;

def greet_user():
    """aaa"""
    print ("aaaa")

def change_map(a):
    a['aa'] = 1;

m = {'aa': 2}
change_map(m);
print(m)
