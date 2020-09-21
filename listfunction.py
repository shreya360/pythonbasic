numbers = [2, 32, 3, 5, 6]
friends = ["nan", "das", "sas", "daff", "das", "das", "das"]

print(friends)

friends.sort()
print(friends)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

print(friends)
friends.extend(numbers)

print(friends)
friends.append("shreya")

print(friends)
friends.insert(1,"catherine")

print(friends)
friends.remove("daff")

print(friends)
friends.pop()

print(friends)
print(friends.index("sas"))

friends.pop()
print(friends)

print(friends.count("das"))

friends2=friends
print(friends2)

friends.clear()
print(friends)