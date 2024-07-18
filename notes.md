# Lec 02 Data Sampling and Probability

## Samples

error:

- chance error
- bias

### Convenience samples

- not random
- pilot testing

### Quota samples

- not random
- First group by one feature, and then do convenience sampling  

### Population, sample, and sampling frame

![image-20240710102707656](C:\Users\86139\AppData\Roaming\Typora\typora-user-images\image-20240710102707656.png)

There might be individuals in your sampling frame that are not in your population!

ensure that the sample is representative of the population.

## Bias vs Chance error

- Bias: One direction (If your sampling method is biased, those biases will be magnified with a larger sample size)  
  - Selection Bias: Systematically excluding particular groups.
  - Response Bias: People don't always tell the truth.
  - Non-response Bias: No answers

- Chance error: Any direction (get smaller as the sample size get larger, but it is unavoidable)

### Probability (Random) Sampling examples

- simple random sample
- systematic sample
- stratified sample
- cluster sample

![image-20240710110711504](C:\Users\86139\AppData\Roaming\Typora\typora-user-images\image-20240710110711504.png)

In order for a sample to be a probability sample:

- you must be able to provide probability that any specified set of individuals will be in the sample.

# Pandas

## Series

```python
s = pd.Series([-1, 10, 2]) # create a series
s.array
s.index

# specify the index
s = pd.Series([-1, 10, 2], index = ["a", "b", "c"])
s.index = ['m', 'n', 'p']
```

## DataFrame

syntax:

```python
pandas.DataFrame(data, index, columns)
# create a dataframe
# 1. from a csv file
elections = pd.read_csv("/data.csv", index_col="Year")

# 2. Using a list and column name
pd.DataFrame([1,2,3], columns=["NUmbers"])
pd.DataFrame([[1, "one"], [2, "two"], [3, "three"]], columns = ["Number", "Description"])

# 3. From a dictionary
pd.DataFrame({"Fruit":["Strawberry", "Orange"], "Price": [5.49, 3.99]})
pd.DataFrame([{"Fruit":"Strawberry", "Price":5.49},
{"Fruit":"Orange", "Price":3.99}])

# 4. From a Series
s_a = pd.Series(["a1", "a2", "a3"], index = ["r1", "r2", "r3"])
s_b = pd.Series(["b1", "b2", "b3"], index = ["r1", "r2", "r3"])
pd.DataFrame({"A-column": s_a, "B-column": s_b})

# modify index
elections.set_index("Party")
# reset index
elections.reset_index()
```

## Slicing with loc, iloc and []

### loc

```python
df.loc[row_labels, column_labels]
# augument: list
elections.loc[[87, 25, 179], ["Year", "Candidate", "Result"]]
# slice
elections.loc[[87, 25, 179], "Popular vote":"%"]
# single value
elections.loc[[87, 25, 179], "Popular vote"]
```

### iloc

```python
df.iloc[row_integers, column_integers]
# list
elections.iloc[[1, 2, 3], [0, 1, 2]]
# slice
elections.iloc[[1, 2, 3], 0:3]
# single value
elections.iloc[[1, 2, 3], 1]
```

### []

```python
# A slice of row integers
elections[3:7] # extract rows from 3-6
# A list of column labels
elections[["Year", "Candidate", "Result"]]
# A single column label
elections["Candidate"] # output series
```

## Conditional Selection

### .isin

```python
names = ["Bella", "Alex", "Narges", "Lisa"]
babynames[babynames["Name"].isin(names)]
```

### .str.startswith

```python
babynames[babynames["Name"].str.startswith("N")]
```

## Adding, removing, and modifying columns

```python
# rename
babynames = babynames.rename(columns={"name_lengths":"Length"})
# drop
babynames = babynames.drop("Length", axis = "columns")
```

## Handy Utility Functions

```python
babynames.describe()
babynames.shape
babynames.size
babynames.sample(5).iloc[:, 2:] # select random 5 samples
babynames["Name"].value_counts() # Series.value_counts counts the number of occurrences of each unique value in a Series
babynames["Name"].unique()
# sort values
babynames["Name"].sort_values()
babynames.sort_values(by = "Count", ascending = False)
```

## Groupby.agg

### Example

```python
elections.groupby("Party").agg(lambda x : x.iloc[0])
```

### groupby.size() and groupby.count()

![image-20240711165524657](C:\Users\86139\AppData\Roaming\Typora\typora-user-images\image-20240711165524657.png)

![image-20240711165533098](C:\Users\86139\AppData\Roaming\Typora\typora-user-images\image-20240711165533098.png)

### groupby.filter()

- groupby.filter takes an argument func
- func is a function that:
  - takes a DataFrame as input
  - Returns either True or False
- filter applies func to each group/sub-DataFrame

### PivotTables

![image-20240711170238815](C:\Users\86139\AppData\Roaming\Typora\typora-user-images\image-20240711170238815.png)

![image-20240711170334458](C:\Users\86139\AppData\Roaming\Typora\typora-user-images\image-20240711170334458.png)

## Join Tables

- Inner join
- left join
- right join
- outer join

# Regular Expressions

## Basic Regex Sytax

![image-20240711171927619](C:\Users\86139\AppData\Roaming\Typora\typora-user-images\image-20240711171927619.png)

## Expanded Regex Syntax

![image-20240711172003143](C:\Users\86139\AppData\Roaming\Typora\typora-user-images\image-20240711172003143.png)

## Convenient Regex

![image-20240711172119747](C:\Users\86139\AppData\Roaming\Typora\typora-user-images\image-20240711172119747.png)

## Regex in Python

```python
import re
re.sub(pattern, repl, text)
re.findall(pattern, text) # Return a list of all matches to pattern. non-overlapping
```

# Word Embedding

## Bag of words

## N-Gram Encoding

- N-Gram: "Bag of sequence of words"

## TF-IDF

### TF(Term frequency)

![image-20240713194431059](C:\Users\86139\AppData\Roaming\Typora\typora-user-images\image-20240713194431059.png)

### IDF (Inverse document frequency)

![image-20240713194446027](C:\Users\86139\AppData\Roaming\Typora\typora-user-images\image-20240713194446027.png)

### tf-idf

![image-20240713194512647](C:\Users\86139\AppData\Roaming\Typora\typora-user-images\image-20240713194512647.png)

# Visualization

## Bar Plot

```python
# pandas
births['Maternal Smoker'].value_counts().plot(kind = 'bar')
# Matplotlib manual
ms = births['Maternal Smoker'].value_counts();
plt.bar(ms.index, ms)
# seaborn
import seaborn as sns
sns.countplot(data = births, x = 'Maternal Smoker');

```

## Histogram

```python
sns.histplot(data = births, x = 'Maternal Pregancy Weight');
```

- Skewness and Tails
  - skewed right (mode > median > mean)
  - skewed left(mode < median < mean)
- Outliers

- Modes
  - local or global maximum
- n = w x h x N
  - n: number of samples in the bin
  - w: width of the bin
  - h: height of the bin
  - N: total number of samples

## Box plots

![image-20240713202855663](C:\Users\86139\AppData\Roaming\Typora\typora-user-images\image-20240713202855663.png)

## Visualization Theory

# Data on the Internet

## Request methods

```python
import requests
```

- GET mothod

```python
res = requests.get('https://bing.com')
res
res.text
```

- POST requests via requests

```python
post_res = requests.post('https://httpbin.org/post',
                         data={'name': 'King Triton'})

post_res
post_res.text
post_res.json()
```

## Json

```python
import json

f = open(os.path.join('data', 'family.json'), 'r')
family_tree = json.load(f)
```

```python
f_other = open(os.path.join('data', 'family.json'))
s = f_other.read()
json.loads(s)
```

- json.load(f): loads a json file from a file object
- json.loads(f): loads a json file from a string 

## BeautifulSoup objects

```python
import bs4
soup = bf4.BeautifulSoup(html_string)
```

### Finding elements in a tree

- `soup.find(tag)`
  - More general: `soup.find(name=None, attrs={}, recursive=True, text=None, **kwargs)`
- `soup.find_all(tag)`

## Nested vs. flat data formats

- **Nested** data formats, like HTML, JSON, and XML, allow us to represent hierarchical relationships between variables.

* **Flat** (i.e. tabular) data formats, like CSV, do not.

# Model & Linear Regression

## modeling process

1. choose a model
   - linear model, MLP ...
2. choose a loss function
   - L1 Loss
   - L2 Loss
3. fit the model
4. evaluate the model

![image-20240715170047482](C:\Users\86139\AppData\Roaming\Typora\typora-user-images\image-20240715170047482.png)

# Feature Engineering and Sklearn

## The `sklearn` Workflow

1. choose a model: `mymodel = lm.LinearRegression()`
2. fit the model: `mymodel.fit(X_train, Y_train)`
3. eval the model: `mymodel.predict(X_val)`

# Estimator, Bias, and Variance

![image-20240715173535883](C:\Users\86139\AppData\Roaming\Typora\typora-user-images\image-20240715173535883.png)

- observation variance
  - Our observation is not accurate compared to the true function
- model variance
  - Our sample is random, thus the model is somehow variance
- model bias
  - Out estimator(fitted model) is different from the true function

# Cross Validation and Regularization

## K-Fold Cross-Validation

For a dataset with K folds:

- Pick one fold as the validation fold
- train the model in the remaining folds
- computer the model's error on the validation field on the validation field
- repeat for all K folds
- cross-validation error = mean of validation errors for k rounds

## Regularization

### L2-Regularization

![image-20240715195140648](C:\Users\86139\AppData\Roaming\Typora\typora-user-images\image-20240715195140648.png)

### Scaling Data for Regularization

Standardize the data, i.e. replace everything with its Z-score

### L1 Regularization

![image-20240715195355594](C:\Users\86139\AppData\Roaming\Typora\typora-user-images\image-20240715195355594.png)

![image-20240715195412141](C:\Users\86139\AppData\Roaming\Typora\typora-user-images\image-20240715195412141.png)

# SQL

