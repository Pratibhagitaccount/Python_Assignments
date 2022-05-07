'''Create a list of elements such that it contains the squares of the first 
and last 5 elements between 1 and30 (both included).'''



#Creation of list_1 having elements between 1 and 30
list_1 = [x for x in range(1,31)]
# creation of list which includes square of first five elements
list_2 = [x*x for x in list_1[:5]]
# creation of list which includes square of last five elements
list_3 = [x*x for x in list_1[-5:]]
# update list_2 with elements of list_2
list_2.extend(list_3)
print(f"First and Last five squared elements of list_1 are: \n {list_2}")