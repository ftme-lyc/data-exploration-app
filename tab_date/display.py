import streamlit as st

from tab_date.logics import DateColumn

def display_tab_date_content(file_path=None, df=None, key=None):
    if df is None:
        st.warning("No dataset loaded.")
        return
    date_col = DateColumn(file_path=file_path, df=df)
    date_col.find_date_cols()
    col_name = st.selectbox("Which numeric column do you want to explore", date_col.cols_list, key=key)
    
    if col_name:
        date_col.set_data(col_name)
        with st.expander("Column Summary", expanded=True):
            st.write('Date Column')
            st.table(date_col.get_summary())
        
            # Display Bar Chart
            st.write('Bar Chart')
            st.altair_chart(date_col.set_barchart())
        
            # Display frequent values
            st.write('Most Frequent Values')
            st.write(date_col.set_frequent())
    """
    --------------------
    Description
    --------------------
    -> display_tab_date_content (function): Function that will instantiate tab_date.logics.DateColumn class, save it into Streamlit session state and call its tab_date.logics.DateColumn.find_date_cols() method in order to find all datetime columns.
    Then it will display a Streamlit select box with the list of datetime columns found.
    Once the user select a datetime column from the select box, it will call the tab_date.logics.DateColumn.set_data() method in order to compute all the information to be displayed.
    Then it will display a Streamlit Expander container with the following contents:
    - the results of tab_date.logics.DateColumn.get_summary() as a Streamlit Table
    - the graph from tab_date.logics.DateColumn.histogram using Streamlit.altair_chart()
    - the results of tab_date.logics.DateColumn.frequent using Streamlit.write
 
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
    