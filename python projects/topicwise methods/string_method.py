""" Dictionaries :
        * you can create a compelx data inside a dictionary easily;
        * collection i.e  unordered changable and indexed;
        * no duplicates allowed;

 """

user= {"name": "jors", "age" : 25 , "soft" : "python"}
print(user)

user1 = dict(name = "harsh", age = 24 , soft = ["idle","pycham","VScode"])  # another way to create dictionary;
print(user1)

print(user1.get("soft"))

print(user.keys())  #

print(user1.values())

x= ("singer1","singer2","singer3")
y=("male", 23)

print(dict.fromkeys(x,y))       # to assign value of "Y" in all the keys and create dictionary;

user.update({"soft" : "nite"})   # to update or create new item in dictionary;
user["name"]="human"            # you can also add by this
print(user)

