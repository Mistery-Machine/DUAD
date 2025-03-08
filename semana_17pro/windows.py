import PySimpleGUI as sg 
from data_manager import load_data

def create_main_window():
  layout=[
    [sg.Text('Financial State')], 
    [sg.Table(values=[], headings=["Type", "Category", "Amount",], key="Table", enable_events=True)],
    [sg.Button("Enter Categorie", key="Add_Cat")],
    [sg.Button("Enter Spending", key="Add_Expense")],
    [sg.Button("Enter Income", key="Add_Income")], 
    [sg.Button("Log out")]
  ]
  return sg.Window("Financial Management", layout, finalize=True)

def window_enter_categorie(): 
  layout =[
    [sg.Text("New Category"), sg.InputText(key='New_Cat')],
    [sg.Button("Save",key='Save_Cat'), sg.Button("Cancel")]
  ]
  return sg.Window("Add Category", layout, modal=True)

def window_enter_movement(type): 
  data=load_data()
  categories=data["categories"] if data["categories"] else ["No categories available"]
  
  layout=[
    [sg.Text(f" Enter {type}")], 
    [sg.Text("Category"), sg.Combo(categories, key='CATEGORY', readonly=True, size=(20, 1))], 
    [sg.Text("Amount"), sg.InputText(key='AMOUNT')], 
    [sg.Button("Save", key='Save_Movement'), sg.Button("Cancel")]
    
  ]
  return sg.Window(f"ADD {type}", layout, modal=True)





























'''window=sg.Window("Finanzas",layout)

while True: 
    event, values = window.read()
    if event== "Log out" or sg.WIN_CLOSED: 
      break'''
