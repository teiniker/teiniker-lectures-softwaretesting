def vector_scalar_multiple(k, vector_a):
    result = []
    for i in range(len(vector_a)):
        # Bug: result.append(k * i)
        result.append(k * vector_a[i])
    return result


def vector_add(vector_a, vector_b):
    v = []
    for i in range(len(vector_a)):
        v.append(vector_a[i] + vector_b[i])
    return v


def vector_scalar_product(vector_a, vector_b):
    result = 0 
    for i in range(len(vector_a)):
        # Bug: result = vector_a[i] * vector_b[i]
        result += vector_a[i] * vector_b[i]
    return result

k = 7
a = [5, 2, 1]
b = [3, 7, 11]

print(__debug__)    

# Add assert statements to automatically observe values
vector_multiple =  vector_scalar_multiple(k, a)
print('k * a = {}'.format(vector_multiple))
assert vector_multiple == [7*5, 7*2, 7*1]

vector_sum =  vector_add(a, b)
print('a + b = {}'.format(vector_sum))
assert vector_sum == [5+3, 2+7, 1+11]

scalar_product = vector_scalar_product(a, b)
print('a * b = {}'.format(scalar_product))
assert scalar_product == 5*3 + 2*7 + 1 *11


