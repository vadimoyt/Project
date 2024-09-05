from functools import reduce

rooms = [
{"name": "Kitchen", "length": 6, "width": 4},
{"name": "Room 1", "length": 5.5, "width": 4.5},
{"name": "Room 2", "length": 5, "width": 4},
{"name": "Room 3", "length": 7, "width": 6.3},
]

new = list(map(lambda y: y["length"] * y["width"], rooms))
print(reduce(lambda x, y : x + y, new))

# sp = []
# for room in rooms:
#     squre = room["length"] * room["width"]
#     sp.append(squre)
#
# print(reduce(lambda x, y: x + y, sp))