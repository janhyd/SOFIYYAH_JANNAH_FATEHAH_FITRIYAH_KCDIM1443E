import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(
    host     = "localhost",
    user     = "root",
    password = "",
    database = "cat_hotel")

mycursor = mydb.cursor()

#mainwindow
window = tk.Tk()
window.geometry("870x560")
window['background'] = '#836953'
window.title("Cat Owner Registration")

labelmenu = tk.Label(window, text="\nWelcome MATE !!", font = ('Comic Sans MS bold', 25), fg="white", bg="#836953")
labelmenu.pack(padx=20, pady=1)

labelmenu = tk.Label(window, text="* Make sure to insert the data carefully, \n so that there will not have any mistake *", font = ('Comic Sans MS bold', 18), fg="white", bg="#836953")
labelmenu.pack(padx=20, pady=1)

labelmenu = tk.Label(window, text="* Only boarding date, grooming package, and haircut can be edited *", font = ('Comic Sans MS bold', 18), fg="white", bg="#836953")
labelmenu.pack(padx=20, pady=1)

labelmenu = tk.Label(window, text="* Please treat our customer carefully and helpfull \n so that we get a good review *", font = ('Comic Sans MS bold', 18), fg="white", bg="#836953")
labelmenu.pack(padx=20, pady=1)

labelmenu = tk.Label(window, text="\n ~~Happy Working~~", font = ('Comic Sans MS bold', 18), fg="white", bg="#836953")
labelmenu.pack(padx=20, pady=1)

labelmenu = tk.Label(window, text=" V⁠●⁠ᴥ⁠●⁠V", font = ('Comic Sans MS bold', 18), fg="white", bg="#836953")
labelmenu.place(x=380, y=470)

def register_page():

    def collect_data():

        accepted = accept_var.get()

        suite_type        = suite_type_combobox.get()
        board_type        = board_type_combobox.get()
        board_day         = int(board_day_combobox.get())
        medicine_type     = medicine_type_combobox.get()
        treatment_session = int(treatment_session_combobox.get())
        grooming_package  = grooming_package_combobox.get()
        grooming_cut      = grooming_cut_combobox.get()
    
        prices = {"Rabies FVRCP" : 90, "Self Check-in & out"    : 0,   "lion"        : 35,
                "FelV VACCINE" : 85, "Self Check-in & Drop"   : 15,  "Asian Lion"  : 35,
                "FHV-1"        : 96, "Pickup & Self Check-out": 15,  "Natural Look": 20,
                "ITRACONAZOLE" : 55, "Pickup & Drop"          : 30,  "Panther"     : 35,
                "TERBINAFINE"  : 61, "Basic"                  : 80,  "Belly Shave" : 20,                "FLUCONAZOLE"  : 58, "Full"                   : 150, "Butt Shave"  : 20,
                "Gold"         : 50, "Deluxe"                 : 200, "None"        : 0,
                "Platinum"     : 100,"Teddy Bear"             : 40,
                "Diamond"      : 150,"tiger"                  : 35,}

        total_suite     = (prices[suite_type] * board_day + prices[board_type])
        total_treatment = (prices[medicine_type] * treatment_session)
        total_grooming  = (prices[grooming_package] + prices[grooming_cut])
        total_prices    = total_suite + total_treatment + total_grooming

        
        output_total = tk.Label(output_frame, text="", fg="white", bg="#836953")
        output_total.grid(row=0, column=1)
        output_total.config(text=f"RM{total_prices}")
        

        if accepted == "Accepted":
            id      = owner_id_entry.get()
            name    = owner_name_entry.get()
            dbirth  = d_b_entry.get()
            mbirth  = m_b_entry.get()
            ybirth  = y_b_entry.get()
            address = owner_address_entry.get()
            phone   = owner_phone_entry.get()
            email   = owner_email_address_entry.get()

            if name and address and phone and email:  
                cat             = cat_name_entry.get()
                cat_age         = cat_age_combobox.get()
                cat_breed       = cat_breed_combobox.get()
                cat_noted       = cat_noted_entry.get()
                board_date      = board_date_entry.get()
                treatment_type  = treatment_type_combobox.get()

                print("Name: ", name)
                print("Birth Date:", dbirth, "/", mbirth, "/", ybirth)
                print("Address:", address)
                print("Contact No:", phone)
                print("Email:", email)
                print(".............")
                print("Cat Name:", cat)
                print("Age:", cat_age)
                print("Breed:", cat_breed)
                print("Notes:", cat_noted)
                print("Suite Type:", suite_type)
                print("Board Type:", board_type)
                print("Board Day:", board_day,)
                print("Board Date:", board_date)
                print("Treatment Type:", treatment_type)
                print("Treatment Session:", treatment_session)
                print("Medicine Type:", medicine_type)         
                print("Grooming Package:", grooming_package)
                print("Grooming Cut:", grooming_cut)
                print("---------------------------------------------------------------")
            else:
                tk.messagebox.showwarning(title= "Error", message= "There are items that require your attention!")
        else:
            tk.messagebox.showwarning(title= "Error", message= "You have not accepted the terms!")  
    

        sql  = "INSERT INTO registration (ID, NAME, ADDRESS, PHONE_NO, EMAIL, CAT_NAME, CAT_AGE, CAT_BREED, NOTES) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val  = (id, name, address, phone, email, cat, cat_age, cat_breed, cat_noted)
        sql2 = "INSERT INTO boarding (SUITE,BOARDING_TYPE,DAY,DAY_CHECK_IN,TOTAL) VALUES (%s,%s,%s,%s,%s)"
        val2 = (suite_type, board_type, board_day, board_date, total_suite)
        sql3 = "INSERT INTO treatment (TREATMENT_TYPE, SESSION,MEDICINE_TYPE,TOTAL) VALUES (%s,%s,%s,%s)"
        val3 = (treatment_type, treatment_session, medicine_type, total_treatment)
        sql4 = "INSERT INTO grooming (PACKAGE,HAIRCUT,TOTAL) VALUES (%s,%s,%s)"
        val4 = (grooming_package, grooming_cut, total_grooming)

        mycursor.execute(sql, val)
        mycursor.execute(sql2, val2)
        mycursor.execute(sql3, val3)
        mycursor.execute(sql4, val4)
        mydb.commit()


    def view_data():
        mydb     = mysql.connector.connect(
        host     = "localhost",
        user     = "root",
        password = "",
        database = "cat_hotel")

        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM registration")

        result = mycursor.fetchall()

        print_record = ''
        if result:
            latest_record = result[-1]
            print_record = f"> {latest_record[0]} \t {latest_record[1]}"
        else:
            print_record = "No records Available"

        view_record = tk.Label(output_frame, text=print_record, fg="white", bg="#836953")
        view_record.grid(row=0, column=3)
    

        mycursor.close()
        mydb.close()

    def edit_data ():
        boarddate = board_date_entry.get()
        groomingpackage = grooming_package_combobox.get()
        groomingcut = grooming_cut_combobox.get()

        mydb = mysql.connector.connect(
            host    ="localhost",
            user    ="root",
            password="",
            database="cat_hotel"
        )
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM boarding")
        boarding_records = mycursor.fetchone()
        mycursor.fetchall()
        mycursor.execute("SELECT * FROM grooming")
        grooming_records = mycursor.fetchone()
        mycursor.fetchall()

        edit_one = ''
        edit_two = ''
        if boarding_records is not None:
            sql_boarding = "UPDATE boarding SET DAY_CHECK_IN = %s WHERE DAY_CHECK_IN = %s"
            val_boarding = (boarddate, boarding_records[3])
            mycursor.execute(sql_boarding, val_boarding)
            mydb.commit()
        if grooming_records is not None:
            sql_grooming = "UPDATE grooming SET PACKAGE = %s, HAIRCUT = %s WHERE PACKAGE = %s AND HAIRCUT = %s"
            val_grooming = (groomingpackage, groomingcut,grooming_records[0],grooming_records[1])
            mycursor.execute(sql_grooming, val_grooming)
            mydb.commit()
            edit_one ="Groom ✓ Board ✓"
        else:
            edit_two ="No updated"

        edit_record = tk.Label(output_frame, text=edit_one, fg="white", bg="#836953")
        edit_record.grid(row=0, column=5)
        edit_record = tk.Label(output_frame, text=edit_two, fg="white", bg="#836953")
        edit_record.grid(row=0, column=5)   

    def delete_data():
        mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "cat_hotel")

        mycursor = mydb.cursor()

        mycursor.execute("SELECT COUNT(*) FROM registration")
        count = mycursor.fetchone()[0]
        mycursor.execute("SELECT COUNT(*) FROM boarding")
        count = mycursor.fetchone()[0]
        mycursor.execute("SELECT COUNT(*) FROM treatment")
        count = mycursor.fetchone()[0]
        mycursor.execute("SELECT COUNT(*) FROM grooming")
        count = mycursor.fetchone()[0]

        delete_one = ''
        delete_two = ''
        if count > 0:
            sql  = "DELETE FROM registration ORDER BY NAME DESC LIMIT 1"
            sql2 = "DELETE FROM boarding ORDER BY SUITE DESC LIMIT 1"
            sql3 = "DELETE FROM treatment ORDER BY TREATMENT_TYPE DESC LIMIT 1"
            sql4 = "DELETE FROM grooming ORDER BY PACKAGE DESC LIMIT 1"
            mycursor.execute(sql)
            mycursor.execute(sql2)
            mycursor.execute(sql3)
            mycursor.execute(sql4)
            mydb.commit()
            delete_one = "Last record deleted."
        else:
            delete_two = "No record   to delete." 
        delete_record = tk.Label(output_frame, text=delete_two, fg="white", bg="#836953")#
        delete_record.grid(row=0, column=7)
        delete_record_two = tk.Label(output_frame, text=delete_one, fg="white", bg="#836953")
        delete_record_two.grid(row=0, column=7)

    #register window
    root = tk.Toplevel(window)
    root.geometry("870x560")
    root['background'] = '#836953'
    root.title("Cat Owner Registration")

    label = tk.Label(root, text = "Customer Registration", font = ('Comic Sans MS bold', 18), fg="white", bg="#836953")
    label.pack(padx=20, pady=1)

    out_frame = tk.Frame(root, bg="#836953")
    out_frame.pack(padx=20, pady=1)

    frame = tk.LabelFrame(out_frame, bg="#836953")
    frame.grid(row=0, column=0)

    #owner
    cat_owner_frame = tk.LabelFrame(frame, text = "Personal Detail", fg="white", bg="#836953")
    cat_owner_frame.grid(row= 0, column=0, sticky="News", padx=1, pady=1)

    owner_id = tk.Label(cat_owner_frame, text="Id :", fg="white", bg="#836953")
    owner_id.grid(row=0, column=0)
    owner_id_entry = tk.Entry(cat_owner_frame, width=23)
    owner_id_entry.grid(row=0, column=1)

    owner_name_label = tk.Label(cat_owner_frame, text="Name :", fg="white", bg="#836953")
    owner_name_label.grid(row=1, column=0)
    owner_name_entry = tk.Entry(cat_owner_frame, width=23)
    owner_name_entry.grid(row=1, column=1)

    owner_birth_date = tk.Label(cat_owner_frame, text="    Birth Date :    ", fg="white", bg="#836953")
    owner_birth_date.grid(row=2, column=0)

    d_b_entry = ttk.Combobox(cat_owner_frame, values=["1","2","3","4","5","6","7","8","9","10",
                                                    "11","12","13","14","15","16","17","18","19","20",
                                                    "21","22","23","24","25","26","27","28","29","30","31"]) 
    d_b_entry.grid(row=2, column=1)
    d_b_entry.set("Date")
    d_b_entry["state"] = 'readonly'

    m_b_entry = ttk.Combobox(cat_owner_frame, values=["01","02","03","04","05","06",
                                                    "07","08","09","10","11","12"]) 
    m_b_entry.grid(row=3, column=1)
    m_b_entry.set("Month")
    m_b_entry["state"] = 'readonly'

    y_b_entry = ttk.Combobox(cat_owner_frame, values=list(range(1960, 2200)))
    y_b_entry.grid(row=4, column=1)
    y_b_entry.set("Year")
    y_b_entry["state"] = 'readonly'

    for widget in cat_owner_frame.winfo_children():
        widget.grid_configure(padx= 10, pady=5)

    cont = tk.LabelFrame(frame, text="-", fg="white", bg="#836953")
    cont.grid(row=0, column=1, sticky="News", padx=1, pady=1)

    owner_address_label = tk.Label(cont, text="       Address :      ", fg="white", bg="#836953")
    owner_address_label.grid(row=5, column=0)
    owner_address_entry = tk.Entry(cont, width=23)
    owner_address_entry.grid(row=5, column=1)

    owner_phone_label = tk.Label(cont, text="Contact No :", fg="white", bg="#836953")
    owner_phone_label.grid(row=6, column=0)
    owner_phone_entry = tk.Entry(cont, width=23)
    owner_phone_entry.grid(row=6, column=1)

    owner_email_address_label = tk.Label(cont, text="Email Address :", fg="white", bg="#836953")
    owner_email_address_label.grid(row=7, column=0)
    owner_email_address_entry = tk.Entry(cont, width=23)
    owner_email_address_entry.grid(row=7, column=1)

    for widget in cont.winfo_children():
        widget.grid_configure(padx= 10, pady=5)

    #cat
    cat_frame = tk.LabelFrame(frame, text="Cat Details", fg="white", bg="#836953")
    cat_frame.grid(row=0, column=2, sticky="News", padx=1, pady=1)

    cat_name_label = tk.Label(cat_frame, text="Name :", fg="white", bg="#836953")
    cat_name_label.grid(row=0, column=0)
    cat_name_entry = tk.Entry(cat_frame, width=23)
    cat_name_entry.grid(row=0, column=1)

    cat_age_label = tk.Label(cat_frame, text="Age :", fg="white", bg="#836953")
    cat_age_label.grid(row=1, column=0)
    cat_age_combobox = ttk.Combobox(cat_frame, values=["Kitten(0-1)", "Young Adult(1-6)",
                                                    "Mature Adult(7-10)", "Senior(>10)"])
    cat_age_combobox.grid(row=1, column=1)
    cat_age_combobox.set("")
    cat_age_combobox["state"] = 'readonly'

    cat_breed_label = tk.Label(cat_frame, text="     Breed :     ", fg="white", bg="#836953")
    cat_breed_label.grid(row=2, column=0)
    cat_breed_combobox = ttk.Combobox(cat_frame, values=["Domestic", "American", "Siamese", "Maine Coon", "Ragdoll", 
                                                        "Russian Blue", "Bengal", "Bombay", "Persian"])
    cat_breed_combobox.grid(row=2, column=1)
    cat_breed_combobox.set("")
    cat_breed_combobox["state"] = 'readonly'

    cat_noted_label = tk.Label(cat_frame, text="Notes :", fg="white", bg="#836953")
    cat_noted_label.grid(row=3, column=0)
    cat_noted_entry = tk.Entry(cat_frame, width=23)
    cat_noted_entry.grid(row=3, column=1)

    for widget in cat_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    #boarding
    boarding_frame = tk.LabelFrame(frame, text="Boarding", fg="white", bg="#836953")
    boarding_frame.grid(row= 1, column=0, sticky="News", padx=1, pady=1)

    suite_type_label = tk.Label(boarding_frame, text="Suite Type :", fg="white", bg="#836953")
    suite_type_label.grid(row=0, column=0)
    suite_type_combobox = ttk.Combobox(boarding_frame, values=["Gold", "Platinum", "Diamond"])
    suite_type_combobox.grid(row=0, column=1)
    suite_type_combobox.set("")
    suite_type_combobox["state"] = 'readonly'

    board_type_label = tk.Label(boarding_frame, text="Boarding Type :", fg="white", bg="#836953")
    board_type_label.grid(row=1, column=0)
    board_type_combobox = ttk.Combobox(boarding_frame, values=["Self Check-in & out",
                                                            "Self Check-in & Drop",
                                                            "Pickup & Self Check-out",
                                                            "Pickup & Drop"])
    board_type_combobox.grid(row=1, column=1)
    board_type_combobox.set("")
    board_type_combobox["state"] = 'readonly'

    board_day_label = tk.Label(boarding_frame, text="Day :", fg="white", bg="#836953")
    board_day_label.grid(row=2, column=0)
    board_day_combobox = ttk.Combobox(boarding_frame, values=["1","2","3","4","5","6","7","8","9","10",
                                                            "11","12","13","14","15","16","17","18","19","20",
                                                            "21","22","23","24","25","26","27","28","29","30","31"])
    board_day_combobox.grid(row=2, column=1)
    board_day_combobox.set("")
    board_day_combobox["state"] = 'readonly'

    board_date_label = tk.Label(boarding_frame, text="Date Check In :", fg="white", bg="#836953")
    board_date_label.grid(row=3, column=0)
    board_date_entry = tk.Entry(boarding_frame, width=23)
    board_date_entry.grid(row=3, column=1)
    board_date_entry.insert(0, "dd/mm/yyyy")

    for widget in boarding_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    #treatment
    treatment_frame = tk.LabelFrame(frame, text="Treatment", fg="white", bg="#836953")
    treatment_frame.grid(row=1, column=1, sticky="News", padx=1, pady=1)

    treatment_type_label = tk.Label(treatment_frame, text="Treatment Type :", fg="white", bg="#836953")
    treatment_type_label.grid(row=0, column=0)
    treatment_type_combobox = ttk.Combobox(treatment_frame, values=["None","vaccine", "Fungus"])
    treatment_type_combobox.grid(row=0, column=1)
    treatment_type_combobox.set("")
    treatment_type_combobox["state"] = 'readonly'

    treatment_session_label = tk.Label(treatment_frame, text="Session :", fg="white", bg="#836953")
    treatment_session_label.grid(row=1, column=0)
    treatment_session_combobox = ttk.Combobox(treatment_frame, values=["0","1","2","3","4"])
    treatment_session_combobox.grid(row=1, column=1)
    treatment_session_combobox.set("")
    treatment_session_combobox["state"] = 'readonly'

    medicine_type_Label = tk.Label(treatment_frame, text="Medicine Type :", fg="white", bg="#836953")
    medicine_type_Label.grid(row=2, column=0)
    medicine_type_combobox = ttk.Combobox(treatment_frame, values=["None","Rabies FVRCP", "FelV VACCINE","FHV-1",
                                                                "ITRACONAZOLE", "TERBINAFINE", "FLUCONAZOLE"])
    medicine_type_combobox.grid(row=2, column=1)
    medicine_type_combobox.set("")
    medicine_type_combobox["state"] = 'readonly'

    for widget in treatment_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    #grooming
    grooming_frame = tk.LabelFrame(frame, text="Grooming", fg="white", bg="#836953")
    grooming_frame.grid(row=1, column=2, sticky="News", padx=1, pady=1)

    grooming_package_label = tk.Label(grooming_frame, text="Package :", fg="white", bg="#836953")
    grooming_package_label.grid(row=0, column=0)
    grooming_package_combobox = ttk.Combobox(grooming_frame, values=["None","Basic", "Full", "Deluxe"])
    grooming_package_combobox.grid(row=0, column=1)
    grooming_package_combobox.set("")
    grooming_package_combobox["state"] = 'readonly'

    grooming_cut_label = tk.Label(grooming_frame, text="Cat Haircut :", fg="white", bg="#836953")
    grooming_cut_label.grid(row=1, column=0)
    grooming_cut_combobox = ttk.Combobox(grooming_frame, values=["None","Teddy Bear","lion","Asian Lion","tiger",
                                                                "Natural Look","Panther","Belly Shave","Butt Shave"])
    grooming_cut_combobox.grid(row=1, column=1)
    grooming_cut_combobox.set("")
    grooming_cut_combobox["state"] = 'readonly'

    for widget in grooming_frame.winfo_children():
        widget.grid_configure(padx= 10, pady=5)

    #terms
    terms_frame = tk.LabelFrame(out_frame, text="Terms & Condition", fg="white", bg="#836953")
    terms_frame.grid(row=1, column=0, sticky="News", padx=1, pady=1)

    accept_var = tk.StringVar(value="Not Accepted")
    terms_check = tk.Checkbutton(terms_frame, text="I accept the terms and condition.", fg="#3d251e",
                                variable=accept_var, onvalue="Accepted", offvalue="Not Accepted", bg="#836953")
    terms_check.grid(row=0, column=0)

    #notes
    output_frame = tk.LabelFrame(out_frame, text="Notes :", fg="white", bg="#836953")
    output_frame.grid(row=2, column=0, sticky="News", padx=1, pady=1)

    total_label = tk.Label(output_frame, text="Total :", fg="white", bg="#836953")
    total_label.grid(row=0, column=0)
    total_label = tk.Label(output_frame, text=". . . . . . . . . . .", fg="#836953", bg="#836953")
    total_label.grid(row=0, column=1)
    view_view = tk.Label(output_frame, text="View Data :", fg="white", bg="#836953")
    view_view.grid(row=0, column=2)
    view_view = tk.Label(output_frame, text=". . . . . . . . . . . . . . . . . . .", fg="#836953", bg="#836953")
    view_view.grid(row=0, column=3)
    edit_view = tk.Label(output_frame, text="Edit Data :", fg="white", bg="#836953")
    edit_view.grid(row=0, column=4)
    edit_view = tk.Label(output_frame, text=". . . . . . . . . . . . . . . . . . .", fg="#836953", bg="#836953")
    edit_view.grid(row=0, column=5)
    delete_view = tk.Label(output_frame, text="Delete Data :", fg="white", bg="#836953")
    delete_view.grid(row=0, column=6)
    delete_view = tk.Label(output_frame, text=". . . . . . . . . . . . . . . . . . .", fg="#836953", bg="#836953")
    delete_view.grid(row=0, column=7)

    for widget in output_frame.winfo_children():
        widget.grid_configure(padx= 10, pady=5)

    button_frame = tk.LabelFrame(out_frame, text="", fg="white", bg="#836953")
    button_frame.grid(row=3, column=0, sticky="News", padx=1, pady=1)

    #button
    enter_button = tk.Button(button_frame, text="Enter", bg="white", command= collect_data)
    enter_button.grid(row=0, column=0, ipadx=59)

    view_button = tk.Button(button_frame, text="View", bg="white", command=view_data)
    view_button.grid(row=0, column=1, ipadx=93)

    update_button = tk.Button(button_frame, text="Edit", bg="white", command=edit_data)
    update_button.grid(row=0, column=2, ipadx=93)

    delete_button = tk.Button(button_frame, text="Delete Last Record", bg="white", command=delete_data)
    delete_button.grid(row=0, column=3, ipadx=60)

    for widget in button_frame.winfo_children():
        widget.grid_configure( pady=5)

    mainmenu_button = tk.Button(out_frame, text="Close", bg="white", command=root.destroy)
    mainmenu_button.grid(row=4, column=0, pady=10, ipadx=393)

register_button = tk.Button(window, text="Register New Customer", bg="white", command=register_page)
register_button.place(x=15, y=390, width=845, height=30)

register_button = tk.Button(window, text="Close", bg="white", command=window.destroy)
register_button.place(x=15, y=430, width=845, height=30)

window.mainloop()