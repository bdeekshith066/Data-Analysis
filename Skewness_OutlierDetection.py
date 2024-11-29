import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def app():
    st.title("Analysis of Skewness, Kurtosis, and Outliers (IQR)")

    uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])
    
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write("**Dataset Overview:**")
        st.dataframe(data.head(16))
        
        # Select only numeric columns
        numeric_data = data.select_dtypes(include=[np.number])

        # Calculate skewness and kurtosis
        st.write("### Skewness and Kurtosis:")
        skewness = numeric_data.skew()
        kurtosis = numeric_data.kurt()
        stats = pd.DataFrame({"Skewness": skewness, "Kurtosis": kurtosis})
        st.write(stats)

        # Descriptions and Conclusions for Skewness
        st.write("### Skewness Analysis:")
        st.write("""
        **Skewness** measures the asymmetry of a distribution:

        - **Highly positively skewed (Skewness > 1):**
          - *Total Cases (2.54), Active (5.64), Discharged (2.52), Deaths (3.86), Active Ratio (5.93), Population (1.92)*
          - These distributions are right-tailed, with most data points clustered at lower values.

        - **Moderately skewed (0 < Skewness ≤ 1):**
          - *Death Ratio (0.48)* shows slight asymmetry but is closer to symmetric.

        - **Negatively skewed:**
          - *Discharge Ratio (-0.63)* indicates a left-tailed distribution.
        """)

        # Descriptions and Conclusions for Kurtosis
        st.write("### Kurtosis Analysis:")
        st.write("""
        **Kurtosis** measures the "tailedness" of a distribution:

        - **Highly kurtotic (Kurtosis > 3):**
          - *Active (32.80), Deaths (17.26), Active Ratio (35.41)*
          - These columns show extreme outliers and peaked distributions.

        - **Close to normal (Kurtosis ≈ 3):**
          - *Death Ratio (0.96)* showing a near-normal distribution.

        - **Platykurtic (Kurtosis < 3):**
          - None of the columns show flat distributions.
        """)

        # Calculate IQR and identify outliers using IQR method
        Q1 = numeric_data.quantile(0.25)
        Q3 = numeric_data.quantile(0.75)
        IQR = Q3 - Q1

        # Calculate the lower and upper bounds for outliers
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        # Identify outliers (values outside the IQR bounds)
        outliers = (numeric_data < lower_bound) | (numeric_data > upper_bound)
        outlier_counts = outliers.sum()

        st.write("### Outliers Detection Using IQR:")
        st.write(f"Outliers detected in each column:")
        st.write(outlier_counts)

        st.write("### Histograms of Numerical Columns:")
        col1, col2 = st.columns(2)

        # Plot histograms for distributions in two columns
        with col1:
            for column in numeric_data.columns[:len(numeric_data.columns)//2]:
                plt.figure(figsize=(6, 4))
                sns.histplot(numeric_data[column], kde=True, bins=20, color='blue')
                plt.title(f"Distribution of {column}")
                plt.xlabel(column)
                plt.ylabel("Frequency")
                st.pyplot(plt)

        with col2:
            for column in numeric_data.columns[len(numeric_data.columns)//2:]: 
                plt.figure(figsize=(6, 4))
                sns.histplot(numeric_data[column], kde=True, bins=20, color='blue')
                plt.title(f"Distribution of {column}")
                plt.xlabel(column)
                plt.ylabel("Frequency")
                st.pyplot(plt)
                
        # Apply log transformation to skewed columns
        log_columns = ['Total Cases', 'Deaths', 'Population']
        for col in log_columns:
            if col in numeric_data.columns:
                numeric_data[f'log_{col}'] = np.log1p(numeric_data[col])  # log1p handles zero values.

        # Create Normal Boxplots
        st.write("### Normal Boxplots (Without Log Transformation)")
        plt.figure(figsize=(6, 4))
        sns.boxplot(data=numeric_data[['Total Cases', 'Active', 'Discharged', 'Deaths', 'Active Ratio', 'Discharge Ratio', 'Death Ratio', 'Population']], orient="h", palette="Set2")
        plt.title("Boxplot of Original Numerical Features")
        plt.xlabel("Features")
        plt.ylabel("Values")
        st.pyplot(plt)

        # Create Log-Transformed Boxplots
        st.write("### Outliers Detection with Log-Transformed Boxplots")
        plt.figure(figsize=(6, 4))
        sns.boxplot(data=numeric_data[['log_Total Cases', 'log_Deaths', 'log_Population']], orient="h", palette="Set2")
        plt.title("Boxplot of Log-Transformed Numerical Features")
        plt.xlabel("Features")
        plt.ylabel("Log-Transformed Values")
        st.pyplot(plt)

        # Descriptions and Conclusions for Outliers
        st.write("""
        **Outliers** are data points that significantly deviate from the rest of the dataset. They are commonly detected using boxplots.

        - **Boxplot Observations**:
          - **Normal Boxplots** show outliers based on the original values (without log transformation).
          - **Log-Transformed Boxplots** show outliers after applying the log transformation to values like *Total Cases*, *Deaths*, and *Population*.
          - The log transformation helps make extreme outliers more visible while compressing the scale of large values.
        """)

        # Save the dataset with skewness and kurtosis included
        stats_file = stats.reset_index().rename(columns={"index": "Feature"})
        csv_data = stats_file.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Skewness, Outliers and Kurtosis Report",
            data=csv_data,
            file_name="skewness_kurtosis_report.csv",
            mime="text/csv",
        )

if __name__ == "__main__":
    app()
