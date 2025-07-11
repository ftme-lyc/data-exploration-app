import streamlit as st

from tab_df.logics import Dataset

def display_tab_df_content(file_path):
    """
    --------------------
    Description
    --------------------
    -> display_overall_df (function): Function that will instantiate tab_df.logics.Dataset class, save it into Streamlit session state and call its tab_df.logics.Dataset.set_data() method in order to compute all information to be displayed.
    Then it will display a Streamlit Expander container with the following contents:
    1. the results of tab_df.logics.Dataset.get_summary() as a Streamlit Table
    2. the results of tab_df.logics.Dataset.table using Streamlit.write()
    Finally it will display a second Streamlit Expander container with a slider to select the number of rows to be displayed and a radio button to select the method (head, tail, sample).
    According to the values selected on the slider and radio button, display the subset of the dataframe accordingly using Streamlit.dataframe
    
    --------------------
    Parameters
    --------------------
    -> file_path (str): File path to uploaded CSV file

    --------------------
    Returns
    --------------------
    -> None
    
    """
    # Initialise Dataset object
    if file_path is None or file_path == '':
        print('No file uploaded')
        return
    else:    
        dataset = Dataset(file_path)
        
        if dataset is None:
            print('No file uploaded')
            return
        else:
            dataset.set_data()
            st.session_state['dataset'] = dataset.df
    
            with st.expander('Dataframe', expanded=True):
                st.table(dataset.get_summary())
                
            with st.expander('Columns', expanded=True):
                st.table(dataset.table)

            with st.expander('Explore Dataframe', expanded=True):
                if dataset.n_rows < 5:
                    min_rows = 1
                    max_rows = dataset.n_rows
                elif dataset.n_rows < 50:
                    min_rows = 5
                    max_rows = dataset.n_rows
                else:
                    min_rows = 5
                    max_rows = 50
                    
                    
                rows = st.slider('Select the Number fo rows to be displayed', min_rows, max_rows, step=1)
                method = st.radio('Exploration Method', ['Head', 'Tail', 'Sample'])
                if method == 'Head':
                    st.dataframe(dataset.get_head(rows))
                elif method == 'Tail':
                    st.dataframe(dataset.get_tail(rows))
                else:
                    st.dataframe(dataset.get_sample(rows))