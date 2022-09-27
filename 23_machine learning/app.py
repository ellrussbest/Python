"""
steps involved in machine learning;
    1. importing the data (which often come in .csv file)
    2. cleaning the data - removing duplicate pattern
    3. split the data into training and testing sets
    4. creating a model
    5. Train the model
    6. make predictions
    7. evaluate and improve the predictions
"""

"""
 libraries and tools for machine learning;
    numpy - provides a multidimensional array
    pandas - data analysis library that provides data frames
            - a data frame is a two dimensional data structure similar to an excel spreadsheet
            - we can select data in a row or column or a range of rows and columns
    matplotlib - 2-d plotting library for plotting graphs and plots
    scikit-learn - provides algorithms like decision trees, neural networks etc.
"""

"""
    when programming machine learning models we use an env
    called jupyter
"""

"""
importing file into jupyter:
    import pandas as pd

    # read_csv returns a dataframe object
    dataframe = pd.read_csv('vgsales.csv')

    # inspecting the data frame
    dataframe

    # checking the description of the dataframe
    # e.g. number of records(rows) and number of columns 
    dataframe.shape

    # gives you an overview of your data frame
    # e.g. mean, count, standard deviation
    # returns a brief information about each column
    dataframe.describe()

    # returns a two dimensional array
    dataframe.values
"""