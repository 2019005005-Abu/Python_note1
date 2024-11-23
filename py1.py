month1={'January','feb','Mar','apr'};
month2={'January','feb','Mar'};
print(month1.union(month2));
print(month1.intersection(month2));
print(month1.difference(month2));
print(month1.symmetric_difference(month2));
x = {1, 1, 2, 3}
print(x)
for i in x:print(i);
x = {1, 4, 3}
y = { 2,3,5}
print(x.intersection(y))
    
dic={
    'name':'Abu Al Shahriar Rifat',
    'SystemId':'2019005005',
    'university':'KIC'
}

for key in dic.items():print(key);
print(end='\n')
for value in dic.items():print(value); 
print(end='\n')
for items in dic:print(items);
dic.update({
    "msc":"Kobe institute of Computing"
})

print(dic);
