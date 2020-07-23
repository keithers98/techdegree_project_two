import pdb
import app
import constants_copy
pdb.set_trace()
another_copy = constants_copy.list_og.copy()
list_copy = constants_copy.list_og[:]
instance = list_copy[0]
list_copy[0]["one"] = 'huzzah' #this change the original

for dicti in list_copy:
    if dicti["one"] == 2:

        list_copy[list_copy.index(dicti)]["one"] = 'you did it' #this changes the original list
        #list_copy[dicti.index()]["one"] = 27 # 'dict' has no attribute index
        #dicti["one"] = 6 #this changes the original
        #list_og = 'hurray'


list_copy.append('dog')   #this does not change the original
print(another_copy)
print(instance)
print(constants_copy.list_og)
print(list_copy)
#print(list_copy('{"one":1}'))
print(list_copy.index({"one":3})) #<<<< to access the dictionary index you must type or reference the entire dictionary!
list = ['cat', 0, 6.7]

# copying a list using slicing
new_list = list[:]

# Adding an element to the new list
new_list.append('dog') #this does not change the original
new_list[0] = "kitty" #this does not change the original
# Printing new and old list
print('Old List:', list)
print('New List:', new_list)

# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# index of 'e' in vowels
index = vowels.index('e')
print('The index of e:', index)

# element 'i' is searched
# index of the first 'i' is returned
index = vowels.index('i')

print('The index of i:', index)
constants = ['q','w']
vowels.append(constants[0:2])
print(vowels)
print(vowels)
