from logging import warning
import pandas
import numpy
import sklearn
import warnings
warnings.filterwarnings("ignore")



class Titanic_Pipe (pandas.DataFrame):
    def __init__ (self, csv_file, target = False, drop_columns = False , report_ = False , return_ = False):
        """initiating and read data
        Arg: 
        data = 'CSV' name (str)
        """
        assert type(csv_file) == str , "file name must be string"
        super (Titanic_Pipe,self).__init__()
        self.frame = pandas.read_csv(csv_file)
        self.preprocessed_ = pandas.DataFrame()
        self.report_= report_
        self.return_= return_
        self.target = target
        self.drop_columns = drop_columns

    def add_report (self, print_, text):
        """ add and print report"""
        if print_:
            print(text)
        else:
            pass

    def Data_Inputting (self, show_report = True , return_data = True):

        """ This class return a quick technical summary
        Arg:
        show_report : show current step 
        return_data = return dataframe """

        if (show_report ==True) and (return_data ==False or return_data ==True):
            self.add_report(True,"---> Step 1. 'Data Inputting' --- Technical Information ---")
            self.add_report(True, f"Data Set Shape = Data set Memory usage = {self.frame.shape}")
            self.add_report(True ,f"Data Set Memory Usage = {self.frame.memory_usage().sum()/1024**2} MB")
            self.add_report(True,f"Data Set index Type :'{type(self.frame.index)}")
            self.add_report(True,f"Data Set Columns Type:'{type(self.frame.columns[0])}")
            self.add_report(True,f"\nData columns 'Type'\n{self.frame.dtypes.value_counts()}")
            self.frame.describe(include='all')

            if return_data:
                return self.frame
            else:
                pass
        else:
            pass

    def Data_Analysis (self, show_report = True, return_data = True):

        """ Analyze the entire data set, Looking for Missing Values , Null and 0 
        Arg:
        
        """
        # Copy 
        self.preprocessed_ = self.frame.copy()

        #Dropping Selected Columns
        if self.drop_columns != False:
            self.frame.drop(self.drop_columns,axis = 1,  inplace=True)

        # Splitting data into data type
        col_number = self.frame.select_dtypes([numpy.number]).columns.to_list()
        col_str = self.frame.select_dtypes(['object']).columns.to_list()

        # Missing Values
        missing_ = self.frame.columns[self.frame.isna().any()].to_list()
        
        # Start step 2 
        if (show_report == True) and (return_data ==True or return_data == False):
            self.add_report(show_report,"\n---> Step 2. 'Data Analysis' --- Searching Missing Values ---")
            
            # Unique values
            if self.target != False:
                target_unique = self.frame[self.target].value_counts().to_dict()
                self.add_report(show_report,f"--> Target columns is {self.target}, Number of Classes {target_unique}")
     
            # fill_missing_values
            for col_ in missing_:
                if col_ in col_number:
                    #counting int | float 
                    num_missing = self.frame[col_].isna().sum()
                    self.add_report(show_report,f"--> The columns {col_} has {num_missing} missing values")
                    self.preprocessed_[col_] = self.preprocessed_[col_].fillna(self.frame[col_].mean(), inplace=True)
                
                if col_ in col_str:
                   #counting str
                   num_missing = self.frame[col_].isna().sum()
                   self.add_report(show_report,f"--> The columns {col_} has {num_missing} missing values")
                   self.preprocessed_[col_]  = self.preprocessed_[col_].fillna(self.frame[col_].mode()[0], inplace=True) 
            
            self.add_report(show_report,"--> Filling Nan Values with mean and mode")
            if return_data :
                return self.preprocessed_
        else:
            if return_data:
                return self.preprocessed_
            

    def next_step (self):
        """NExt step"""
        pass