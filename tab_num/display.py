import streamlit as st

from tab_num.logics import NumericColumn

def display_tab_num_content(file_path=None, df=None):
    if df is None:
        st.warning("No dataset loaded.")
        return
    num_col = NumericColumn(file_path=file_path, df=df)
    num_col.find_num_cols()
    col_name = st.selectbox("Which numeric column do you want to explore", num_col.cols_list)

    if col_name:
        num_col.set_data(col_name)
        with st.expander("Column Summary", expanded=True):
            st.write('Numeric Column')
            st.table(num_col.get_summary())
        
            # Display histogram
            st.write('Histogram')
            st.altair_chart(num_col.set_histogram(), use_container_width=True)
        
            # Display frequent values
            st.write('Most Frequent Values')
            st.write(num_col.set_frequent())

    """
    --------------------
    Description
    --------------------
    -> display_tab_num_content (function): Function that will instantiate tab_num.logics.NumericColumn class, save it into Streamlit session state and call its tab_num.logics.NumericColumn.find_num_cols() method in order to find all numeric columns.
    Then it will display a Streamlit select box with the list of numeric columns found.
    Once the user select a numeric column from the select box, it will call the tab_num.logics.NumericColumn.set_data() method in order to compute all the information to be displayed.
    Then it will display a Streamlit Expander container with the following contents:
    - the results of tab_num.logics.NumericColumn.get_summary() as a Streamlit Table
    - the graph from tab_num.logics.NumericColumn.histogram using Streamlit.altair_chart()
    - the results of tab_num.logics.NumericColumn.frequent using Streamlit.write
 
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
    