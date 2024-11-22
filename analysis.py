import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for seaborn
sns.set(style="whitegrid")

# Define the app function
def app():
    # Title and file uploader
    st.title("Dataset Analysis - Multiple Graphs")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        # Load the dataset
        df = pd.read_csv(uploaded_file)
        
        # Display an overview of the dataset
        st.write("## Dataset Overview")
        st.write(f"Total Rows: {df.shape[0]}")
        st.write(f"Total Columns: {df.shape[1]}")
        st.write(df.head())  # Display the first few rows

        # Create 3x3 grid of subplots
        fig, axes = plt.subplots(3, 3, figsize=(15, 15))
        fig.tight_layout(pad=5.0)

        # Plot 1: Histogram of the first numerical column
        sns.histplot(df[df.columns[0]], ax=axes[0, 0], kde=True)
        axes[0, 0].set_title(f"Histogram of {df.columns[0]}")

        # Plot 2: Histogram of the second numerical column
        sns.histplot(df[df.columns[1]], ax=axes[0, 1], kde=True)
        axes[0, 1].set_title(f"Histogram of {df.columns[1]}")

        # Plot 3: Scatter plot of the first two numerical columns
        if df.shape[1] > 1:
            sns.scatterplot(data=df, x=df.columns[0], y=df.columns[1], ax=axes[0, 2])
            axes[0, 2].set_title(f"Scatter Plot of {df.columns[0]} vs {df.columns[1]}")

        # Plot 4: Box plot of the first numerical column
        sns.boxplot(x=df[df.columns[0]], ax=axes[1, 0])
        axes[1, 0].set_title(f"Box Plot of {df.columns[0]}")

        # Plot 5: Correlation heatmap of the dataset
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=axes[1, 1])
        axes[1, 1].set_title("Correlation Heatmap")

        # Plot 6: Bar plot of the first categorical column
        if len(df.select_dtypes(include=['object']).columns) > 0:
            sns.countplot(x=df.select_dtypes(include=['object']).columns[0], data=df, ax=axes[1, 2])
            axes[1, 2].set_title(f"Count Plot of {df.select_dtypes(include=['object']).columns[0]}")

        # Plot 7: Line plot of the first numerical column
        sns.lineplot(data=df[df.columns[0]], ax=axes[2, 0])
        axes[2, 0].set_title(f"Line Plot of {df.columns[0]}")

        # Plot 8: KDE plot of the second numerical column
        sns.kdeplot(data=df[df.columns[1]], ax=axes[2, 1], fill=True)
        axes[2, 1].set_title(f"KDE Plot of {df.columns[1]}")

        # Plot 9: Violin plot of the first numerical column
        sns.violinplot(x=df[df.columns[0]], ax=axes[2, 2])
        axes[2, 2].set_title(f"Violin Plot of {df.columns[0]}")

        # Display all graphs
        st.pyplot(fig)
    else:
        st.write("Please upload a dataset to view the visualizations.")

# Call the app function
if __name__ == "__main__":
    app()
