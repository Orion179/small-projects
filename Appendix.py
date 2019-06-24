#prints appendix numbers less than user input
a=[0,1,1,2,3,5,8,13,21,34,55,89,144,233,377]  #create appedix

num=int(input("Choose a number: "))  #prompts user
lit=[]  #creates space for refrenced numbers
for i in a:
    if i<num:
        lit.append(i)
        print (lit)