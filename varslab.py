x = "This is a python programme"
y = 10
z = 5.5

type_x = type(x)
type_y = type(y)
type_z = type(z)

print(type_x)
print(type_y)
print(type_z)

print(y+z)
print(y+int(z))
print(z+float(y))

print(type(str(z)))

print(x+str(y)+str(z))

#print(x+y)#doesnt work