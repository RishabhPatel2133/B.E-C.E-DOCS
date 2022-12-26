import numpy as np

print("\n")

#1D array
print("1d array")
arr1d = np.array([1,2,3])
print(arr1d)

print("\n")

#2D array
print("2d array")
arr2d=np.array([[11,22,33],[44,55,66]])
print(arr2d)

print("\n")

#3D array
print("3d array")
arr3d = np.array([[[10,20,30],[1,2,3]],[[10,20,30],[1,2,3]]])
print (arr3d)

print("\n")

#to copy array we use "arrayname.copy()"
print("copying arr1 into arr2")
arr1=np.array([1,2,3])
arr2=arr1.copy()
print("arr1:",arr1)
print("arr2:",arr2)

print("\n")

#to change array element we use "array-name=array-name.view()" then "array-name[element-index]=new-element"
print("using view changing array element")
arr=np.array([1,2,3,4])
print("previus array:",arr)
arr=arr.view()
arr[1]=40
print("new array:",arr)

print("\n")

#to reshape the array we use "array2-name=array1-name.reshape()"
print("using reshape changing array shape(dimension)")
d1arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
print("old array:",d1arr)
newarr=d1arr.reshape(2,3,3) #first 2 define raw, 3 define colums ,last 3 define element
print("reshaped array:\n",newarr)

print("\n")

print("shorting array using 'new-array=np.short(old-array-name)' ")
shortingarr=np.array([1,4,2,6,3,5])
print("given array :",shortingarr)
op = np.sort(shortingarr)
print("shorted array :",op)

print("\n")

#to get maximum valu from array we use "np.max()"
print("maximum value from the array")
gg = np.max(shortingarr)
print(gg)
#to get minimum value from the array we use "np.min()"
print("minimum value from the array")
nhk = np.min(shortingarr)
print(nhk)

print("\n")

#to take random elements in array we use 'np.random' here we have to declare the tipe we want so here we use 'np.random.randtype(starting-point,ending-point,number-of-elements)
import numpy as np
arr = np.random.randint(1,100,5)
print(arr)


boolArr = arr > 50
print(boolArr) 