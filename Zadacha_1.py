all = []
our = []
def get_avg_unique2(lst1,lst2):
    for i in lst1:
        if lst1.count(i) > 1:
            our.append(i)

    for i in lst2:
        if lst2.count(i) > 1:
            our.append(i)

            
    for i in our:
        if our.count(i) > 1:
            all.append(i)

    return round(sum(all)/len(all),1)

get_avg_unique2([1,2,3,4],[2,3,1,5])
print(all)