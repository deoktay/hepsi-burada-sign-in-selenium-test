file = open("userinfo.txt" , "r", encoding= "UTF-8")
lines = list()
for i in file:
  lines.append(i)

email = lines[0]
password = lines[1]

file.close()