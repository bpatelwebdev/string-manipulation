

def Function_to_count(str, List_1):
    '''this function counts the repeated occurance of words/characters passed through List_1'''
    Dict_1 = {}  # creating an empty dictionart
    # convert list to set to eliminate duplicates
    Temp_set = set(List_1)
    # each value in set is a key thus to assign null value initially the following loop is run
    for i in Temp_set:
        Dict_1.update({i: 0})  # assigns each key a value 0 initially
    # the following loop is to count the occurance of the word i.e key in the list created from paragraph
    for i in List_1:
        Dict_1[i] += 1

    # get the values of dictionary
    Value_1 = Dict_1.values()
    # sort the values to the orders in position
    Value_1.sort()
    # reverse the list as we need top 5 most repeated words
    Value_1.reverse()

    # loop to check the value and print the key value pair
    print("The top five "+str+" are as below")
    for k, v in Dict_1.items():
        if v in Value_1[
                0:5]:  # just need top 5 to slicing is performed. We can change the number of top words requied from the slicing
            print(k,v)
    Dict_1.clear()

    return()

#Creating an arbitary srting

String_1 = "Python is an interpreted, object-oriented, high-level programming language with" \
       " dynamic semantics. Its high-level built in data structures, combined with dynamic " \
       "typing and dynamic binding, make it very attractive for Rapid Application Development, " \
       "as well as for use as a scripting or glue language to connect existing components together." \
       " Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost" \
       " of program maintenance. as Python supports modules and packages, which encourages program modularity" \
       " and code reuse. The Python interpreter and the extensive standard library are available in source " \
       "or binary form without charge for all major platforms, and can be freely distributed."

#Converting the paragraph into list
#to create list of words we need to split the values of paragraph by blank space
#so we use .split(" ") and use list comprehension to eliminate blank spaces.

Function_to_count('words',list(String_1.split(" ")))

Function_to_count('characters',[i for i in list(String_1) if i != ' '])



