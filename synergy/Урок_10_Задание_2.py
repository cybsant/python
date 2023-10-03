"""
num_dict = {}
for i in range(10, -6, -1):
    num_dict[i] = i ** 2
print(num_dict)
"""
# =)
print({i: i ** 2 for i in range(10, -6, -1)})
