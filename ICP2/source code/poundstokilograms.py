num = int(input("enter number of students--->")) #input no of studenst
lbs = []  #created empty list
for i in range(0,num):
    wt = int(input("enter weight of students in lbs----->")) #input weight of each student
    lbs.append(wt)
print("weight of each student----->",lbs)
kgs = [round(x/2.2045,3) for x in lbs] #list comprehension to convert from lbs to kgs
print("the weights of student in kilograms are--->",kgs)
