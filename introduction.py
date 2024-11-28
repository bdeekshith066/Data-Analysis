import streamlit as st
import pandas as pd

def app():
    st.title("Interactive Data Analysis and Cleaning")

    st.subheader(":orange[Upload Your Dataset]")
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        # Normalize column names
        df.columns = df.columns.str.strip().str.title()  # Normalize column names
        df.columns = df.columns.str.replace(' ', '_')  # Replace spaces with underscores
        
        st.write("Uploaded Dataset:")
        st.write(df)
        
        st.subheader(":orange[Dataset Overview]")
        st.write("### 1. First Five Rows of the Dataset")
        st.write(df.head())

        st.write("### 2. Dataset Shape")
        st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
        
        st.write("### 3. Dataset Columns")
        st.write(df.columns.tolist())

        st.write("### 4. Missing Values in Each Column")
        st.write(df.isnull().sum())

        # Data Cleaning Options
        st.subheader(":orange[Data Cleaning Options]")
        
        # Fill Missing Values
        if st.button("Fill Missing Values with 0"):
            df.fillna(0, inplace=True)
            st.write("Missing values filled with 0.")
            st.write(df)

        # Rename Columns
        if st.button("Rename Columns to Title Case"):
            df.columns = df.columns.str.title()
            st.write("Renamed Columns:")
            st.write(df.columns.tolist())
        
        # Replacing Values
        replace_value = st.text_input("Enter a Value to Replace (Optional)")
        new_value = st.text_input("Enter the New Value to Replace With")
        if st.button("Replace Values"):
            if replace_value and new_value:
                try:
                    # Handle numbers as well as strings
                    if replace_value.isdigit():
                        replace_value = int(replace_value)
                    if new_value.isdigit():
                        new_value = int(new_value)
                    
                    # Replace the values in the dataframe
                    df.replace(to_replace=replace_value, value=new_value, inplace=True)
                    st.write(f"Replaced '{replace_value}' with '{new_value}' in the dataset.")
                    st.write(df)
                except ValueError:
                    st.error("Please ensure that the values entered are valid numbers or strings.")
        
        # Adding a New Column
        if st.button("Add Population Density (Cases/Population) Column"):
            if 'Total_Cases' in df.columns and 'Population' in df.columns:
                df['Population_Density'] = df['Total_Cases'] / df['Population']
                st.write("Added Population Density Column:")
                st.write(df)

        # Descriptive Statistics
        st.subheader(":orange[Descriptive Statistics]")
        st.write("Summary Statistics of Numerical Columns:")
        st.write(df.describe())

        # Data Aggregation
        st.subheader(":orange[Data Aggregation]")
        st.write("Aggregate Total Cases and Deaths:")
        if 'Total_Cases' in df.columns and 'Deaths' in df.columns:
            aggregate_data = df.agg({'Total_Cases': ['sum', 'mean'], 'Deaths': ['sum', 'mean']})
            st.write(aggregate_data)
        else:
            st.error("Required columns ('Total_Cases', 'Deaths') are missing.")
        
        # Visualization (Optional Feature)
        st.subheader(":orange[Visualization Options]")
        if st.checkbox("Show Total Cases by State/UT"):
            st.bar_chart(df.set_index("State/Uts")["Total_Cases"])

        st.subheader("Summary")
        st.write("""
        This interactive app allows you to upload your dataset, view a summary, clean data, and perform basic aggregation and visualization tasks.
        Explore the options and gain insights into your dataset!
        """)

if __name__ == "__main__":
    app()
