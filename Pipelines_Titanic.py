import pandas 
import numpy 
import sklearn 


class Titanic_Pipe (pandas.DataFrame):
    def __init__ (self, csv_file):
        """initiating and read data
        Arg: 
        data = 'CSV' name (str)


        """
        assert type(csv_file) == str , "file name must be string"
        super (Titanic_Pipe,self).__init__()
        self.csv_file= csv_file
        self.frame = pandas.read_csv(self.csv_file)


    def add_report (self, print_, text):
        """ add and print report"""
        if print_:
            print(text) 
        else:
            pass

    def Data_Inputting (self, show_report , return_data):
        
        """ This class return a quick technical summary
        Arg:
        show_report : show current step 
        return_data = return dataframe """

        if (show_report ==True) and (return_data ==False | return_data ==True):
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



  
