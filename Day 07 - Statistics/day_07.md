# Day 07 / Day 60 💻
## Statistics 📊
*Statistics is everywhere.*

**Use Cases**
* Weather Forecast (what are the chances)
* Currency/crypto/shares prediction
* Salary prediction

### **1. Languauge of Statistics**
Graphs, Plots, visualizations

What are the aspect of statistics in the following?
1. Average income a specific country or job sector (mean)
2. Ranking of cities based on population, income, religion etc. (max)
3. Weather forecast, will it rain tomorrow? (likelihood)
4. Currency/crypto/shares prediction (variance)
5. Women spend more on shopping then men (t-test)

### **2. Types of Data**
#### **A. Type 1**
|Cross Sectional|Time Series|
|:---:|:---:|
|Data which is collected at one point of time|Data which is collected over a period of time|
|**example:** how many students attended class today|**example:** Number of Coivd-19 cases from 2020 to 2022|

#### **B. Type 2**
|Univariate|Multivariate|
|:---:|:---:|
|Data contains only 1 variable|Data contains more than 1 variable|
|**example:** how does drinking water only affects person's health|**example:** how does drinking water, doing exercise and eating protien shake affects person's health|

### **3. Types of Variables**
_categorical -> nomial_

#### **A. Type 1**
|Bionomial|Multinomial|
|:---:|:---:|
|Data has only 2 categories|Data has more than 2 categories|
|**example:** Does the person likes pizza or burger|**example:** how many travel choices did a person has|

#### **B. Ordinal Variable**
Data ranked or ordered. (no fixed unit of measurement)
**example:** How many cellphones students in class has, student will be ranked 1st with the most numbers of cellphones and last student will be who has least or no cellphones.

#### **C. Ratio Data**
Data have natural zero. 
**example:** how many unites were sold today. (20% more sales today than yesterday)

#### **D. Interval Variables**
Ordered and characterized data
**example:**  Weather is 4 fegree hotter than last summer

### **3. Measure of Central Tendency**
Mean, Median & Mode

#### Population vs Sample
* **Population** research has more power ans is also more accurate.
* **Samples** are used to reduce the cost of data collection

### Notion and Terms of Statistics
**Complete Statistics Cheatsheet from MIT**: [Statistics Cheat Sheet](https://web.mit.edu/~csvoss/Public/usabo/stats_handout.pdf)
1. **_N_**: size of  population
2. **n**: size of sample
3. **Σ** : Sum
4. **Measurement**: Number or attribute somputed from each member of a population. 
5. **Qualitative Data**: Categorical and NON_NUMERIC data
6. **Quantitative Data**: Numerical Data
7. **Mean**: Sum divided by number of observations
    * Meaningful for intervals and ratio data
    * Outliers hange the **mean** of data, that is why **median** is useful
```python
import statistics
statistics.mean([4, 8, 6, 5, 3, 2, 8, 9, 2, 5])
5.2
```

8. **Median**: Middle number in a sorted ascending or descending or list of numbers
    * Unique for each dataset
    * outliers does not has affect on median
    * Ratios, intervals and ordinal data has best use for median
```python
import statistics
statistics.median([3, 5, 1, 4, 2])
3
```

9. **Mode**: Value that occurs most frequently 
```python
import statistics
statistics.mode([4, 1, 2, 2, 3, 5])
2

statistics.multimode([4, 1, 2, 2, 3, 5, 4])
[4, 2]

statistics.mode(["few", "few", "many", "some", "many"])
'few'
statistics.multimode(["few", "few", "many", "some", "many"])
['few', 'many']
```

### **4. Measure of Dispersion**
 * State of data getting dispersed, stretched, or spread out in different categories
 * Range from minimum to maximum is called **dispersion of data**
    * **standard daviation (std)** or **standard error (se)** or **variance** or **bell curve**

### How to read data from bell curve:
Example:
Data from 100 shops in a town

![Bell Curve Example](bellcurveexample.jpg)

We need to check standard deviation or dispertion as well along with mean

**Mean with Standard Deviation is more useful than just Mean**









