def count_zero_pairs(numbers):
    counter = 0
    
    for index_x in range(0, len(numbers)):
        for index_y in range (index_x, len(numbers)):
            x = numbers[index_x]
            y = numbers[index_y]
            if x + y == 0:
                counter += 1
                print (x, y)
                
    return counter
        
