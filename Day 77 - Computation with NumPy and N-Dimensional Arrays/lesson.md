# Day 77 - NumPy Arrays, Vectorized Computation, and Matrix Operations

Today, we step underneath pandas and work directly with the structure that powers most numeric computing in Python: the **ndarray**. NumPy is less about table labels and more about shape, axes, and operations that apply to an entire block of numbers at once.

If pandas is great for analysis across columns and rows, NumPy is great for math across vectors, matrices, tensors, and images.

## 1. Understand the Shape of an ndarray

The notebook begins with a one-dimensional array:

```python
my_array = np.array([1.1, 9.2, 8.1, 4.7])
my_array.shape
my_array.ndim
```

Two properties matter immediately:

- `shape` tells you the length of each axis
- `ndim` tells you how many axes there are

Those two checks become your fastest debugging tools in NumPy. If an operation produces a result you did not expect, inspect the shape first.

The notebook then moves to a 2D array:

```python
array_2d = np.array([[1, 2, 3, 9], [5, 6, 7, 8]])

print(f'array_2d has {array_2d.ndim} dimensions')
print(f'Its shape is {array_2d.shape}')
print(f'It has {array_2d.shape[0]} rows and {array_2d.shape[1]} columns')
print(array_2d)
```

This is where the mental model shifts from nested Python lists to axes. You are no longer just indexing into containers. You are selecting positions across dimensions.

## 2. Slice Multi-Dimensional Data by Axis

Once you have a matrix, indexing gets more precise:

```python
array_2d[1,2]
array_2d[0, :]
```

That same idea extends to the 3D `mystery_array`:

```python
mystery_array = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],
                          [[7, 86, 6, 98],
                           [5, 1, 0, 4]],
                          [[5, 36, 32, 48],
                           [97, 0, 27, 18]]])

mystery_array.ndim
mystery_array.shape
mystery_array[2,1,3]
```

The key idea is simple but powerful: provide one index per axis. If you leave an axis open with `:`, NumPy returns all values along that axis.

That is why high-dimensional data becomes manageable once you learn to read the shape. The shape tells you how many indices a full selection requires.

## 3. Generate Arrays Instead of Typing Values by Hand

NumPy becomes much more useful once you stop creating arrays manually and start generating them with structure.

`linspace()` is one of the most important helpers in the notebook:

```python
x = np.linspace(start=0, stop=100, num=9)
print(x)

y = np.linspace(start=-3, stop=3, num=9)
plt.plot(x, y)
```

This is better than plain integer counting when you need evenly spaced numeric samples for plotting, modeling, or simulation.

The notebook also generates random arrays:

```python
z = np.random.random((3,3,3))
print(z.shape)

noise = np.random.randint(low=0, high=255, size=(128,128,3))
plt.imshow(noise)
plt.show()
```

That second example is a useful bridge into image thinking. A random RGB image is just a 3D array with height, width, and color channels.

## 4. Treat Images as Arrays

The image section makes the NumPy model feel concrete. The notebook loads an image and converts it into an array:

```python
my_img = Image.open(file_name)
img_array = np.array(my_img)

plt.imshow(img_array)
plt.imshow(img_gray, cmap='gray')
```

Once the image is an array, transformations become numeric operations:

```python
plt.imshow(np.flip(img_gray), cmap='gray')
plt.imshow(np.rot90(img))

solar_img = 255 - img
plt.imshow(solar_img)
```

This is vectorized computation in practice. You are not looping pixel by pixel in Python. You are describing an operation on the whole array, and NumPy applies it efficiently across the full structure.

That is the deeper lesson of the day. NumPy is powerful because it lets you think in whole-array operations:

- slice whole regions
- transform every value at once
- work across multiple dimensions without nested loops

## How to Run the NumPy Notebook

1. Install the libraries used in the notebook:
   ```bash
   pip install numpy matplotlib pillow scipy
   ```
2. Open `Computation_with_NumPy_and_N_Dimensional_Arrays.ipynb`.
3. Run the notebook in order so the arrays and image variables are defined before the later visualization cells.
4. Verify the main checkpoints:
   - inspect `shape` and `ndim`
   - index into the 3D array correctly
   - generate numeric arrays with `linspace()`
   - transform images with NumPy operations

## Summary

Today, you learned that NumPy is built around structure. The shape of an array tells you how to index it, how to slice it, and which operations make sense. Once you start thinking in terms of axes and vectorized operations, arrays, matrices, and images all begin to look like the same kind of object.
