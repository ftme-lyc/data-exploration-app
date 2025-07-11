import streamlit as st
import pandas as pd
from tab_text.logics import TextColumn

def display_tab_text_content(file_path=None,df=None):
    """
    --------------------
    Description
    --------------------
    -> display_tab_text_content (function): Function that will instantiate tab_text.logics.TextColumn class, save it into Streamlit session state and call its tab_text.logics.TextColumn.find_text_cols() method in order to find all text columns.
    Then it will display a Streamlit select box with the list of text columns found.
    Once the user select a text column from the select box, it will call the tab_text.logics.TextColumn.set_data() method in order to compute all the information to be displayed.
    Then it will display a Streamlit Expander container with the following contents:
    - the results of tab_text.logics.TextColumn.get_summary() as a Streamlit Table
    - the graph from tab_text.logics.TextColumn.histogram using Streamlit.altair_chart()
    - the results of tab_text.logics.TextColumn.frequent using Streamlit.write
 
    --------------------
    Parameters
    --------------------
    -> file_path (str): File path to uploaded CSV file (optional)
    -> df (pd.DataFrame): Loaded dataframe (optional)

    --------------------
    Returns
    --------------------
    -> None

    """
    # Initialize TextColumn instance
    text_column = TextColumn(file_path=file_path, df=df)
    text_column.find_text_cols()
    st.session_state["text_column"] = text_column

    if not text_column.cols_list:
        st.write("No text columns found in the dataset.")
        return

    # Select a text column to analyze
    selected_col = st.selectbox("Which text column do you want to explore", options=text_column.cols_list)

    # Process the selected column
    text_column.set_data(selected_col)

    # Display summary, histogram, and frequent values
    with st.expander("Text Column", expanded=True):
        st.table(text_column.get_summary())  # Display summary
        st.write("Bar Chart")
        st.altair_chart(text_column.set_barchart())  # Display barchart
        st.write("Most Frequent Values")
        st.write(text_column.set_frequent())  # Display most frequent values