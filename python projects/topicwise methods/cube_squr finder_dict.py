def cube_finder():
    cube ={}
    sqre={}
    num= int(input("enter a number till you want squares and cubes : "))
    for i in range(1,num+1):
        cube.update({i:i**3})         # OR
        sqre[i] = i**2
    print(f"the squares are{sqre}")
    print(f"the cubes are: {cube}")

cube_finder()