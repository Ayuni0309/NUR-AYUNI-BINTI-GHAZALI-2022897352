import tkinter as tk
import mysql.connector

# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Fee Aquarium"
)

mycursor = mydb.cursor()

def collect_data():
    customer_name = name_entry.get()
    package_type = package_var.get()
    packs = int(packs_entry.get())
    
    prices = {
        "Package A": 250,
        "Package B": 400
  
    }
    
    total_price = (prices[package_type] * packs)

    sql = "INSERT INTO customer (Customer_Name, Package_Type, Package_Pack, Package_Price) VALUES (%s, %s, %s, %s)"
    val = (customer_name, package_type, packs, total_price)
    mycursor.execute(sql, val)
    mydb.commit()
 
    output_label.config(text=f"Package: {package_type}, Packs: {packs}, Total Price: RM{total_price}")

root = tk.Tk()
root.title("Registeration Entrance Fee Aquarium")
root.geometry('600x600')

root.configure(bg = '#FAEBD7')

label = tk.Label(root, text='Calculate your Package Price', font=("Times New Romans",14, "bold"), bg = '#EEDFCC')
label.pack(ipadx = 10, ipady = 10)

name_label = tk.Label(root, text = "Customer Name", bg = '#8B8878')
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

prices_text = tk.Text(root, height = 15, width = 45, bg = '#F5F5DC')
prices_text.pack(pady=20)

prices_text.insert(tk.END, "Package & Prices:\n\n")
prices_text.insert(tk.END, "Package A: Family Package \nPrice: RM250\n\n")
prices_text.insert(tk.END, "Package B: Holiday Package \nPrice: RM400\n\n")
prices_text.configure(state='disabled')

packs_label = tk.Label(root, text="Choose Your Package", bg = '#8B8878')
packs_label.pack()

package_var = tk.StringVar(root)
package_var.set("Select Your Package")
trip_dropdown = tk.OptionMenu(root, package_var, "Package A", "Package B")
trip_dropdown.pack(pady = 10)

packs_label = tk.Label(root, text= "Packs:", bg = '#8B8878')
packs_label.pack()
packs_entry = tk.Entry(root)
packs_entry.pack()

label = tk.Label(root, text ='Price Package', font =("Times New Romans", 12), bg = '#8B8878')
label.pack(ipadx = 10, ipady = 10)
output_label = tk.Label(root, text = "")
output_label.pack()

insert_button = tk.Button(root, text = "Insert Data", command = collect_data)
insert_button.pack()

root.mainloop() 