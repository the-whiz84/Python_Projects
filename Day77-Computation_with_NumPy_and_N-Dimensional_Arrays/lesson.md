# Computation with `NumPy` and N-Dimensional Arrays

No Data Science course can be complete without learning NumPy (Numerical Python). 
NumPy is a Python library that’s used in almost every field of science and engineering. 
It’s practically THE standard for working with numerical data in Python. The case studies for how NumPy is being used speak for themselves 😮:
- **FIRST IMAGE OF A BLACK HOLE** - How `NumPy`, together with libraries like `SciPy` and `Matplotlib` that depend on NumPy, enabled the Event Horizon Telescope to produce the first ever image of a black hole
- **DETECTION OF GRAVITATIONAL WAVES** - In 1916, Albert Einstein predicted gravitational waves; 100 years later their existence was confirmed by LIGO scientists using `NumPy`.

So far, we’ve been using Pandas, which is built on top of NumPy. Think of Pandas as a high-level data manipulation tool that includes functionality for working with time-series or for grouping, joining, merging and finding missing data (i.e., everything we’ve been doing so far). NumPy on the other hand shines with low-level tasks, like doing serious math and calculations.

## 1. NumPy's `ndarray` - Incredible Power at Your Fingertips!

Let’s import NumPy

    import numpy as np

    import matplotlib.pyplot as plt
    from scipy import misc # contains an image of a racoon!
    from PIL import Image # for reading image files

The crown jewel of NumPy is the `ndarray`. The **ndarray** is a <i>homogeneous n-dimensional array</i> object. What does that mean? 🤨

A Python List or a Pandas DataFrame can contain a mix of strings, numbers, or objects (i.e., a mix of different types). 
**Homogenous** means all the data have to have the same data type, for example all floating-point numbers.

And **n-dimensional** means that we can work with everything from a single column (1-dimensional) to the matrix (2-dimensional) to a bunch of matrices stacked on top of each other (n-dimensional).

<img src="https://img-c.udemycdn.com/redactor/raw/2020-10-12_15-34-45-6fdebf22c1ab4c51fd82687144c0f215.gif">


### 1-Dimension

Let’s create a 1-dimensional array (i.e., a **“vector”**)

    my_array = np.array([1.1, 9.2, 8.1, 4.7])

We can see `my_array` is 1 dimensional by looking at its shape

    my_array.shape
    (4,)
    
We access an element in a ndarray similar to how we work with a Python List, namely by that element's index:

    my_array[2]
    np.float64(8.1)

Let’s check the dimensions of my_array with the `ndim` attribute:

    my_array.ndim
    1


### 2-Dimensions

Now, let’s create a 2-dimensional array (i.e., a **“matrix”**)

    array_2d = np.array([[1, 2, 3, 9], [5, 6, 7, 8]])

Note we have two pairs of square brackets. This array has 2 rows and 4 columns. NumPy refers to the dimensions as **axes**, so the first axis has length 2 and the second axis has length 4.

    print(f'array_2d has {array_2d.ndim} dimensions')
    print(f'Its shape is {array_2d.shape}')
    print(f'It has {array_2d.shape[0]} rows and {array_2d.shape[1]} columns')
    print(array_2d)

    array_2d has 2 dimensions
    Its shape is (2, 4)
    It has 2 rows and 4 columns
    [[1 2 3 9]
    [5 6 7 8]]

Again, you can access a particular row or a particular value with the square bracket notation. To access a particular value, you have to provide an **index** for each dimension. 
We have two dimensions, so we need to provide an index for the row and for the column. Here’s how to access the 3rd value in the 2nd row:

    array_2d[1,2]
    np.int64(7)

To access an entire row and all the values therein, you can use the `:` operator just like you would do with a Python List. 
Here’s the entire first row:

    array_2d[0, :]
    array([1, 2, 3, 9])


### N-Dimensions

An array of 3 dimensions (or higher) is often referred to as a **”tensor”**. Yes, that’s also where **Tensorflow**, the popular machine learning tool, gets its name. 
A tensor simply refers to an n-dimensional array. 
Using what you've learned about 1- and 2-dimensional arrays, can you apply the same techniques to tackle a more complex array?

**Challenge**
- How many dimensions does the array below have?
- What is its shape (i.e., how many elements are along each axis)?
- Try to access the value 18 in the last line of code.
- Try to retrieve a 1-dimensional vector with the values [97, 0, 27, 18]
- Try to retrieve a (3,2) matrix with the values [[ 0, 4], [ 7, 5], [ 5, 97]]


**Solution**: Working with Higher Dimensions

This is really where we have to start to wrap our heads around how **ndarrays** work because it takes some getting used to the notation.

The `ndim` and `shape` attributes show us the number of dimensions and the length of the axes respectively.

    print(f'We have {mystery_array.ndim} dimensions')
    print(f'The shape is {mystery_array.shape}')

The shape is (3, 2, 4), so we have 3 elements along axis #0, 2 elements along axis #1 and 4 elements along axis #3.

To access the value `18` we, therefore, have to provide three different indices - one for each axis. As such, we locate the number at index 2 for the first axis, index number 1 for the second axis, and index number 3 for the third axis.

    mystery_array[2, 1, 3]

The values [97, 0, 27, 18] live on the 3rd axis and are on position 2 for the first axis and position 1 on the second axis. Hence we can retrieve them like so:

    mystery_array[2, 1, :]

Finally, to retrieve all the first elements on the third axis, we can use the colon operator for the other two dimensions.

    mystery_array[:, :, 0]

With the square brackets serving as your guide, the ndarray is quite difficult to visualize for 3 or more dimensions. 
So if any of this was unclear or confusing, pause on this lesson for a minute and play around with the array above. 
Try selecting different subsets from the array. That way you can get comfortable thinking along the different dimensions of the ndarray.

    mystery_array.ndim
    3

    mystery_array.shape
    (3, 2, 4)

    mystery_array[2,1,3]
    np.int64(18)

    mystery_array[2,1,:]
    array([97,  0, 27, 18])

    mystery_array[:,:,0]
    array([[ 0,  4],
       [ 7,  5],
       [ 5, 97]])


## 2. Generating and Manipulating `ndarrays`

**NumPy** has many many pages of documentation on all of its extensive functionality. 
But rather than go through the list one by one, the best way to actually learn NumPy is to apply it to a series of small problems. 
That way you can familiarize yourself with how to use NumPy for the common use cases that you'll encounter on your own data science journey too.

### Challenge 1
Use <a href="https://numpy.org/doc/stable/reference/generated/numpy.arange.html">.arange()</a> to create a a vector a with values ranging from 10 to 29. 
You should get this:

    print(a)

    [10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29]

Previously we created NumPy arrays manually where we specified each and every value like this: `np.array([1.1, 9.2, 8.1, 4.7])`

We can also generate a NumPy arrays using some built-in functions like `.arange()`. In this case, we can create an array of evenly spaced values by just providing a start and stop value.

    a = np.arange(10, 30)
    print(a)

    [10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29]

### Challenge 2

Use Python slicing techniques on `a` to:
- Create an array containing only the last 3 values of `a`
- Create a subset with only the 4th, 5th, and 6th values
- Create a subset of `a` containing all the values except for the first 12 (i.e., `[22, 23, 24, 25, 26, 27, 28, 29]`)
- Create a subset that only contains the even numbers (i.e, every second number)


    a[-3:]
    array([27, 28, 29])

    b = a[3:6]
    print(b)
    [13 14 15]

    c = a[12:]
    print(c)
    [22 23 24 25 26 27 28 29]

    d = a[::2]
    print(d)
    [10 12 14 16 18 20 22 24 26 28]

This should be a little bit of revision for using the colon : operator to select a range or interval in an array.

The last 3 values in the array:

    a[-3:]

An interval between two values:

    a[3:6]

All the values except the first 12:

    a[12:]

Every second value (i.e., all the even values in our case)

    a[::2]

### Challenge 3

Reverse the order of the values in a, so that the first element comes last:
    
    [29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]

If you need a hint, you can check out this part of the <a href="https://numpy.org/devdocs/user/absolute_beginners.html#how-to-reverse-an-array">NumPy beginner's guide</a>

    reverse_a = np.flip(a)
    print(reverse_a)
    [29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10]

To reverse the order of an array, you can either use the (double) colon operator once again or use the built-in `.flip()` function. 
Either way works.

    np.flip(a)

or

    a[::-1]

### Challenge 4

Print out all the indices of the non-zero elements in this array: [6,0,9,0,0,5,0]

    b = np.array([6, 0, 9, 0, 0, 5, 0])
    b[b != 0]
    array([6, 9, 5])

 If you did a quick Google search, chances are you discovered the built-in `.nonzero()` function to print out all the non-zero elements. You can use it like so:

    b = np.array([6,0,9,0,0,5,0])
    nz_indices = np.nonzero(b)
    nz_indices # note this is a tuple
    (array([0, 2, 5]),)

#This does not seem to work in 2024

### Challenge 5

Use NumPy to generate a 3x3x3 array with random numbers

Hint: Use the <a href="https://numpy.org/doc/stable/reference/random/index.html#module-numpy.random">.random() function</a>

The `.random()` function is another way to quickly create a ndarray, just like `.arange()`. 
The `.random()` function lives under `np.random` so you'll either have to import random

    from numpy.random import random
    z = random((3,3,3))
    z

or use the full path to call it.

    z = np.random.random((3,3,3)) # without an import statement
    print(z.shape)
    z

    (3, 3, 3)

    array([[[0.92229483, 0.10097038, 0.04623102],
        [0.26637463, 0.6294085 , 0.32618499],
        [0.77571865, 0.41155769, 0.11350707]],

       [[0.23206643, 0.22975407, 0.48804269],
        [0.21763848, 0.16314077, 0.50495574],
        [0.36957769, 0.66893063, 0.25469753]],

       [[0.93377489, 0.84398379, 0.59232446],
        [0.165734  , 0.27566743, 0.42234953],
        [0.62567175, 0.99900463, 0.726447  ]]])

### Challenge 6

Use <a href="https://numpy.org/doc/stable/reference/generated/numpy.linspace.html">.linspace()</a> to create a vector x of size 9 with values spaced out evenly between 0 to 100 (both included).

    x = np.linspace(start=0, stop=100, num=9)
    x
    array([  0. ,  12.5,  25. ,  37.5,  50. ,  62.5,  75. ,  87.5, 100. ])

The `.linspace()` function is very similar to `.arange()` and great for generating evenly spaced numbers over an interval. 
To generate the vector use:

    x = np.linspace(0, 100, num=9)
    print(x)
    x.shape
    (9,)

### Challenge 7

Use `.linspace()` to create another vector `y` of size 9 with values between -3 to 3 (both included). 
Then plot x and y on a line chart using ***Matplotlib***.

    y = np.linspace(start=-3, stop=3, num=9)
    plt.plot(x, y)

A common use-case for `.linspace()` is to generate the points that you'd like to plot on a chart.

    y = np.linspace(start=-3, stop=3, num=9)
    plt.plot(x, y)
    plt.show()


### Challenge 8

Use NumPy to generate an array called `noise` with shape 128x128x3 that has random values. 
Then use Matplotlib's <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html">.imshow()</a> to display the array as an image.

The random values will be interpreted as the RGB colors for each pixel.

    noise = np.random.randint(low=0, high=255, size=(128,128,3))
    noise.shape
    plt.imshow(noise)
    plt.show()

When you have a 3-dimensional array with values between 0 and 1 (or 0 to 255), we can use Matplotlib to interpret these values as the red-green-blue (RGB) values for a pixel.

    noise = np.random.random((128,128,3))
    print(noise.shape)
    plt.imshow(noise)

That's pretty cool, right?! We've just generated a 128x128 pixel image of random noise because each dimension in our NumPy array can be interpreted to hold the color information for a pixel.


## 3. Broadcasting, Scalars and Matrix Multiplication

### Linear Algebra with Vectors

NumPy is designed to do math (and do it well!). This means that NumPy will treat vectors, matrices and tensors in a way that a mathematician would expect. For example, if you had two vectors:

    v1 = np.array([4, 5, 2, 7])
    v2 = np.array([2, 1, 3, 3])

And you add them together

    v1 + v2

The result will be a ndarray where all the elements have been added together.

    array([ 6, 6, 5, 10])

In contrast, if we had two Python Lists

    list1 = [4, 5, 2, 7]
    list2 = [2, 1, 3, 3]

adding them together would just concatenate the lists.

    list1 + list2
    # output: [4, 5, 2, 7, 2, 1, 3, 3]

Multiplying the two vectors together also results in an element by element operation:

    v1 * v2

Gives us `array([ 8, 5, 6, 21])` since 4x2=8, 5x1=5 and so on. And for a Python List, this operation would not work at all.

    list1 * list2 # error!


### Broadcasting

Now, oftentimes you'll want to do some sort of operation between an array and a single number. 
In mathematics, this single number is often called a **scalar**. For example, you might want to multiply every value in your NumPy array by 2:

<img src="https://img-c.udemycdn.com/redactor/raw/2020-10-12_16-01-36-b9c2fefd91ad6764599526cd883cc721.gif">

In order to achieve this result, NumPy will make the shape of the smaller array - our scalar - compatible with the larger array. 
This is what the documentation refers to when it mentions the term "**broadcasting**".

The same rules about 'expanding' the smaller ndarray hold true for 2 or more dimensions. 
We can see this with a 2-Dimensional Array:

    array_2d = np.array([[1, 2, 3, 4], 
                        [5, 6, 7, 8]])

The scalar operates on an element by element basis.

    array_2d + 10
    array([[11, 12, 13, 14],
       [15, 16, 17, 18]])
    
The documentation on broadcasting also shows us a few more examples:

<img src="https://img-c.udemycdn.com/redactor/raw/2020-10-12_16-07-56-fbba1b975a8b7e2ad2cc5323ebe4d771.png">


### Matrix Multiplication

But what if we're not multiplying our ndarray by a single number? What if we multiply it by another vector or a 2-dimensional array? 
In this case, we follow the rules of <a href='https://en.wikipedia.org/wiki/Matrix_multiplication#Illustration'>linear algebra.</a>

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-12_17-01-09-7243f82f4dd88bec877e3206fb9d9add.png'>

**Challenge: **
Let's multiply a1 with b1. Looking at the Wikipedia example above, work out the values for c12 and c33 on paper. 
Then use the <a href="https://numpy.org/doc/stable/reference/generated/numpy.matmul.html">.matmul()</a> function or the `@` operator to check your work.

    a1 = np.array([[1, 3],
               [0, 1],
               [6, 2],
               [9, 7]])

    b1 = np.array([[4, 1, 3],
                [5, 8, 5]])

    print(f'{a1.shape}: a has {a1.shape[0]} rows and {a1.shape[1]} columns.')
    print(f'{b1.shape}: b has {b1.shape[0]} rows and {b1.shape[1]} columns.')
    print('Dimensions of result: (4x2)*(2x3)=(4x3)')


    np.matmul(a1, b1)
    array([[19, 25, 18],
        [ 5,  8,  5],
        [34, 22, 28],
        [71, 65, 62]])

    a1 @ b1
    array([[19, 25, 18],
       [ 5,  8,  5],
       [34, 22, 28],
       [71, 65, 62]])

**Solution**: Matrix multiplication with NumPy

The solution code is pretty straightforward

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-12_17-09-52-f6340c29d54b49927078ab4c2c105441.png'>

But how did the calculations arrive at 25 for c12 and 28 for c33? Substituting the number into the formula we get:

c12 = 1*1 + 3*8 = 1 + 24 = 25

c33 = 6*3 + 2*5 = 18 + 10 = 28


## 4. Manipulating Images as ndarrays

Images are nothing other than a collection of pixels. And each pixel is nothing other than value for a color. 
And any color can be represented as a combination of red, green, and blue (RGB).

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-12_17-25-44-d5854190572f3330c9e306fbf2933923.gif'>

### Import Statements

    from scipy import misc # Deprecated
    from scipy import datasets ## contains an image of a racoon!
    from PIL import Image # for reading image files

You should two import statements at the top. **Scipy** and **PIL** will help us work with images.

The Scipy library contains an image of a racoon under 'miscellaneous' (misc). We an fetch it like so:

    img = misc.face()

    /var/folders/3q/zg5b2vcj50nc6cwf_t1v64wm0000gn/T/ipykernel_11045/347613074.py:1: DeprecationWarning: scipy.misc.face has been deprecated in SciPy v1.10.0; and will be completely removed in SciPy v1.12.0. Dataset methods have moved into the scipy.datasets module. Use scipy.datasets.face instead.
  img = misc.face()
#Deprecated

    img = datasets.face()

and display it using Matplotlib's `.imshow()`

    plt.imshow(img)

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-12_17-33-27-9e2e3bb61614dd8f814429f9f7dd6b50.png'>

**Challenge**
What is the data type of img? Also, what is the shape of img and how many dimensions does it have? 
What is the resolution of the image?

**Solution**: An image as a ndarray

Let us question the nature of our reality and take a look under the surface. Here's what our "image" actually looks like: 

<img src="https://img-c.udemycdn.com/redactor/raw/2020-10-13_09-28-44-6f41078c913d2304ad5e606add8704e2.png">

We can now clearly see that we're dealing with a ndarray. And it's a 3 dimensional array at that.

    type(img)
    numpy.ndarray

    img.shape
    (768, 1024, 3)

    img.ndim
    3

There are three matrices stacked on top of each other - one for the red values, one for the green values and one for the blue values. 
Each matrix has a 768 rows and 1024 columns, which makes sense since 768x1024 is the resolution of the image.

**Challenge**
Now can you try and convert the image to black and white? All you need need to do is use a formula.

<img src="https://img-c.udemycdn.com/redactor/raw/2020-10-12_17-56-16-aff5999394e88abae2995c6d700a8cb1.png">

Y_linear is what we're after - our black and white image. However, this formula only works if our red, green and blue values are between 0 and 1 - namely in sRGB format. 
Currently the values in our `img` range from 0 to 255. So:

- Divide all the values by 255 to convert them to sRGB.
- Multiply the sRGB array by the grey_vals array (provided) to convert the image to grayscale.
- Finally use Matplotlib's `.imshow()` with the `colormap` parameter set to gray `cmap=gray` to display the result.

**Solution**: Converting an image to grayscale

The first step is a division by a scalar

    sRGB_array = img / 255

Here NumPy will use broadcasting to divide all the values in our ndarray by 255.

Next, we use matrix multiplication to multiply our two ndarrays together.

    grey_vals = np.array([0.2126, 0.7152, 0.0722])

These are the values given by the formula above

    img_gray = sRGB_array @ grey_vals

We can either multiply them together with the @ operator or the .matmul() function.

    img_gray = sRGB_array @ grey_vals
    img_gray = np.matmul(sRGB_array, grey_vals)

Finally, to show the image we use Matplotlib

    plt.imshow(img_gray, cmap='gray')

The `cmap` parameter is important here. If we leave it out the function will not know that is dealing with a black and white image.

<img src="https://img-c.udemycdn.com/redactor/raw/2020-10-12_18-03-51-46b947197834216ff69717fd4ac7dd58.png">


**Challenge**
Can you manipulate the images by doing some operations on the underlying ndarrays? 
See if you can change the values in the ndarray so that:

1) You flip the grayscale image upside down like so:

<img src="https://img-c.udemycdn.com/redactor/raw/2020-10-13_09-48-42-6da00043154d3fd57f2b979b692125c1.png">

2) Rotate the colour image:

<img src="https://img-c.udemycdn.com/redactor/raw/2020-10-13_09-48-48-618965070981a8096f73de791f750b21.png">

3) Invert (i.e., solarize) the colour image. 
To do this you need to convert all the pixels to their "opposite" value, so black (0) becomes white (255).

<img src="https://img-c.udemycdn.com/redactor/raw/2020-10-13_09-48-54-e30020abc219020c9a4c214cc55a6da1.png">

**Solution**: Manipulating the ndarray to change the image

For the first challenge, all you need to do is reverse the order of the rows and the columns in the NumPy array with the `.flip()` function:

You can display the upside down image in a single line of code:

    plt.imshow(np.flip(img_gray), cmap='gray')

To rotate the image, all you need to do is rotate the array with `.rot90()`
This will rotate our image too:

    plt.imshow(np.rot90(img))

Inverting the colour image is a bit more tricky. It involved making use of NumPy's ability to broadcast when doing operations with a scalar. 
In this case, our scalar is 255 - the maximum value for a pixel in RGB (see gif at the very top). 
If we subtract the values of our img from 255, then we get the opposite value for each pixel:

    solar_img = 255 - img
    plt.imshow(solar_img)

### Use Your Own Images

I've provided a .jpg file in the starting .zip file, so you can try your code out with an image that isn't a racoon 🦝. 
The key is that your image should have 3 channels (red-green-blue). 
If you use a .png file with 4 channels there are additional pre-processing steps involved to replicate what we're doing here.

How do you open an image and put it into a NumPy array?

<img src="https://img-c.udemycdn.com/redactor/raw/2020-10-13_10-29-27-3a3e2d19291e4b76effc62168f2023cd.png">

First, make sure you've added the image to your project. All you need to do is use the PIL library to open the image and then create the ndarray using the image. 
You should see that your ndarray has 3 dimensions. The shape will be the resolution of your image.

Now feel free to manipulate your own images as you see fit. If you discover something particularly cool, be sure to share in the comments below! 

    file_name = 'yummy_macarons.jpg'

    my_img = Image.open(file_name)
    img_array = np.array(my_img)

    print(img_gray.shape)
    plt.imshow(img_array)
    (768, 1024)

<img src="https://img-c.udemycdn.com/redactor/raw/2020-10-13_10-34-04-6e3c1ebc7c0899aefd0d78ad8e899634.png">


## 5. Learning Points & Summary

In this lesson we looked at how to:
- Create arrays manually with `np.array()`
- Generate arrays using  `.arange()`, `.random()`, and `.linspace()`
- Analyze the shape and dimensions of a ndarray
- Slice and subset a ndarray based on its indices
- Do linear algebra like operations with scalars and matrix multiplication
- Use **NumPys** broadcasting to make ndarray shapes compatible
- Manipulate images in the form of ndarrays
