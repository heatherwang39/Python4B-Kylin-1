from Admin import Admin
from Employee import Employee

import csv
from tkinter import *

class AttendanceSystem:
    def __init__(self, admin_file, employee_file):
        self.admin_file = admin_file
        self.employee_file = employee_file
        self.admin_list = []
        self.employee_list = []
        
        # Load files
        self.load_admin_file()
        self.load_employee_file()
        
        # Start GUI
        self.login_types()
    
    def load_employee_file(self):
        try:
            with open(self.employee_file, "r") as f:
                csv_reader = csv.DictReader(f)
                for row in csv_reader:
                    first_name = row["first name"]
                    last_name = row["last name"]
                    id = row["ID"]
                    phone_number = row["phone number"]
                    address = row["address"]
                    present = int(row["present"])
                    absence = int(row["absence"])
                    employee = Employee(first_name, last_name, id, phone_number, address, present, absence)
                    self.employee_list.append(employee)
        except FileNotFoundError:
            with open(self.admin_file, "w", newline = '') as f:
                fieldnames = ["first name", "last name", "ID", "phone number", "address", "present", "absence"]
                csv_writer = csv.DictWriter(f, fieldnames = fieldnames)
                csv_writer.writeheader()
    
    def load_admin_file(self):
        try:
            with open(self.admin_file, "r") as f:
                csv_reader = csv.DictReader(f)
                for row in csv_reader:
                    first_name = row["first name"]
                    last_name = row["last name"]
                    id = row["ID"]
                    password = row["password"]
                    admin = Admin(first_name, last_name, id, password)
                    self.admin_list.append(admin)
        except FileNotFoundError:
            with open(self.employee_file, "w", newline = '') as f:
                csv_writer = csv.DictWriter(f)
                fieldnames = ["first name", "last name", "ID", "password"]
                csv_writer.writeheader()
    
    def login_types(self):
        login_type_window = Tk()
        login_type_window.geometry("400x200")
        def admin():
            self.admin_login()
        def employee():
            self.record_attendance()
        Button(login_type_window, text = "Admin", command = admin).grid(row = 0, column = 0)
        Button(login_type_window, text = "Employee", command = employee).grid(row = 0, column = 1)
    
    def admin_login(self):
        admin_login_window = Tk()
        admin_login_window.geometry("400x200")
        Label(admin_login_window, text = "ID: ").grid(row = 0, column = 0)
        id_entry = Entry(admin_login_window)
        id_entry.grid(row = 0, column = 1)
        Label(admin_login_window, text = "Password: ").grid(row = 1, column = 0)
        password_entry = Entry(admin_login_window)
        password_entry.grid(row = 1, column = 1)
        
        def verification():
            condition = True
            for admin in self.admin_list:
                if id_entry.get() == admin.get_id():
                    if password_entry.get() == admin.get_password():
                        condition = False
                        self.admin_options()
            if condition:
                messagebox.showinfo(title = "Error", message = "Password or username is incorrect, please try again...")
        Button(admin_login_window, text = "Enter", command = verification).grid(row = 2, column = 1)
    
    def admin_options(self):
        admin_options = Tk()
        admin_options.geometry("400x200")
        def clear_system():
            self.confirmation()
        def see_employee_info():
            for employee in self.employee_list:
                if employee.get_id() == id_entry.get():
                    self.show_employee_info(employee)
        Button(admin_options, text = "Clear System", command = clear_system).grid(row = 0, column = 0)
        Label(admin_options, text = "See Employee Info").grid(row = 1, column = 0)
        id_entry = Entry(admin_options)
        id_entry.grid(row = 1, column = 1)
        Button(admin_options, text = "Enter", command = see_employee_info).grid(row = 1, column = 2)
    
    def confirmation(self):
        confirmation_window = Tk()
        confirmation_window.geometry("400x200")
        def yes():
            for employee in self.employee_list:
                employee.set_present(0)
                employee.set_absence(0)
            self.update_employee_file()
            confirmation_window.destroy()
        def no():
            confirmation_window.destroy()
        Button(confirmation_window, text = "Yes", command = yes).grid(row = 0, column = 0)
        Button(confirmation_window, text = "No", command = no).grid(row = 0, column = 1)
    
    def update_employee_file(self):
        with open(self.employee_file, "w", newline = '') as f:
            fieldnames = ["first name", "last name", "ID", "phone number", "address", "present", "absence"]
            csv_writer = csv.DictWriter(f, fieldnames = fieldnames)
            csv_writer.writeheader()
            for employee in self.employee_list:
                csv_writer.writerow({"first name": employee.get_first_name(),
                                     "last name": employee.get_last_name(),
                                     "ID": employee.get_id(),
                                     "phone number": employee.get_phone_number(), 
                                     "address": employee.get_address(),
                                     "present": "0",
                                     "absence": "0"})
    
    def record_attendance(self):
        record_attendance_window = Tk()
        record_attendance_window.geometry("600x400")
        Label(record_attendance_window, text = "Please Enter Your Worker's ID: ").grid(row = 0, column = 0)
        id_entry = Entry(record_attendance_window)
        id_entry.grid(row = 1, column = 0)
        def record():
            condition = True
            for employee in self.employee_list:
                if employee.get_id() == id_entry.get():
                    condition = False
                    employee.set_present(employee.get_present() + 1)
                    self.show_employee_info(employee)
            if condition:
                messagebox.showinfo(title = "Error", message = "Invalid Employee ID, please try again...")
            else:            
                self.update_employee_file()
        Button(record_attendance_window, text = "Enter", command = record).grid(row = 2, column = 0)
    
    def show_employee_info(self, employee):
        employee_info_window = Tk()
        employee_info_window.geometry("800x600")
        Label(employee_info_window, text = "First Name: ").grid(row = 0, column = 0)
        Label(employee_info_window, text = employee.get_first_name()).grid(row = 0, column = 1)
        Label(employee_info_window, text = "Last Name: ").grid(row = 1, column = 0)
        Label(employee_info_window, text = employee.get_last_name()).grid(row = 1, column = 1)
        Label(employee_info_window, text = "ID: ").grid(row = 2, column = 0)
        Label(employee_info_window, text = employee.get_id()).grid(row = 2, column = 1)
        Label(employee_info_window, text = "Phone Number: ").grid(row = 3, column = 0)
        Label(employee_info_window, text = employee.get_phone_number()).grid(row = 3, column = 1)
        Label(employee_info_window, text = "Address: ").grid(row = 4, column = 0)
        Label(employee_info_window, text = employee.get_address()).grid(row = 4, column = 1)
        Label(employee_info_window, text = "Number of Presents: ", fg = "#BCEE68").grid(row = 5, column = 0)
        Label(employee_info_window, text = employee.get_present(), fg = "#BCEE68").grid(row = 5, column = 1)
        Label(employee_info_window, text = "Number of Absents: ", fg = "#FF3030").grid(row = 6, column = 0)
        Label(employee_info_window, text = employee.get_absence(), fg = "#FF3030").grid(row = 6, column = 1)
