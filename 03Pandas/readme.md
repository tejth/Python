# Introduction to Pandas

You can think of pandas as an extremely powerful version of Excel, with a lot more features.
pip install pandas

<ul>
Introduction to Pandas
<li>Series</li>
<li>DataFrames</li>
<li>Missing Data</li>
<li>GroupBy</li>
<li>Merging,Joining,and Concatenating
Operations</li>
<li>Data Input and Output</li>
</ul>

# Series

A Series is very similar to a NumPy array (in fact it is built on top of the NumPy array object). What differentiates the NumPy array from a Series, is that a Series can have axis labels, meaning it can be indexed by a label, instead of just a number location. It also doesn't need to hold numeric data, it can hold any arbitrary Python Object.

# DataFrames

DataFrames are the workhorse of pandas and are directly inspired by the R programming language. We can think of a DataFrame as a bunch of Series objects put together to share the same index. Let's use pandas to explore this topic!

# Missing Data

pandas also provides ways to handle Missing Data such as nan

# Groupby

The groupby method allows you to group rows of data together and call aggregate functions

# Merging, Joining, and Concatenating

There are 3 main ways of combining DataFrames together: Merging, Joining and Concatenating.

# Operations

There are lots of operations with pandas that will be really useful to you, but don't fall into any distinct category

# Data Input and Output

Involves ways of Getting and setting data inside various files such as csv,html etc..
