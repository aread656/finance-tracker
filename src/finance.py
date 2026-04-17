import os
import csv
import utils
from transaction import Transaction
from personalFunctions import removeUnwantedRows
class Finance:

    income_categories = ["Pay", "Gift", "Dividend", "Loans", "Misc"]
    expense_categories = ["Bills", "Transport", "Groceries", "Clothing", "Charity", "Emergency", "Leisure", "Misc"]

    def __init__(self, filename = "financeRecords.csv"):
        self.transactions = []
        self.filename = filename
    def readCSV(self,path):
        output_rows=[]
        if os.path.exists(path):
            with open(file=path,mode="r",encoding="cp1252",newline="") as f:
                reader = csv.DictReader(f)
                for line in reader:
                    #categorise -amount as expense, +amount as income
                    amt_str = line["Amount"].replace(",","").strip()
                    line["is_income"] = float(amt_str) > 0
                    line["Amount"] = abs(float(amt_str))

                    #use utils CATEGORY_MAP to map to custom categories
                    category_key = (line.get("Category"),line.get("Subcategory"))
                    mapped_category = utils.CATEGORY_MAP.get(category_key)
                    if not mapped_category:
                        line["Category"]="Misc"
                    else:
                        line["Category"]=mapped_category

                    #remove unecessary rows
                    line.pop("Balance",None)
                    line.pop("Status",None)
                    line.pop("Reconciled",None)
                    line.pop("Subcategory",None)

                    new_trans = Transaction(
                        amount = line["Amount"], category = line["Category"],
                        date = line["Date"], description = line["Text"],
                        type = line["is_income"]
                    )
                    output_rows.append(new_trans)
        return output_rows
    def addTransaction(self):
        return
    def deleteTransaction(self):
        return
    def listTransactions(self):
        if self.transactions:
            for t in self.transactions:
                print(t)
            return
        print("No transactions recorded")
        return
    def editTransaction(self):
        return
    
if __name__ == "__main__":
    f = Finance()
    f.transactions = f.readCSV("data/StatementJul25-Apr26.csv")
    f.listTransactions()