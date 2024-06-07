import pandas as pd
import tkinter as tk

# Load the dataset
load = pd.read_csv(r"C:\Users\Lenovo\dataset1.csv")
df = pd.read_csv(r"C:\Users\Lenovo\dataset1.csv")

def detect_sql_keywords(input_data):
    sql_keywords = ['select', 'from', 'where', 'insert', 'update', 'delete', 'create', 'alter', 'drop', 'OR']
    for keyword in sql_keywords:
        if keyword.lower() in input_data.lower():
            return True
    return False

def detect_special_characters(input_data):
    special_chars = ["'", "-", "(", ")", ";", "#", "/*", "*/", "--"]
    for char in special_chars:
        if char in input_data:
            return True
    return False

def detect_sql_payloads(input_data, payload_list):
    for payload in payload_list:
        if payload.lower() in input_data.lower():
            return True
    return False

def load_payloads_from_file(file_path):
    with open(file_path, 'r') as file:
        payloads = [line.strip() for line in file]
    return payloads

def detect_sql_injection(input_data, headers, payload_list):
    if detect_sql_keywords(input_data) or detect_special_characters(input_data) or detect_sql_payloads(input_data, payload_list):
        print("SQL injection detected")
    else:
        print("No SQL injection detected")

    if 'User-Agent' in headers:
        user_agent = headers['User-Agent']
        if detect_sql_keywords(user_agent) or detect_special_characters(user_agent) or detect_sql_payloads(user_agent, payload_list):
            print("SQL injection detected ")
        else:
            print("No SQL injection detected ")

def on_button_click():
    input_data = entry.get()
    payload_list = load_payloads_from_file(r"C:\Users\Lenovo\dataset1.csv")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    detect_sql_injection(input_data, headers, payload_list)

root = tk.Tk()
root.title("Web Attack Detection")
root.geometry("400x300")

tk.Label(root, text="URL of the website:", font=('Helvetica', 14)).pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack(pady=9)
button = tk.Button(root, text="SQL Detection", font=('Helvetica', 14), command=on_button_click, bg='lightblue', fg='black')
button.pack(pady=20)

root.mainloop()
