# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification


def sumvalues(values):
    """A function that receives a list/array and returns the sum of the values in that sequence. 
    
    Itereates through the items (i) in the list.
    If the data in the list is a sting, it will raise an Exception.
    Otherwise it will add the value to the sum variable.
    If for loop is competed without the Exception being raised, sum will be returned.
    """    
    
    sum = 0
    for i in values:
        if type(i) == str:
            raise Exception('There are non-numerical values in your list')
        else:    
            sum += i
    return sum

def maxvalue(values):
    """A function that receives a list/array and returns the index of the maximum value in that sequence.
    
    Sets the first value in the list to the variable maximum.
    Itereates through the items (i) in the list.
    If the data in the list is a sting, it will raise an Exception.
    Otherwise if the value of i is greater than the value assigned to maximum, maximum will now get assigned the value of i.
    If i is not greater than maximum then the for loop will continue.
    At the end of the for loop the maxvalue variable will be the largest value in the list.
    The next for loop iterates through each value of the list using its index.
    If the value at the index is the same at the maxvalue variable the index will be saved to the location variable and then returned at the end of the for loop.
    """    
    
    maximum = values[0]
    for i in values:
        if type(i) == str:
            raise Exception('There are non-numerical values in your list')
        elif i > maximum:
            maximum = i
    for index in range(len(values)):
        if maximum == values[index]:
            location = index

    return location

def minvalue(values):
    """A function that receives a list/array and returns the index of the minimum value in that sequence. 
    
    Sets the first value in the list to the variable minimum.
    Itereates through the items (i) in the list.
    If the data in the list is a sting, it will raise an Exception.
    Otherwise if the value of i is less than the value assigned to minimum, minimum will now get assigned the value of i.
    If i is not less than minimum then the for loop will continue.
    At the end of the for loop the minvalue variable will be the smallest value in the list.
    The next for loop iterates through each value of the list using its index.
    If the value at the index is the same at the minvalue variable the index will be saved to the location variable and then returned at the end of the for loop.
    """    

    minimum = values[0]
    for i in values:
        if type(i) == str:
            raise Exception('There are non-numerical values in your list')
        elif i < minimum:
            minimum = i
    for index in range(len(values)):
        if minimum == values[index]:
            location = index
    return location

def meanvalue(values):
    """A function that receives a list/array and returns the arithmetic mean value of that list/array.

    Itereates through the items (i) in the list.
    If the data in the list is a sting, it will raise an Exception.
    Otherwise it will add the value to the sum variable and add 1 to the counter variable.
    Once for loop is finished the function returns the sum divided by the counter.
    """    

    sum = 0
    counter = 0 #counts how many values there are
    for i in values:
        if type(i) == str:
            raise Exception('There are non-numerical values in your list')
        sum += i
        counter += 1
    return sum/counter #sum of values divided by the number of values gives the mean

def countvalue(values, x):
    """A function that receives a list/array (values) and a value, x, and returns the number of occurrences of the value x in the list/array values. 

    Itereates through the items (i) in the list.
    If the data in the list is a sting, it will raise an Exception.
    Otherwise if value i in the list is the same as the parameter x the counter is increased by 1.
    Once for loop finished, the value of the counter variable is returned.
    """    

    counter = 0
    for i in values:
        if i == x:
            counter += 1
    return counter
