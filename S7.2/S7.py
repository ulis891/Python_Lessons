# spis = [1, 2, 3, 5, 8, 15, 23, 38]

# for i in spis:
#     if i%2==0:
#         print(i,i**2)

# print(lambda i, i**2: i%2==0, spis)


# sppppis = '1 34 6 47 5 5 34 78 4 4 65 9 0'

# array1=list(map(int, sppppis.split(' ')))

# transformation = lambda x: x
# transformed_values = list(map(transformation, array1))

# print(transformed_values)
# if array1 == transformed_values:
#     print("o'lright")
# else: print('shatafuckt UP')


# orbits = [(1,3),(2.5,10),(7,2),(6,6), (4,3)]
# def find_farthest_orbit(list_orbits):
    # s_array = list(map(lambda r: (r[0] != r[1]) * r[0] * r[1], list_orbits))
    # return orbits[s_array.index(max(s_array))]
# 
# print(find_farthest_orbit(orbits))

values = [0,2,10,6,7]

def same_by(funk,val):
    return len(list(filter(funk, val))) == 0  
            

if same_by(lambda x: x % 2, values):
    print("Good")
else:
    print("Bad")