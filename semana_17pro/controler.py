import PySimpleGUI as sg
from windows import create_main_window, window_enter_categorie, window_enter_movement
from data_manager import load_data, add_transaction, add_category

class FinanzasApp:
    def __init__(self):
        self.window = create_main_window()  
        self.update_table()

    def handle_add_category(self):
        category_win = window_enter_categorie()
        event_cat, values_cat = category_win.read()
        
        if event_cat == "Save_Cat":
           category_name = values_cat["New_Cat"].strip()
           
           if category_name: 
             add_category(category_name)
             sg.popup("Category Saved: ", category_name, auto_close=True, auto_close_duration=2)
             self.update_table()
           else: 
             sg.popup_error("Category name cannot be empty. ")
        category_win.close()
        

    def handle_add_transaction(self, transaction_type):
      data=load_data()
      if not data["categories"]: 
        sg.popup_error("Please enter a new category first. ")
        return
      
      transaction_win=window_enter_movement(transaction_type)
      event_trans, values_trans =transaction_win.read()
      
      if event_trans == "Save_Movement":  
        category = values_trans["CATEGORY"].strip()
        amount = values_trans["AMOUNT"].strip()
        
        if category and amount.isnumeric():
          add_transaction(transaction_type, category, int(amount))
          sg.popup(f"{transaction_type} added: " + category + ", " + amount, auto_close=True, auto_close_duration=2)
          self.update_table()
        else: 
          sg.popup_error("Invalid Input, Make sure category and amount are filled correctly.")
      transaction_win.close()

    def update_table(self):
      data =load_data()
      table_data =[[t["type"], t["category"], t["amount"]] for t in data["transactions"]]
      self.window["Table"].update(values=table_data)
      

    def run(self):
        while True:
            event, values = self.window.read()
            if event in (sg.WIN_CLOSED, "Log out"):
                break
            if event == "Add_Cat":
                self.handle_add_category()
            if event == "Add_Expense":
                self.handle_add_transaction("Expense")
            if event == "Add_Income":
                self.handle_add_transaction("Income")
        self.window.close()
    
 
         
         
       
      
  


