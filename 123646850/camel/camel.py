a = input("camelCase: ").strip()
r = ""
for i in range(0, len(a)):
    if a[i].isupper():
        r = r + str("_"+a[i].lower())
    else:
        r = r + a[i]
print("snake case: ", r)


