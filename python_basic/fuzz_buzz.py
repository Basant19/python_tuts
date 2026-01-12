def fuzz_buzz(lst):
    result=[]
    for num in lst:
        if num % 3 == 0 and num % 5 == 0:
            result.append("fuzzbuzz")
        elif num % 3 == 0:
            result.append("fuzz")
        elif num % 5 == 0:
            result.append ("buzz")
        else:
            result.append (num)
    return result

element_list=[1,2,3,4,5,15,18,20,22]
print ("elements:",element_list)
print (fuzz_buzz(element_list))
