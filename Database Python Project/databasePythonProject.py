from tkinter import *

import mysql.connector

cnx = mysql.connector.connect(user ='root',password='jasper', database = 'team')
cursor = cnx.cursor()

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text = "Welcome to the Borussia Dortmund Database:\n"
              "Select what you would like to know about").grid(row = 0, column = 1, columnspan = 2, sticky = W)

        #staff button
        self.staff = BooleanVar()
        Checkbutton(self, text = "Staff", variable = self.staff, command = self.update_main).grid(row = 1, column = 0, columnspan = 2, sticky = W)

        #player button
        self.player = BooleanVar()
        Checkbutton(self, text = "Players and Stats", variable = self.player, command = self.update_main).grid(row = 2, column = 0, columnspan = 2, sticky = W)
        




    
    def create_player_widgets(self):
        Label(self, text = "Select a player to display stats").grid(row = 5, column = 0, columnspan = 2, sticky = W)

        #Lewandowski Button
        self.lewandowski = BooleanVar()
        Checkbutton(self, text = "Lewandowski", variable = self.lewandowski, command = self.update_player).grid(row = 6, column = 0, sticky = W)

        #Reus Button
        self.reus = BooleanVar()
        Checkbutton(self, text = "Reus", variable = self.reus, command = self.update_player).grid(row = 7, column = 0, sticky = W)

        #Mkhitaryan Button
        self.mkhitaryan = BooleanVar()
        Checkbutton(self, text = "Mkhitaryan", variable = self.mkhitaryan, command = self.update_player).grid(row = 8, column = 0, sticky = W)

        #Blaszczykowski Button
        self.blaszczykowski = BooleanVar()
        Checkbutton(self, text = "Blaszczykowski", variable = self.blaszczykowski, command = self.update_player).grid(row = 9, column = 0, sticky = W)

        #Bender Button
        self.bender = BooleanVar()
        Checkbutton(self, text = "Bender", variable = self.bender, command = self.update_player).grid(row = 10, column = 0, sticky = W)

        #Gundogan Button
        self.gundogan = BooleanVar()
        Checkbutton(self, text = "Gundogan", variable = self.gundogan, command = self.update_player).grid(row = 11, column = 0, sticky = W)

        #Schmelzer Button
        self.schmelzer = BooleanVar()
        Checkbutton(self, text = "Schmelzer", variable = self.schmelzer, command = self.update_player).grid(row = 12, column = 0, sticky = W)

        #Hummels Button
        self.hummels = BooleanVar()
        Checkbutton(self, text = "Hummels", variable = self.hummels, command = self.update_player).grid(row = 13, column = 0, sticky = W)

        #Subotic Button
        self.subotic = BooleanVar()
        Checkbutton(self, text = "Subotic", variable = self.subotic, command = self.update_player).grid(row = 14, column = 0, sticky = W)

        #Piszczek Button
        self.piszczek = BooleanVar()
        Checkbutton(self, text = "Piszczek", variable = self.piszczek, command = self.update_player).grid(row = 15, column = 0, sticky = W)

        #Wiedenfeller Button
        self.weidenfeller = BooleanVar()
        Checkbutton(self, text = "Weidenfeller", variable = self.weidenfeller, command = self.update_player).grid(row = 16, column = 0, sticky = W)

        self.fullteam = BooleanVar()
        Checkbutton(self, text = "Full Team", variable = self.fullteam, command = self.update_player).grid(row=17, column = 0, sticky = W)

        self.text = Text(self, width = 50, height = 20, wrap = WORD)
        self.text.grid(row = 18, column = 0, columnspan = 2, sticky = W)

    def create_staff_widgets(self):
        Label(self, text = "Select the staff member to display info").grid(row = 5, column = 4, columnspan = 2, sticky = W)

        #Klopp Button
        self.klopp = BooleanVar()
        Checkbutton(self, text = "Klopp", variable = self.klopp, command = self.update_staff).grid(row = 6, column = 4, sticky = W)

        #Buvac Button
        self.buvac = BooleanVar()
        Checkbutton(self, text = "Buvac", variable = self.buvac, command = self.update_staff).grid(row = 7, column = 4, sticky = W)

        #Krawietz Button
        self.krawietz = BooleanVar()
        Checkbutton(self, text = "Krawietz", variable = self.krawietz, command = self.update_staff).grid(row = 8, column = 4, sticky = W)

        #Schlumberger Button
        self.schlumberger = BooleanVar()
        Checkbutton(self, text = "Schlumberger", variable = self.schlumberger, command = self.update_staff).grid(row = 9, column = 4, sticky = W)

        #Beck Button
        self.beck = BooleanVar()
        Checkbutton(self, text = "Beck", variable = self.beck, command = self.update_staff).grid(row = 10, column = 4, sticky = W)

        #de Beer Button
        self.deBeer = BooleanVar()
        Checkbutton(self, text = "de Beer", variable = self.deBeer, command = self.update_staff).grid(row = 11, column = 4, sticky = W)

        #Wangler Button
        self.wangler = BooleanVar()
        Checkbutton(self, text = "Wangler", variable = self.wangler, command = self.update_staff).grid(row = 12, column = 4, sticky = W)

        #Zetzmann Button
        self.zetzmann = BooleanVar()
        Checkbutton(self, text = "Zetzmann", variable = self.zetzmann, command = self.update_staff).grid(row = 13, column = 4, sticky = W)

        self.text2 = Text(self, width = 50, height = 20, wrap = WORD)
        self.text2.grid(row = 18, column = 4, columnspan = 2, sticky = W)


        

    def update_player(self):

        message = ""

        if self.lewandowski.get():
            cnx = mysql.connector.connect(user ='root',password='jasper', database = 'team')
            cursor = cnx.cursor()
            query = ("SELECT * FROM roster NATURAL JOIN stats WHERE name = 'Lewandowski'")
            cursor.execute(query)
            for (jersey_number, name, weight, height, nationality, position, age, salary, goals, assists, saves, clean_sheets, shots_on_target, shots_off_target, game_played) in cursor:
                message += ("Number {}, {}, Position: {}, Weight: {}lbs, Height: {}cm, Nationality: {}, Age: {}, Salary: {}, Goals: {}, Assists: {}, Saves: {}, Clean Sheets : {}, Shots on target: {}, Shots off target: {}, Games Played: {}".format
                            (jersey_number, name, weight, height, nationality, position, age, salary, goals, assists, saves, clean_sheets, shots_on_target, shots_off_target, game_played))
                message += "\n\n"

        if self.reus.get():
            cnx = mysql.connector.connect(user ='root',password='jasper', database = 'team')
            cursor = cnx.cursor()
            query = ("SELECT * FROM roster NATURAL JOIN stats WHERE name = 'Reus'")
            cursor.execute(query)
            for (jersey_number, name, weight, height, nationality, position, age, salary, goals, assists, saves, clean_sheets, shots_on_target, shots_off_target, game_played) in cursor:
                message += ("Number {}, {}, Position: {}, Weight: {}lbs, Height: {}cm, Nationality: {}, Age: {}, Salary: {}, Goals: {}, Assists: {}, Saves: {}, Clean Sheets : {}, Shots on target: {}, Shots off target: {}, Games Played: {}".format
                            (jersey_number, name, weight, height, nationality, position, age, salary, goals, assists, saves, clean_sheets, shots_on_target, shots_off_target, game_played))
                message += "\n\n"

        if self.mkhitaryan.get():
            cnx = mysql.connector.connect(user ='root',password='jasper', database = 'team')
            cursor = cnx.cursor()
            query = ("SELECT * FROM roster NATURAL JOIN stats WHERE name = 'Mkhitaryan'")
            cursor.execute(query)
            for (jersey_number, name, weight, height, nationality, position, age, salary, goals, assists, saves, clean_sheets, shots_on_target, shots_off_target, game_played) in cursor:
                message += ("Number {}, {}, Position: {}, Weight: {}lbs, Height: {}cm, Nationality: {}, Age: {}, Salary: {}, Goals: {}, Assists: {}, Saves: {}, Clean Sheets : {}, Shots on target: {}, Shots off target: {}, Games Played: {}".format
                            (jersey_number, name, weight, height, nationality, position, age, salary, goals, assists, saves, clean_sheets, shots_on_target, shots_off_target, game_played))
                message += "\n\n"

        if self.blaszczykowski.get():
            cnx = mysql.connector.connect(user ='root',password='jasper', database = 'team')
            cursor = cnx.cursor()
            query = ("SELECT * FROM roster NATURAL JOIN stats WHERE name = 'Blaszczykowski'")
            cursor.execute(query)
            for (jersey_number, name, weight, height, nationality, position, age, salary, goals, assists, saves, clean_sheets, shots_on_target, shots_off_target, game_played) in cursor:
                message += ("Number {}, {}, Position: {}, Weight: {}lbs, Height: {}cm, Nationality: {}, Age: {}, Salary: {}, Goals: {}, Assists: {}, Saves: {}, Clean Sheets : {}, Shots on target: {}, Shots off target: {}, Games Played: {}".format
                            (jersey_number, name, weight, height, nationality, position, age, salary, goals, assists, saves, clean_sheets, shots_on_target, shots_off_target, game_played))
                message += "\n\n"

        if self.bender.get():
            cnx = mysql.connector.connect(user ='root',password='jasper', database = 'team')
            cursor = cnx.cursor()
            query = ("SELECT * FROM roster NATURAL JOIN stats WHERE name = 'Bender'")
            cursor.execute(query)
            for (jersey_number, name, weight, height, nationality, position, age, salary, goals, assists, saves, clean_sheets, shots_on_target, shots_off_target, game_played) in cursor:
                message += ("Number {}, {}, Position: {}, Weight: {}lbs, Height: {}cm, Nationality: {}, Age: {}, Salary: {}, Goals: {}, Assists: {}, Saves: {}, Clean Sheets : {}, Shots on target: {}, Shots off target: {}, Games Played: {}".format
                            (jersey_number, name, weight, height, nationality, position, age, salary, goals, assists, saves, clean_sheets, shots_on_target, shots_off_target, game_played))
                message += "\n\n"

        if self.gundogan.get():
            cnx = mysql.connector.connect(user ='root',password='jasper', database = 'team')
            cursor = cnx.cursor()
            query = ("SELECT * FROM roster NATURAL JOIN stats WHERE name = 'Gundogan'")
            cursor.execute(query)
            for (jersey_number, name, weight, height, nationality, position, age, salary, goals, assists, saves, clean_sheets, shots_on_target, shots_off_target, game_played) in cursor:
                message += ("Number {}, {}, Position: {}, Weight: {}lbs, Height: {}cm, Nationality: {}, Age: {}, Salary: {}, Goals: {}, Assists: {}, Saves: {}, Clean Sheets : {}, Shots on target: {}, Shots off target: {}, Games Played: {}".format
                            (jersey_number, name, weight, height, nationality, position, age, salary, goals, assists, saves, clean_sheets, shots_on_target, shots_off_target, game_played))
                message += "\n\n"

        if self.schmelzer.get():
            cnx = mysql.connector.connect(user ='root',password='jasper', database = 'team')
            cursor = cnx.cursor()
            query = ("SELECT * FROM roster NATURAL JOIN stats WHERE name = 'Schmelzer'")
            cursor.execute(query)
            for (jersey_number, name, weight, height, nationality, position, age, salary, goals, assists, saves, clean_sheets, shots_on_target, shots_off_target, game_played) in cursor:
                message += ("Number {}, {}, Position: {}, Weight: {}, Height: {}, Nationality: {}, Age: {}, Salary: {}, Goals: {}, Assists: {}, Saves: {}, Clean Sheets : {}, Shots on target: {}, Shots off target: {}, Games Played: {}".format
                            (jersey_number, name, weight, height, nationality, position, age, salary, goals, assists, saves, clean_sheets, shots_on_target, shots_off_target, game_played))
                message += "\n\n"

        if self.hummels.get():
            cnx = mysql.connector.connect(user ='root',password='jasper', database = 'team')
            cursor = cnx.cursor()
            query = ("SELECT * FROM roster NATURAL JOIN stats WHERE name = 'Hummels'")
            cursor.execute(query)
            for (jersey_number, name, weight, height, nationality, position, age, salary, goals, assists, saves, clean_sheets, shots_on_target, shots_off_target, game_played) in cursor:
                message += ("Number {}, {}, Position: {}, Weight: {}lbs, Height: {}cm, Nationality: {}, Age: {}, Salary: {}, Goals: {}, Assists: {}, Saves: {}, Clean Sheets : {}, Shots on target: {}, Shots off target: {}, Games Played: {}".format
                            (jersey_number, name, weight, height, nationality, position, age, salary, goals, assists, saves, clean_sheets, shots_on_target, shots_off_target, game_played))
                message += "\n\n"

        if self.subotic.get():
            cnx = mysql.connector.connect(user ='root',password='jasper', database = 'team')
            cursor = cnx.cursor()
            query = ("SELECT * FROM roster NATURAL JOIN stats WHERE name = 'Subotic'")
            cursor.execute(query)
            for (jersey_number, name, weight, height, nationality, position, age, salary, goals, assists, saves, clean_sheets, shots_on_target, shots_off_target, game_played) in cursor:
                message += ("Number {}, {}, Position: {}, Weight: {}lbs, Height: {}cm, Nationality: {}, Age: {}, Salary: {}, Goals: {}, Assists: {}, Saves: {}, Clean Sheets : {}, Shots on target: {}, Shots off target: {}, Games Played: {}".format
                            (jersey_number, name, weight, height, nationality, position, age, salary, goals, assists, saves, clean_sheets, shots_on_target, shots_off_target, game_played))
                message += "\n\n"

        if self.piszczek.get():
            cnx = mysql.connector.connect(user ='root',password='jasper', database = 'team')
            cursor = cnx.cursor()
            query = ("SELECT * FROM roster NATURAL JOIN stats WHERE name = 'Piszczek'")
            cursor.execute(query)
            for (jersey_number, name, weight, height, nationality, position, age, salary, goals, assists, saves, clean_sheets, shots_on_target, shots_off_target, game_played) in cursor:
                message += ("Number {}, {}, Position: {}, Weight: {}lbs, Height: {}cm, Nationality: {}, Age: {}, Salary: {}, Goals: {}, Assists: {}, Saves: {}, Clean Sheets : {}, Shots on target: {}, Shots off target: {}, Games Played: {}".format
                            (jersey_number, name, weight, height, nationality, position, age, salary, goals, assists, saves, clean_sheets, shots_on_target, shots_off_target, game_played))
                message += "\n\n"

        if self.weidenfeller.get():
            cnx = mysql.connector.connect(user ='root',password='jasper', database = 'team')
            cursor = cnx.cursor()
            query = ("SELECT * FROM roster NATURAL JOIN stats WHERE name = 'Weidenfeller'")
            cursor.execute(query)
            for (jersey_number, name, weight, height, nationality, position, age, salary, goals, assists, saves, clean_sheets, shots_on_target, shots_off_target, game_played) in cursor:
                message += ("Number {}, {}, Position: {}, Weight: {}lbs, Height: {}cm, Nationality: {}, Age: {}, Salary: {}, Goals: {}, Assists: {}, Saves: {}, Clean Sheets : {}, Shots on target: {}, Shots off target: {}, Games Played: {}".format
                            (jersey_number, name, weight, height, nationality, position, age, salary, goals, assists, saves, clean_sheets, shots_on_target, shots_off_target, game_played))
                message += "\n\n"
                

        if self.fullteam.get():
            cnx = mysql.connector.connect(user ='root',password='jasper', database = 'team')
            cursor = cnx.cursor()
            query = ("SELECT * FROM team_stats")
            cursor.execute(query)
            for (goals, assists, wins, draws, losses, shutouts, fouls) in cursor:
                message += ("Goals: {}, Assists: {}, Wins: {}, Draws: {}, Losses: {}, Shutouts: {}, Fouls: {}".format
                            (goals, assists, wins, draws, losses, shutouts, fouls))
                message += "\n\n"
                

        self.text.delete(0.0, END)
        self.text.insert(0.0, message)


        
        
        
    def update_staff(self):
        message = ""

        if self.klopp.get():
            cnx = mysql.connector.connect(user ='root',password='jasper', database = 'team')
            cursor = cnx.cursor()
            query = ("SELECT * FROM staff WHERE name = 'Klopp'")
            cursor.execute(query)
            for (ID, name, position, age, salary) in cursor:
                message += ("ID Number: {}, Name: {}, Position: {}, Age: {}, Salary: {}".format
                            (ID, name, position, age, salary))
                message += "\n\n"
                
        if self.buvac.get():
            cnx = mysql.connector.connect(user ='root',password='jasper', database = 'team')
            cursor = cnx.cursor()
            query = ("SELECT * FROM staff WHERE name = 'Buvac'")
            cursor.execute(query)
            for (ID, name, position, age, salary) in cursor:
                message += ("ID Number: {}, Name: {}, Position: {}, Age: {}, Salary: {}".format
                            (ID, name, position, age, salary))
                message += "\n\n"
                
        if self.krawietz.get():
            cnx = mysql.connector.connect(user ='root',password='jasper', database = 'team')
            cursor = cnx.cursor()
            query = ("SELECT * FROM staff WHERE name = 'Krawietz'")
            cursor.execute(query)
            for (ID, name, position, age, salary) in cursor:
                message += ("ID Number: {}, Name: {}, Position: {}, Age: {}, Salary: {}".format
                            (ID, name, position, age, salary))
                message += "\n\n"
                
        if self.schlumberger.get():
            cnx = mysql.connector.connect(user ='root',password='jasper', database = 'team')
            cursor = cnx.cursor()
            query = ("SELECT * FROM staff WHERE name = 'Schlumberger'")
            cursor.execute(query)
            for (ID, name, position, age, salary) in cursor:
                message += ("ID Number: {}, Name: {}, Position: {}, Age: {}, Salary: {}".format
                            (ID, name, position, age, salary))
                message += "\n\n"
                
        if self.deBeer.get():
            cnx = mysql.connector.connect(user ='root',password='jasper', database = 'team')
            cursor = cnx.cursor()
            query = ("SELECT * FROM staff WHERE name = 'de Beer'")
            cursor.execute(query)
            for (ID, name, position, age, salary) in cursor:
                message += ("ID Number: {}, Name: {}, Position: {}, Age: {}, Salary: {}".format
                            (ID, name, position, age, salary))
                message += "\n\n"
                
        if self.wangler.get():
            cnx = mysql.connector.connect(user ='root',password='jasper', database = 'team')
            cursor = cnx.cursor()
            query = ("SELECT * FROM staff WHERE name = 'Wangler'")
            cursor.execute(query)
            for (ID, name, position, age, salary) in cursor:
                message += ("ID Number: {}, Name: {}, Position: {}, Age: {}, Salary: {}".format
                            (ID, name, position, age, salary))
                message += "\n\n"
                
        if self.zetzmann.get():
            cnx = mysql.connector.connect(user ='root',password='jasper', database = 'team')
            cursor = cnx.cursor()
            query = ("SELECT * FROM staff WHERE name = 'Zetzmann'")
            cursor.execute(query)
            for (ID, name, position, age, salary) in cursor:
                message += ("ID Number: {}, Name: {}, Position: {}, Age: {}, Salary: {}".format
                            (ID, name, position, age, salary))
                message += "\n\n"
                
        if self.beck.get():
            cnx = mysql.connector.connect(user ='root',password='jasper', database = 'team')
            cursor = cnx.cursor()
            query = ("SELECT * FROM staff WHERE name = 'Beck'")
            cursor.execute(query)
            for (ID, name, position, age, salary) in cursor:
                message += ("ID Number: {}, Name: {}, Position: {}, Age: {}, Salary: {}".format
                            (ID, name, position, age, salary))
                message += "\n\n"
                
        self.text2.delete(0.0, END)
        self.text2.insert(0.0, message)





    def update_main(self):

        if self.staff.get():
            self.create_staff_widgets()

        if self.player.get():
            self.create_player_widgets()

root = Tk()
root.title("Player selector")
root.geometry("1550x600")
app = Application(root)

root.mainloop()



