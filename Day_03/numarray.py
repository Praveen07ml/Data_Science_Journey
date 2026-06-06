
# numpy is a python library is used to work with Numerical data and arrays efficeintl

import numpy as np

#creating arrays

arr1 = np.array([1,2,3,4,5,6])
print(arr1)
print()

arr2 = np.zeros((3,4))
print(arr2)
print()

arr3 = np.ones((2,4))
print(arr3)
print()


arr4 = np.arange(0,10,2)
print(arr4)

# checking Shape

print(arr1.shape)
print(arr2.shape)
print(arr3.shape)
print(arr4.shape)

arra = np.array([[1,2,3],[4,5,6],[7,8,9]
                

])

print(arra.shape)

# indexing


print(arra[0,2])
print(arra[1,1])
print(arra[2])
print(arra[2,0])
print(arra[0,2])

print(arra[0,2])



#slicing

print(arr4[1:4])

print(arra[2,:])

print(arra[:,2])


#math on arrays

arra2 = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(arra * arra2)

print(arra + arra2)


# statistics on arrays

print(arra.mean())
print(arra.std())
print(arra.min())
print(arra.max())
print(arra.sum())

arra = np.array([1,2,3,4,5,6,7,8,9,10])

print(arra.shape)
print(arra.mean())
print(arra.std())
print(arra.min())
print(arra.max())


arra = np.array(
    [[1,2,3,4],
     [4,5,6,5],
     [7,8,9,10]]
)

print(arra[:,1])


arra1 = arra[:]

print(arra1 + arra)
print()
print(arra * arra1)