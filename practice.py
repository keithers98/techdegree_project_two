list = [{'one':1}, {'one':2}, {'one':3}]                                                                                                                

for dicti in list:                                                                                                                                        
    if dicti['one'] == 2:                                                                                                                                 
        dicti['one'] = 1   
print(list)

list_copy = list
print(list_copy)
