#Given a dictionary that contains mapping of employee and his manager as a number of (employee, manager) pairs like below. 

#{ "A", "C" },
##{ "B", "C" },
#{ "C", "F" },
#{ "D", "E" },
#{ "E", "F" },
#{ "F", "F" } 

#In this example C is manager of A, 
#C is also manager of B, F is manager 
#of C and so on.
#Write a function to get no of employees under each manager in the hierarchy not just their direct reports. It may be assumed that an employee directly reports to only one manager. In the above dictionary the root node/ceo is listed as reporting to himself. 
#Output should be a Dictionary that contains following. 



from collections import defaultdict
def assign(t):
    d=defaultdict()
    for i in t:
        if i[0]==i[1]:
            continue
        if i[0] not in d:
            d[i[0]]=[]
        if i[1] not in d:
            d[i[0]]=i[1]
        else:
            d[i[0]].append(i[1])

    
    c = defaultdict()   # store    manager:count of employee    as key value
    for manager in d:
        c[manager] = len(d[manager])
        for employee in d[manager]:
            c[manager] += len(d[employee])
        print("{} : {}".format(manager,c[manager]))   