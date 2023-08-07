# Day 18 / Day 60 💻
## Tensorflow [![Tensorflow Badge](https://img.shields.io/badge/-Tensorflow-FF6F00?style=flat&logo=tensorflow&logoColor=white&link=https://www.upwork.com/freelancers/~01e4a957c2b59dee15)](https://www.tensorflow.org/)

## 🤖 Machine Learning
Machine Learning makes the rules for us. 👇

<p align="center">
<img src="https://inlocrobotics.com/wp-content/uploads/2021/03/classical-programming-vs-machine-learning.jpg" width="600" height="400">
</p>


**GOAL:** Acieve highest accuracy possible

## 🧠 Neural Networks
Layered represntation of Data

![](https://www.tibco.com/sites/tibco/files/media_entity/2021-05/neutral-network-diagram.svg)

> **What are features and labels?** \
> Labels are also called output information

![](https://developers.google.com/static/machine-learning/intro-to-ml/images/labeled_example.png)

> `Training Data has Features and Labels both.` \
> `Testing Data only has Features as it predicts Labels.`

### 🟠 Supervised Learning
* Most common type of learning

**Features -> Labels** \
Example: predicitng final exam marks of student based on module 1 and module 2

### 🟠 Unupervised Learning

**Features Only** \
Example: clustering

### 🟠 Reinforcement Learning
* Environment
* Agent
* Reward

## How it works?
2 Main components
#### 1. Graphs
* It creates graph of partial computations. 
* When we write code, we create  graphs. 
* When we create variable it writes down, variable 3 is sum of variable 1 and variable 2. it does not store the values but computations. 

> As different computations are linked to each other , that's why it is called graph.

#### 2. Sessions
* A way of executing part or entire graph
* When we start a session, we start executing parts of graphs 


## 🔶 What are Tensors?
A tensor is a generalization of vectors and matrices to potentially higer dimensions.
* Vector can have nay dimension in it
 * If it has x1 then it has 1 dimensions
 * if it has x1, y1 then ith as 2 dimension

### 🔵 Data Types in Tensors
* float32 _(most common)_ , int32, string and others 

**Shape:** It represents the dimensions

### 🔵 How to make a Tensor?

```python
string = tf.Variable("This is a String", tf.string)
number = tf.Variable(324, tf.int64)
floating = tf.Variable(4.247, tf.float64)
```
### 🥇 Rank/Degree of Tensors
 It menas the number of dimension involved in the tensor. 

The above created [tensors](#how-to-make-a-tensor) are or Rank 0, also known as a Scalar

#### Higher Rank/Dimension Tensors
```python
rank1_tensor = tf.Variable(["Test", "One Dimension"], tf.String)
rank2_tensor = tf.Variable([["Test", "Two"], ["Test2", "dimension"]], tf.String)
```

> **Dimensions can be determined by deepest level of nested list**

#### To check the dimension of a tensor:
```python
tf.rank(rank2_tensor)
```

#### To check the shape of a tensor:
```python
rank2_tensor.shape
```
> `TensorShape([2, 2])`

First 2 represents the number of lists it has Second 2 represnts number of elements in each list

Similarly, 
```python
rank3_tensor = tf.Variable([["Test", "Two", "additonal"], ["Test2", "dimension", "additonal"], ["additonal", "additonal", "additonal"]], tf.String)

rank3_tensor.shape
```
> `TensorShape([3, 3])`

`rank3_tensor` has 3 lists and each list has 3 elements

### 🔵 Changing Shapes

```python
tensor1 = tf.ones([1,2,3])  # tf.ones() creates a shape [1,2,3] tensor full of ones
print(tensor1)
```

> `tf.Tensor( 
[[[1. 1. 1.]
  [1. 1. 1.]]], shape=(1, 2, 3), dtype=float32)`

in above **shape=(1, 2, 3)**, the tensor has 1 interioir list, then 2 lists inside it and then 3 elements inside those two lists.

Now we well **reshape** tensor1 into 2 ,3, 1 sape which will mean that it will have 2 interior lists, those two lists will have 3 lists each inside them and then those three lists will have 1 element each.

```python
tensor2 = tf.reshape(tensor1, [2,3,1])  # reshape existing data to shape [2,3,1]
tensor3 = tf.reshape(tensor2, [3, -1])  # -1 tells the tensor to calculate the size of the dimension in that place
                                        # this will reshape the tensor to [3,3]
                                                                             
# The numer of elements in the reshaped tensor MUST match the number in the original

print(tensor1)
print(tensor2)
```


`tf.Tensor(` \
`[[[1.]` \
`  [1.]` \
`  [1.]]` 
  
`[[1.]` \
`  [1.]` \
`  [1.]]], shape=(2, 3, 1), dtype=float32)`

## 🔵 Types of Tensors
* Variable (tf.Variable)
* Constant
* Placeholder
* SparseTensor

Exceppt Variable, all the other tensors are immutable, which means that there value can not be changed during the execution

We use **Variable** tensor when we want to change the value of tensor

## Evaluating Tensors
To evaluate a tensor, we need to create a [session](#2-sessions)

```python
with tf.Session() as sess:
    tesnor.eval() # tesnor = name of your tensor
```