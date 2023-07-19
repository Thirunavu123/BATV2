import pandas as pd
import streamlit as st

def main():
    st.title("Excel File Uploader")

    # File uploader widget
    uploaded_file = st.file_uploader("Upload Excel file2", type=["xlsx", "xls"])

    if uploaded_file is not None:
        try:
            # Read the Excel file
            df = pd.read_excel(uploaded_file)

            # Display the contents of the Excel file
            st.write("Excel file contents:")
            st.dataframe(df)
        except Exception as e:
            st.error("Error: Unable to load the Excel file.")
            st.error(str(e))

if __name__ == "__main__":
    main()
