#=============================== .format()   The String Formatting 

value = "hello {} i'm  the {} string {}"

# insert the value instead of {} brackets 
# print(value.format("inserted","inserted","inserted"))

#  insert the value in order they are 
# print("hello {} i'm  the {} string {}".format("One" , "two" , "three")) 

# insert the value based on there key place
# print("hello {key1} i'm  the {key3} string {key2}".format(key1="One" ,key2= "two" , key3="three")) 

name = "Ashok" 
print(f"my name is {name}")  # as same as .format 


# f  work  same as .format()

# =============================== "{value:width.precision f}" float formatting Follows

result = 1000/777
print(result)   # 1.287001287001287

# // the first value {key : no Of Blank spaces.length of result, f used for prevent to round the number}
print("the formatted {res:1.3}".format(res =result)) # result =  1.29
print("the formatted {res:1.3f}".format(res =result)) # result =  1.287
