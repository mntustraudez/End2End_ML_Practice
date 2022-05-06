from Pipelines_Titanic import Titanic_Pipe
import pandas


data_name = r"C:\Users\Marvin Garcia\Desktop\end_to_end_titanic_ml\data\train.csv"
drop_ = ['PassengerId','Name','Ticket','Cabin']

Starting = Titanic_Pipe(data_name, drop_columns= drop_)
Starting.Data_Analysis(True,True)