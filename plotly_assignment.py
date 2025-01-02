# Q1. Load the Titanic Dataset and Plot a Scatter Plot
import seaborn as sns
import plotly.express as px
titanic = sns.load_dataset("titanic")
fig = px.scatter(titanic, x="age", y="fare", title="Age vs Fare Scatter Plot")
fig.show()

# Q2. Box Plot Using the Tips Dataset
tips = px.data.tips()
fig = px.box(tips, x="day", y="total_bill", title="Box Plot of Total Bill by Day")
fig.show()

# Q3. Histogram for sex vs total_bill with Additional Parameters
# Histogram with additional parameters
fig = px.histogram(
    tips,
    x="sex",
    y="total_bill",
    pattern_shape="smoker",
    color="day",
    title="Histogram of Total Bill by Sex",
)
fig.show()

# Q4. Scatter Matrix for the Iris Dataset
from plotly.data import iris
iris = px.data.iris()
fig = px.scatter_matrix(
    iris,
    dimensions=["sepal_length", "sepal_width", "petal_length", "petal_width"],
    color="species",
    title="Scatter Matrix of Iris Dataset",
)
fig.show()

"""
What is a Distplot?
A distplot is a combination of a histogram and a kernel density estimation (KDE) plot. It shows the distribution of a dataset.

Plotly express does not have a direct distplot function, but you can achieve a similar effect using px.histogram with marginal="rug" or marginal="box" for added details.
"""
fig = px.histogram(
    tips,
    x="total_bill",
    marginal="rug",
    title="Distplot-like Visualization of Total Bill",
    nbins=30,
)
fig.show()
