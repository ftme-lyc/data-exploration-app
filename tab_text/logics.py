import pandas as pd
import altair as alt
import streamlit as st

class TextColumn:
    """
    --------------------
    Description
    --------------------
    -> TextColumn (class): Class that manages a column from a dataframe of text data type

    --------------------
    Attributes
    --------------------
    -> file_path (str): Path to the uploaded CSV file (optional)
    -> df (pd.Dataframe): Pandas dataframe (optional)
    -> cols_list (list): List of columns names of dataset that are text type (default set to empty list)
    -> serie (pd.Series): Pandas serie where the content of a column has been loaded (default set to None)
    -> n_unique (int): Number of unique value of a serie (default set to None)
    -> n_missing (int): Number of missing values of a serie (default set to None)
    -> n_empty (int): Number of times a serie has empty value (default set to None)
    -> n_mode (int): Mode value of a serie (default set to None)
    -> n_space (int): Number of times a serie has only space characters (default set to None)
    -> n_lower (int): Number of times a serie has only lowercase characters (default set to None)
    -> n_upper (int): Number of times a serie has only uppercase characters (default set to None)
    -> n_alpha (int): Number of times a serie has only alphabetical characters (default set to None)
    -> n_digit (int): Number of times a serie has only digit characters (default set to None)
    -> barchart (alt.Chart): Altair barchart displaying the count for each value of a serie (default set to empty)
    -> frequent (pd.DataFrame): Datframe containing the most frequest value of a serie (default set to empty)

    """
    def __init__(self, file_path=None, df=None):
        self.file_path = file_path
        self.df = pd.read_csv(file_path) if file_path else df
        self.cols_list = []
        self.serie = None
        self.n_unique = None
        self.n_missing = None
        self.n_empty  = None
        self.n_mode = None
        self.n_space = None
        self.n_lower = None
        self.n_upper = None
        self.n_alpha = None
        self.n_digit = None
        self.barchart = alt.Chart()
        self.frequent = pd.DataFrame(columns=['value', 'occurrence', 'percentage'])
        
    def find_text_cols(self):
        """
        --------------------
        Description
        --------------------
        -> find_text_cols (method): Class method that will load the uploaded CSV file as Pandas DataFrame and store it as attribute (self.df) if it hasn't been provided before.
        Then it will find all columns of text data type and store the results in the relevant attribute (self.cols_list).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if self.df is None and self.file_path:
            self.df = pd.read_csv(self.file_path)
        
        self.cols_list = [col for col in self.df.columns if self.df[col].dtype == 'object']

    def set_data(self, col_name):
        """
        --------------------
        Description
        --------------------
        --------------------
        Description
        --------------------
        -> set_data (method): Class method that sets the self.serie attribute with the relevant column from the dataframe and then computes all requested information from self.serie to be displayed in the Text section of Streamlit app 

        --------------------
        Parameters
        --------------------
        -> col_name (str): Name of the text column to be analysed

        --------------------
        Returns
        --------------------
        -> None
        """
        self.reset_attributes()
        self.serie = self.df[col_name].astype(str)  # Convert to string for consistent text handling
        self.set_unique()
        self.set_missing()
        self.set_empty()
        self.set_mode()
        self.set_whitespace()
        self.set_lowercase()
        self.set_uppercase()
        self.set_alphabet()
        self.set_digit()
        self.set_barchart()
        self.set_frequent()

    def reset_attributes(self):
        """Resets all calculated attributes."""
        self.cols_list = []
        self.serie = None
        self.n_unique = None
        self.n_missing = None
        self.n_empty = None
        self.n_mode = None
        self.n_space = None
        self.n_lower = None
        self.n_upper = None
        self.n_alpha = None
        self.n_digit = None
        self.barchart = alt.Chart()
        self.frequent = pd.DataFrame(columns=['value', 'occurrence', 'percentage'])

    def convert_serie_to_text(self):
        """
        --------------------
        Description
        --------------------
        -> convert_serie_to_text (method): Class method that convert a Pandas Series to text data type and store the results in the relevant attribute (self.serie).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if not self.serie.empty:
            self.serie = self.serie.astype(str)

    def is_serie_none(self):
        """
        --------------------
        Description
        --------------------
        -> is_serie_none (method): Class method that checks if self.serie is empty or none 

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> (bool): Flag stating if the serie is empty or not

        """
        return self.serie is None
        

    def set_unique(self):
        """
        --------------------
        Description
        --------------------
        -> set_unique (method): Class method that computes the number of unique value of a serie and store the results in the relevant attribute(self.n_unique).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if self.serie is not None:
            self.n_unique = self.serie.nunique()
        

    def set_missing(self):
        """
        --------------------
        Description
        --------------------
        -> set_missing (method): Class method that computes the number of missing value of a serie and store the results in the relevant attribute(self.n_missing).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if self.serie is not None:
            self.n_missing = self.serie.isnull().sum()        

    def set_empty(self):
        """
        --------------------
        Description
        --------------------
        -> set_empty (method): Class method that computes the number of times a serie has empty value and store the results in the relevant attribute(self.n_empty).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if self.serie is not None:
            self.n_empty = (self.serie == "").sum()        

    def set_mode(self):
        """
        --------------------
        Description
        --------------------
        -> set_mode (method): Class method that computes the mode value of a serie and store the results in the relevant attribute(self.n_mode).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if self.serie is not None:
            self.n_mode = self.serie.mode().iloc[0] if not self.serie.mode().empty else None        

    def set_whitespace(self):
        """
        --------------------
        Description
        --------------------
        -> set_whitespace (method): Class method that computes the number of times a serie has only space characters and store the results in the relevant attribute(self.n_space).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if self.serie is not None:
            self.n_space = (self.serie.str.isspace()).sum()        

    def set_lowercase(self):
        """
        --------------------
        Description
        --------------------
        -> set_lowercase (method): Class method that computes the number of times a serie has only lowercase characters and store the results in the relevant attribute(self.n_lower).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if self.serie is not None:
            self.n_lower = self.serie.str.islower().sum()        

    def set_uppercase(self):
        """
        --------------------
        Description
        --------------------
        -> set_uppercase (method): Class method that computes the number of times a serie has only uppercase characters and store the results in the relevant attribute(self.n_upper).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if self.serie is not None:
            self.n_upper = self.serie.str.isupper().sum()        
    
    def set_alphabet(self):
        """
        --------------------
        Description
        --------------------
        -> set_alphabet (method): Class method that computes the number of times a serie has only alphabetical characters and store the results in the relevant attribute(self.n_alpha).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if self.serie is not None:
            self.n_alpha = self.serie.str.isalpha().sum()        

    def set_digit(self):
        """
        --------------------
        Description
        --------------------
        -> set_digit (method): Class method that computes the number of times a serie has only digit characters and store the results in the relevant attribute(self.n_digit).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if self.serie is not None:
            self.n_digit = self.serie.str.isdigit().sum()        

    def set_barchart(self):  
        """
        --------------------
        Description
        --------------------
        -> set_barchart (method): Class method that computes the Altair barchart displaying the count for each value of a serie and store the results in the relevant attribute(self.barchart).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if not self.is_serie_none():
            self.barchart = alt.Chart(self.serie.reset_index()).mark_bar().encode(
                x=alt.X(self.serie.name),
                y=alt.Y('count()', title='Count of Records')).properties(width=600,height=400)
        return self.barchart
    
    def set_frequent(self, end=20):
        """
        --------------------
        Description
        --------------------
        -> set_frequent (method): Class method that computes the Dataframe containing the most frequest value of a serie and store the results in the relevant attribute(self.frequent).

        --------------------
        Parameters
        --------------------
        -> end (int):
            Parameter indicating the maximum number of values to be displayed

        --------------------
        Returns
        --------------------
        -> None

        """
        if self.serie is not None:
            freq = self.serie.value_counts().head(end)
            self.frequent = pd.DataFrame({'value':freq.index, 'occurrence':freq.values, 'percentage':(freq.values/len(self.serie))*100})
            return self.frequent  

    def get_summary(self):
        """
        --------------------
        Description
        --------------------
        -> get_summary_df (method): Class method that formats all requested information from self.serie to be displayed in the Overall section of Streamlit app as a Pandas dataframe with 2 columns: Description and Value

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> (pd.DataFrame): Formatted dataframe to be displayed on the Streamlit app

        """
        summary_data = {
            "Number of Unique Values": self.n_unique,
            "Number of Rows with Missing Values": self.n_missing,
            "Number of Empty Rows": self.n_empty,
            "Number of Rows with Only Whitespace": self.n_space,
            "Number of Rows with Only Lowercase": self.n_lower,
            "Number of Rows with Only Uppercase": self.n_upper,
            "Number of Rows with Only Alphabet": self.n_alpha,
            "Number of Rows with Only Digits": self.n_digit,
            "Mode Value": self.n_mode
        }
        return pd.DataFrame(list(summary_data.items()), columns=["Description", "Value"])  
