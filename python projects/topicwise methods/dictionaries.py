""" Dictionaries :
        * you can create a compelx data inside a dictionary easily;
        * collection i.e  unordered changable and indexed;
        * no duplicates allowed;

 """

user= {"name": "jors", "age" : 25 , "soft" : "python"}
#print(user)

user1 = dict(name = "harsh", age = 24 , soft = ["idle","pycham","VScode"])  # another way to create dictionary;
#print(user1)

print(user1.get("soft"))        # to get/access any key values

print(user1.get("softer","not found"))  # if you dont want to return a false
                                        # statement you can overrite it with any statement

#print(user.keys())  #

#print(user1.values())

x= ("singer1","singer2","singer3")
y=("male", 23)

for key,value in user.item():
    print(f"{key}   :  {value}")             # to print key value pair using item()


    
#print(dict.fromkeys(x,y))       # to assign value of "Y" in all the keys and create dictionary;

user1.update({"softn" : "nite"})    # to update a dictionary with other  dictionary;
print(user1)
user["name"]="human"            # you can also add by this
#print(user)

retrn = user1.pop("softn")      # it will pop the item and we can return the values in a variable.
print(retrn)
#print(user1)

rex = user1.popitem()       # it will pop a random key and return a tuple with key and values;
print(rex)

d1 = user.copy()                # to copy
print(d1.items())

d1.clear()           # to clear the dictionary;
