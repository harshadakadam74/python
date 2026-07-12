l = [11,45,1,2,4,6,1,1]
print(l)
l.append(12)
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.reverse()
print(l)

print(l.index(2))
print(l.count(1))

m = l.copy()
m[0] = 0
print(l)

l.insert(1, 899)
m = [900, 55, 478]
k = l + m
print(k)
l.extend(m)
print(l)
