a = 10
b = 20
c = 30
avg = (a + b + c)/3
print("avg =", avg)
if avg > a and avg > b and avg > c:
    print(" avg is higher than a, b and c")
else: 
    if avg > a and avg >b: 
        print("avg is higher than a and b")
    else:
        if avg > a and avg > c:
            print(" avg is higher than a and c")
        else:
            if avg > b and avg > c:
                print("avg is higher than b and c")
            else:
                if avg > a :
                    print (" avg is just higher than a")
                else:
                    if avg > b:
                        print("avg is just higher than b")
                    else:
                        if avg > c:
                            print("avg is just higher than c")