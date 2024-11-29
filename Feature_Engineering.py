import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import time

def upload_files():
    col1, col2, col4, col3 = st.columns([1, 1, 0.2, 1]) 
    
    df1, df2 = None, None 
    
    with col1:
        uploaded_file1 = st.file_uploader("Upload Excel File 1", type=["xlsx"], key="file1")
        
        if uploaded_file1 is not None:
            df1 = pd.read_excel(uploaded_file1)
            st.write("**:orange[DataSet 1 Overview]**")
            st.write(f"Total Rows: {df1.shape[0]} || Total Columns: {df1.shape[1]}")
            st.dataframe(df1.head(16))  

    with col2:
        uploaded_file2 = st.file_uploader("Upload Excel File 2", type=["xlsx"], key="file2")
        
        if uploaded_file2 is not None:
            df2 = pd.read_excel(uploaded_file2)
            st.write("**:orange[DataSet 2 Overview]**")
            st.write(f"Total Rows: {df2.shape[0]} || Total Columns: {df2.shape[1]}")
            st.dataframe(df2.head(16))  
        
    with col3:
        st.video("videos/Inner.mp4", autoplay=True, loop=True, muted=True)
        st.video("videos/Outer.mp4", autoplay=True, loop=True, muted=True)
        st.video("videos/Left.mp4", autoplay=True, loop=True, muted=True)
        
    return df1, df2

def app():
    st.title("COVID-19 Data Analysis with Feature Engineering & Heatmap")
    st.write('---')

    def stream_typing_animation(text):
   
        for char in text:
            yield char
            time.sleep(0.05)

# Main code
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("What is a Heatmap?"):
            st.write("### :orange[What is a Heatmap?]")
            text = (
                "A heatmap is a graphical representation of data where individual values are "
                "represented by color gradients, making it easy to identify patterns, correlations, "
                "and relationships in large datasets."
            )
            st.write_stream(stream_typing_animation(text))

    with col2:
        if st.button("What is Feature Engineering?"):
            st.write("### :orange[What is Feature Engineering?]")
            text = (
                "Feature engineering is the process of creating new input features or transforming "
                "existing ones to improve the performance of machine learning models or to enhance data analysis."
            )
            st.write_stream(stream_typing_animation(text))

    with col3:
        if st.button("Why Have We Chosen This Method?"):
            st.write("### :orange[Why Have We Chosen This Method?]")
            text = (
                "This approach combines feature engineering and heatmaps to reveal meaningful insights, "
                "highlight key relationships, and support data-driven decisions effectively, especially "
                "for public health analysis like COVID-19."
            )
            st.write_stream(stream_typing_animation(text))

    st.write('---')
        
    uploaded_file = st.file_uploader("Upload the COVID-19 dataset (CSV)", type=["csv"])
    
    if uploaded_file is not None:
        covid_data = pd.read_csv(uploaded_file)
        st.write("**Dataset Overview:**")
        st.dataframe(covid_data.head(16))

        # Feature Engineering
        st.write("### Performing Feature Engineering...")
        
        # Add derived metrics: Cases and Deaths per 100k population
        covid_data['Cases per 100k Population'] = (covid_data['Total Cases'] / covid_data['Population']) * 100000
        covid_data['Deaths per 100k Population'] = (covid_data['Deaths'] / covid_data['Population']) * 100000

        # Select only numeric columns for correlation
        numeric_columns = covid_data.select_dtypes(include=[np.number])  # Select only numeric data
        correlation_matrix = numeric_columns.corr()

        # Display results
        st.write("### Updated Dataset with New Features:")
        st.dataframe(covid_data.head())

        st.write("### Correlation Matrix:")
        st.write(correlation_matrix)

        # Generate and display heatmap
        st.write("### Correlation Heatmap:")
        plt.figure(figsize=(10, 6))
        sns.heatmap(
            correlation_matrix, 
            annot=True, 
            fmt=".2f", 
            cmap="coolwarm", 
            cbar=True,
            square=True, 
            linewidths=0.5,
            xticklabels=correlation_matrix.columns,
            yticklabels=correlation_matrix.columns
        )
        st.pyplot(plt)

        # Save the updated dataset
        st.download_button(
            label="Download Updated Dataset",
            data=covid_data.to_csv(index=False).encode('utf-8'),
            file_name="Updated_Covid_Data.csv",
            mime="text/csv",
        )

# Run the app
if __name__ == "__main__":
    app()
