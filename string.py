s="mississippi"
list1=list(s)
dict={}
sorted_dict={}
for x in list1:
    if x in dict:
        dict[x]+=1
    else:
       dict[x]=1
value=sorted(dict,key=dict.get,reverse=True)
for w in value:
    sorted_dict[w]=dict[w]
for key, value in sorted_dict.items():
        print(key,"-",value)
