list1= [1,2,3,6,8,2,5,7,2,5,0]

lc=[i for i in list1 if i>2]

print(lc)

set1=set([2,3,8,7,2,5,5,7])
sc={i for i in set1 if i%2==0}
print(sc)

cities=["Dhaka", "Mumbai", "Lahore", "Newyork", "Paris"]
countries= ["Bangladesh", "India", "Pakistan", "USA", "France"]

z=zip(cities, countries)

dc={city: country for city, country in zip(cities, countries)}
print(dc)

for keys, values in dc.items():
    print(values+": "+ keys)