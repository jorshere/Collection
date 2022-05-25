'''zip() function:
            * it is used to ziping up  values of two or more list, to its corresponding values;
            * it will giv a zip object i.e iterator;
            * on printing it will give tuples of zipped values as inside a list:
                    lisi1=[x,y,z]        list2=[a,b,c,d]
                    output: [(x,a),(y,b),(z,c)]
            * if elements inside lists are not equal, it will zip the least values
            and skip yhe rest;
'''

uid= ["ram","shyam","kayam","roro"]
rol = [23,54,"65t"]
year = [1992,1995,1997,2001]

print(list(zip(uid,rol,year)))

roll1 = dict(zip(uid,rol))  # to use zip() to make dictionary
pri=iter(roll1.items())
print(next(pri))
print(next(pri))


for i,j in dict(zip(uid,rol)).items():
    print(f"{i} : {j}")

set1 = [('a',1),('b',1)]    #to convert list of set to a dictionary;
print(dict(set1))