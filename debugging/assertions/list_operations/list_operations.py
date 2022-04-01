def list_multiple(k, l):
    result = []
    for i in range(len(l)):
        # Bug: result.append(k * i)
        result.append(k * l[i])
    return result


def list_sum(l1, l2):
    v = []
    for i in range(len(l1)):
        # Bug: v.append(l1 + l2)
        v.append(l1[i] + l2[i])
    return v


k = 7
a = [5, 2, 1]
b = [3, 7, 11]

print(__debug__)    

# Add assert statements to automatically observe values
list_multiple =  list_multiple(k, a)
print(f'k * a = {list_multiple}')
assert list_multiple == [7*5, 7*2, 7*1]

list_sum =  list_sum(a, b)
print(f'a + b = {list_sum}')
assert list_sum == [5+3, 2+7, 1+11]
