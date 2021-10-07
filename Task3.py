a = list(input())
c = ""
a.append("end")
for i in a:
    if i == " ":
        print(c[::-1], " ", end="")
        c = ""
    if i == "end":
        print(c[::-1], end="")
    c = c+i