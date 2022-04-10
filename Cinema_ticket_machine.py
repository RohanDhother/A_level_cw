
#this imports the tkinter module
from tkinter import *

#this imports the sqlite3 module
import sqlite3

#this imports validate_email from the module validate_email
from validate_email import validate_email

#this imports the time module
import time

#this imports the datetime module
from datetime import *

def code_restart(): #this is a function

    #this opens the database
    with sqlite3.connect('database.db') as db:

        #this sets the variable cursor to equal db.cursor
        cursor=db.cursor()

        class countdown_class: #this is the class for the timer

            def __init__(self, countdown): #this is initialises the class
                
                self.countdown= countdown #this links the window to the class
                countdown.overrideredirect(1) #this raises the window to the top
                #this creates the background
                self.bg=Label(countdown, bg="black", width=10, height=10)
                self.bg.place(relx=0, rely=0)
                #this resizes the window and puts it in the top right
                countdown.geometry('%dx%d+%d+%d' % (65, 63, 1303, 0))
                 #this raises the window to the top
                countdown.overrideredirect(1)
                #this removes the top bar from the window
                countdown.resizable(width = False, height = False)
                #this calls the function timer
                self.timer()
                
            def timer(self): #this is a function

                #this sets the variable start to 1
                self.start=1
                #this sets the variable start_second to 0
                self.start_seconds=0
                #this sets the variable to False
                self.time_end=False
                #this displays the timer
                self.time_left_label_film_select=Label(countdown, text=":", font=("Courier", 20), fg="white", bg="black", width=1, height=2)
                self.time_left_label_film_select.place(relx=0.2, rely=0)
                self.display_time_film_select=Label(countdown, text=4, font=("Courier", 20), fg="white", bg="black", height=2)
                self.display_time_film_select.place(relx=0, rely=0)
                self.display_time_seconds_film_select=Label(countdown, text="00", font=("Courier", 20), fg="white", bg="black", height=2)
                self.display_time_seconds_film_select.place(relx=0.4, rely=0)
                self.display_time_film_select.config(text=4, font=("Courier", 20), fg="white", bg="black")
                
                
                def change_value_the_time_seconds(): #this is a function

                    #this sets the variable the_seconds_time to 59 - the variable start_second
                    self.the_seconds_time=(59-self.start_seconds)
                    #this checks if the length of the variable the_second_time equals 1
                    if len(str(self.the_seconds_time))==1:

                        #this sets the variable the_second_time to "0" and the variable the_second_time
                        self.the_seconds_time="0"+str(self.the_seconds_time)

                    #this checks if start_second does not equal 60
                    if self.start_seconds!=60:

                        #this updates the seconds
                        self.display_time_seconds_film_select.config(text=self.the_seconds_time, font=("Courier", 20), fg="white", bg="black")                    
                        self.display_time_seconds_film_select.after(1000, change_value_the_time_seconds)
                        #this increases the variable start_seconds by 1
                        self.start_seconds+=1

                    else:

                        #this sets the variable start_second to 0
                        self.start_seconds=0
                        #this increases the variable start by 1
                        self.start+=1
                        #this sets the variable the_time to 5 - the variable start
                        self.the_time=(5-self.start)
                        #this checks if the variable the_time equals -1
                        if self.the_time==-1:
                            #this checks if page_number is bigger 8 or equal to 1
                            if menu.page_number>8 or menu.page_number==1:

                                pass

                            else:

                                    #this lowers the window
                                    countdown.attributes("-topmost", 0)
                                    #this imports the module time
                                    import time
                                    #this raises the window
                                    out_of_time.attributes("-topmost", 1)
                                    #this creates a 10s delay
                                    time.sleep(10)
                                    #this calls the function timer
                                    self.timer()

                                    #this loops until i equals aseats from the class Ticket
                                    for i in range(Ticket.aseats):

                                        try:

                                            xseats.pop(i) #this removes a item from the list xseats
                                            yseats.pop(i) #this removes a item from the list yseats

                                        except(Exception):

                                            pass
                                        
                                    code_restart() #this calls the function code_restart

                            
                        else:

                            #this updates the time
                            self.display_time_film_select.config(text=self.the_time, font=("Courier", 20), fg="white", bg="black")
                            #this calls the function change_value_the_time_seconds
                            change_value_the_time_seconds()

                #this calls the function change_value_the_time_seconds
                change_value_the_time_seconds()

        class out_of_time_class: #this is the class for out of time

            def __init__(self, out_of_time): #this initialises the class

                self.out_of_time= out_of_time #this links the window to the class
                out_of_time.overrideredirect(1) #this raises the window to the top
                out_of_time.geometry("%dx%d+0+0" % (w, h)) #this resizes the window
                #this remvoes the top bar from the window
                out_of_time.resizable(width = False, height = False)
                #this creates the background
                self.ticket_bg_image = PhotoImage(file="menu_bg.gif")
                self.ticket_bg_Label = Label(out_of_time, image=menu.bg_image, bg="black")
                self.ticket_bg_Label.grid()
                #this creates a white box on the window
                self.white_bg = Label(out_of_time, bg="white", width=165, height=43)
                self.white_bg.place(relx=0.077, rely=0.09)
                #this displays the message saying that the timer has ran out
                self.out_of_time_label=Label(out_of_time, bg="white", font=("Courier", 20), text="""         You have ran out of time

                  Please try again

                Some seats may have gone""")
                self.out_of_time_label.place(relx=0.1, rely=0.3)
                
        def ticket_num(): #this is a function

            #this selects the username from the database
            cursor.execute("""SELECT username FROM tickets""")
            #this sets the variable ids to the length of the results
            ids=len(cursor.fetchall())
            #this displays the number the customer is
            ticket_number=Label(collect_ticket, bg="white", font=("Courier", 90), text=ids)
            ticket_number.place(relx=0.45, rely=0.45)

        class collect_ticket_class: #this is the class for ticket infomation

            def __init__(self, collect_ticket): #this initialises the class

                self.collect_ticket = collect_ticket #this links the window with the class
                collect_ticket.overrideredirect(1) #this raises the window to the top
                collect_ticket.geometry("%dx%d+0+0" % (w, h)) #this resizes the window
                #this removes the top bar from the window
                collect_ticket.resizable(width = False, height = False)
                #this creates the background
                self.ticket_bg_image = PhotoImage(file="menu_bg.gif")
                self.ticket_bg_Label = Label(collect_ticket, image=menu.bg_image, bg="black")
                self.ticket_bg_Label.grid()
                #this creates a white box on the window
                self.white_bg = Label(collect_ticket, bg="white", width=165, height=43)
                self.white_bg.place(relx=0.077, rely=0.09)
                #this is the label that tells the customer what to do with the number
                self.ticket_collect=Label(collect_ticket, bg="white", font=("Courier", 20), text="""            Thank you for booking with us

            Please take this number to the screen entrance.
                where an assistant will meet you.


                    
                """)
                self.ticket_collect.place(relx=0.077, rely=0.2)
                self.show_card=Label(collect_ticket, bg="white", font=("Courier", 20), text="       You may be asked to verify your card details.")
                self.show_card.place(relx=0.15, rely=0.7)
                
                def submit_selected(): #this is a function

                    #this loops untils i equals the variable aseats from the Ticket class
                    for i in range(Ticket.aseats):

                        try:

                            xseats.pop(i) #this removes an item from the list xseats
                            yseats.pop(i) #this removes an item from the list yseats

                        except(Exception):

                            pass
                        
                    code_restart() #this calls a function called code_restart            
    

                #this makes a done button
                self.submit_btn= Button(collect_ticket, text="Done", width="20", height="3", command=submit_selected)
                self.submit_btn.configure(font=("Courier", 15), fg="white", bg="black")
                self.submit_btn.place(relx=0.4, rely=0.81)
                

        class payment_class: #this is the class for payment

            def __init__(self, payment): #this initialises the class

                def submit_selected(): #this is a function

                     #this sets the variable two_words to False
                    self.two_words=False
                    #this sets the variable space_count to 0
                    self.space_count=0

                    #this loops until i equals the length of card_name -1
                    for i in range(len(self.card_name.get())-1):

                        #this looks for a space in the string
                        if " " in self.card_name.get()[i]:

                            #this sets the variable two_word to True
                            self.two_words=True
                            #this increases the variable space_count by 1
                            self.space_count+=1
                                    

                    #this sets the variable card_correct to True
                    self.card_correct=True

                    #this checks if the entry box are not filled
                    if self.variable2.get()=="None" or self.card_number.get()=="" or self.card_name.get()=="" or self.security_code.get()=="" or self.card_number.get()=="" or self.variable.get()=="Month" or self.variable1.get()=="Year":
                        #this creates an error
                        self.empty=Label(payment, bg="red", font=("Courier", 15), text="Please enter all fields", width=120)
                        self.empty.place(relx=0, rely=0)
                        
                        def kill_empty():
                            
                            self.empty.place_forget()
                            
                        self.empty.after(2000, kill_empty) #this kills the error after 2000ms

                    #this checks if the card number is not 16 characters long
                    elif len(self.card_number.get())!=16:
                                                                                                                                                                             
                        #this creates an error
                        self.fakecard_number=Label(payment, bg="red", font=("Courier", 15), text="Card number incorrect", width=120)
                        self.fakecard_number.place(relx=0, rely=0)
                        
                        def kill_fakecard_number():
                            
                            self.fakecard_number.place_forget()
                            
                        self.fakecard_number.after(2000, kill_fakecard_number) #this kills the error after 2000ms

                    #this checks if the sercuirty code is not 3 characters long
                    elif len(pay.security_code.get())!=3:

                        #this creates an error
                        self.fakesecurity_code=Label(payment, bg="red", font=("Courier", 15), text="Ssecurity code incorrect", width=120)
                        self.fakesecurity_code.place(relx=0, rely=0)
                        
                        def kill_fakesecurity_code():
                            
                            self.fakesecurity_code.place_forget()
                            
                        self.fakesecurity_code.after(2000, kill_fakesecurity_code) #this kills the error after 2000ms

                    #this checks if the variable data_correct equals False
                    elif self.date_correct==False:

                        #this creates an error
                        self.date_wrong=Label(payment, bg="red", font=("Courier", 15), text="Date has expired", width=120)
                        self.date_wrong.place(relx=0, rely=0)
                        
                        def kill_date_wrong():
                            
                            self.date_wrong.place_forget()
                            
                        self.date_wrong.after(2000, kill_date_wrong) #this kills the error after 2000ms

                    #this checks if the card name ends with a space
                    elif self.card_name.get()[len(self.card_name.get())-1]==" ":

                        #this creates an error
                        self.space_end=Label(payment, bg="red", font=("Courier", 15), text="Remove space at end", width=120)
                        self.space_end.place(relx=0, rely=0)

                        def kill_space_end():
                            
                            self.space_end.place_forget()
                            
                        self.space_end.after(2000, kill_space_end) #this kills the error after 2000ms

                    #this checks if the variable two_words equals False
                    elif self.two_words==False:

                        #this creates an error
                        self.space_end=Label(payment, bg="red", font=("Courier", 15), text="Please enter first and last name on card", width=120)
                        self.space_end.place(relx=0, rely=0)

                        def kill_space_end():
                            
                            self.space_end.place_forget()
                            
                        self.space_end.after(2000, kill_space_end) #this kills the error after 2000ms

                    else:

                        #this sets the variable length_of_card_name to the length of the card name
                        self.length_of_card_name=len(self.card_name.get())
                        self.letter_count=0 #this sets the variable letter_count to 0

                        #this loops until i equals the variable length_of_card_name
                        for i in range(self.length_of_card_name):

                            #this checks if the i number in the card number is a letter
                            if self.card_name.get()[i].isdigit()==False:

                                #this increases the variable letter_count by 1
                                self.letter_count+=1

                        #this checks if length_of_card_name does not equal letter_count
                        if self.length_of_card_name!=self.letter_count:

                            #this creates an error
                            self.fakecard_name=Label(payment, bg="red", font=("Courier", 15), text="Card name not valid", width=120)
                            self.fakecard_name.place(relx=0, rely=0)
                            self.card_correct=False
                            
                            def kill_fakecard_name():
                                
                                self.fakecard_name.place_forget()
                                
                            self.fakecard_name.after(2000, kill_fakecard_name) #this kills the error after 2000ms

                        #this checks if the variable card_correct equals True
                        if self.card_correct==True:

                            try:

                                int(self.card_number.get()) #this tries to make card number a number

                            except(Exception):

                                #this creates an error
                                self.fakecard_number=Label(payment, bg="red", font=("Courier", 15), text="Card number incorrect", width=120)
                                self.fakecard_number.place(relx=0, rely=0)
                                self.card_correct=False #this sets the variable card_correct to False
                                
                                def kill_fakecard_number():
                                    
                                    self.fakecard_number.place_forget()
                                    
                                self.fakecard_number.after(2000, kill_fakecard_number) #this kills the error after 2000ms

                        #this checks if the variable card_correct equals True
                        if self.card_correct==True:

                            try:

                                int(self.security_code.get()) #this tries to make security code a number

                            except(Exception):

                                #this creates an error
                                self.fakesecurity_code=Label(payment, bg="red", font=("Courier", 15), text="Security code incorrect", width=120)
                                self.fakesecurity_code.place(relx=0, rely=0)
                                self.card_correct=False
                                
                                def kill_fakesecurity_code():
                                    
                                    self.fakesecurity_code.place_forget()
                                    
                                self.fakesecurity_code.after(2000, kill_fakesecurity_code) #this kills the error after 2000ms

                        #this checks if the variable card_correct equals True
                        if self.card_correct==True:

                            #this selects name_on_card from the table cards
                            cursor.execute("""SELECT name_on_card FROM cards""")
                            #this saves the results
                            self.cardids=cursor.fetchall()
                            #this sets the variable cardid_number to the length of cardids + 1
                            self.cardid_number=len(self.cardids)+1
                            #this selects ticketid from the tickets table
                            cursor.execute("""SELECT ticketid FROM tickets""")
                            #this saves the results
                            self.id=cursor.fetchall()
                            #this sets the variable ids to the length of id + 1
                            self.ids=len(self.id)+1
                            #this inserts the card details into the database and saves the database
                            cursor.execute("""INSERT into cards (cardid, name_on_card, card_number, security_code, month, year, type_of_card, ticketid)VALUES (?,?,?,?,?,?,?,?)""", (self.cardid_number, str(self.card_name.get()), self.card_number.get(), self.security_code.get(),self.variable.get(), self.variable1.get(), self.variable2.get(), self.ids))
                            db.commit()
                            #this raises the window
                            collect_ticket.attributes("-topmost", 1)
                            #this calls the function ticket_num
                            ticket_num()
                            #this lowers the window
                            payment.attributes("-topmost", 0)
                            
                def option_changed(*args): #this is a function

                    import datetime #this imports the module datetime

                    #this sets the variable now to the current date
                    self.now=datetime.datetime.now()

                    try:
                                                                                                                                                                                  
                        #this checks if the current year is equal to the year inputted
                        if int(self.now.year)==int(format(self.variable1.get())):

                            #this checks if the current month is bigger than the month inputted
                            if int(self.now.month)>int(format(self.variable.get())):

                                #this sets the variable date_correct to False
                                self.date_correct=False

                            else:

                                #this sets the variable date_correct to True
                                self.date_correct=True

                        #this checks if the current year is bigger than the year inputted
                        elif int(self.now.year)>int(format(self.variable1.get())):

                            #this sets the variable date_correct to False
                            self.date_correct=False

                        else:

                            #this sets the variable date_correct to True
                            self.date_correct=True

                    except(Exception):

                        pass
            
                def option_changed1(*args): #this is a function
                    
                    import datetime #this imports the module datetime
                    #this sets the variable now to the current date
                    self.now=datetime.datetime.now()
                        
                    try:
                        
                        #this checks if the current year is equal to the year inputted
                        if int(self.now.year)==int(format(self.variable1.get())):

                            #this checks if the current month is bigger than the month inputted
                            if int(self.now.month)>int(format(self.variable.get())):

                                #this sets the variable date_correct to False
                                self.date_correct=False

                            else:

                                #this sets the variable date_correct to True
                                self.date_correct=True

                        #this checks if the current year is bigger than the year inputted
                        elif int(self.now.year)>int(format(self.variable1.get())):

                            #this sets the variable date_correct to False
                            self.date_correct=False

                        else:

                            #this sets the variable date_correct to True
                            self.date_correct=True

                    except(Exception):

                        pass

                def option_changed2(*args): #this is a function
                    
                    pass

                #this sets the variable date_correct to False 
                self.date_correct=False
                #this links the window to the class
                self.payment = payment
                #this raises the window to the top
                payment.overrideredirect(1)
                #this resizes the window
                payment.geometry("%dx%d+0+0" % (w, h))
                #this removes the top bar of the window
                payment.resizable(width = False, height = False)
                #this creates the background for the window
                self.bg_image= PhotoImage(file="menu_bg.gif") 
                self.bg=Label(payment, image=self.bg_image, bg="black")
                self.bg.grid()
                #this creates a white box on the window
                self.white=Label(payment, bg="white", width=165, height=43)
                self.white.place(relx=0.077, rely=0.09)
                #this creates a title for window
                self.title=Label(payment, text="Please enter your card details", font=("Courier", 35), bg="white")
                self.title.place(relx=0.2, rely=0.11)
                self.type_of_card_label=Label(payment, width=12, bg="white", fg="black", font=("Courier", 25), text="Type of card")
                self.type_of_card_label.place(relx=0.15, rely=0.22)
                #this creates the type of card dropdown
                self.variable2 = StringVar(payment)
                self.variable2.set("None")
                self.variable2.trace("w", option_changed2)
                self.type_card=OptionMenu(payment, self.variable2,"Mastercard","Visa","Amex")
                self.type_card.configure(font=("Courier", 20), fg="white", bg="black",  width=13, height=1)
                self.type_card.place(relx=0.35, rely=0.22)
                #this creates the entry boxes
                self.card_name=Entry(payment, bd=20, width=50, bg="black", fg="white", insertbackground="white", font=("Courier", 10)) 
                self.card_name_label=Label(payment, width=12, bg="white", fg="black", font=("Courier", 25), text="Name on card")
                self.card_number_label=Label(payment, width=12, bg="white", fg="black", font=("Courier", 25), text="Card number")
                self.security_code_label=Label(payment, width=13, bg="white", fg="black", font=("Courier", 25), text="Security code")
                self.card_number=Entry(payment, bd=20, width="50", bg="black", fg="white", insertbackground="white", font=("Courier", 10))
                self.security_code=Entry(payment, bd=20, width="10", bg="black", fg="white", insertbackground="white", font=("Courier", 10))
                #this makes the image that says what cards we accept
                self.card_safety_pic=PhotoImage(file="card_safety.gif")
                self.card_safety=Label(payment, image=self.card_safety_pic, bg="white")
                self.card_safety.place(relx=0.63, rely=0.68)
                #this creates the month and year dropdown
                self.variable = StringVar(payment)
                self.variable.set(  "Month"  )
                self.variable.trace("w", option_changed)
                self.variable1 = StringVar(payment)
                self.variable1.set(  "Year"  )
                self.variable1.trace("w", option_changed1)
                self.month=OptionMenu(payment, self.variable,"01"  ,  "02"   ,  "03"  ,  "04"  ,  "05"  ,  "06"  ,  "07"  ,  "08"  ,  "09"  ,  "10"  ,  "11"  ,  "12"  )
                self.month.configure(font=("Courier", 20), fg="white", bg="black",  width=5, height=1)
                self.year=OptionMenu(payment, self.variable1, "2018" , "2019" , "2020" , "2021" , "2022" , "2023" , "2024" , "2025" , "2026" )
                self.year.configure(font=("Courier", 20), fg="white", bg="black",  width=5, height=1)
                self.card_expiration_date=Label(payment, width=15, bg="white", fg="black", font=("Courier", 25), text="Expiration date")
                #this creates a done button
                self.submit_btn= Button(payment, text="Done", width="20", height="3", command=submit_selected)
                self.submit_btn.configure(font=("Courier", 15), fg="white", bg="black")
                self.submit_btn.place(relx=0.4, rely=0.81)
                self.card_name.place(relx=0.35, rely=0.29)
                self.card_name_label.place(relx=0.15, rely=0.3)
                self.card_number_label.place(relx=0.14, rely=0.41)
                self.security_code_label.place(relx=0.148, rely=0.52)
                self.card_number.place(relx=0.35, rely=0.4)
                self.security_code.place(relx=0.35, rely=0.51)
                self.month.place(relx=0.35, rely=0.6)
                self.year.place(relx=0.46, rely=0.6)
                self.card_expiration_date.place(relx=0.12, rely=0.6)
                
                def keybu(): #this is a function
                    
                    keyboard.deiconify() #this unhides the keyboard

                #this creates the keyboard button
                self.keybut=Button(payment, text="keyboard", command=keybu,font=("Courier", 20), fg="white", bg="black")
                self.keybut.place(relx=0.81, rely=0.83)


        class enter_signup_class: #this is a class for the sign-up page
            
            def __init__(self, enter_signup): #this initialises the class

                self.signup=False #this sets the variable signup to False
                self.enter_signup = enter_signup #this links the window to the class
                enter_signup.overrideredirect(1) #this raises the window to the top
                enter_signup.geometry("%dx%d+0+0" % (w, h)) #this resizes the window
                enter_signup.resizable(width = False, height = False) #this removes the top bar from the window
                #this creates the databases
                cursor.execute("""CREATE TABLE IF NOT EXISTS films(filmid integer PRIMARY KEY,
                                  film text);""")
                cursor.execute("""CREATE TABLE IF NOT EXISTS time(timeid integar PRIMARY KEY,
                                  time text, screen integar, seats_left integar, filmid integer,
                                  FOREIGN KEY(filmid) REFERENCES films(filmid));""")
                cursor.execute("""CREATE TABLE IF NOT EXISTS seats(seatid integar PRIMARY KEY,
                                  xseats integer, yseats integer, timeid integar,
                                  FOREIGN KEY(timeid) REFERENCES time(timeid));""")
                cursor.execute("""CREATE TABLE IF NOT EXISTS tickets(ticketid integar AUTONUMBER PRIMARY KEY, username text,
                                  password text, email text ,
                                  aseats integer, price integar, seatid integar, FOREIGN KEY(seatid) REFERENCES seats(seatid)
                                  );""")
                cursor.execute("""CREATE TABLE IF NOT EXISTS cards(cardid integar AUTONUMBER PRIMARY KEY, name_on_card text,
                                  card_number integar, security_code integar,
                                  month text, year text, type_of_card text, ticketid integar, FOREIGN KEY(ticketid) REFERENCES tickets(ticketid)
                                  );""")
                cursor.execute("""SELECT film FROM films""") #this selects the films from the table films
                self.film_check=cursor.fetchall() #this saves the results
                
                if len(self.film_check)==0: #this checks if films table is empty

                    #this fills the database with the inital stuff
                    cursor.execute("""INSERT INTO films (filmid, film) VALUES (1, "Thor ragnarok")""")
                    cursor.execute("""INSERT INTO films (filmid, film) VALUES (2, "Baby driver")""")
                    cursor.execute("""INSERT INTO films (filmid, film) VALUES (3, "Dunkirk")""")
                    cursor.execute("""INSERT INTO films (filmid, film) VALUES (4, "Blade runner 2049")""")
                    cursor.execute("""INSERT INTO time (timeid, time, screen, seats_left, filmid) VALUES (1, "11:00", 2, 140, 1)""")
                    cursor.execute("""INSERT INTO time (timeid, time, screen, seats_left, filmid) VALUES (2, "13:00", 5, 140, 1)""")
                    cursor.execute("""INSERT INTO time (timeid, time, screen, seats_left, filmid) VALUES (3, "17:00", 10, 140, 1)""")
                    cursor.execute("""INSERT INTO time (timeid, time, screen, seats_left, filmid) VALUES (4, "21:00", 5, 140, 1)""")
                    cursor.execute("""INSERT INTO time (timeid, time, screen, seats_left, filmid) VALUES (5, "12:00", 4, 140, 2)""")
                    cursor.execute("""INSERT INTO time (timeid, time, screen, seats_left, filmid) VALUES (6, "14:00", 7, 140, 2)""")
                    cursor.execute("""INSERT INTO time (timeid, time, screen, seats_left, filmid) VALUES (7, "19:00", 2, 140, 2)""")
                    cursor.execute("""INSERT INTO time (timeid, time, screen, seats_left, filmid) VALUES (8, "22:00", 6, 140, 2)""")
                    cursor.execute("""INSERT INTO time (timeid, time, screen, seats_left, filmid) VALUES (9, "11:30", 3, 140, 3)""")
                    cursor.execute("""INSERT INTO time (timeid, time, screen, seats_left, filmid) VALUES (10, "15:30", 8, 140, 3)""")
                    cursor.execute("""INSERT INTO time (timeid, time, screen, seats_left, filmid) VALUES (11, "18:00", 1, 140, 3)""")
                    cursor.execute("""INSERT INTO time (timeid, time, screen, seats_left, filmid) VALUES (12, "20:30", 4, 140, 3)""")
                    cursor.execute("""INSERT INTO time (timeid, time, screen, seats_left, filmid) VALUES (13, "10:30", 1, 140, 4)""")
                    cursor.execute("""INSERT INTO time (timeid, time, screen, seats_left, filmid) VALUES (14, "13:30", 6, 140, 4)""")
                    cursor.execute("""INSERT INTO time (timeid, time, screen, seats_left, filmid) VALUES (15, "16:45", 9, 140, 4)""")
                    cursor.execute("""INSERT INTO time (timeid, time, screen, seats_left, filmid) VALUES (16, "20:00", 3, 140, 4)""")
                    
                self.bg_image = PhotoImage(file="menubg_8.gif") #this sets the variable bg_image to an image
                #this creates a label for the background
                self.bg = Label(enter_signup, image=self.bg_image, bg="black")
                self.bg.grid()
                #this creates the entry boxes
                self.username=Entry(enter_signup, bd=20, width="105", bg="black", fg="white", insertbackground="white", font=("Courier", 10))
                self.username.place(relx=0.2054, rely=0.2)
                self.password=Entry(enter_signup, bd=20, show="*",width="105", bg="black", fg="white", insertbackground="white", font=("Courier", 10))
                self.password.place(relx=0.2054, rely=0.34)
                self.passwordcon=Entry(enter_signup,show="*", bd=20, width="105", bg="black", fg="white", insertbackground="white", font=("Courier", 10))
                self.passwordcon.place(relx=0.2054, rely=0.5)
                self.email=Entry(enter_signup, bd=20, width="105", bg="black", fg="white", insertbackground="white", font=("Courier", 10))
                self.email.place(relx=0.2054, rely=0.72)

                def sumbit_selected(): #this is a function

                    countdown.attributes("-topmost", 1) #this raises the window
                    self.signup=True #this sets th variable signup to True
                    self.username1=str(format(self.username.get())) #this sets the variable username1 to what is in the username entry box
                    username2=str(format(self.username.get())) #this sets the variable username2 to what is in the username entry box
                    cursor.execute("""SELECT username FROM tickets""") #this gets the usernames from the database
                    self.resultuser = cursor.fetchall() #this saves the results
                    self.final_resultuser = [i[0] for i in self.resultuser] #this puts the results into a list
                    self.lengthuser = len(self.final_resultuser) #this sets the variable lengthuser to the length of final_resultuser
                    self.checkuser = 0 #this sets the variable checkuser to 0
                    #this sets the password1 to what is inputted into the password entry box
                    self.password1=str(format(self.password.get()))
                    #this sets the is_valid to if the email is valid
                    self.is_valid = validate_email(self.email.get())
                    #this sets the password1 to what is inputted into the password entry box
                    self.email_changed=str(format(self.email.get()))
                    self.usercheck=0 #this sets the variable usercheck to 0
                    #this sets the variable username_taken_error to False
                    self.username_taken_error=False
                    
                    for i in range(self.lengthuser): #this loops untils i equals to lengthuser

                        #this checks if username1 equals i number in the list final_resultuser
                        if self.username1==str(self.final_resultuser[i]):

                            #this raises the window
                            countdown.attributes("-topmost", 1)
                            #this sets the variable username_taken_error to True 
                            self.username_taken_error=True

                    #this checks if username_taken_error equals True
                    if self.username_taken_error==True:

                        #this raises the window
                        countdown.attributes("-topmost", 1)
                        #this displays the error
                        self.fakeuser=Label(enter_signup, bg="red", font=("Courier", 15), text="Username is taken", width=120)
                        self.fakeuser.place(relx=0, rely=0)
                                    
                        def kill_fakeuser():

                            self.fakeuser.place_forget()
                            
                        self.usercheck=1 #this sets the variable usercheck to 1
                        self.fakeuser.after(2000, kill_fakeuser) #this kills the error after 2000ms

                    #this checks if the entry box are empty
                    if self.username.index("end") == 0 or self.password.index("end")==0 or self.passwordcon.index("end")==0 or self.email.index("end")==0:

                        #this raises the window
                        countdown.attributes("-topmost", 1)
                        #this displays the error
                        self.empty=Label(enter_signup, text="Please enter all fields", width=120, bg="red", font=("Courier", 15))
                        self.empty.place(relx=0, rely=0)
                        
                        def kill_empty():
                                        
                            self.empty.place_forget()
                                        
                        self.empty.after(2000, kill_empty) #this kills the error after 2000ms
                        

                    #this checks if the the passwords match
                    elif self.password.get()!= self.passwordcon.get():

                        #this raises the window
                        countdown.attributes("-topmost", 1)
                        #this displays the error
                        self.copy_error=Label(enter_signup, text="Passwords do not match", width=120, bg="red", font=("Courier", 15))
                        self.copy_error.place(relx=0,rely=0)

                        def kill_copy_error():
                                        
                            self.copy_error.place_forget()
                                        
                        self.copy_error.after(2000, kill_copy_error) #this kills the error after 2000ms

                    #this checks if the variable is_valid is False
                    elif self.is_valid==False:

                        #this raises the window
                        countdown.attributes("-topmost", 1)
                        #this displays the error
                        self.fakeemail=Label(enter_signup, text="please enter valid email", width=120, bg="red", font=("Courier", 15))
                        self.fakeemail.place(relx=0,rely=0)

                        def kill_fakeemail():
                                        
                            self.fakeemail.place_forget()
                                        
                        self.fakeemail.after(2000, kill_fakeemail) #this kills the error after 2000ms

                    #this checks if checkuser equals 0 and usercheck equals 0
                    elif self.checkuser==0 and self.usercheck==0:

                        #this sets variable price to the variable tot from the class Ticket
                        self.price=Ticket.tot
                        #this gets the usernames from the database
                        cursor.execute("""SELECT username FROM tickets""")
                        #this saves the results
                        idlength=cursor.fetchall()
                        self.id=len(idlength)+1 #this  sets a variable id to the length of idlength+1
                        cursor.execute("""SELECT xseats FROM seats""") #this gets the xseats from the database
                        idslength=cursor.fetchall() #this saves the results
                        self.ids=len(idslength)+1 #this  sets a variable ids to the length of idlength+1
                        #this inserts the infomation into the database and saves the database
                        cursor.execute("""INSERT INTO tickets (ticketid, username, password, email, aseats, price, seatid)VALUES (?,?,?,?,?,?,?)""",(self.id, str(self.username1),str(self.password1),str(self.email_changed), int(Ticket.aseats), str(self.price), self.ids))
                        db.commit()
                        self.length=len(xseats) #this sets the variable length to the length of xseats

                        for i in range(self.length): #this loops until i equals length
                            
                            if i==0: #this checks if i equals 0
                                
                                cursor.execute("""INSERT INTO seats (seatid, xseats, yseats, timeid)VALUES (?,?,?,?)""",(self.ids, int(xseats[i]),int(yseats[i]), int(menu.timeid)))

                            else:
                                
                                self.ids+=1 #this increases the variable ids by 1
                                #this inserts the seats information
                                cursor.execute("""INSERT INTO seats (seatid, xseats, yseats, timeid)VALUES (?,?,?,?)""",(self.ids, int(xseats[i]),int(yseats[i]), int(menu.timeid)))

                        db.commit() #this saves the database
                        payment.attributes("-topmost", 1) #this raises the window
                        menu.page_number=9 #this sets the variable page_number to 9
                        enter_signup.attributes("-topmost", 0) #this raises the window
                        menu.seats_left-=Ticket.aseats #this decreases the seats left by aseats
                        #this updates the database and saves
                        cursor.execute("""UPDATE time SET seats_left=? WHERE timeid=?""", (menu.seats_left, menu.timeid,))
                        db.commit()

                #this makes a done button
                self.submit_btn=Button(enter_signup, text="Done", width="20", height="3", command=sumbit_selected, font=("Courier", 15), fg="white", bg="black") 
                self.submit_btn.place(relx=0.4, rely=0.84)
                
                def back_to_menu(): #this is a function

                    pick_login.attributes("-topmost", 1) #this raises the window
                    self.signup=False #this sets the variable signup to False
                    self.username.destroy() #this destroys the entry box
                    self.password.destroy() #this destroys the entry box
                    self.passwordcon.destroy() #this destroys the entry box
                    menu.page_number=6 #this sets the page_number to 6
                    self.email.destroy() #this destroys the entry box
                    #this creates the entry boxes
                    self.username=Entry(enter_signup, bd=20, width="105", bg="black", fg="white", insertbackground="white", font=("Courier", 10))
                    self.username.place(relx=0.2054, rely=0.2)
                    self.password=Entry(enter_signup, bd=20, show="*",width="105", bg="black", fg="white", insertbackground="white", font=("Courier", 10))
                    self.password.place(relx=0.2054, rely=0.34)
                    self.passwordcon=Entry(enter_signup,show="*", bd=20, width="105", bg="black", fg="white", insertbackground="white", font=("Courier", 10))
                    self.passwordcon.place(relx=0.2054, rely=0.5)
                    self.email=Entry(enter_signup, bd=20, width="105", bg="black", fg="white", insertbackground="white", font=("Courier", 10))
                    self.email.place(relx=0.2054, rely=0.72)                
                    enter_login.attributes("-topmost", 0) #this lowers the window
                    try:
                        Countdown.display_time_film_select.destroy() #this destroys the window

                    except(Exception):
                        pass
                    try:
                        Countdown.display_time_seconds_film_select.destroy() #this destroys the window
                    except(Exception):
                        pass
                    Countdown.timer() #this calls the function timer
                    countdown.attributes("-topmost", 1) #this raises the window

                    try:

                        self.fakeuser.destroy() #this destroys the error

                    except(Exception):
                        
                        pass
                    
                    try:
                        
                        self.empty.destroy() #this destroys the error

                    except(Exception):
                        
                        pass

                    try:
                        
                        self.copy_error.destroy() #this destroys the error

                    except(Exception):
                        
                        pass

                    try:
                        
                        self.fakeemail.destroy() #this destroys the error

                    except(Exception):
                        
                        pass

                    try:
                        
                        self.fakepass.destroy() #this destroys the error

                    except(Exception):
                        
                        pass

                #this makes a back button
                self.back_button=Button(enter_signup, text="Back", command=back_to_menu)
                self.back_button.configure(font=("Courier", 20), fg="white", bg="black")
                self.back_button.place(relx=0.01, rely=0.01)
                
                def keybu(): #this is a function
                    
                    keyboard.deiconify() #this unhides the keyboard
                    try:
                        Countdown.display_time_film_select.destroy() #this destroys the error

                    except(Exception):
                        pass
                    try:
                        Countdown.display_time_seconds_film_select.destroy() #this destroys the error
                    except(Exception):
                        pass
                    Countdown.timer() #this calls the function timer
                    countdown.attributes("-topmost", 1) #this raises the window

                #this makes the keyboard button
                self.keybut=Button(enter_signup, text="keyboard", command=keybu,font=("Courier", 20), fg="white", bg="black")
                self.keybut.place(relx=0.82, rely=0.82)
                
                
        class login_class: #this is the class for the login page

            def __init__(self, enter_login): #this initialises the class

                self.enter_login = enter_login #this links the window to the class
                enter_login.overrideredirect(1) #this raises the window to the top
                enter_login.geometry("%dx%d+0+0" % (w, h)) #this resizes the window
                enter_login.resizable(width = False, height = False) #this removes the top bar from the window
                self.login_bg_image = PhotoImage(file="login_1.gif") #this sets the variable login_bg_image to an image
                #this creates the background
                self.login_bg = Label(enter_login, image=self.login_bg_image, bg="black")
                self.login_bg.grid()
                
                def callback(event):#this is a function
                    
                    countdown.attributes("-topmost", 1) #this raises the window
                    
                self.login_bg.bind("<Button-1>", callback) #this links the label to the function
                self.enter_track = 0 #this sets the variable enter_track to 0
                self.shift_track = 0 #this sets the variable shift_track to 0
                #this creates the username and password entry boxes
                self.username=Entry(enter_login, bd=25, width="105", bg="black", fg="white", insertbackground="white", font=("Courier", 10))
                self.username.place(relx=0.24, rely=0.29)
                self.password=Entry(enter_login, bd=25, show="*", width="105", bg="black", fg="white", insertbackground="white", font=("Courier", 10))
                self.password.place(relx=0.24, rely=0.5)
                self.username_track = int(len(self.username.get())) #this sets the variable username_track to the length of the username entry box
                self.password_track = int(len(self.password.get())) #this sets the variable username_track to the length of the password entry box

                def submit_selected(): #this is a function

                    countdown.attributes("-topmost", 1) #this raises the function
                    cursor.execute("""SELECT username FROM tickets""") #this selects usernames from the table tickets
                    self.user_login = cursor.fetchall() #this saves the results
                    self.final_user_login = [i[0] for i in self.user_login] #this puts the results into a list
                    self.user_found=False #this sets the variable user_found to False
                    self.user_real=False #this sets the variable user_real to False
                    
                    
                    for i in range(len(self.final_user_login)): #loops until i equals the length of the variable final_user_login

                        #this checks if username the customer enters is in the database
                        if str(format(self.username.get()))==self.final_user_login[i]:

                            self.user_found=True #this sets the variable user_found to True
                             #this sets the variable user_login to the user that matches the username the customer entered
                            self.user_login=str(format(self.final_user_login[i]))

                    if self.user_found==True: #this checks if the user_found equals True

                        #this gets the password associated with the username from the database
                        cursor.execute("""SELECT password FROM tickets WHERE username=?""", (self.user_login,))
                        self.password_login = cursor.fetchall() #this saves the results
                        self.final_password_login = [i[0] for i in self.password_login] #this puts the results into a list
                        self.password_login = str(format(self.final_password_login[0])) #this takes the first thing in in the list

                        #this checks if the password entered matches the password from the database
                        if str(format(self.password.get()))==str(self.password_login):

                            self.user_real=True #this sets the variable user_real to True

                    if self.user_real==True: #if user_real equals True

                        #this gets the email from that account
                        cursor.execute(""" SELECT email FROM tickets WHERE username=?""", (self.username.get(),))
                        self.email_changed=str(format(cursor.fetchall())) #this saves the results
                        username2=str(format(self.username.get())) #this sets the username entered to the variable username2
                        self.price=Ticket.tot #this gets the total price of tickets
                        cursor.execute("""SELECT username FROM tickets""") #this gets the usernames from the database
                        idlength=cursor.fetchall() #this saves the results
                        self.id=len(idlength)+1 #this sets the variable id to the length of idlength+1
                        cursor.execute("""SELECT xseats FROM seats""") #this gets the xseats from the database
                        idslength=cursor.fetchall() #this saves the results
                        self.ids=len(idslength)+1 #this sets the variable ids to the length of idlength+1
                        #this inserts the ticketid, username, password, email, aseats, price, seatid into the database
                        cursor.execute("""INSERT INTO tickets (ticketid, username, password, email, aseats, price, seatid)VALUES (?,?,?,?,?,?,?)""",(self.id, str(self.user_login), str(self.password_login), str(self.email_changed), int(Ticket.aseats), str(self.price), self.ids))
                        db.commit() #this saves the database
                        self.length=len(xseats) #this sets the variable length to the length of the list xseats

                        for i in range(self.length): #this loops until i equals the value of the variable length

                            if i==0: #if the variable i equals 0

                                #this inserts the seatid, xseats, yseats, timeid into the database
                                cursor.execute("""INSERT INTO seats (seatid, xseats, yseats, timeid)VALUES (?,?,?,?)""",(self.ids, int(xseats[i]),int(yseats[i]), int(menu.timeid)))

                            else:

                                self.ids+=1 #this increases the variable ids by 1
                                #this inserts the seatid, xseats, yseats, timeid into the database
                                cursor.execute("""INSERT INTO seats (seatid, xseats, yseats, timeid)VALUES (?,?,?,?)""",(self.ids, int(xseats[i]),int(yseats[i]), int(menu.timeid)))

                        db.commit() #this saves the database
                        cursor.execute("""SELECT * FROM seats""") #this gets everything from the seats table
                        payment.attributes("-topmost", 1) #this raises the window
                        menu.page_number=9 #this sets the variable page_number from the class menu to 9
                        enter_login.attributes("-topmost", 0) #this lowers the window
                        menu.seats_left-=Ticket.aseats #this decreases the variable seats_left by the variable aseats from the class Ticket
                        #this update the number of seats available for that showing and saves it to the database
                        cursor.execute("""UPDATE time SET seats_left=? WHERE timeid=?""", (menu.seats_left, menu.timeid,))
                        db.commit()

                    else:

                        #this creates an error and after 2000ms it destroys it
                        self.not_found=Label(enter_login, text="login not recognised", font=("Courier", 15), fg="white", bg="black")
                        self.not_found.place(relx=0.4, rely=0.8)

                        def kill_not_found():
                                        
                            self.not_found.place_forget()
                                        
                        self.not_found.after(2000, kill_not_found)
                    

                #this creates a button when the customer is done with this page
                self.submit_btn=Button(enter_login, text="Done", width="20", height="3", command=submit_selected, font=("Courier", 15), fg="white", bg="black") 
                self.submit_btn.place(relx=0.4, rely=0.84)
                
                def keybu(): #this is a function
                    
                    keyboard.deiconify() #this uncovers the keyboard
                    try:
                        Countdown.display_time_film_select.destroy() #this destroys the window
                                                                                                                                                                                    
                    except(Exception):
                        pass
                    try:
                        Countdown.display_time_seconds_film_select.destroy() #this destroys the window
                    except(Exception):
                        pass
                    Countdown.timer() #this calls the function timer from the class Countdown
                    countdown.attributes("-topmost", 1) #this raises the window
                    
                self.keybut=Button(enter_login, text="keyboard", command=keybu,font=("Courier", 20), fg="white", bg="black")
                self.keybut.place(relx=0.8, rely=0.8)

                def back_to_menu(): #this is a function

                    pick_login.attributes("-topmost", 1) #this raises the window
                    self.username.destroy() #this destroys the entry box
                    self.password.destroy() #this destroys the entry box
                    menu.page_number=6 #this sets the variable page_number from the class menu to 6
                    self.enter_track = 0 #this sets the variable enter_track to 0
                    self.shift_track = 0 #this sets the variable shift_track to 0
                    #this creates the username and password entry boxes
                    self.username=Entry(enter_login, bd=25, width="105", bg="black", fg="white", insertbackground="white", font=("Courier", 10))
                    self.username.place(relx=0.24, rely=0.29)
                    self.password=Entry(enter_login, bd=25, show="*", width="105", bg="black", fg="white", insertbackground="white", font=("Courier", 10))
                    self.password.place(relx=0.24, rely=0.5)
                    enter_login.attributes("-topmost", 0) #this lowers the window
                    try:
                        Countdown.display_time_film_select.destroy() #this destroys the window

                    except(Exception):
                        pass
                    try:
                        Countdown.display_time_seconds_film_select.destroy() #this destroys the window
                    except(Exception):
                        pass
                    Countdown.timer() #this calls the function timer from the class Countdown
                    countdown.attributes("-topmost", 1) #this raises the window
                    
                    try:

                        self.not_found.destroy() #this destroys the error

                    except(Exception):
                        
                        pass                    

                #this creates a back button to the previous page
                self.back_button=Button(enter_login, text="Back", command=back_to_menu)
                self.back_button.configure(font=("Courier", 20), fg="white", bg="black")
                self.back_button.place(relx=0.01, rely=0.01)
                
        class keyboard_class: #this is the class for the keyboard

            def __init__(self, keyboard): #this is to initialise the class

                keyboard.resizable(0,0)
                keyboard.geometry("%dx%d+0+0" % (888, 450)) #this resizes the window
                keyboard.overrideredirect(1) #this raises the window to the top
                
                def user(event): #this is a function
                    
                    try:
                        
                        countdown.attributes("-topmost", 1) #this raises the window
                        keyboard.attributes("-topmost", 1) #this raises the window
                        
                    except(Exception):
                        
                        pass

                    #this sets the variable enter_track from the class Enter to the variable username from the class Enter
                    Enter.enter_track=Enter.username
                #this binds the entry box to a function
                Enter.username.bind("<FocusIn>", user)
                
                def user1(event): #this is a function

                    countdown.attributes("-topmost", 1) #this raises the window
                    keyboard.attributes("-topmost", 1) #this raises the window
                    #this sets the variable enter_track from the class Enter to the variable password from the class Enter
                    Enter.enter_track=Enter.password
                #this binds the entry box to a function
                Enter.password.bind("<FocusIn>", user1)

                def user2(event): #this is a function

                    countdown.attributes("-topmost", 1) #this raises the window
                    keyboard.attributes("-topmost", 1) #this raises the window
                    #this sets the variable enter_track from the class Enter to the variable username from the class Enter_signup
                    Enter.enter_track=Enter_signup.username

                #this binds the entry box to a function
                Enter_signup.username.bind("<FocusIn>", user2)

                def user3(event): #this is a function

                    countdown.attributes("-topmost", 1) #this raises the window
                    keyboard.attributes("-topmost", 1) #this raises the window
                    #this sets the variable enter_track from the class Enter to the variable password from the class Enter_signup
                    Enter.enter_track=Enter_signup.password

                #this binds the entry box to a function
                Enter_signup.password.bind("<FocusIn>", user3)

                def user4(event): #this is a function

                    countdown.attributes("-topmost", 1) #this raises the window
                    keyboard.attributes("-topmost", 1) #this raises the window
                    #this sets the variable enter_track from the class Enter to the variable passwordcon from the class Enter_signup
                    Enter.enter_track=Enter_signup.passwordcon

                #this binds the entry box to a function
                Enter_signup.passwordcon.bind("<FocusIn>", user4)

                def user5(event): #this is a function

                    countdown.attributes("-topmost", 1) #this raises the window
                    keyboard.attributes("-topmost", 1) #this raises the window
                    #this sets the variable enter_track from the class Enter to the variable email from the class Enter_signup
                    Enter.enter_track=Enter_signup.email

                #this binds the entry box to a function
                Enter_signup.email.bind("<FocusIn>", user5)

                def user6(event): #this is a function

                    keyboard.attributes("-topmost", 1) #this raises the window
                    #this sets the variable enter_track from the class Enter to the variable card_name from the class pay
                    Enter.enter_track=pay.card_name

                #this binds the entry box to a function
                pay.card_name.bind("<FocusIn>", user6)

                def user7(event): #this is a function

                    keyboard.attributes("-topmost", 1) #this raises the window
                    #this sets the variable enter_track from the class Enter to the variable card_number from the class pay
                    Enter.enter_track=pay.card_number

                #this binds the entry box to a function
                pay.card_number.bind("<FocusIn>", user7)

                def user8(event): #this is a function

                    keyboard.attributes("-topmost", 1) #this raises the window
                    #this sets the variable enter_track from the class Enter to the variable security_code from the class pay
                    Enter.enter_track=pay.security_code

                #this binds the entry box to a function
                pay.security_code.bind("<FocusIn>", user8)

                def keyh(): #this is a function

                    try:
                        Countdown.display_time_film_select.destroy() #this destroys the window

                    except(Exception):
                        pass
                    try:
                        Countdown.display_time_seconds_film_select.destroy() #this destroys the window
                    except(Exception):
                        pass
                    Countdown.timer() #this calls the function timer from the class Countdown
                    countdown.attributes("-topmost", 1) #this raises the window
                    keyboard.withdraw() #this hides the window

                def move_window(event): #this is a function

                    if menu.page_number>8: #this checks if the page_number is bigger than 8
                        
                        pass
                    
                    else:
                        
                            try:
                                Countdown.display_time_film_select.destroy() #this destroys the window

                            except(Exception):
                                pass
                            try:
                                Countdown.display_time_seconds_film_select.destroy() #this destroys the window
                            except(Exception):
                                pass
                            Countdown.timer() #this calls the function timer from the class Countdown
                            countdown.attributes("-topmost", 1) #this raises the window
                            
                    keyboard.geometry('+{0}+{1}'.format(event.x_root, event.y_root)) #this links the window to the label

                #this makes a title bar
                self.title_bar = Label(keyboard, bg='black', width=300, height=2)
                self.title_bar.place(relx=0, rely=0)
                self.title_bar.bind('<B1-Motion>', move_window)
                #this makes a delete button on the window
                self.X = Button(keyboard, text="X", width=3, height=1, command=keyh, borderwidth=0, font=("Calibri (Body)", 15), fg="white", bg="black")
                self.X.place(relx=0.96, rely=0)
                #this creates a frame
                self.frame1=Frame(keyboard, width=1000, height=300)
                self.frame1.config(bg="black")
                self.frame1.place(relx=0, rely=0.082)
                
                def back_selected(): #this is a function

                    if menu.page_number>8: #this checks if the page_number is bigger than 8
                        
                        pass
                    
                    else:
                        
                            try:
                                Countdown.display_time_film_select.destroy() #this destroys the window

                            except(Exception):
                                pass
                            try:
                                Countdown.display_time_seconds_film_select.destroy() #this destroys the window
                            except(Exception):
                                pass
                            Countdown.timer() #this calls the function timer from the class Countdown
                            countdown.attributes("-topmost", 1) #this raises the window
                            
                    #this sets the variable track to equal the length of Enter.enter_track.get()
                    track=len(Enter.enter_track.get())
                    Enter.enter_track.delete(track-1) #this deletes the last thing in the entry box
                    Enter.enter_track.icursor(track-1) #this moves the cursor back a space
                        
                def space_selected(): #this is a function

                    if menu.page_number>8: #this checks if the page_number is bigger than 8
                        
                        pass
                    
                    else:
                        
                            try:
                                Countdown.display_time_film_select.destroy() #this destroys the window

                            except(Exception):
                                pass
                            try:
                                Countdown.display_time_seconds_film_select.destroy() #this destroys the window
                            except(Exception):
                                pass
                            Countdown.timer() #this calls the function timer from the class Countdown
                            countdown.attributes("-topmost", 1) #this raises the window

                    #this sets the variable track to equal the length of Enter.enter_track.get()
                    track=len(Enter.enter_track.get())
                    Enter.enter_track.insert(track, " ") #this inserts into the entry box a space
                    Enter.enter_track.icursor(track+1) #this moves the entry box one space forward
                    
                def shift_selected(): #this is a function

                    if menu.page_number>8: #this checks if the page_number is bigger than 8
                        
                        pass
                    
                    else:
                        
                            try:
                                Countdown.display_time_film_select.destroy() #this destroys the window

                            except(Exception):
                                pass
                            try:
                                Countdown.display_time_seconds_film_select.destroy() #this destroys the window
                            except(Exception):
                                pass
                            Countdown.timer() #this calls the function timer from the class Countdown
                            countdown.attributes("-topmost", 1) #this raises the window
                            
                    if Enter.shift_track==0: #this checks if shift_track is equal to 0

                        #this changes the button image
                        Keyboard.shift_off.config(image=Keyboard.shift_on_image, bg="white")
                        self.text11=[] #this sets the variable text11 to a empty list
                        Keyboard.text1=["!",'"',"£","$","%","^","&","*","(",")"] #this sets the variable text1 to the list
                        Keyboard.text2=["q","w","e","r","t","y","u","i","o","p"] #this sets the variable text2 to the list
                        Keyboard.text3=["a","s","d","f","g","h","j","k","l","@"] #this sets the variable text3 to the list
                        Keyboard.text4=["z","x","c","v","b","n","m","<",">","/"] #this sets the variable text4 to the list
                        self.text11.append(Keyboard.text1) #this adds text1 to the list text11
                        self.text11.append(Keyboard.text2) #this adds text2 to the list text11
                        self.text11.append(Keyboard.text3) #this adds text3 to the list text11
                        self.text11.append(Keyboard.text4) #this adds text4 to the list text11
                        self.btn1=[[0 for x in range(4)] for x in range(10)] #this creates a array of buttons
                        
                        for x in range(10): #this loops until x equals 10
                            
                            for y in range(4): #this loops until y equals 4

                                #this creates a button                                
                                self.btn1[x][y] = Button(self.frame1,command= lambda x2=x, y2=y: color_change2(x2,y2), width=4, height=2, bg="black", text=self.text11[y][x].title(), font=("Courier", 20), fg="white")
                                                                                                                                                                                        
                                if y==1: #this checks if y equals 1
                                    
                                    x2=x+2 #this sets the variable x2 to x+2
                                    self.btn1[x][y].grid(column=x2, row=y) #this places the button in the array
                                    x2=x2-2 #this sets the variable x2 to x-2
                                    
                                elif y==2: #this checks if y equals 2
                                    
                                    x2=x+1 #this sets the variable x2 to x+1
                                    self.btn1[x][y].grid(column=x2, row=y)
                                    x2=x2-1 #this sets the variable x2 to x-1
                                    
                                elif y==3: #this checks if y equals 3
                                    
                                    x2=x+1 #this sets the variable x2 to x+1
                                    self.btn1[x][y].grid(column=x2, row=y)
                                    x2=x2-1 #this sets the variable x2 to x-1
                                    
                                else:
                                    
                                    self.btn1[x][y].grid(column=x, row=y) #this places the button on the frame
                                    
                        Keyboard.left_br.config(text="{") #this changes the text on the button
                        Keyboard.right_br.config(text="}") #this changes the text on the button
                        Keyboard.hash.config(text="~") #this changes the text on the button
                        Keyboard.minus.config(text="_") #this changes the text on the button
                        Keyboard.equals.config(text="+") #this changes the text on the button
                        Keyboard.sem.config(text=":") #this changes the text on the button
                        Keyboard.at.config(text="\\") #this changes the text on the button
                        Enter.shift_track=1 #this sets the variable shift_track from the class Enter to 1
                        
                    elif Enter.shift_track==1: #this checks if the variable shift_track from the class is equal to 1

                        #this changes the button image
                        Keyboard.shift_off.config(image=Keyboard.shift_off_image, bg="black")
                        Enter.shift_track=0 #this sets the variable shift_track from the class Enter to 0
                        self.text=[] #this creates a empty list called text
                        Keyboard.text1=["1","2","3","4","5","6","7","8","9","0"] #this sets the variable text1 to the list
                        Keyboard.text2=["q","w","e","r","t","y","u","i","o","p"] #this sets the variable text2 to the list
                        Keyboard.text3=["a","s","d","f","g","h","j","k","l","'"] #this sets the variable text3 to the list
                        Keyboard.text4=["z","x","c","v","b","n","m",",",".","?"] #this sets the variable text4 to the list
                        self.text.append(Keyboard.text1) #this adds text1 to the list text
                        self.text.append(Keyboard.text2) #this adds text2 to the list text
                        self.text.append(Keyboard.text3) #this adds text3 to the list text
                        self.text.append(Keyboard.text4) #this adds text4 to the list text
                        Keyboard.left_br.config(text="[") #this changes the text on the button
                        Keyboard.right_br.config(text="]") #this changes the text on the button
                        Keyboard.hash.config(text="#") #this changes the text on the button
                        Keyboard.minus.config(text="-") #this changes the text on the button
                        Keyboard.equals.config(text="=") #this changes the text on the button
                        Keyboard.sem.config(text=";") #this changes the text on the button
                        Keyboard.at.config(text="|") #this changes the text on the button
                        #this creates a array of buttons
                        self.btn1=[[0 for x in range(4)] for x in range(10)]
                        
                        for x in range(10): #this loops until x is equal to 10
                            
                            for y in range(4): #this loops until y is equal to 4

                                #this creates a button
                                self.btn1[x][y] = Button(self.frame1,command= lambda x2=x, y2=y: color_change2(x2,y2), width=4, height=2, bg="black", text=self.text[y][x], font=("Courier", 20), fg="white")

                                if y==1: #this checks if y equals to 1
                                    
                                    x2=x+2 #this sets the variable x2 to x+2 
                                    self.btn1[x][y].grid(column=x2, row=y)
                                    x2=x2-2 #this sets the variable x2 to x-2
                                    
                                elif y==2: #this checks if y equals to 2
                                    
                                    x2=x+1 #this sets the variable x2 to x+1
                                    self.btn1[x][y].grid(column=x2, row=y)
                                    x2=x2-1 #this sets the variable x2 to x-1
                                    
                                elif y==3: #this checks if y equals to 3
                                    
                                    x2=x+1 #this sets the variable x2 to x+1
                                    #this places the button on the frame
                                    self.btn1[x][y].grid(column=x2, row=y)
                                    x2=x2-1 #this sets the variable x2 to x-1
                                    
                                else:

                                     #this places the button on the frame
                                    self.btn1[x][y].grid(column=x, row=y)
                                    
                def at_selected(): #this is a function

                    if menu.page_number>8: #this checks if the page_number is bigger than 8

                        pass

                    else:
                        
                            try:
                                Countdown.display_time_film_select.destroy() #this detroys the window

                            except(Exception):
                                pass
                            try:
                                Countdown.display_time_seconds_film_select.destroy() #this detroys the window
                            except(Exception):
                                pass
                            Countdown.timer() #this calls the function timer from the class Countdown
                            countdown.attributes("-topmost", 1) #this raises the window

                    #this checks if shift_track is equal to 1 or if shift_track is equal to 2
                    if Enter.shift_track==1 or Enter.shift_track==2:

                        #this sets the variable track to the length of enter_track
                        track=len(Enter.enter_track.get())
                        #this inserts a \\ into the entry box
                        Enter.enter_track.insert(track, "\\")
                        #this moves the cursor forwards a space
                        Enter.enter_track.icursor(track+1)
                        shift_selected() #this calls a function called shift_selected
                            
                    else:

                        #this sets the variable track to the length of enter_track
                        track=len(Enter.enter_track.get())
                        #this inserts a | into the entry box
                        Enter.enter_track.insert(track, "|")
                        #this moves the cursor forwards a space
                        Enter.enter_track.icursor(track+1)
                                
                def left_br_selected(): #this is a function

                    #this checks if the page_number is bigger than 8
                    if menu.page_number>8:

                        pass

                    else:
                        
                            try:
                                 #this destroys the window                                
                                Countdown.display_time_film_select.destroy()

                            except(Exception):
                                pass
                            try:
                                 #this destroys the window
                                Countdown.display_time_seconds_film_select.destroy()
                            except(Exception):
                                pass
                             #this calls the function timer from the class Countdown
                            Countdown.timer()
                            #this raises the window
                            countdown.attributes("-topmost", 1)

                    #this checks if shift_track is equal to 1 or if shift_track is equal to 2
                    if Enter.shift_track==1 or Enter.shift_track==2:

                        #this sets the variable track to the length of enter_track
                        track=len(Enter.enter_track.get())
                        #this inserts a { into the entry box
                        Enter.enter_track.insert(track, "{")
                        #this moves the cursor forwards a space
                        Enter.enter_track.icursor(track+1)
                        shift_selected() #this calls the function shift_selected
                            
                    else:

                        #this sets the variable track to the length of enter_track
                        track=len(Enter.enter_track.get())
                        #this inserts a [ into the entry box
                        Enter.enter_track.insert(track, "[")
                        #this moves the cursor forwards a space
                        Enter.enter_track.icursor(track+1)
                                
                def right_br_selected(): #this is a function

                    #this checks if the page_number is bigger than 8
                    if menu.page_number>8:

                        pass

                    else:
                        
                            try:
                                 #this destroys the window                                
                                Countdown.display_time_film_select.destroy()

                            except(Exception):
                                pass
                            try:
                                 #this destroys the window
                                Countdown.display_time_seconds_film_select.destroy()
                            except(Exception):
                                pass
                             #this calls the function timer from the class Countdown
                            Countdown.timer()
                            #this raises the window
                            countdown.attributes("-topmost", 1)
                            
                    #this checks if shift_track is equal to 1 or if shift_track is equal to 2
                    if Enter.shift_track==1 or Enter.shift_track==2:

                        #this sets the variable track to the length of enter_track
                        track=len(Enter.enter_track.get())
                        #this inserts a } into the entry box
                        Enter.enter_track.insert(track, "}")
                        #this moves the cursor forwards a space
                        Enter.enter_track.icursor(track+1)
                        #this calls the function shift_selected
                        shift_selected()
                            
                    else:

                        #this sets the variable track to the length of enter_track
                        track=len(Enter.enter_track.get())
                        #this inserts a ] into the entry box
                        Enter.enter_track.insert(track, "]")
                        #this moves the cursor forwards a space
                        Enter.enter_track.icursor(track+1)
                        
                def hash_selected(): #this is a function

                    if menu.page_number>8:

                        pass

                    else:
                        
                            try:
                                 #this destroys the window                                
                                Countdown.display_time_film_select.destroy()

                            except(Exception):
                                pass
                            try:
                                 #this destroys the window
                                Countdown.display_time_seconds_film_select.destroy()
                            except(Exception):
                                pass
                             #this calls the function timer from the class Countdown
                            Countdown.timer()
                            #this raises the window
                            countdown.attributes("-topmost", 1)

                    #this checks if shift_track is equal to 1 or if shift_track is equal to 2     
                    if Enter.shift_track==1 or Enter.shift_track==2:

                        #this sets the variable track to the length of enter_track
                        track=len(Enter.enter_track.get())
                        #this inserts a ~ into the entry box
                        Enter.enter_track.insert(track, "~")
                        #this moves the cursor forwards a space
                        Enter.enter_track.icursor(track+1)
                        shift_selected()
                            
                    else:

                        #this sets the variable track to the length of enter_track
                        track=len(Enter.enter_track.get())
                        #this inserts a # into the entry box
                        Enter.enter_track.insert(track, "#")
                        #this moves the cursor forwards a space
                        Enter.enter_track.icursor(track+1)
                                
                def minus_selected(): #this is a function

                    if menu.page_number>8:

                        pass

                    else:
                        
                            try:
                                 #this destroys the window                                
                                Countdown.display_time_film_select.destroy()

                            except(Exception):
                                pass
                            try:
                                 #this destroys the window
                                Countdown.display_time_seconds_film_select.destroy()
                            except(Exception):
                                pass
                             #this calls the function timer from the class Countdown
                            Countdown.timer()
                            #this raises the window
                            countdown.attributes("-topmost", 1)

                    #this checks if shift_track is equal to 1 or if shift_track is equal to 2
                    if Enter.shift_track==1 or Enter.shift_track==2:

                        #this sets the variable track to the length of enter_track
                        track=len(Enter.enter_track.get())
                        #this inserts a _ into the entry box
                        Enter.enter_track.insert(track, "_")
                        #this moves the cursor forwards a space
                        Enter.enter_track.icursor(track+1)
                        shift_selected() #this calls the function shift_selected
                            
                    else:

                        #this sets the variable track to the length of enter_track
                        track=len(Enter.enter_track.get())
                        #this inserts a - into the entry box
                        Enter.enter_track.insert(track, "-")
                        #this moves the cursor forwards a space
                        Enter.enter_track.icursor(track+1)

                #this is the same for all other function for typing in letters from the keyboard              
                def equals_selected():

                    if menu.page_number>8:

                        pass

                    else:
                        
                            try:
                                Countdown.display_time_film_select.destroy()

                            except(Exception):
                                pass
                            try:
                                Countdown.display_time_seconds_film_select.destroy()
                            except(Exception):
                                pass
                            Countdown.timer()   
                            countdown.attributes("-topmost", 1)
                            
                    if Enter.shift_track==1 or Enter.shift_track==2:
                    
                        track=len(Enter.enter_track.get())
                        Enter.enter_track.insert(track, "+")
                        Enter.enter_track.icursor(track+1)
                        shift_selected()
                            
                    else:

                        track=len(Enter.enter_track.get())
                        Enter.enter_track.insert(track, "=")
                        Enter.enter_track.icursor(track+1)
                                
                def sem_selected():

                    if menu.page_number>8:

                        pass

                    else:
                        
                            try:
                                Countdown.display_time_film_select.destroy()

                            except(Exception):
                                pass
                            try:
                                Countdown.display_time_seconds_film_select.destroy()
                            except(Exception):
                                pass
                            Countdown.timer()   
                            countdown.attributes("-topmost", 1)
                            
                    if Enter.shift_track==1 or Enter.shift_track==2:
                        
                        track=len(Enter.enter_track.get())
                        Enter.enter_track.insert(track, ":")
                        Enter.enter_track.icursor(track+1)
                        shift_selected()
                        
                    else:
                        
                        track=len(Enter.enter_track.get())
                        Enter.enter_track.insert(track, ";")
                        Enter.enter_track.icursor(track+1)

                #this creates a back button
                self.back_sp_image = PhotoImage(file="backsp.gif")
                self.back_sp = Button(self.frame1, width=142, height=77,fg="black", image=self.back_sp_image, bg="black", command=back_selected)
                self.back_sp.place(relx=0.833,rely=0)
                #this creates minus button
                self.minus=Button(self.frame1, width=4, height=2, font=("Courier", 20), fg="white", bg="black", text="-", command=minus_selected)
                self.minus.grid(column=0, row=1)
                #this creates the equals button
                self.equals=Button(self.frame1, width=4, height=2, font=("Courier", 20), fg="white", bg="black", text="=", command=equals_selected)
                self.equals.grid(column=1, row=1)
                #this creates the shift button
                self.shift_off_image = PhotoImage(file="shiftm.gif")
                self.shift_off = Button(self.frame1, width=68, height=77, image=self.shift_off_image, bg="black", command=shift_selected)
                self.shift_off.grid(column=0, row=2)
                self.shift_on_image = PhotoImage(file="shiftm.gif")
                #this creates the semicolon button
                self.sem=Button(self.frame1, width=4, height=2, bg="black", fg="white", text=";", font=("Courier", 20), command=sem_selected)
                self.sem.grid(column=11, row=2)
                #this creates the space bar button
                self.space=space=Button(keyboard, width=36, height=2, bg="black", command=space_selected, text=" ",font=("Courier", 20))
                self.space.place(relx=0.167, rely=0.819)
                #this creates the @ button
                self.at=Button(self.frame1, width=4, height=2, bg="black", text="|", font=("Courier", 20), fg="white", command=at_selected)
                self.at.grid(column=11, row=3)
                #this creates the left bracket button
                self.left_br=Button(self.frame1, width=4, height=2, bg="black", text="[", font=("Courier", 20), fg="white", command=left_br_selected)
                self.left_br.grid(column=0, row=4)
                #this creates the right bracket button
                self.right_br=Button(self.frame1, width=4, height=2, bg="black", text="]", font=("Courier", 20), fg="white", command=right_br_selected)
                self.right_br.grid(column=1, row=4)
                #this creates the hash button
                self.hash=Button(self.frame1, width=4, height=2, bg="black", text="#", font=("Courier", 20), fg="white", command=hash_selected)
                self.hash.grid(column=0, row=3)
                self.text=[] #this creates the empty list called text
                self.text1=["1","2","3","4","5","6","7","8","9","0"] #this creates a list called text1
                self.text2=["q","w","e","r","t","y","u","i","o","p"] #this creates a list called text2
                self.text3=["a","s","d","f","g","h","j","k","l","'"] #this creates a list called text3
                self.text4=["z","x","c","v","b","n","m",",",".","?"] #this creates a list called text4
                self.text.append(self.text1) #this adds the list to the list text
                self.text.append(self.text2) #this adds the list to the list text
                self.text.append(self.text3) #this adds the list to the list text
                self.text.append(self.text4) #this adds the list to the list text
                
                def color_change2(x2,y2): #this is a function
                    
                    #this checks if the page_number is bigger than 8
                    if menu.page_number>8:

                        pass

                    else:
                        
                            try:
                                 #this destroys the window                                
                                Countdown.display_time_film_select.destroy()

                            except(Exception):
                                pass
                            try:
                                 #this destroys the window
                                Countdown.display_time_seconds_film_select.destroy()
                            except(Exception):
                                pass
                             #this calls the function timer from the class Countdown
                            Countdown.timer()
                            #this raises the window
                            countdown.attributes("-topmost", 1)

                    #this checks if shift_track is equal to 1 or if shift_track is equal to 2
                    if Enter.shift_track==1 or Enter.shift_track==2:

                        #this sets the variable track to the length of enter_track
                        track=len(Enter.enter_track.get())
                        #this inserts a self.text11[y2][x2].title() into the entry box
                        Enter.enter_track.insert(track, self.text11[y2][x2].title())
                        #this moves the cursor forwards a space
                        Enter.enter_track.icursor(track+1)
                        
                    else:

                        #this sets the variable track to the length of enter_track
                        track=len(Enter.enter_track.get())
                        #this inserts a self.text[y2][x2] into the entry box
                        Enter.enter_track.insert(track, self.text[y2][x2])
                        #this moves the cursor forwards a space
                        Enter.enter_track.icursor(track+1)

                    #this checks if shift_track is equal to 1
                    if Enter.shift_track==1:

                        #this calls the function shift_selected
                        shift_selected()

                    #this checks if shift_track is equal to 2
                    elif Enter.shift_track==2: 

                        #this calls the function shift_selected
                        shift_selected()

                #this creates an array of buttons
                self.btn1=[[0 for x in range(4)] for x in range(10)]
                
                for x in range(10): #this loops until x equals 10
                    
                    for y in range(4): #this loops until y equals 4

                        #this creates button for array
                        self.btn1[x][y] = Button(self.frame1,command= lambda x2=x, y2=y: color_change2(x2,y2), width=4, height=2, bg="black", text=self.text[y][x], font=("Courier", 20), fg="white")

                        if y==1: #this checks if y equals 1

                            #this sets the variable x2 to x+2
                            x2=x+2
                            #this places the button on the frame
                            self.btn1[x][y].grid(column=x2, row=y)
                            #this sets the variable x2 to x-2
                            x2=x2-2
                            
                        elif y==2: #this checks if y equals 2

                            #this sets the variable x2 to x+1
                            x2=x+1
                            #this places the button on the frame
                            self.btn1[x][y].grid(column=x2, row=y)
                            #this sets the variable x2 to x-1
                            x2=x2-1
                            
                        elif y==3: #this checks if y equals 3

                            #this sets the variable x2 to x+2
                            x2=x+1
                            #this places the button on the frame
                            self.btn1[x][y].grid(column=x2, row=y)
                            #this sets the variable x2 to x-2
                            x2=x2-1
                            
                        else:

                            #this places the button on the frame
                            self.btn1[x][y].grid(column=x, row=y)
                
        class pick_login_class: #this is the class for picking the login type

            def __init__(self, pick_login): #this initialises the class

                self.pick_login = pick_login #this links the window to the class
                pick_login.overrideredirect(1) #this raises the window to the top
                pick_login.geometry("%dx%d+0+0" % (w, h)) #this resizes the window
                pick_login.resizable(width = False, height = False) #this removes the top bar of the window
                
                def login_selected(): #this is a function

                    enter_login.attributes("-topmost", 1) #this raises the window
                    menu.page_number=7 #this sets the variable page_number from the class menu to 7
                    pick_login.attributes("-topmost", 0) #this lowers the window
                    try:
                        Countdown.display_time_film_select.destroy() #this destroys the window

                    except(Exception):
                        pass
                    try:
                        Countdown.display_time_seconds_film_select.destroy() #this destroys the window
                    except(Exception):
                        pass
                    Countdown.timer() #this calls the function timer from the class Countdown
                    countdown.attributes("-topmost", True) #this raises the window
                    
                def signup_selected(): #this is a function

                    enter_signup.attributes("-topmost", 1) #this raises the window
                    menu.page_number=8 #this sets the variable page_number from the class menu to 8
                    pick_login.attributes("-topmost", 0) #this lowers the window
                    try:
                        Countdown.display_time_film_select.destroy() #this destroys the window

                    except(Exception):
                        pass
                    try:
                        Countdown.display_time_seconds_film_select.destroy() #this destroys the window
                    except(Exception):
                        pass
                    Countdown.timer() #this calls the function timer from the class Countdown
                    countdown.attributes("-topmost", True) #this raises the window

                #this makes a label for the background
                self.pick_login_bg = Label(pick_login, image=menu.bg_image, bg="black")
                self.pick_login_bg.grid()
                def callback(event): #this is a function
                    countdown.attributes("-topmost", 1) #this raises the window
                self.pick_login_bg.bind("<Button-1>", callback) #this links the button to the function
                #this makes the login and sign up buttons
                self.login=Button(pick_login, text="login", font=("Courier", 20), fg="white", bg="black", command=login_selected, width=25, height=5)
                self.signup=Button(pick_login, text="sign up", font=("Courier", 20), fg="white", bg="black", command=signup_selected, width=25, height=5)
                self.login.place(relx=0.13, rely=0.43)
                self.signup.place(relx=0.53, rely=0.43)

                def back_to_menu(): #this is a function

                    seat_select.attributes("-topmost", 1) #this raises the window
                    menu.page_number=5 #this the variable page_number from the class menu to 5
                    pick_login.attributes("-topmost", 0) #this lowers the window
                    try:
                        Countdown.display_time_film_select.destroy() #this destroys the window

                    except(Exception):
                        pass
                    try:
                        Countdown.display_time_seconds_film_select.destroy() #this destroys the window
                    except(Exception):
                        pass
                    Countdown.timer() #this calls the function timer from the class Countdown
                    countdown.attributes("-topmost", 1) #this raises the window

                #this makes a back button to the previous page
                self.back_to_menu_button=Button(pick_login, text="Back", command=back_to_menu)
                self.back_to_menu_button.configure(font=("Courier", 20), fg="white", bg="black")
                self.back_to_menu_button.place(relx=0.01, rely=0.01)
                
        class seat_class: #this is the class for selecting the location of seats
            
            def __init__(self, seat_select): #this initialises the class
                
                self.seat_select = seat_select #this links the class to the window seat_select
                seat_select.overrideredirect(1) #this raises the window to the top
                seat_select.geometry("%dx%d+0+0" % (w, h)) #this resizes the window
                seat_select.resizable(width = False, height = False) #this removes the top bar from the window
                self.aaseats = 0 #this sets the variable aaseats to 0
                self.seats_bg_image = PhotoImage(file="menu_bg.gif") #this sets the variable seats_bg_image to an image for the background
                self.seats_bg = Label(seat_select, image=self.seats_bg_image, bg="black") #this makes a label for the background
                self.seats_bg.grid() #this places the label on the window
                self.white_bg = Label(seat_select, bg="white", width=165, height=43) #this creates a white box on the window
                def callback(event): #this is a function that is called when the customer clicks on the background
                    countdown.attributes("-topmost", 1) #this raises the window
                self.white_bg.bind("<Button-1>", callback) #this links the label to the function
                self.white_bg.place(relx=0.077, rely=0.09) #this places the label to the window
                self.seat_title = Label(seat_select, text="Please pick your seats", font=("Courier", 35), bg="white") #this makes the title
                self.seat_title.place(relx=0.28, rely=0.11) #this places the title on the window

                def back_to_menu(): #this is a function

                    ticket_select.attributes("-topmost", 1) #this raises the window
                    menu.page_number=4 #this sets the variable page_number from the menu class to 4
                    seat_select.attributes("-topmost", 0) #this lowers the window
                    Seat.seat_number=0 #this sets the variable seat_number from the class Seat to 0
                    try:
                        Countdown.display_time_film_select.destroy() #this tries to destroy the window

                    except(Exception):
                        pass
                    try:
                        Countdown.display_time_seconds_film_select.destroy() #this tries to destroy the window
                    except(Exception):
                        pass
                    Countdown.timer() #this calls the function timer from the class Countdown
                    countdown.attributes("-topmost", 1) #this raises the window
                    
                    for i in range(Ticket.aseats): #this is a for loop to remove the xseats and yseats items

                        try:

                            xseats.pop(i) #this removes a xseats item from the list
                            yseats.pop(i) #this removes a yseats item from the list

                        except(Exception):

                            pass
                        
                    Seat.aaseats=0 #this sets the variable aaseats from the class Seat to 0
                    
                    try:

                        self.fakeseat.destroy() #this removes an error from the window

                    except(Exception):
                        
                        pass

                #this creates a back button to the previous page
                self.back_button=Button(seat_select, text="Back", command=back_to_menu)
                self.back_button.configure(font=("Courier", 20), fg="white", bg="black")
                self.back_button.place(relx=0.01, rely=0.01)

                def seat_selected(): #this is a function

                    countdown.attributes("-topmost", 1) #this raises the window
                    
                    if Seat.aaseats<Ticket.aseats: #this checks if aaseats from the class Seat is smaller than aseats from the class Ticket

                        #this displays an error on the window
                        self.fakeseat=Label(seat_select, bg="red", font=("Courier", 15), text="Please pick all your seats", width=120)
                        self.fakeseat.place(relx=0, rely=0)

                        def kill_fakeseat():
                                        
                            self.fakeseat.place_forget()
                                        
                        self.fakeseat.after(2000, kill_fakeseat) #this kills the error from the window after 2000ms

                    else:

                        seat_select.attributes("-topmost", 0) #this lowers the window
                        menu.page_number=6 #this sets the variable page_number from the class menu to 6
                        pick_login.attributes("-topmost", 1) #this raises the window
                        try:
                            Countdown.display_time_film_select.destroy() #this destroys the window

                        except(Exception):
                            pass
                        try:
                            Countdown.display_time_seconds_film_select.destroy() #this destroys the window
                        except(Exception):
                            pass
                        Countdown.timer() #this calls the function timer from the class Countdown
                        countdown.attributes("-topmost", True) #this raises the window

                        try:

                            self.fakeseat.destroy() #this destroys the error from the window

                        except(Exception):
                        
                            pass

                #this creates the letter of the columns on the array of buttons for seats       
                self.nseat = Label(seat_select, text="""
                        A
                        
                        B
                        
                        C
                        
                        D
                        
                        E
                        
                        F
                        
                        G
                        
                        H
                        """, font=("Courier", 17), bg="white", fg="black")
                self.nseat.place(relx=0.6, rely=0.25)
                #this creates a done button when the customer is done with this page
                self.submit_btn= Button(seat_select, text="Done", width="20", height="3", command=seat_selected)
                self.submit_btn.configure(font=("Courier", 15), fg="white", bg="black")
                self.submit_btn.place(relx=0.4, rely=0.81)
                #this creates a grey box to tell the customer where the screen is
                self.screen=Label(seat_select, text="Screen", width=78, height=2, bg="grey", font=("Courier", 15))
                self.screen.place(relx=0.09, rely=0.2)
                #this is the key for what the blue and black button on the array mean
                self.key_white=Button(seat_select, width=5, height=3, bg="#0601A1", state=DISABLED)
                self.key_white.place(relx=0.09, rely=0.83)
                self.key_black=Button(seat_select, width=5, height=3, bg="black", state=DISABLED)
                self.key_black.place(relx=0.24, rely=0.83)
                self.key_white_text=Label(seat_select, text="Available", font=("Courier", 17), bg="white", fg="black")
                self.key_white_text.place(relx=0.13, rely=0.84)
                self.key_black_text=Label(seat_select, text="Unavailable", font=("Courier", 17), bg="white", fg="black")
                self.key_black_text.place(relx=0.28, rely=0.84)
                self.seat_number=0 #this sets the variable seat_number to 0
                #these create the counters
                #number of seats selected
                self.seat_counter=Label(seat_select, text="You have selected "+str(self.seat_number)+" seats", font=("Courier", 17), bg="white", fg="black")
                self.seat_counter.place(relx=0.6, rely=0.8)
                #number of seats that are booked
                self.seats_booked=Label(seat_select, text="You have booked "+str(Ticket.aseats)+" seats", font=("Courier", 17), bg="white", fg="black")
                self.seats_booked.place(relx=0.6, rely=0.84)
                self.seats_left_number=Ticket.aseats
                #number of seats left to select
                self.seats_left_selected=Label(seat_select, text="You have "+str(self.seats_left_number)+" seats left to select", font=("Courier", 17), bg="white", fg="black")
                self.seats_left_selected.place(relx=0.6, rely=0.88)
                
        def checker(): #this is a function

            try:
                Countdown.display_time_film_select.destroy() #this destroys the window

            except(Exception):
                pass
            try:
                Countdown.display_time_seconds_film_select.destroy() #this destroys the window
            except(Exception):
                pass
            Countdown.timer() #this calls the function timer from the class Countdown
            countdown.attributes("-topmost", True) #this raises the window
            #this resets the counters
            Seat.seats_booked.config(text="You have booked "+str(Ticket.aseats)+" seats")
            Seat.seats_left_selected.config(text="You have "+str(Ticket.aseats)+" seats left to select")
            Seat.seats_left_number=Ticket.aseats
            Seat.seat_number=0 #this sets the variable seat_number from the class Seat to 0
            Seat.seat_counter.config(text="You have selected "+str(Seat.seat_number)+" seats")

            def color_change1(x1,y1): #this a function

                try:
                    Countdown.display_time_film_select.destroy() #this destroys the window

                except(Exception):
                    pass
                try:
                    Countdown.display_time_seconds_film_select.destroy() #this destroys the window
                except(Exception):
                    pass
                Countdown.timer() #this calls the function timer from the class Countdown
                countdown.attributes("-topmost", True) #this raises the window
                s=len(xseats) #this sets the variable s to the length of the list xseats
                i=0 #this sets the variable i to 0
                unclicked=False #this sets the variable unclicked to False
                
                while i<s and unclicked==False: #this loops while i is smaller than s and unclicked equals False

                    x11=x1+5 #this sets the variable x11 to the x1 add 5

                    #this checks if the i number in the list xseats equals to x11 and i number in the list yseats equals to y1
                    if xseats[i]==x11 and yseats[i]==y1: 

                        btn[x1][y1].config(bg="#0601A1") #this makes the button blue
                        xseats.pop(i) #this removes the a item from the list xseats
                        yseats.pop(i) #this removes the a item from the list yseats
                        #this minuses 1 from the variable aaseats from the class Seat
                        Seat.aaseats=Seat.aaseats-1
                        s=len(xseats) #this sets the variable s to the length of the list xseats
                        unclicked=True #this sets the variable unclicked to True
                        Seat.seat_number-=1 #this minuses 1 from the variable seat_number from the class Seat
                        #this updates the counters
                        Seat.seat_counter.config(text="You have selected "+str(Seat.seat_number)+" seats")
                        Seat.seats_left_number+=1
                        Seat.seats_left_selected.config(text="You have "+str(Seat.seats_left_number)+" seats left to select")
                        
                    i+=1 #this increases the variable i by 1

                if unclicked==False: #this checks if unclicked is equal to False

                    #this checks if aaseats from the class Seat is smaller than aseats from the class Ticket
                    if Seat.aaseats<Ticket.aseats:

                        btn[x1][y1].config(bg="white") #this makes the button white
                        Seat.aaseats=Seat.aaseats+1 #this increases the variable aaseats from the class Seat
                        xseats.append(x1+5) #this adds the value of x1+5 to the list xseats
                        yseats.append(y1) #this adds the value of y1 to the list yseats
                        Seat.seat_number+=1 #this increases the variable seat_number from the class Seat by 1
                        #this updates the counters
                        Seat.seat_counter.config(text="You have selected "+str(Seat.seat_number)+" seats")
                        Seat.seats_left_number-=1
                        Seat.seats_left_selected.config(text="You have "+str(Seat.seats_left_number)+" seats left to select")

            def color_change2(x2,y2): #this is a function

                try:
                    Countdown.display_time_film_select.destroy() #this destroys the window

                except(Exception):
                    pass
                try:
                    Countdown.display_time_seconds_film_select.destroy() #this destroys the window
                except(Exception):
                    pass
                Countdown.timer() #this calls the function timer from the class Countdown
                countdown.attributes("-topmost", 1) #this raises the window
                s1=len(xseats) #this sets the variable s1 to the length of xseats
                unclicked=False #this sets the variable unclicked to False
                t=0 #this sets the variable t to 0

                while t<s1 and unclicked==False: #this loops while t is smaller than s1 and unclicked equals False

                    #this checks if the t number in the list xseats equals to x2 and t number in the list yseats equals to y2
                    if xseats[t]==x2 and yseats[t]==y2:

                        btn1[x2][y2].config(bg="#0601A1") #this makes the button blue
                        xseats.pop(t) #this removes a item from the list xseats
                        yseats.pop(t) #this removes a item from the list yseats
                        Seat.aaseats=Seat.aaseats-1 #this decreases the aaseats value by 1
                        unclicked=True #this sets the variable unclicked to True
                        s1=len(xseats) #this sets the variable s1 to the length of xseats
                        #this updates the counter
                        Seat.seat_number-=1
                        Seat.seat_counter.config(text="You have selected "+str(Seat.seat_number)+" seats")
                        Seat.seats_left_number+=1
                        Seat.seats_left_selected.config(text="You have "+str(Seat.seats_left_number)+" seats left to select")
                        
                    t+=1 #this increases the value of t by 1

                if unclicked==False: #this checks if unclicked equals False

                    #this checks if aaseats from the class Seat is smaller than aseats from the class Ticket
                    if Seat.aaseats<Ticket.aseats:

                        btn1[x2][y2].config(bg="white") #this makes the button white
                        Seat.aaseats=Seat.aaseats+1 #this increases the variable aaseats from the class by 1
                        xseats.append(x2) #this adds the value of x2 to the list xseats
                        yseats.append(y2) #this adds the value of y2 to the list yseats
                        #this updates the counters
                        Seat.seat_number+=1 
                        Seat.seat_counter.config(text="You have selected "+str(Seat.seat_number)+" seats")
                        Seat.seats_left_number-=1
                        Seat.seats_left_selected.config(text="You have "+str(Seat.seats_left_number)+" seats left to select")

            def color_change3(x3,y3): #this is a function

                try:
                    Countdown.display_time_film_select.destroy() #this destroys the window

                except(Exception):
                    pass
                try:
                    Countdown.display_time_seconds_film_select.destroy() #this destroys the window 
                except(Exception):
                    pass
                Countdown.timer() #this calls the function timer from the class Countdown
                countdown.attributes("-topmost", 1) #this raises the window
                s2=len(xseats) #this sets the variable s2 to the length of xseats
                m=0 #this sets the variable m to 0
                unclicked=False #this sets the variable unclicked to False

                while m<s2 and unclicked==False: #this loops while m is smaller than s2 and unclicked equals False

                    x33=x3+15 #this sets the variable x33 to the value of x3+15

                    #this checks if the t number in the list xseats equals to x2 and t number in the list yseats equals to y2
                    if xseats[m]==x33 and yseats[m]==y3:

                        btn2[x3][y3].config(bg="#0601A1") #this makes button blue
                        xseats.pop(m) #this removes a item from the list xseats
                        yseats.pop(m) #this removes a item from the list yseats
                        Seat.aaseats=Seat.aaseats-1 #this decreases the variable aaseats from the class Seat by 1
                        s2=len(xseats) #this sets the variable s2 to length of the list xseats
                        #this updates the counters
                        Seat.seat_number-=1
                        Seat.seat_counter.config(text="You have selected "+str(Seat.seat_number)+" seats")
                        Seat.seats_left_number+=1
                        Seat.seats_left_selected.config(text="You have "+str(Seat.seats_left_number)+" seats left to select")
                        unclicked=True #this sets the variable unclicked to True
                        
                    m+=1 #this increases the variable m by 1
                        

                if unclicked==False: #this checks if the variable unclicked equals False

                    #this checks if aaseats from the class Seat is smaller than aseats from the class Ticket
                    if Seat.aaseats<Ticket.aseats:

                        btn2[x3][y3].config(bg="white") #this makes the button white
                        Seat.aaseats=Seat.aaseats+1 #this increases the variable aaseats from the class Seat by 1
                        xseats.append(x3+15) #this adds the value of x3+15 to the list xseats
                        yseats.append(y3) #this adds the value of y3 to the list yseats
                        #this updates the counters
                        Seat.seat_number+=1
                        Seat.seat_counter.config(text="You have selected "+str(Seat.seat_number)+" seats")
                        Seat.seats_left_number-=1
                        Seat.seats_left_selected.config(text="You have "+str(Seat.seats_left_number)+" seats left to select")

            #this creates the frames for the array of buttons to go in
            frame=Frame(seat_select)
            frame.place(relx=0.27,rely=0.27)
            frame1=Frame(seat_select)
            frame1.place(relx=0.09,rely=0.27)
            frame2=Frame(seat_select)
            frame2.place(relx=0.615,rely=0.27)
            #this selects xseats from the table seats where timeid equals the variable timeid from the class menu
            cursor.execute("""SELECT xseats FROM seats WHERE timeid=?""",(menu.timeid,))
            resultx = cursor.fetchall() #this saves the results
            final_resultx = [i[0] for i in resultx] #this formats the results into a list
            #this selects yseats from the table seats where timeid equals the variable timeid from the class menu
            cursor.execute("""SELECT yseats FROM seats WHERE timeid=?""",(menu.timeid,))
            resulty= cursor.fetchall() #this saves the results
            final_resulty=[i[0] for i in resulty] #this formats the results into a list
            btn1=[[0 for x in range(7)] for x in range(5)] #this makes an array of buttons

            for x in range(5): #this iteratives through until x is equal 5

                for y in range(7): #this iteratives through until y is equal 7

                    length=len(final_resultx) #this sets a variable length to the length of final_resultx
                    btn1n=0 #this sets the variable btn1n to 0

                    for i in range(length): #this iteratives through untils i equals the value of the variable length

                        #this checks if x equals i number in the list final_resultx and y equals i number in final_resulty
                        if x==final_resultx[i] and y==final_resulty[i]:

                            btn1[x][y] = Button(frame1, width=5, height=3, bg="black", state=DISABLED) #this makes a disabled button
                            btn1n=1 #this sets the variable btn1n to 1
                            btn1[x][y].grid(column=x, row=y) #this places the button on the frame

                    if btn1n==0: #this checks if btn1n equals 0

                        #this creates a button and places it on the frame
                        btn1[x][y] = Button(frame1,command= lambda x2=x, y2=y: color_change2(x2,y2), width=5, height=3, bg="#0601A1", state='normal')
                        btn1[x][y].grid(column=x, row=y)

            btn=[[0 for x in range(7)] for x in range(10)] #this creates a array of buttons
            
            for x in range(10): #this iteratives through until x is equal 10

                for y in range(7): #this iteratives through until y is equal to 7

                    length=len(final_resultx) #this sets the variable length to the length of final_resultx
                    btnn=0 #this sets the variable btnn to 0

                    for i in range(length): #this iteratives through until i is equal to the variable length

                        #this checks if x+5 is equal to i number in the list final_resultx and y is equal to i number in the list final_resulty
                        if x+5==final_resultx[i] and y==final_resulty[i]:

                           btn[x][y] = Button(frame, width=5, height=3, bg="black", state=DISABLED) #this creates a disabled button
                           btnn=1 #this sets the variable btnn to 1

                    if btnn==0: #this checks if btnn is equal to 0

                        #this creates a buton on the array
                        btn[x][y] = Button(frame,command= lambda x1=x, y1=y: color_change1(x1,y1), width=5, height=3, bg="#0601A1", state='normal')

                    btn[x][y].grid(column=x, row=y) #this places the button on the frame

            btn2=[[0 for x in range(7)] for x in range(5)] #this creates an array of buttons
            
            for x in range(5): #this iteratives through until x equals to 5

                for y in range(7): #this iteratives through until y equals to 7 

                    btn2n=0 #this sets the variable btn2n to 0
                    length=len(final_resultx) #this sets length to the length of the list final_resultx

                    for i in range(length): #this iteratives through until i equals the variable length

                        #this checks if x+10 is equal to i number in the list final_resultx and y is equal to i number in the list final_resulty
                        if x+10==final_resultx[i] and y==final_resulty[i]:

                            #this creates a disabled button
                            btn2[x][y] = Button(frame2, width=5, height=3, bg="black", state=DISABLED)
                            btn2n=1 #this sets the varaible btn2n to 1

                    if btn2n==0: #this checks if btn2n is equal to 0 

                        #this creates a button on the array
                        btn2[x][y] = Button(frame2,command= lambda x3=x, y3=y: color_change3(x3,y3), width=5, height=3, bg="#0601A1", state='normal')

                    btn2[x][y].grid(column=x, row=y) #this places the button on the frame     

        class ticket_class: #this the class for selecting number of seats

            def __init__(self, ticket_select): #this initialises the class

                self.ticket_select = ticket_select #this links the class to the window
                ticket_select.overrideredirect(1) #this raises the window to the top
                ticket_select.geometry("%dx%d+0+0" % (w, h)) #this resizes the window
                ticket_select.resizable(width = False, height = False) #this removes the top bar of the window
                self.aseats = 0 #this sets the variable aseats to 0
                self.ticket_bg_image = PhotoImage(file="menu_bg.gif") #this sets the variable ticket_bg_image to an image
                self.ticket_bg_Label = Label(ticket_select, image=self.ticket_bg_image, bg="black") #this edits the label
                def callback(event): #this is a function that is called when the cusotmer clicks on the background
                    countdown.attributes("-topmost", 1) #this raises the window
                self.ticket_bg_Label.bind("<Button-1>", callback) #this links the label to a function
                self.ticket_bg_Label.grid() #this places the label on the window
                self.white_bg = Label(ticket_select, bg="white", width=165, height=43) #this edits the label
                def callback(event): #this is a function that is called when the cusotmer clicks on the label
                    countdown.attributes("-topmost", 1) #this raises the window
                self.white_bg.bind("<Button-1>", callback) #this links the label to a function
                self.white_bg.place(relx=0.077, rely=0.09) #this places the label on the window
                self.ticket_title = Label(ticket_select, text="Please pick your type of tickets", font=("Courier", 35), bg="white")
                #this makes the title
                self.ticket_title.place(relx=0.17, rely=0.11) #this places the title on the window

                #adult

                self.adult_Label = Label(ticket_select, text="        ..................................   ", font=("Courier", 20), bg="white")
                #this make the dots
                self.adult_Label.place(relx=0.15, rely=0.301) #this places the label on the window
                self.adult=Label(ticket_select, text="Adult", font=("Courier", 20), bg="white") #this make the label saying the type of seat
                self.adult.place(relx=0.15, rely=0.31) #this places the label on the window
                self.adult_price=Label(ticket_select, text="£12.50", font=("Courier", 20), bg="white") #this makes the label for the price
                self.adult_price.place(relx=0.68, rely=0.31) #this places the label on the window
                #this is repeated for the four different type of seats

                #child

                self.child_Label=Label(ticket_select, text="        ..................................   ", font=("Courier", 20), bg="white")
                self.child_Label.place(relx=0.15, rely=0.426)
                self.child=Label(ticket_select, text="Child", font=("Courier", 20), bg="white")
                self.child.place(relx=0.15, rely=0.435)
                self.child_price=Label(ticket_select, text="£9.50", font=("Courier", 20), bg="white")
                self.child_price.place(relx=0.68, rely=0.435)

                #student

                self.student_Label=Label(ticket_select, text="        ..................................   ", font=("Courier", 20), bg="white")
                self.student_Label.place(relx=0.15, rely=0.551)
                self.student=Label(ticket_select, text="Student", font=("Courier", 20), bg="white")
                self.student.place(relx=0.15, rely=0.56)
                self.student_price=Label(ticket_select, text="£10.00", font=("Courier", 20), bg="white")
                self.student_price.place(relx=0.68, rely=0.56)

                #senior
                
                self.senior_Label=Label(ticket_select, text="        ..................................   ", font=("Courier", 20), bg="white")
                self.senior_Label.place(relx=0.15, rely=0.676)
                self.senior=Label(ticket_select, text="Senior", font=("Courier", 20), bg="white")
                self.senior.place(relx=0.15, rely=0.685)
                self.senior_price=Label(ticket_select, text="£10.00", font=("Courier", 20), bg="white")
                self.senior_price.place(relx=0.68, rely=0.685)

                def option_changed(): #this function totals the cost of all the seats selected

                    Ticket.tot=(self.adult*12.50)+(self.child*9.50)+(self.student*10.00)+(self.senior*10.00) #this stores the total cost
                    
                    if self.adult==0 and self.child==0 and self.student==0 and self.senior==0: #this checks if all the number of seats are empty
                        
                        Ticket.tot=0.00 #this sets the variable tot from the class Ticket to 0.00
                        
                    Ticket.tot=("£{0:.2f}".format(Ticket.tot)) #this rounds the variable tot to 2 sf
                        
                    self.total.config(text=Ticket.tot) #this displays the total cost
                    Ticket.aseats = self.adult+self.child+self.student+self.senior #this total the number of seats
                    self.total_tickets.config(text=Ticket.aseats) #this the total number of seats
                    countdown.attributes("-topmost", 1) #this raises the countdown window

                def done_ticket(): #this is a function

                    if Ticket.aseats==0: #this checks if the customer has selected no seats

                        #this displays a error on the window
                        self.faketicket=Label(ticket_select, bg="red", font=("Courier", 15), text="Please pick a ticket", width=120)
                        self.faketicket.place(relx=0, rely=0)

                        def kill_faketicket():
                                        
                            self.faketicket.place_forget()
                                        
                        self.faketicket.after(2000, kill_faketicket) #after 2000ms the error disappears

                    else:

                        checker() #this calls the function checker
                        seat_select.attributes("-topmost", 1) #this raises the window
                        menu.page_number=5 #this sets the variable page_number to 5
                        ticket_select.attributes("-topmost", 0) #this lowers the window
                        try:
                            Countdown.display_time_film_select.destroy() #this tries to destroy the window

                        except(Exception):
                            pass
                        try:
                            Countdown.display_time_seconds_film_select.destroy() #this tries to destroy the window
                        except(Exception):
                            pass
                        Countdown.timer() #this calls the function called timer  
                        countdown.attributes("-topmost", True) #this raises the window

                        try:

                            self.faketicket.destroy() #this removes the error

                        except(Exception):
                        
                            pass

                def information(): #this is a function

                    self.info_bg_image = PhotoImage(file="infobg_1.gif") #this sets a variable to an image
                    self.info_bg_Label = Label(ticket_select, image=self.info_bg_image, bg="black") #this creats a label
                    self.info_bg_Label.place(relx=0, rely=0) #this places the label
                    def callback(event): #this is a function
                        countdown.attributes("-topmost", 1) #this raises the window
                    self.info_bg_Label.bind("<Button-1>", callback) #this links a label to a function
                    try:
                        Countdown.display_time_film_select.destroy() #this tries to destroy the window

                    except(Exception):
                        pass
                    try:
                        Countdown.display_time_seconds_film_select.destroy() #this tries to destroy the window
                    except(Exception):
                        pass
                    Countdown.timer() #this calls the function called timer   
                    countdown.attributes("-topmost", True) #this raises the window

                    def bgexit(): #this is a function

                        self.info_bg_Label.destroy() #this destroys the label
                        try:
                            Countdown.display_time_film_select.destroy() #this tries to destroy the window

                        except(Exception):
                            pass
                        try:
                            Countdown.display_time_seconds_film_select.destroy() #this tries to destroy the window
                        except(Exception):
                            pass
                        Countdown.timer() #this calls the function called timer   
                        countdown.attributes("-topmost", 1) #this raises the window
                        self.X.destroy() #this destroys a button

                    #this creates a button and puts it on the window
                    self.X=Button(ticket_select, text="X", width=3, height=1, command=bgexit, borderwidth=0)
                    self.X.config(font=("Calibri (Body)", 15), fg="black", bg="white")
                    self.X.place(relx=0.849, rely=0.11)

                def adult_plus_selected(): #this is a function

                    try:
                        Countdown.display_time_film_select.destroy()  #this tries to destroy the window

                    except(Exception):
                        pass
                    try:
                        Countdown.display_time_seconds_film_select.destroy()  #this tries to destroy the window
                    except(Exception):
                        pass
                    Countdown.timer() #this calls the function called timer   
                    countdown.attributes("-topmost", 1) #this raises the window

                    total_seats=self.adult+self.child+self.student+self.senior #this totals the number of seats

                    if total_seats==menu.seats_left: #this checks if the customer reaches the max amount of seats available

                        #this creates an error when the customer tries to book more seats than available
                        self.ticket_plus=Label(ticket_select, bg="red", font=("Courier", 15), text="You have reached max amount of seats available", width=120)
                        self.ticket_plus.place(relx=0, rely=0)
                        
                        def ticket_plus_kill():

                            self.ticket_plus.place_forget()
                            
                        self.ticket_plus.after(2000, ticket_plus_kill) #this destroys the error after 2000ms
                        
                    else:
                        
                        self.adult=self.adult+1 #add one to the amount of adults booked
                        self.adult_amount.config(text=str(self.adult)) #converts to string and change value of amount of booked
                        option_changed() #calls the option_changed function
                #this is done for all types of seats

                def adult_minus_selected():

                    try:
                        Countdown.display_time_film_select.destroy()

                    except(Exception):
                        pass
                    try:
                        Countdown.display_time_seconds_film_select.destroy()
                    except(Exception):
                        pass
                    Countdown.timer()   
                    countdown.attributes("-topmost", 1)

                    if self.adult==0:

                        self.ticket_minus=Label(ticket_select, bg="red", font=("Courier", 15), text="You cannot buy negative amount of tickets", width=120)
                        self.ticket_minus.place(relx=0, rely=0)
                        
                        def ticket_minus_kill():

                            self.ticket_minus.place_forget()
                            
                        self.ticket_minus.after(2000, ticket_minus_kill)
                        
                    else:

                        self.adult=self.adult-1 #subtract one to the amount of adults booked
                        self.adult_amount.config(text=str(self.adult))
                        option_changed()

                def student_plus_selected():

                    try:
                        Countdown.display_time_film_select.destroy()

                    except(Exception):
                        pass
                    try:
                        Countdown.display_time_seconds_film_select.destroy()
                    except(Exception):
                        pass
                    Countdown.timer()   
                    countdown.attributes("-topmost", 1)

                    total_seats=self.adult+self.child+self.student+self.senior

                    if total_seats==menu.seats_left:

                        self.ticket_plus=Label(ticket_select, bg="red", font=("Courier", 15), text="You have reached max amount of seats available", width=120)
                        self.ticket_plus.place(relx=0, rely=0)
                        
                        def ticket_plus_kill():

                            self.ticket_plus.place_forget()
                            
                        self.ticket_plus.after(2000, ticket_plus_kill)
                        
                    else:
                        
                        self.student=self.student+1
                        self.student_amount.config(text=str(self.student))
                        option_changed()

                def student_minus_selected():

                    try:
                        Countdown.display_time_film_select.destroy()

                    except(Exception):
                        pass
                    try:
                        Countdown.display_time_seconds_film_select.destroy()
                    except(Exception):
                        pass
                    Countdown.timer()   
                    countdown.attributes("-topmost", 1)

                    if self.student==0:

                        self.ticket_minus=Label(ticket_select, bg="red", font=("Courier", 15), text="You cannot buy negative amount of tickets", width=120)
                        self.ticket_minus.place(relx=0, rely=0)
                        
                        def ticket_minus_kill():

                            self.ticket_minus.place_forget()
                            
                        self.ticket_minus.after(2000, ticket_minus_kill)
                        
                    else:

                        self.student=self.student-1
                        self.student_amount.config(text=str(self.student))
                        option_changed()


                def child_plus_selected():

                    try:
                        Countdown.display_time_film_select.destroy()

                    except(Exception):
                        pass
                    try:
                        Countdown.display_time_seconds_film_select.destroy()
                    except(Exception):
                        pass
                    Countdown.timer()   
                    countdown.attributes("-topmost", 1)

                    total_seats=self.adult+self.child+self.student+self.senior

                    if total_seats==menu.seats_left:

                        self.ticket_plus=Label(ticket_select, bg="red", font=("Courier", 15), text="You have reached max amount of seats available", width=120)
                        self.ticket_plus.place(relx=0, rely=0)
                        
                        def ticket_plus_kill():

                            self.ticket_plus.place_forget()
                            
                        self.ticket_plus.after(2000, ticket_plus_kill)
                        
                    else:
                        
                        self.child=self.child+1
                        self.child_amount.config(text=str(self.child))
                        option_changed()

                def child_minus_selected():

                    try:
                        Countdown.display_time_film_select.destroy()

                    except(Exception):
                        pass
                    try:
                        Countdown.display_time_seconds_film_select.destroy()
                    except(Exception):
                        pass
                    Countdown.timer()   
                    countdown.attributes("-topmost", 1)

                    if self.child==0:

                        self.ticket_minus=Label(ticket_select, bg="red", font=("Courier", 15), text="You cannot buy negative amount of tickets", width=120)
                        self.ticket_minus.place(relx=0, rely=0)
                        
                        def ticket_minus_kill():

                            self.ticket_minus.place_forget()
                            
                        self.ticket_minus.after(2000, ticket_minus_kill)
                        
                    else:

                        self.child=self.child-1
                        self.child_amount.config(text=str(self.child))
                        option_changed()

                def senior_plus_selected():

                    try:
                        Countdown.display_time_film_select.destroy()

                    except(Exception):
                        pass
                    try:
                        Countdown.display_time_seconds_film_select.destroy()
                    except(Exception):
                        pass
                    Countdown.timer()   
                    countdown.attributes("-topmost", 1)

                    total_seats=self.adult+self.child+self.student+self.senior

                    if total_seats==menu.seats_left:

                        self.ticket_plus=Label(ticket_select, bg="red", font=("Courier", 15), text="You have reached max amount of seats available", width=120)
                        self.ticket_plus.place(relx=0, rely=0)
                        
                        def ticket_plus_kill():

                            self.ticket_plus.place_forget()
                            
                        self.ticket_plus.after(2000, ticket_plus_kill)
                        
                    else:
                        
                        self.senior=self.senior+1
                        self.senior_amount.config(text=str(self.senior))
                        option_changed()

                def senior_minus_selected():

                    try:
                        Countdown.display_time_film_select.destroy()

                    except(Exception):
                        pass
                    try:
                        Countdown.display_time_seconds_film_select.destroy()
                    except(Exception):
                        pass
                    Countdown.timer()         
                    countdown.attributes("-topmost", 1)
                    
                    if self.senior==0:

                        self.ticket_minus=Label(ticket_select, bg="red", font=("Courier", 15), text="You cannot buy negative amount of tickets", width=120)
                        self.ticket_minus.place(relx=0, rely=0)
                        
                        def ticket_minus_kill():

                            self.ticket_minus.place_forget()
                            
                        self.ticket_minus.after(2000, ticket_minus_kill)
                        
                    else:

                        self.senior=self.senior-1
                        self.senior_amount.config(text=str(self.senior))
                        option_changed()
                        
                        
                self.adult=0 #this sets the variable adult to 0
                self.child=0 #this sets the variable child to 0
                self.student=0 #this sets the variable student to 0
                self.senior=0 #this sets the variable senior to 0
                #adult
                self.adult_amount=Label(ticket_select, font=("Courier", 20), fg="black", bg="white",  width=5, height=1, text=str(self.adult))
                self.adult_plus=Button(ticket_select, font=("Courier", 10), fg="white", bg="black",  width=2, height=1, text="+", command=adult_plus_selected)
                self.adult_amount.place(relx=0.8, rely=0.31)
                self.adult_plus.place(relx=0.79, rely=0.3)
                self.adult_minus=Button(ticket_select, font=("Courier", 10), fg="white", bg="black",  width=2, height=1, text="-", command=adult_minus_selected)
                self.adult_minus.place(relx=0.79, rely=0.34)
                #child
                self.child_amount=Label(ticket_select, font=("Courier", 20), fg="black", bg="white",  width=5, height=1, text=str(self.child))
                self.child_amount.place(relx=0.8, rely=0.435)
                self.child_plus=Button(ticket_select, font=("Courier", 10), fg="white", bg="black",  width=2, height=1, text="+", command=child_plus_selected)
                self.child_plus.place(relx=0.79, rely=0.42)
                self.child_minus=Button(ticket_select, font=("Courier", 10), fg="white", bg="black",  width=2, height=1, text="-", command=child_minus_selected)
                self.child_minus.place(relx=0.79, rely=0.46)
                #student
                self.student_amount=Label(ticket_select, font=("Courier", 20), fg="black", bg="white",  width=5, height=1, text=str(self.student))
                self.student_amount.place(relx=0.8, rely=0.56)
                self.student_plus=Button(ticket_select, font=("Courier", 10), fg="white", bg="black",  width=2, height=1, text="+", command=student_plus_selected)
                self.student_plus.place(relx=0.79, rely=0.55)
                self.student_minus=Button(ticket_select, font=("Courier", 10), fg="white", bg="black",  width=2, height=1, text="-", command=student_minus_selected)
                self.student_minus.place(relx=0.79, rely=0.588)
                #senior
                self.senior_amount=Label(ticket_select, font=("Courier", 20), fg="black", bg="white",  width=5, height=1, text=str(self.senior))
                self.senior_amount.place(relx=0.8, rely=0.685)
                self.senior_plus=Button(ticket_select, font=("Courier", 10), fg="white", bg="black",  width=2, height=1, text="+", command=senior_plus_selected)
                self.senior_plus.place(relx=0.79, rely=0.68)
                self.senior_minus=Button(ticket_select, font=("Courier", 10), fg="white", bg="black",  width=2, height=1, text="-", command=senior_minus_selected)
                self.senior_minus.place(relx=0.79, rely=0.719)
                self.tot = 0.00 #this sets the variable tot to 0.00
                #this puts the total of seats booked and their prices on the window
                self.total = Label(ticket_select, text="£0.00", font=("Courier", 20), bg="white")
                self.total.place(relx=0.679, rely=0.76)
                self.total_tickets=Label(ticket_select, text=0, font=("Courier", 20), bg="white")
                self.total_tickets.place(relx=0.8235, rely=0.76)
                self.total_text = Label(ticket_select, text="Total:", font=("Courier", 20), fg="black", bg="white")
                self.total_text.place(relx=0.6, rely=0.76)
                #this is the infomation page
                self.info=Button(ticket_select, text="i", width=2, height=1, command=information)
                self.info.config(font=("Courier", 15), fg="white", bg="black")
                self.info.place(relx=0.87, rely=0.85)
                #this is the button when the customer is done with this page
                self.submit_btn= Button(ticket_select, text="Done", width="20", height="3", command=done_ticket)
                self.submit_btn.configure(font=("Courier", 15), fg="white", bg="black")
                self.submit_btn.place(relx=0.4, rely=0.81)
                
                def back_to_menu(): #this is an function

                    time_select.attributes("-topmost", 1) #this raises the window
                    self.adult=0 #this sets the variable adult to 0
                    self.child=0 #this sets the variable child to 0
                    self.student=0 #this sets the variable student to 0
                    self.senior=0 #this sets the variable senior to 0
                    menu.page_number=3 #this sets the variable page_number to 3
                     #this destroys the totaler
                    Ticket.total_tickets.destroy()
                    self.total.destroy() 
                    #this makes a total of the amount of seats booked
                    Ticket.total_tickets=Label(ticket_select, text=0, font=("Courier", 20), bg="white")
                    Ticket.total_tickets.place(relx=0.8235, rely=0.76)
                    self.total = Label(ticket_select, text="£0.00", font=("Courier", 20), bg="white")
                    self.total.place(relx=0.7, rely=0.75)
                    #this displays the total amount of seats booked for each type
                    self.child_amount.config(text=str(self.child))
                    self.adult_amount.config(text=str(self.adult))
                    self.student_amount.config(text=str(self.student))
                    self.senior_amount.config(text=str(self.senior))                
                    self.aseats = 0 #this sets the variable aseats to 0
                    ticket_select.attributes("-topmost", 0) #this lowers the window
                    try:
                        Countdown.display_time_film_select.destroy() #this destroys the window

                    except(Exception):
                        pass
                    try:
                        Countdown.display_time_seconds_film_select.destroy() #this destroys the window
                    except(Exception):
                        pass
                    Countdown.timer() #this calls the function timer     
                    countdown.attributes("-topmost", 1) #this raises the window
                    
                    try:

                        self.faketicket.destroy() #this destroys the error

                    except(Exception):
                        
                        pass

                #this creates the back button
                self.back_to_menu_button=Button(ticket_select, text="Back", command=back_to_menu)
                self.back_to_menu_button.configure(font=("Courier", 20), fg="white", bg="black")
                self.back_to_menu_button.place(relx=0.01, rely=0.01)
                
        def seats_amount(): #this is a function
            
            cursor.execute("""SELECT seats_left FROM time WHERE timeid=?""",(menu.timeid,))
            #this selects seats_left from the table time where timeid = the variable timeid from menu class
            taken_seats_list=cursor.fetchall() #this saves the results
            taken_seats=[i[0] for i in taken_seats_list]
            menu.seats_left=taken_seats[0] #this takes the first thing from the list
            #this creates a label to say how many seats are avilable
            seats_left=Label(ticket_select, font=("Courier", 15), fg="black", bg="white", text="You have "+str(menu.seats_left)+" seats available")
            seats_left.place(relx=0.1, rely=0.87)
            try:
                    Countdown.display_time_film_select.destroy() #this destroys the window

            except(Exception):
                    pass
            try:
                    Countdown.display_time_seconds_film_select.destroy() #this destroys the window
            except(Exception):
                    pass
            Countdown.timer() #this calls the function timer  
            countdown.attributes("-topmost", True) #this raises the window
            
        class time_class: #this the class for the time selection
            
            def __init__(self, time_select): #this initailises the class
                
                self.time_select = time_select #this links the class to the window time_select
                self.thor_time_bg_image = PhotoImage(file="menubg_4.gif")
                #this sets the variable thor_time_bg_image to the background of the time selection if they pick thor
                self.baby_time_bg_image = PhotoImage(file="menubg_9.gif")
                #this sets the variable baby_time_bg_image to the background of the time selection if they pick baby driver
                self.dunkirk_time_bg_image = PhotoImage(file="menubg_6.gif")
                #this sets the variable dunkirk_time_bg_image to the background of the time selection if they pick dunkirk
                self.blade_time_bg_image = PhotoImage(file="menubg_7.gif")
                #this sets the variable blade_time_bg_image to the background of the time selection if they pick blade runner
                self.time_bg=Label(time_select, bg="black", width=w, height=h)
                #this sets the variable time_bg to the label for the background
                countdown.attributes("-topmost", 1) #this raises the countdown window
                def callback(event): #this is a function that is called if the background is clicked on
                    countdown.attributes("-topmost", 1) #this raises the countdown window
                self.time_bg.bind("<Button-1>", callback) #this links the label background to a function
                
        def time(): #this is a function for setting the background

            try:
                    Countdown.display_time_film_select.destroy() #this tries to destroy the window

            except(Exception):
                    pass
            try:
                    Countdown.display_time_seconds_film_select.destroy() #this tries to destroy the window
            except(Exception):
                    pass
            Countdown.timer() #this calls the function timer
            countdown.attributes("-topmost", True) #this raises the window countdown
            time_select.overrideredirect(1) #this makes the window on the top
            time_select.geometry("%dx%d+0+0" % (w, h)) #this resizes the window
            time_select.resizable(width = False, height = False) #this removes the top bar of the window
            time_button_1 = Button(time_select) #this creates a time selection button
            time_button_1.config(width="15", height="2", bg="black", font=("Courier", 33), fg="white") #this edits a selection page button
            time_button_2 = Button(time_select) #this creates a time selection button
            time_button_2.config(width="15", height="2", bg="black", font=("Courier", 33), fg="white") #this edits a selection page button
            time_button_3 = Button(time_select) #this creates a time selection button
            time_button_3.config(width="15", height="2", bg="black", font=("Courier", 33), fg="white") #this edits a selection page button
            time_button_4 = Button(time_select) #this creates a time selection button
            time_button_4.config(width="15", height="2", bg="black", font=("Courier", 33), fg="white") #this edits a selection page button

            def back_to_menu(): #this function returns to the previous page

                film_select.attributes("-topmost", 1) #this raises the film_select window
                time_select.attributes("-topmost", 0) #this lowers the time_select window
                menu.page_number=2 #this sets the variable page_number from the menu class to 2
                try:
                    Countdown.display_time_film_select.destroy() #this tries to destroy the window

                except(Exception):
                    pass
                try:
                    Countdown.display_time_seconds_film_select.destroy() #this tries to destroy the window
                except(Exception):
                    pass
                Countdown.timer() #this calls the function timer    
                countdown.attributes("-topmost", 1) #this raises the window countdown
            
            back_button=Button(time_select, text="Back", command=back_to_menu) #this sets the variable back_button to the button to go back a page
            back_button.configure(font=("Courier", 20), fg="white", bg="black") #this edits the button
            back_button.place(relx=0.03, rely=0.05) #this places the button on the page

            def time_1_selected(): #this a function

                if menu.filmid==1: #this checks if the filmid is 1
                    
                    menu.timeid = 1 #this sets the variable filmid from the class menu to 1

                elif menu.filmid==2: #this checks if the filmid is 2

                    menu.timeid = 5 #this sets the variable filmid from the class menu to 5

                elif menu.filmid==3: #this sets the variable filmid from the class menu to 3

                     menu.timeid=9 #this sets the variable filmid from the class menu to 9

                else:

                    menu.timeid=13 #this sets the variable filmid from the class menu to 13

                ticket_select.attributes("-topmost", 1) #this raises the window ticket_select
                menu.page_number=4 #this sets the variable page_number from the menu class to 4
                time_select.attributes("-topmost", 0) #this lowers the window time_select
                seats_amount() #this calls the function seats_amount

            def time_2_selected(): #this is a funtion

                if menu.filmid==1: #this checks if the filmid is 1

                    menu.timeid=2 #this sets the variable filmid from the class menu to 2

                elif menu.filmid==2: #this checks if the filmid is 2

                    menu.timeid=6 #this sets the variable filmid from the class menu to 6

                elif menu.filmid==3: #this checks if the filmid is 3

                    menu.timeid=10 #this sets the variable filmid from the class menu to 10

                else:

                    menu.timeid=14 #this sets the variable filmid from the class menu to 14

                ticket_select.attributes("-topmost", 1) #this raises the window ticket_select
                menu.page_number=4 #this sets the variable page_number from the menu class to 4
                time_select.attributes("-topmost", 0) #this lowers the window time_select
                seats_amount() #this calls the function seats_amount

            def time_3_selected(): #this is a funtion

                if menu.filmid==1: #this checks if the filmid is 1

                    menu.timeid=3 #this sets the variable filmid from the class menu to 3

                elif menu.filmid==2: #this checks if the filmid is 2

                    menu.timeid=7 #this sets the variable filmid from the class menu to 7

                elif menu.filmid==3: #this checks if the filmid is 3

                    menu.timeid=11 #this sets the variable filmid from the class menu to 11

                else:

                    menu.timeid=15 #this sets the variable filmid from the class menu to 15

                ticket_select.attributes("-topmost", 1) #this raises the window ticket_select
                menu.page_number=4 #this sets the variable page_number from the menu class to 4
                time_select.attributes("-topmost", 0) #this lowers the window time_select
                seats_amount() #this calls the function seats_amount

            def time_4_selected(): #this is a funtion

                if menu.filmid==1: #this checks if the filmid is 1

                    menu.timeid=4 #this sets the variable filmid from the class menu to 4

                elif menu.filmid==2: #this checks if the filmid is 2

                    menu.timeid=8 #this sets the variable filmid from the class menu to 8

                elif menu.filmid==3: #this checks if the filmid is 3

                    menu.timeid=12 #this sets the variable filmid from the class menu to 12

                else:

                    menu.timeid=16 #this sets the variable filmid from the class menu to 16

                ticket_select.attributes("-topmost", 1) #this raises the window ticket_select
                menu.page_number=4 #this sets the variable page_number from the menu class to 4
                time_select.attributes("-topmost", 0) #this lowers the window time_select
                seats_amount() #this calls the function seats_amount
                
            if menu.filmid==1: #this checks if the filmid is 1

                cursor.execute("""SELECT seats_left FROM time WHERE timeid=?""",(1,)) #get all seats_left from time table where timeid=1
                taken_seats_list=cursor.fetchall() #this saves the results to the variable taken_seats_list
                taken_seats=[i[0] for i in taken_seats_list]
                menu.seats_left_1=taken_seats[0] #this takes the fist thing in the list
                cursor.execute("""SELECT seats_left FROM time WHERE timeid=?""",(2,)) #get all seats_left from time table where timeid=2
                taken_seats_list=cursor.fetchall() #this saves the results to the variable taken_seats_list
                taken_seats=[i[0] for i in taken_seats_list]
                menu.seats_left_2=taken_seats[0] #this takes the fist thing in the list
                cursor.execute("""SELECT seats_left FROM time WHERE timeid=?""",(3,)) #get all seats_left from time table where timeid=3
                taken_seats_list=cursor.fetchall() #this saves the results to the variable taken_seats_list
                taken_seats=[i[0] for i in taken_seats_list]
                menu.seats_left_3=taken_seats[0] #this takes the fist thing in the list
                cursor.execute("""SELECT seats_left FROM time WHERE timeid=?""",(4,)) #get all seats_left from time table where timeid=4
                taken_seats_list=cursor.fetchall() #this saves the results to the variable taken_seats_list
                taken_seats=[i[0] for i in taken_seats_list]
                menu.seats_left_4=taken_seats[0] #this takes the fist thing in the list
                Time.time_bg.config(image=Time.thor_time_bg_image) #this edits the background
                hour_now=datetime.now().hour #this takes the current hour
                minute_now=datetime.now().minute #this takes the current minute
                #this is done for all films
                #Thor_time_1100
                
                if hour_now>11: #this checks if hour_now>11
                    
                    time_button_1.config(text="11:00", bg="grey", state=DISABLED) #this disables the button
                    
                elif hour_now==11: #this checks if hour_now==11

                    if minute_now>0: #this checks if minute>0

                        time_button_1.config(text="11:00", bg="grey", state=DISABLED) #this disables the button
                        
                    else:

                            if menu.seats_left_1>0: #this checks if seats_left is>0

                                time_button_1.config(text="11:00", command=time_1_selected) #this edits the button

                            else:

                                    time_button_1.config(text="11:00", bg="grey", state=DISABLED) #this disables the button
                                    

                else:

                        if menu.seats_left_1>0: #this checks if seats_left is>0

                             time_button_1.config(text="11:00", command=time_1_selected) #this edits the button

                        else:

                                time_button_1.config(text="11:00", bg="grey", state=DISABLED) #this disables the button
                #this time and seats check is done on all times and films                               
                #Thor_time_1300
                        
                if hour_now>13:
                    
                    time_button_2.config(text="13:00", bg="grey", state=DISABLED)
                    
                elif hour_now==13:

                    if minute_now>0:

                        time_button_2.config(text="13:00", bg="grey", state=DISABLED)
                        
                    else:
                            if menu.seats_left_2>0:

                                 time_button_2.config(text="13:00", command=time_2_selected)

                            else:

                                    time_button_2.config(text="13:00", bg="grey", state=DISABLED)
                                
                else:

                        if menu.seats_left_2>0:

                            time_button_2.config(text="13:00", command=time_2_selected)

                        else:

                                time_button_2.config(text="13:00", bg="grey", state=DISABLED)
                
                #Thor_time_1700
                        
                if hour_now>17:
                    
                    time_button_3.config(text="17:00", bg="grey", state=DISABLED)
                    
                elif hour_now==17:

                    if minute_now>0:

                        time_button_3.config(text="17:00", bg="grey", state=DISABLED)
                        
                    else:

                            if menu.seats_left_3>0:

                                 time_button_3.config(text="17:00", command=time_3_selected)

                            else:

                                    time_button_3.config(text="17:00", bg="grey", state=DISABLED)

                else:

                        if menu.seats_left_3>0:

                            time_button_3.config(text="17:00", command=time_3_selected)

                        else:

                                time_button_3.config(text="17:00", bg="grey", state=DISABLED)
                        
                #Thor_time_2100
                        
                if hour_now>21:
                    
                    time_button_4.config(text="21:00", bg="grey", state=DISABLED)
                    
                elif hour_now==21:

                    if minute_now>0:

                        time_button_4.config(text="21:00", bg="grey", state=DISABLED)
                        
                    else:

                            if menu.seats_left_4>0:

                                 time_button_4.config(text="21:00", command=time_4_selected)

                            else:

                                    time_button_4.config(text="21:00", bg="grey", state=DISABLED)

                else:

                        if menu.seats_left_4>0:

                            time_button_4.config(text="21:00", command=time_4_selected)

                        else:

                                time_button_4.config(text="21:00", bg="grey", state=DISABLED)

            elif menu.filmid==2:

                cursor.execute("""SELECT seats_left FROM time WHERE timeid=?""",(5,))
                taken_seats_list=cursor.fetchall()
                taken_seats=[i[0] for i in taken_seats_list]
                menu.seats_left_1=taken_seats[0]
                cursor.execute("""SELECT seats_left FROM time WHERE timeid=?""",(6,))
                taken_seats_list=cursor.fetchall()
                taken_seats=[i[0] for i in taken_seats_list]
                menu.seats_left_2=taken_seats[0]
                cursor.execute("""SELECT seats_left FROM time WHERE timeid=?""",(7,))
                taken_seats_list=cursor.fetchall()
                taken_seats=[i[0] for i in taken_seats_list]
                menu.seats_left_3=taken_seats[0]
                cursor.execute("""SELECT seats_left FROM time WHERE timeid=?""",(8,))
                taken_seats_list=cursor.fetchall()
                taken_seats=[i[0] for i in taken_seats_list]
                menu.seats_left_4=taken_seats[0]
                Time.time_bg.config(image=Time.baby_time_bg_image)
                hour_now=datetime.now().hour
                minute_now=datetime.now().minute
                #Baby_time_1200
                
                if hour_now>12:
                    
                    time_button_1.config(text="12:00", bg="grey", state=DISABLED)
                    
                elif hour_now==12:

                    if minute_now>0:

                        time_button_1.config(text="12:00", bg="grey", state=DISABLED)
                        
                    else:

                            if menu.seats_left_1>0:

                                time_button_1.config(text="12:00", command=time_1_selected)

                            else:

                                    time_button_1.config(text="12:00", bg="grey", state=DISABLED)

                else:

                        if menu.seats_left_1>0:

                            time_button_1.config(text="12:00", command=time_1_selected)

                        else:

                                time_button_1.config(text="12:00", bg="grey", state=DISABLED)
                                                
                #Baby_time_1400
                if hour_now>14:
                    
                    time_button_2.config(text="14:00", bg="grey", state=DISABLED)
                    
                elif hour_now==14:

                    if minute_now>0:

                        time_button_2.config(text="14:00", bg="grey", state=DISABLED)
                        
                    else:

                            if menu.seats_left_2>0:

                                time_button_2.config(text="14:00", command=time_2_selected)

                            else:

                                    time_button_2.config(text="14:00", bg="grey", state=DISABLED)

                else:

                        if menu.seats_left_2>0:

                            time_button_2.config(text="14:00", command=time_2_selected)

                        else:

                                time_button_2.config(text="14:00", bg="grey", state=DISABLED)
                        
                #Baby_time_1900
                if hour_now>19:
                    
                    time_button_3.config(text="19:00", bg="grey", state=DISABLED)
                    
                elif hour_now==19:

                    if minute_now>0:

                        time_button_3.config(text="19:00", bg="grey", state=DISABLED)
                        
                    else:

                            if menu.seats_left_3>0:

                                time_button_3.config(text="19:00", command=time_3_selected)

                            else:

                                    time_button_3.config(text="19:00", bg="grey", state=DISABLED)

                else:

                        if menu.seats_left_3>0:

                            time_button_3.config(text="19:00", command=time_3_selected)

                        else:

                                time_button_3.config(text="19:00", bg="grey", state=DISABLED)
                        
                #Baby_time_2200
                if hour_now>22:
                    
                    time_button_4.config(text="22:00", bg="grey", state=DISABLED)
                    
                elif hour_now==22:

                    if minute_now>0:

                        time_button_4.config(text="22:00", bg="grey", state=DISABLED)
                        
                    else:

                            if menu.seats_left_4>0:

                                time_button_4.config(text="22:00", command=time_4_selected)

                            else:

                                    time_button_4.config(text="22:00", bg="grey", state=DISABLED)

                else:

                        if menu.seats_left_4>0:

                            time_button_4.config(text="22:00", command=time_4_selected)

                        else:

                                time_button_4.config(text="22:00", bg="grey", state=DISABLED)

            elif menu.filmid==3:

                cursor.execute("""SELECT seats_left FROM time WHERE timeid=?""",(9,))
                taken_seats_list=cursor.fetchall()
                taken_seats=[i[0] for i in taken_seats_list]
                menu.seats_left_1=taken_seats[0]
                cursor.execute("""SELECT seats_left FROM time WHERE timeid=?""",(10,))
                taken_seats_list=cursor.fetchall()
                taken_seats=[i[0] for i in taken_seats_list]
                menu.seats_left_2=taken_seats[0]
                cursor.execute("""SELECT seats_left FROM time WHERE timeid=?""",(11,))
                taken_seats_list=cursor.fetchall()
                taken_seats=[i[0] for i in taken_seats_list]
                menu.seats_left_3=taken_seats[0]
                cursor.execute("""SELECT seats_left FROM time WHERE timeid=?""",(12,))
                taken_seats_list=cursor.fetchall()
                taken_seats=[i[0] for i in taken_seats_list]
                menu.seats_left_4=taken_seats[0]
                Time.time_bg.config(image=Time.dunkirk_time_bg_image)
                hour_now=datetime.now().hour
                minute_now=datetime.now().minute
                #Dunkirk_time_1130
                if hour_now>11:
                    
                    time_button_1.config(text="11:30", bg="grey", state=DISABLED)
                    
                elif hour_now==11:

                    if minute_now>30:

                        time_button_1.config(text="11:30", bg="grey", state=DISABLED)
                        
                    else:

                            if menu.seats_left_1>0:

                                time_button_1.config(text="11:30", command=time_1_selected)

                            else:

                                    time_button_1.config(text="11:30", bg="grey", state=DISABLED)

                else:

                        if menu.seats_left_1>0:

                            time_button_1.config(text="11:30", command=time_1_selected)

                        else:

                                time_button_1.config(text="11:30", bg="grey", state=DISABLED)
                
                #Dunkirk_time_1530
                if hour_now>15:
                    
                    time_button_2.config(text="15:30", bg="grey", state=DISABLED)
                    
                elif hour_now==15:

                    if minute_now>30:

                        time_button_2.config(text="15:30", bg="grey", state=DISABLED)
                        
                    else:

                            if menu.seats_left_2>0:

                                time_button_2.config(text="15:30", command=time_2_selected)

                            else:

                                    time_button_2.config(text="15:30", bg="grey", state=DISABLED)

                else:

                        if menu.seats_left_2>0:

                            time_button_2.config(text="15:30", command=time_2_selected)

                        else:

                                time_button_2.config(text="15:30", bg="grey", state=DISABLED)

                #Dunkirk_time_1800
                if hour_now>18:
                    
                    time_button_3.config(text="18:00", bg="grey", state=DISABLED)
                    
                elif hour_now==18:

                    if minute_now>0:

                        time_button_3.config(text="18:00", bg="grey", state=DISABLED)
                        
                    else:

                            if menu.seats_left_3>0:

                                time_button_3.config(text="18:00", command=time_3_selected)

                            else:

                                    time_button_3.config(text="18:00", bg="grey", state=DISABLED)

                else:

                        if menu.seats_left_3>0:

                            time_button_3.config(text="18:00", command=time_3_selected)

                        else:

                                time_button_3.config(text="18:00", bg="grey", state=DISABLED)
                #Dunkirk_time_2030
                if hour_now>20:
                    
                    time_button_4.config(text="20:30", bg="grey", state=DISABLED)
                    
                elif hour_now==20:

                    if minute_now>30:

                        time_button_4.config(text="20:30", bg="grey", state=DISABLED)
                        
                    else:

                            if menu.seats_left_4>0:

                                time_button_4.config(text="20:30", command=time_4_selected)

                            else:

                                    time_button_4.config(text="20:30", bg="grey", state=DISABLED)

                else:

                        if menu.seats_left_4>0:

                            time_button_4.config(text="20:30", command=time_4_selected)

                        else:

                                time_button_4.config(text="20:30", bg="grey", state=DISABLED)

            elif menu.filmid==4:

                cursor.execute("""SELECT seats_left FROM time WHERE timeid=?""",(13,))
                taken_seats_list=cursor.fetchall()
                taken_seats=[i[0] for i in taken_seats_list]
                menu.seats_left_1=taken_seats[0]
                cursor.execute("""SELECT seats_left FROM time WHERE timeid=?""",(14,))
                taken_seats_list=cursor.fetchall()
                taken_seats=[i[0] for i in taken_seats_list]
                menu.seats_left_2=taken_seats[0]
                cursor.execute("""SELECT seats_left FROM time WHERE timeid=?""",(15,))
                taken_seats_list=cursor.fetchall()
                taken_seats=[i[0] for i in taken_seats_list]
                menu.seats_left_3=taken_seats[0]
                cursor.execute("""SELECT seats_left FROM time WHERE timeid=?""",(16,))
                taken_seats_list=cursor.fetchall()
                taken_seats=[i[0] for i in taken_seats_list]
                menu.seats_left_4=taken_seats[0]
                Time.time_bg.config(image=Time.blade_time_bg_image)
                hour_now=datetime.now().hour
                minute_now=datetime.now().minute
                #Blade_time_1030
                
                if hour_now>10:
                    
                    time_button_1.config(text="10:30", bg="grey", state=DISABLED)
                    
                elif hour_now==10:

                    if minute_now>30:

                        time_button_1.config(text="10:30", bg="grey", state=DISABLED)
                        
                    else:

                            if menu.seats_left_1>0:

                                time_button_1.config(text="10:30", command=time_1_selected)

                            else:

                                    time_button_1.config(text="10:30", bg="grey", state=DISABLED)

                else:

                        if menu.seats_left_1>0:

                            time_button_1.config(text="10:30", command=time_1_selected)

                        else:

                                time_button_1.config(text="10:30", bg="grey", state=DISABLED)
                        
                #Blade_time_1330
                        
                if hour_now>13:
                    
                    time_button_2.config(text="13:30", bg="grey", state=DISABLED)
                    
                elif hour_now==13:

                    if minute_now>30:

                        time_button_2.config(text="13:30", bg="grey", state=DISABLED)
                        
                    else:

                            if menu.seats_left_2>0:

                                time_button_2.config(text="13:30", command=time_2_selected)

                            else:

                                    time_button_2.config(text="13:30", bg="grey", state=DISABLED)

                else:

                        if menu.seats_left_2>0:

                            time_button_2.config(text="13:30", command=time_2_selected)

                        else:

                                time_button_2.config(text="13:30", bg="grey", state=DISABLED)
                        
                #Blade_time_1645
                        
                if hour_now>16:
                    
                    time_button_3.config(text="16:45", bg="grey", state=DISABLED)
                    
                elif hour_now==16:

                    if minute_now>45:

                        time_button_3.config(text="16:45", bg="grey", state=DISABLED)
                        
                    else:

                            if menu.seats_left_3>0:

                                time_button_3.config(text="16:45", command=time_3_selected)

                            else:

                                    time_button_3.config(text="16:45", bg="grey", state=DISABLED)

                else:

                        if menu.seats_left_3>0:

                            time_button_3.config(text="16:45", command=time_3_selected)

                        else:

                                time_button_3.config(text="16:45", bg="grey", state=DISABLED)
                        
                #Blade_time_2000
                        
                if hour_now>20:
                    
                    time_button_4.config(text="20:00", bg="grey", state=DISABLED)
                    
                elif hour_now==20:

                    if minute_now>0:

                        time_button_4.config(text="20:00", bg="grey", state=DISABLED)
                        
                    else:

                            if menu.seats_left_4>0:

                                time_button_4.config(text="20:00", command=time_4_selected)

                            else:

                                    time_button_4.config(text="20:00", bg="grey", state=DISABLED)

                else:

                        if menu.seats_left_4>0:

                            time_button_4.config(text="20:00", command=time_4_selected)

                        else:

                                time_button_4.config(text="20:00", bg="grey", state=DISABLED)

            time_button_1.place(relx=0.15, rely=0.3) #this places the button
            time_button_2.place(relx=0.15, rely=0.6) #this places the button
            time_button_3.place(relx=0.55, rely=0.3) #this places the button
            time_button_4.place(relx=0.55, rely=0.6) #this places the button
            Time.time_bg.place(relx=0, rely=0)  #this places the background
            countdown.attributes("-topmost", True) #this raises the countdown window
            
        class film_class: #this the film class
            
            def __init__(self, film_select): #this intialise things set for this class
                
                def thor_selected(): #this the function when the customer clicks the thor film picture
                    
                    menu.filmid=1 #this sets the variable filmid from the class menu to 1
                    time() #this calls the time function
                    time_select.attributes("-topmost", 1) #this raises the time_select window
                    film_select.attributes("-topmost", 0) #this lowers the film_select window
                    
                def baby_selected(): #this the function when the customer clicks the baby driver film picture
                    
                    menu.filmid=2 #this sets the variable filmid from the class menu to 2
                    time() #this calls the time function
                    menu.page_number=3 #this sets the variable page_number from the menu class to 3
                    time_select.attributes("-topmost", 1) #this raises the time_select window
                    film_select.attributes("-topmost", 0) #this lowers the film_select window      

                def dunkirk_selected(): #this the function when the customer clicks the dunkirk film picture
                    
                    menu.filmid=3 #this sets the variable filmid from the class menu to 3
                    time() #this calls the time function
                    time_select.attributes("-topmost", 1) #this raises the time_select window
                    film_select.attributes("-topmost", 0) #this lowers the film_select window 
                    
                def blade_selected(): #this the function when the customer clicks the blade runner film picture
                    
                    menu.filmid=4 #this sets the variable filmid from the class menu to 4
                    time() #this calls the time function
                    menu.page_number=3 #this sets the variable page_number from the menu class to 3
                    time_select.attributes("-topmost", 1) #this raises the time_select window
                    film_select.attributes("-topmost", 0) #this lowers the film_select window
                                    
                def back_to_menu(): #this is a function to go to the main menu
                    
                    film_select.attributes("-topmost", 0) #this lowers the film_select window
                    menu.page_number=1 #this sets the variable page_number from the menu class to 1
                    master.attributes("-topmost", 1) #this raises the master window
                    
                self.film_select = film_select #this links the film_select to the class
                film_select.overrideredirect(1) #this makes the film_select window raise to the the top
                film_select.geometry("%dx%d+0+0" % (w, h)) #this resizes the window
                film_select.resizable(width = False, height = False) #this removes the top bar on the window
                self.bg_Label=Label(film_select, image=menu.film_select_bg, bg="black") #this the label for the background
                self.bg_Label.grid() #this places the background on the window
                self.thor_button = Button(film_select, command=thor_selected, bg="black") #this creates the thor picture button
                self.thor_button.config(image=menu.thor_button_image,width="200",height="200") #this edits the thor picture button
                self.thor_button.place(relx=0.075, rely=0.25) #this places the thor picture button
                self.baby_button = Button(film_select, command=baby_selected, bg="black") #this creates the baby driver picture button
                self.baby_button.config(image=menu.baby_button_image,width="200",height="200") #this edits the baby driver picture button
                self.baby_button.place(relx=0.075, rely=0.65) #this places the baby driver picture button
                self.dunkirk_button = Button(film_select, command=dunkirk_selected, bg="black") #this creates the dunkirk picture button
                self.dunkirk_button.config(image=menu.dunkirk_button_image,width="200",height="200") #this edits the dunkirk picture button
                self.dunkirk_button.place(relx=0.53, rely=0.25) #this places the dunkirk picture button
                self.blade_button = Button(film_select, command=blade_selected, bg="black") #this creates the blade runner picture button
                self.blade_button.config(image=menu.blade_button_image,width="200",height="200") #this edits the blade runner picture button
                self.blade_button.place(relx=0.53, rely=0.65) #this places the blade runner picture button
                self.back_to_menu_button=Button(film_select, text="Back", command=back_to_menu) #this makes the back button to the main menu
                self.back_to_menu_button.configure(font=("Courier", 20), fg="white", bg="black") #this edits the back button
                self.back_to_menu_button.place(relx=0.03, rely=0.05) #this places the back button
                def callback(event): #this is a function that is called when the background is clicked on
                    countdown.attributes("-topmost", 1) #this rasies the countdown window
                self.bg_Label.bind("<Button-1>", callback) #this links a function to a label
                
        class menu_class: #this is the main menu class
                            
            def __init__(self, master): #this intialise things set for this class
                
                self.filmid = 0 #this sets the variable filmmid to 0
                self.master = master #this links the class to the tkinter webpage called master
                self.timeid=0 #this sets the variable timeid to 0
                self.seats_left_1=0 #this sets the variable seats_left_1 to 0
                self.seats_left_2=0 #this sets the variable seats_left_2 to 0
                self.seats_left_3=0 #this sets the variable seats_left_3 to 0
                self.blade_button_image = PhotoImage(file="blade.gif") #this sets the variable blade_button_image to an image for the film blade
                self.dunkirk_button_image = PhotoImage(file="dunkirk.gif") #this sets the variable dunkirk_button_image to an image for the film dunkirk
                self.seats_left_4=0 #this sets the variable seats_left_4 to 0
                self.page_number=1 #this sets the variable page_number to 1
                self.bg_image = PhotoImage(file="menu_bg.gif") #this sets the variable bg_image to a background
                self.thor_button_image = PhotoImage(file="thor.gif") #this sets the variable thor_button_image to an image for the film thor
                self.film_select_bg=PhotoImage(file="menubg_3.gif") #this sets the variable film_select_bg to the background for the film selection page
                self.baby_button_image = PhotoImage(file="baby.gif") #this sets the variable baby_button_image to an image for the film baby driver
                master.overrideredirect(1) #this makes the window come to the top
                master.geometry("%dx%d+0+0" % (w, h)) #this scales the window to the screen
                master.resizable(width = False, height = False) #this removes the top window bar
                self.menu_bg_image = PhotoImage(file = "menu_bg1.gif") #this sets the variable menu_bg_image for the main menu background
                self.menu_bg = Label(master, image=self.menu_bg_image, bg="black") #this sets the variable menu_bg to a label for the background of the main menu
                self.menu_bg.grid() #this places the background on the window
                self.start=0 #this sets the variable start to 0
                self.start_seconds=0 #this sets the variable start_seconds to 0
                self.buy_tickets_button = Button(master, text="Buy Tickets")#this sets the variable buy_tickets_button to the button to go to the film selection page 
                self.buy_tickets_button.config(width=30, height=6, font=("Courier", 20), fg="white", bg="black", command = self.film_select) 
                self.buy_tickets_button.place(relx=0.32, rely=0.6) #this places the button on the page
                       
            def film_select(self): #this the function that is called when the customer presses the button on the main menu

                film_select.attributes("-topmost", 1) #this raises the window film_select to the top
                try:
                    Countdown.display_time_film_select.destroy() #this tries to delete the display_time_film_select window

                except(Exception):
                    pass
                try:
                    Countdown.display_time_seconds_film_select.destroy() #this tries to delete the display_time_seconds_film_select window
                except(Exception):
                    pass
                Countdown.timer() #this calls the function Countdown
                menu.page_number=2
                master.attributes("-topmost", 0) #this lowers the window master
                countdown.attributes("-topmost", 1) #this raises the window countdown
                

        #this creates empty lists
        tseats=[]
        xseats=[]
        yseats=[]
        #this sets the variable username2 to ""
        username2=""
        #this makes the window
        master = Toplevel()
        #this sets the variables w and h to the size of the screen
        w, h = master.winfo_screenwidth(), master.winfo_screenheight()
        #this links the class to the window
        menu = menu_class(master)
        #this raises the window
        master.attributes("-topmost", 1)
        #this makes the window
        countdown=Toplevel()
        #this lowers the window
        countdown.attributes("-topmost", 0)
        #this links the class to the window
        Countdown=countdown_class(countdown)
        #this makes the window
        time_select = Toplevel()
        #this makes the window
        ticket_select = Toplevel()
        #this makes the window
        seat_select = Toplevel()
        #this lowers the window
        time_select.attributes("-topmost", 0)
        #this lowers the window
        ticket_select.attributes("-topmost", 0)
        #this makes the window
        film_select = Toplevel()
        #this lowers the window
        film_select.attributes("-topmost", 0)
        #this lowers the window
        seat_select.attributes("-topmost", 0)
        #this makes the window
        Film = film_class(film_select)
        #this makes the window
        Time = time_class(time_select)
        #this links the class to the window
        Ticket = ticket_class(ticket_select)
        #this links the class to the window
        Seat = seat_class(seat_select)
        #this makes the window
        pick_login = Toplevel()
        #this lowers the window
        pick_login.attributes("-topmost", 0)
        #this links the class to the window
        Pick = pick_login_class(pick_login)
        #this makes the window
        enter_signup = Toplevel()
        #this lowers the window
        enter_signup.attributes("-topmost", 0)
        #this links the class to the window
        Enter_signup=enter_signup_class(enter_signup)
        #this makes the window
        enter_login = Toplevel()
        #this lowers the window
        enter_login.attributes("-topmost", 0)
        #this links the class to the window
        Enter = login_class(enter_login)
        #this makes the window
        payment = Toplevel()
        #this lowers the window
        payment.attributes("-topmost", 0)
        #this links the class to the window
        pay = payment_class(payment)
        #this makes the window
        keyboard = Toplevel()
        #this lowers the window
        keyboard.attributes("-topmost", 0)
        #this links the class to the window
        Keyboard = keyboard_class(keyboard)
        #this makes the window
        collect_ticket=Toplevel()
        #this lowers the window
        collect_ticket.attributes("-topmost", 0)
        #this links the class to the window
        Collect_ticket=collect_ticket_class(collect_ticket)
        #this makes the window
        out_of_time=Toplevel()
        #this lowers the window
        out_of_time.attributes("-topmost", 0)
        #this links the class to the window
        Out=out_of_time_class(out_of_time)
        
code_restart() #this calls the function code_restart
