
# TODO: Debugging
# A) Verify the results by using assert statements.
# B) Locate the bug by using an interactive debugger.
# C) Fix the bug.

def vector_scalar_multiple(k, vector_a):
    result = []
    for i in range(len(vector_a)):
        result.append(k * i)
    return result


def vector_add(vector_a, vector_b):
    v = []
    for i in range(len(vector_a)):
        v.append(vector_a[i] + vector_b[i])
    return v


def vector_scalar_product(vector_a, vector_b):
    result = 0 
    for i in range(len(vector_a)):
        result = vector_a[i] * vector_b[i]
    return result

k = 7
a = [5, 2, 1]
b = [3, 7, 11]

vector_multiple =  vector_scalar_multiple(k, a)
print('k * a = {}'.format(vector_multiple))

vector_sum =  vector_add(a, b)
print('a + b = {}'.format(vector_sum))

scalar_product = vector_scalar_product(a, b)
print('a * b = {}'.format(scalar_product))


