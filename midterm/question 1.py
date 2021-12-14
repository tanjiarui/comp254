def find_max(data: [int]):
    if not data:
        return 0
    else:return max(data[0], find_max(data[1:]))

print(find_max([6,2,3,7,5,6]))