'''     Advance Min() , max() , Sorted() Function.......

'''

# Min(), Max()

mylia = [{'name':'thanos','HP':300,'rank':2},
        {'name':'golem','HP':500,'rank':5},
        {'name':'pikachu','HP':150,'rank':4}
        ]

manya = min(mylia, key= lambda item : item.get('HP'))['rank']
print(manya)

# Example 2

myli = {'thanos':{'HP':300,'rank':2},
        'golem':{'HP':500,'rank':5},
        'pikachu':{'HP':150,'rank':4}
        }
kanya = max(myli, key= lambda x : myli[x]['HP'])
print(kanya)

# Sorted()

sots = sorted(mylia, key= lambda x : x['HP'])
print(sots)

# to reverse the  sorted list;
sot2 = sorted(myli , key= lambda k : myli[k]['HP'],reverse= True)
print(sot2)