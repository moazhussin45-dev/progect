str_length = input("please type length: \n")
str_width  = input("please type width: \n")
str_miter  = input("please type miter:\n")
length = float(str_length)
width  = float(str_width)
miter  = float(str_miter)
area = length * width
str_area = str(area)
print("the area is:"+str_area)
cost = area * miter
str_cost = str(cost)
print("the cost is:"+str_cost)
print("the area is: " + str(area) + " and the cost is: " + str(cost))