import streamlit as st
import pandas as pd

def app():
    # App Title
    st.title("Introduction to Data Analysis")

    # What is Data Analysis
    st.subheader(":orange[What is Data Analysis?]")
    st.write("""
    Data Analysis is the process of inspecting, cleansing, transforming, and modeling data to discover useful information, inform conclusions, and support decision-making.
    It helps uncover patterns, trends, and insights in raw data.
    """)

    # Main Libraries in Data Analysis
    st.subheader(":orange[Main Libraries Used in Data Analysis]")
    st.write("""
    1. **Pandas**: For data manipulation and analysis.
    2. **NumPy**: For numerical computations.
    3. **Matplotlib**: For creating static visualizations.
    4. **Seaborn**: For advanced visualizations built on Matplotlib.
    5. **Scikit-learn**: For machine learning and predictive analytics.
    """)

    # Operations Performed in Data Analysis
    st.subheader(":orange[Operations Performed in Data Analysis]")
    st.write("""
    Here are some of the common operations performed in data analysis:
    - **Data Cleaning**: Handling missing values, correcting inconsistencies.
    - **Exploratory Data Analysis (EDA)**: Summarizing main characteristics of data.
    - **Feature Engineering**: Creating or transforming variables.
    - **Data Visualization**: Creating graphs and charts to understand data.
    - **Statistical Analysis**: Drawing conclusions using statistical tests.
    """)

    # Common Commands in Pandas
    st.subheader(":orange[Common Pandas Commands]")
    st.write("Below are some common Pandas commands along with their explanation and outputs:")

    # Sample DataFrame for Demonstration
    data = {
        "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
        "Age": [25, 30, 35, 40, 22],
        "Salary": [50000, 60000, 70000, 80000, 45000]
    }
    df = pd.DataFrame(data)
    st.write("Sample Dataset:")
    st.write(df)
    col1, col2, col3 = st.columns(3)
    df = pd.DataFrame(data)
    # Column 1: Common Commands
    with col1:
        st.header("Common Pandas Commands")
        st.write("Below are some common Pandas commands along with their explanation and outputs:")
        st.write("Sample Dataset:")
        st.write(df)

        # Command 1: Viewing the first few rows of the dataset
        st.subheader("1. Viewing the First Few Rows")
        st.code("df.head()")
        st.write(df.head())

        # Command 2: Checking for missing values
        st.subheader("2. Checking for Missing Values")
        st.code("df.isnull().sum()")
        st.write(df.isnull().sum())

        # Command 3: Descriptive statistics
        st.subheader("3. Descriptive Statistics")
        st.code("df.describe()")
        st.write(df.describe())

    # Column 2: Data Cleaning and Transformation
    with col2:
        st.header("Data Cleaning and Transformation")

        # Handling missing values
        st.subheader("1. Handling Missing Values")
        st.code("df.fillna(value=0)")
        st.write(df.fillna(value=0))

        # Renaming columns
        st.subheader("2. Renaming Columns")
        st.code("df.rename(columns={'Salary': 'Income'}, inplace=True)")
        df.rename(columns={'Salary': 'Income'}, inplace=True)
        st.write(df)

        # Replacing values
        st.subheader("3. Replacing Values")
        st.code("df.replace(to_replace=50000, value=52000, inplace=True)")
        df.replace(to_replace=50000, value=52000, inplace=True)
        st.write(df)

        # Adding a new column
        st.subheader("4. Adding a New Column")
        st.code("df['Tax'] = df['Income'] * 0.2")
        df['Tax'] = df['Income'] * 0.2
        st.write(df)

    # Column 3: Data Aggregation
    with col3:
        st.header("Data Aggregation")

        # Grouping data
        st.subheader("1. Grouping and Aggregating")
        st.code("df.groupby('Age')['Income'].mean()")
        grouped_data = df.groupby('Age')['Income'].mean()
        st.write(grouped_data)

        # Aggregating multiple functions
        st.subheader("2. Aggregating with Multiple Functions")
        st.code("df.agg({'Income': ['sum', 'mean'], 'Tax': 'max'})")
        aggregated_data = df.agg({'Income': ['sum', 'mean'], 'Tax': 'max'})
        st.write(aggregated_data)

        # Cumulative sum
        st.subheader("3. Cumulative Sum")
        st.code("df['CumulativeIncome'] = df['Income'].cumsum()")
        df['CumulativeIncome'] = df['Income'].cumsum()
        st.write(df[['Name', 'Income', 'CumulativeIncome']])

        # Closing Note
        st.subheader("Summary")
        st.write("""
        In this section, we provided an introduction to data analysis, the libraries commonly used, and key Pandas operations with examples.
        These commands are fundamental and form the foundation for more advanced data analysis tasks.
        """)
if __name__ == "__main__":
    app()
