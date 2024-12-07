import streamlit as st
import pandas as pd

def upload_files():
    col1, col2, col4, col3 = st.columns([1, 1, 0.2, 1])  
    
    df1, df2 = None, None  # Initialize as None
    
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
    st.title("Walkthrough of Various Data Analysis Operations")
    
    # File upload and display overview in the same column
    df1, df2 = upload_files()
    
    # Proceed with operations if both datasets are uploaded
    if df1 is not None and df2 is not None:
        st.write("### Select Data Operation")
        
        # Operations selection after files are uploaded
        operation = st.selectbox("Select Operation", ["Concatenate", "Merge", "Union", "Join", "Intersection"])
        
        if operation == "Concatenate":
            axis = st.selectbox("Select Axis", ["0 (Vertical)", "1 (Horizontal)"])
            axis = 0 if axis == "0 (Vertical)" else 1
            st.write(f"Concatenating along axis {axis}")

            # Check for duplicate column names if concatenating horizontally
            if axis == 1:  # Horizontal Concatenation
                # Check for duplicate column names
                common_columns = df1.columns.intersection(df2.columns).tolist()
                if common_columns:
                    # Add suffix to columns with the same name in both dataframes
                    df1 = df1.rename(columns={col: f"{col}_df1" for col in common_columns})
                    df2 = df2.rename(columns={col: f"{col}_df2" for col in common_columns})
                    st.warning(f"Duplicate columns found: {common_columns}. Suffixes added to make column names unique.")
                
                # Perform the horizontal concatenation after renaming duplicate columns
                result = pd.concat([df1, df2], axis=axis)
                st.write("### Result of Horizontal Concatenation:")
                st.dataframe(result)

            elif axis == 0:  # Vertical Concatenation
                # Perform vertical concatenation
                result = pd.concat([df1, df2], axis=axis)
                st.write("### Result of Vertical Concatenation:")
                st.dataframe(result)

        elif operation == "Merge":
            st.write("### Merge Operation: You need at least one common column to merge.")
            how = st.selectbox("Select Join Type", ["inner", "outer", "left", "right"])
            on_column = st.text_input("Enter common column name to merge on (e.g., 'ID')")
            
            if on_column:
                try:
                    result = pd.merge(df1, df2, how=how, on=on_column)
                    st.write("### Result of Merge:")
                    st.dataframe(result)
                except KeyError:
                    st.error(f"Column '{on_column}' not found in both dataframes. Please provide valid column names.")
            else:
                st.error("Please enter a column to merge on.")

        elif operation == "Union":
            st.write("### Union Operation: Combines both dataframes with the same columns, removing duplicates.")
            try:
                result = pd.concat([df1, df2]).drop_duplicates()
                st.write("### Result of Union:")
                st.dataframe(result)
            except Exception as e:
                st.error(f"Error during Union operation: {str(e)}")

        elif operation == "Join":
            st.write("### Join Operation: You need at least one common index to join.")
            how = st.selectbox("Select Join Type", ["inner", "outer", "left", "right"])
            suffix_left = st.text_input("Enter suffix for overlapping columns in the first dataframe (default: '_x')", value="_x")
            suffix_right = st.text_input("Enter suffix for overlapping columns in the second dataframe (default: '_y')", value="_y")

            try:
                result = df1.join(df2, how=how, lsuffix=suffix_left, rsuffix=suffix_right)
                st.write("### Result of Join:")
                st.dataframe(result)
            except Exception as e:
                st.error(f"Error during Join operation: {str(e)}")

        elif operation == "Intersection":
            st.write("### Intersection Operation: Returns only the rows with common index and columns in both dataframes.")
            try:
                result = pd.merge(df1, df2, how="inner")
                st.write("### Result of Intersection:")
                st.dataframe(result)
            except Exception as e:
                st.error(f"Error during Intersection operation: {str(e)}")

    else:
        st.warning("Please upload both files to proceed with operations.")

if __name__ == "__main__":
    app()
