# with open("day.csv") as f:
#    i = f.readlines()
#    print(i)


# import csv
#
# with open("day.csv") as f:
#    i = csv.reader(f)
#    temp = []
#    for r in i:
#        a = r[1]
#        if a != "temp":
#            temp.append( int(a))
#    print(temp)


import pandas
#
# b = pandas.read_csv("day.csv")
# c = b["temp"]
#
##c = b["temp"].to_list()
##a = 0
##for i in c:
##    a += i
##    v = a / len(c)
##print(v)
# v = b[b.day =="Monday"]
##d = c.max()
# w = v.temp
# r = w + 273
# print(r)

# a = {
# "Name":["any","sola"],
# "Age":[1,3]
# }
# d = pandas.DataFrame(a)
# print(d)


import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color = len(data[data["Primary Fur Color"] == "Gray"])
Red = len(data[data["Primary Fur Color"] == "Cinnamon"])
Black = len(data[data["Primary Fur Color"] == "Black"])
print(color)
print(Red)
print(Black)

darafr = {
    "fur color":["Gray", "Cinnamon", "Black"],
    "number":[color,Red,Black]
}

daraf = pandas.DataFrame(darafr)
daraf.to_csv("new.csv")