import pandas as pd
import tkinter as tk

# Load the payloads from the datasetads

def detect_sql_keywords(input_data):
    sql_keywords = ['select', 'from', 'where', 'insert', 'update', 'delete', 'create', 'alter', 'drop', 'OR']
    for keyword in sql_keywords:
        if keyword.lower() in input_data.lower():
            return True
    return False

def detect_special_characters(input_data):
    special_chars = ["'", "-", "(", ")", ";", "#", "\"", "--"]
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

def detect_sql_injection(input_data, payload_list):
    if detect_sql_keywords(input_data) or detect_special_characters(input_data) or detect_sql_payloads(input_data, payload_list):
        print("SQL injection detected")
    else:
        print("No SQL injection detected")

# XSS functions
def xss_special_characters(input_data):
    xss_special_chars = ['<', '>', '"', "'", '&', '(', ')', '[',']',';','{','}','/*']
    for char in xss_special_chars:
        if char in input_data:
            return True
    return False

def xss_payload(input_data, payload_list):
    for payload in payload_list:
        if payload.lower() in input_data.lower():
            return True
    return False

def xss_load_payloads_from_file(file_path):
    with open(file_path, 'r') as file:
        payloads = [line.strip() for line in file]
    return payloads

def xss_special_keyword(input_data):
    xss_keyword = [
        'script', 'img', 'iframe', 'link', 'object', 'embed', 'style', 'base', 'form', 'input', 'textarea', 'a', 'div', 'span',
        'javascript:', 'alert', 'prompt', 'confirm', 'eval', 'Function', 'setTimeout', 'setInterval', 'window', 'document', 'cookie',
        'localStorage', 'sessionStorage', 'innerHTML', 'outerHTML',
        'onload', 'onerror', 'onclick', 'onmouseover', 'onmouseout', 'onchange', 'onsubmit', 'onreset', 'onfocus', 'onblur',
        'onkeypress', 'onkeydown', 'onkeyup', 'onresize', 'onmousemove',
        'src', 'href', 'action', 'style', 'data'
    ]
    for keyword in xss_keyword:
        if keyword.lower() in input_data.lower():
            return True
    return False

def xss_detection(input_data, payload_list):
    if xss_special_characters(input_data) or xss_special_keyword(input_data) or xss_payload(input_data, payload_list):
        print("XSS detected")
    else:
        print("No XSS detected")

def on_button_click():
    input_data = entry.get()
    payload_list = load_payloads_from_file(r"C:\Users\Lenovo\dataset1.csv")
    input_data = entry.get()
    detect_sql_injection(input_data, payload_list)
    xss_detection(input_data, payload_list)

root = tk.Tk()
root.title("Web Attack Detection")
root.geometry("400x300")

tk.Label(root, text="URL of the website:", font=('Helvetica', 14)).pack(pady=5)
entry = tk.Entry(root, width=30)
entry = tk.Entry(root, width=30)
entry.pack(pady=9)

button_sql = tk.Button(root, text="vulnerability check", font=('Helvetica', 14), command=on_button_click, bg='lightblue', fg='black')
button_sql.pack(pady=20)

root.mainloop()
