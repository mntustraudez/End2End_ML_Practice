import pandas 
import numpy 
import sklearn 


class Titanic_Pipe (pandas.DataFrame):
    def __init__ (self, csv_file):
        """initiating and read data
        Arg: 
        data = 'CSV' name (str)


        """
        assert csv_file == str , "file name must be string"
        self.csv_file= csv_file


    def add_report (self, text, print_ = False):
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
        pass


Titanic_Pipe(7897).Data_Inputting()


    
