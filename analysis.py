import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

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

        # Create 3x3 grid of subplots with increased figure size
        fig, axes = plt.subplots(3, 3, figsize=(18, 18))
        fig.tight_layout(pad=6.0)  # Increase padding for better spacing

        # Plot 1: Histogram of the first numerical column
        sns.histplot(df[df.columns[0]], ax=axes[0, 0], kde=True)
        axes[0, 0].set_title(f"Histogram of {df.columns[0]}")
        axes[0, 0].set_xlabel(df.columns[0])
        axes[0, 0].set_ylabel("Frequency")

        # Plot 2: Histogram of the second numerical column
        sns.histplot(df[df.columns[1]], ax=axes[0, 1], kde=True)
        axes[0, 1].set_title(f"Histogram of {df.columns[1]}")
        axes[0, 1].set_xlabel(df.columns[1])
        axes[0, 1].set_ylabel("Frequency")

        # Plot 3: Scatter plot of the first two numerical columns
        if df.shape[1] > 1:
            sns.scatterplot(data=df, x=df.columns[0], y=df.columns[1], ax=axes[0, 2])
            axes[0, 2].set_title(f"Scatter Plot of {df.columns[0]} vs {df.columns[1]}")
            axes[0, 2].set_xlabel(df.columns[0])
            axes[0, 2].set_ylabel(df.columns[1])

        # Plot 4: Box plot of the first numerical column
        sns.boxplot(x=df[df.columns[0]], ax=axes[1, 0])
        axes[1, 0].set_title(f"Box Plot of {df.columns[0]}")
        axes[1, 0].set_xlabel(df.columns[0])

        # Plot 5: Correlation heatmap of the dataset
        numeric_df = df.select_dtypes(include=['float64', 'int64'])
        if not numeric_df.empty:
            sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=axes[1, 1])
            axes[1, 1].set_title("Correlation Heatmap")
        else:
            axes[1, 1].text(0.5, 0.5, "No numeric data for correlation", ha='center', va='center', fontsize=12)
            axes[1, 1].set_title("Correlation Heatmap (No Data)")

        # Plot 6: Bar plot of the first categorical column
        categorical_cols = df.select_dtypes(include=['object']).columns
        if len(categorical_cols) > 0:
            sns.countplot(x=df[categorical_cols[0]], ax=axes[1, 2])
            axes[1, 2].set_title(f"Count Plot of {categorical_cols[0]}")
            axes[1, 2].set_xlabel(categorical_cols[0])
            axes[1, 2].set_ylabel("Count")

        # Plot 7: Line plot of the first numerical column
        sns.lineplot(data=df[df.columns[0]], ax=axes[2, 0])
        axes[2, 0].set_title(f"Line Plot of {df.columns[0]}")
        axes[2, 0].set_xlabel("Index")
        axes[2, 0].set_ylabel(df.columns[0])

        # Plot 8: KDE Plot
        if len(numeric_df.columns) > 1:
            second_numeric_column = numeric_df.columns[1]
            sns.kdeplot(data=df[second_numeric_column], ax=axes[2, 1], fill=True)
            axes[2, 1].set_title(f"KDE Plot of {second_numeric_column}")
            axes[2, 1].set_xlabel(second_numeric_column)
            axes[2, 1].set_ylabel("Density")
        else:
            axes[2, 1].text(0.5, 0.5, "No numeric data available for KDE Plot", ha='center', va='center', fontsize=12)
            axes[2, 1].set_title("KDE Plot (No Data)")

        # Plot 9: Violin plot of the first numerical column
        sns.violinplot(x=df[df.columns[0]], ax=axes[2, 2])
        axes[2, 2].set_title(f"Violin Plot of {df.columns[0]}")
        axes[2, 2].set_xlabel(df.columns[0])

        # Display all graphs
        st.pyplot(fig)
    else:
        st.write("Please upload a dataset to view the visualizations.")

    def stream_typing_animation(text):
    
        for char in text:
            yield char
            time.sleep(0.02)

# Content descriptions
    contents = [
        "### Histogram (Plots 1 & 2)\n\n**Purpose:** Show the distribution of the first two numerical columns.\n\n**Implementation:**\n```python\nsns.histplot(df[df.columns[0]], ax=axes[0, 0], kde=True)\n```\n\n**Why?**\nHistograms reveal the frequency distribution of data, and the KDE (Kernel Density Estimate) curve provides insights into the data's underlying probability density.",

        "### Scatter Plot (Plot 3)\n\n**Purpose:** Visualize the relationship between the first two numerical columns.\n\n**Implementation:**\n```python\nsns.scatterplot(data=df, x=df.columns[0], y=df.columns[1], ax=axes[0, 2])\n```\n\n**Why?**\nScatter plots help identify correlations or patterns, such as clustering or trends between two variables.",

        "### Box Plot (Plot 4)\n\n**Purpose:** Highlight the distribution, median, and outliers of the first numerical column.\n\n**Implementation:**\n```python\nsns.boxplot(x=df[df.columns[0]], ax=axes[1, 0])\n```\n\n**Why?**\nBox plots are excellent for spotting anomalies (outliers) and understanding data spread.",

        "### Correlation Heatmap (Plot 5)\n\n**Purpose:** Display pairwise correlations between numerical columns.\n\n**Implementation:**\n```python\nsns.heatmap(numeric_df.corr(), annot=True, cmap=\"coolwarm\", ax=axes[1, 1])\n```\n\n**Why?**\nCorrelation matrices show relationships between variables, helping identify dependencies or redundancies.",

        "### Count Plot (Plot 6)\n\n**Purpose:** Count occurrences of each category in the first categorical column.\n\n**Implementation:**\n```python\nsns.countplot(x=df[categorical_cols[0]], ax=axes[1, 2])\n```\n\n**Why?**\nCount plots provide insights into categorical data distributions, aiding in spotting dominant categories.",

        "### Line Plot (Plot 7)\n\n**Purpose:** Show trends or patterns in the first numerical column over indices.\n\n**Implementation:**\n```python\nsns.lineplot(data=df[df.columns[0]], ax=axes[2, 0])\n```\n\n**Why?**\nLine plots highlight time-series trends or index-based patterns.",

        "### KDE Plot (Plot 8)\n\n**Purpose:** Display the probability density function of the second numerical column.\n\n**Implementation:**\n```python\nsns.kdeplot(data=df[second_numeric_column], ax=axes[2, 1], fill=True)\n```\n\n**Why?**\nKDE plots smooth out histograms, offering a continuous view of data density.",

        "### Violin Plot (Plot 9)\n\n**Purpose:** Combine box plots and KDE plots for the first numerical column.\n\n**Implementation:**\n```python\nsns.violinplot(x=df[df.columns[0]], ax=axes[2, 2])\n```\n\n**Why?**\nViolin plots are useful for understanding data distribution and variability at a glance."
    ]
    rows = [st.columns(3) for _ in range(3)]

    # Place buttons and write_stream in the grid
    plot_names = [
    "Histogram Plot",
    "Scatter Plot",
    "Box Plot",
    "Correlation Heatmap",
    "Count Plot",
    "Line Plot",
    "KDE Plot",
    "Violin Plot"
]

    for idx, content in enumerate(contents):
        row_idx, col_idx = divmod(idx, 3)
        col = rows[row_idx][col_idx]
        with col:
            if st.button(f"Show {plot_names[idx]}"):
                st.write_stream(stream_typing_animation(content))

# Call the app function
if __name__ == "__main__":
    app()
