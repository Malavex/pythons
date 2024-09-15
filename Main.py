import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category,get_date,get_description
import matplotlib.pyplot as plt

class CSV:
    CSV_file="finance_data.csv"
    Columns=["date", "amount", "category", "description"]
    Format= "%d-%m-%Y"
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_file)
        except FileNotFoundError:
            df=pd.DataFrame(columns=cls.Columns)
            df.to_csv(cls.CSV_file,index=False)
            
    @classmethod
    def add_entry(cls,date,amount,category,description):
           new_entry = {
               "date": date,
               "amount": amount,
               "category":category,
               "description": description
            } 
           with open(cls.CSV_file,"a") as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=cls.Columns)
            writer.writerow(new_entry)
            
            print("Entry added successfully")
    @classmethod
    def get_transaction(cls,start_date, End_date):
        df= pd.read_csv(cls.CSV_file)
        df["date"]=pd.to_datetime(df["date"], format= CSV.Format)
        start_date= datetime.strptime(start_date,CSV.Format)
        End_date= datetime.strptime(End_date,CSV.Format)
        mask = (df["date"]>=start_date)&(df["date"]<=End_date)
        filtered_df= df.loc[mask]
        if filtered_df.empty:
            print('No Transactions found in date range')
        else:
            print(f"Transaction from {start_date.strftime(CSV.Format)} to {End_date.strftime(CSV.Format)}")
            print(
                filtered_df.to_string(
                    index=False, formatters ={"date":lambda x :x.strftime(CSV.Format)} 
                      )
                  ) 
            total_income=filtered_df[filtered_df["category"]== "Income"] ["amount"].sum()   
            total_expense=filtered_df[filtered_df["category"]== "Expense"]["amount"].sum()  
            print("\n Summary:")
            print(f"Total income: ${total_income:.2f}")
            print(f"Total expense: ${total_expense:.2f}")
            print(f"Net savings: ${(total_income - total_expense):.2f}")
            return filtered_df

def plot_transaction(df):
    df.set_index("date",inplace=True)
    income_df=(df[df["category"]=="Income"]
    .resample("D")
    .sum()
    .reindex(df.index,fill_value=0)
    )
    expense_df=(df[df["category"]=="Expense"]
    .resample("D")
    .sum()
    .reindex(df.index,fill_value=0)
    )
    plt.figure(figsize=(10,5))
    plt.plot(income_df,income_df["amount"],label= "Income",color= "pink" )
    plt.plot(income_df,income_df["amount"], label= "Expense",color ="purple")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.legend()
    plt.grid(True)
    plt.title("anything")
    plt.show()
   
def add():
    CSV.initialize_csv()
    date= get_date("Enter the date of the transaction (dd-mm-yyyy) or enter for today's date ",
                   allow_default=True,)
    amount= get_amount()
    category= get_category()
    description=get_description()
    CSV.add_entry(date, amount, category, description)

def main():
    while True:
        print("\n1.Add  a new transaction")
        print("2. View transactions and summary within a date range")
        print("3.Exit")
        choice=input("Enter your choice (1-3)")
        if choice =="1":
            add()
        elif choice =="2":
               start_date = get_date("Enter the start date dd-mm-yyyy: ")
               End_date = get_date("Enter the end  date dd-mm-yyyy: ")
               df= CSV.get_transaction(start_date,End_date )
               if input("do you want to see a graph Y/N ").lower == "Y":
                   plot_transaction(df)
        elif choice=="3":
               print("exiting program.....")
               break
        else: 
            print("Invalid answer please enter 1-3")


if __name__== "__main__":
    main()
