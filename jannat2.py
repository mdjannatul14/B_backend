#string
name = "jannat"
print(type(name))

name = "jannatul ferdous"
print(f"my name is md{name}")#stirng formatting string er moddhe variable use korar jonno amra f use kori

#number type
number = 20
print(type(number))

#module & pip install = eta holo kono kicu age theke bana ace amra jusr pip er maddhome niya asbo jenom pip er maddho me bass install kore ante parbo

# booleam data type
j = 20
a = 19
print(j<a) #False
print(type(j>a)) #True
print(type(j==a)) #False

#binary data type
binary = [2,3,3,232,3,23,23,23,3,33,32,3]
b = bytes(binary)    #imutable data type mane holo amra jodi bytes er moddhe kono value assign kori tahole seta change kora jabe na
#b[0] = 200
print(binary)

#bytesarray data type
binary1 = [2,3,3,232,3,23,23,23,3,33,32,3]
ba = bytearray(binary1)  #mutable data type mane holo amra jodi bytearray er moddhe kono value assign kori tahole seta change kora jabe
ba[0] = 200
print(ba[0])
print(list(ba))

#none data type
a = None
print(type(a))