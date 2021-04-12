from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random


#Creating the RPS class
class RPS:
	#set up the window
	def __init__(self, master):
		self.master = master
		master.config(bg = "green")
		master.title("Rock..Paper..Scissors")
		master.iconbitmap("icon.ico")
		master.maxsize(800,500)
		master.minsize(800, 500)
		master.geometry("800x500+220+100")
		messagebox.showinfo("Author", "This game was developed by Rohit Joe Mendus.")
		messagebox.showinfo("Welcome", "Welcome to this game.")	
		self.score_1 = 0
		self.score_2 = 0
		self.turns = 0


	#Setting up the exit confirmation
	def exit(self):
		res = messagebox.askyesno("Exit?", "Are you sure you want to exit the game?")
		if res == 1:
			self.master.destroy()


	#Set up the clear screen function
	def clear(self):
		lis = self.master.winfo_children()
		for i in lis:
			i.destroy()


	#Checking if a game is finished
	def check(self, type_, limit):
		self.clear()
		lab7 = Label(self.master, text = "", bg = "green", fg = "red", font = ('Helvetica', 30))
		lab7.place(x = 200, y = 200)
		if type_ == "Best of":
			if str(limit) == str(self.turns):
				if self.score_1 == self.score_2:
					lab7.config(text = "The game is a draw\nPlayer: " + str(self.score_1) + "  Computer: " + str(self.score_2))
				elif self.score_1 > self.score_2:
					lab7.config(text = "Player wins the game!\nPlayer: " + str(self.score_1) + "  Computer: " + str(self.score_2))
				elif self.score_2 > self.score_1:
					lab7.config(text = "Computer wins the game!\nPlayer: " + str(self.score_1) + "  Computer: " + str(self.score_2))
				return 1
			else:
				return 0

		elif type_ == "Score limit":
			if self.score_1 == int(limit):
				lab7.config(text = "Player wins the game!\nPlayer: " + str(self.score_1) + "  Computer: " + str(self.score_2))
				return 1
			elif self.score_2 == int(limit):
				lab7.config(text = "Computer wins the game!\nPlayer: " + str(self.score_1) + "  Computer: " + str(self.score_2))
				return 1
			return 0


	#Making rock, paper, scissor coundown
	def countdown(self, choose, choice_2):
		self.clear()
		#lab5 = Label(self.master, text = "Rock...")
		lab4 = Label(self.master, text = "Rock...", bg = "green", fg = "red", font = ('Helvetica', 45))
		lab4.place(x = 310, y = 190)
		self.master.after(1000, lambda: lab4.config(text = "Paper...", fg = "blue"))
		self.master.after(2000, lambda: lab4.config(text = "Scissors!", fg = "yellow"))
		self.master.after(3000, lambda: lab4.config(text = choose + "    Vs    " + choice_2,  fg = "#360202", bg = "green", font = ('Helvetica', 50)))
		self.master.after(3000, lambda: lab4.place(x = 60, y = 190))
		self.master.after(4000, lambda: self.clear())


	#Creating a function that manages the tkinter after methods
	def manage(self, opt, choose, choice_2):
		if opt == 1:
			self.countdown(choose, choice_2)
		elif opt == 2:
			self.master.after(4000, lambda: self.check_output(choose, choice_2))
		elif opt == 3:
			self.outcome = self.check(self.type_, self.limit)


	#Creating a second function that manages the tkinter after method
	def manage_2(self, opt):
		if opt == 3:
			self.outcome = self.check(self.type_, self.limit)		


	#Managing to proceed to the next game
	def new_game(self, nex):
		if nex  != 1:
			self.play(self.type_, self.limit)
		else:
			self.score_1 = 0
			self.score_2 = 0
			self.turns = 0
			self.clear()
			self.set_menu()


	#Checking individual rounds of the game
	def check_output(self, choice_1, choice_2):
		lab6 = Label(self.master, text = "", bg = "green", fg = "blue", font = ('Helvetica', 30))
		lab6.place(x = 200, y = 200)
		if choice_1 == choice_2:
			self.master.after(3000, lab6.config(text = "It is a draw!\nNobody got any points!"))
			self.turns += 1
		elif choice_1 == "Rock":
			if choice_2 == "Paper":
				self.master.after(3000, lab6.config(text = "Paper covers Rock!\nComputer gets a point!!!"))
				self.score_2 += 1
				self.turns += 1
			else:
				self.master.after(3000, lab6.config(text = "Rock smashes Scissors!\nPlayer gets a point!!!"))
				self.score_1 += 1
				self.turns += 1
		elif choice_1 == "Paper":
			if choice_2 == "Scissors":
				self.master.after(3000, lab6.config(text = "Scissors cuts paper!\nComputer gets a point!!!"))
				self.score_2 += 1
				self.turns += 1
			else:
				self.master.after(3000, lab6.config(text = "Paper covers Rock!\nPlayer gets a point!!!"))
				self.score_1 += 1
				self.turns += 1
		elif choice_1 == "Scissors":
			if choice_2 == "Rock":
				self.master.after(3000, lab6.config(text = "Rock smashes Scissors!\nComputer gets a point!!!"))
				self.score_2 += 1
				self.turns += 1
			else:
				self.master.after(3000, lab6.config(text = "Scissors cuts paper!\nPlayer gets a point!!!"))
				self.score_1 += 1
				self.turns += 1
		self.master.after(5000, lambda: self.manage_2(3))
		self.master.after(8000, lambda: self.new_game(self.outcome))
		
	
	#Setting the second gameplay of the game
	def game_play2(self, choose):
		choices = ["Rock", "Paper", "Scissors"]
		choice_2 = random.choice(choices)
		self.manage(1, choose, choice_2)
		self.manage(2, choose, choice_2)


	#Setting the first gameplay of the game
	def game_play(self, a, b):
		lab1 = Label(self.master, text = "Player " + str(self.score_1) + "/" + str(b), fg = "blue", font = ('Helvetica', 18), bg = "green")
		lab2 = Label(self.master, text = "Computer " + str(self.score_2) + "/" + str(b), fg = "red", font = ('Helvetica', 18), bg = "green")
		lab3 = Label(self.master, text = "Choose", fg = "#022e03", font = ('Helvetica', 30), bg = "green")
		lab1.place(x = 30, y = 30)
		lab2.place(x = 600, y = 30)
		lab3.place(x = 320, y = 70)
		but1 = Button(self.master, text = "Rock", bg = "red", fg = "white", font = ('Helvetica', 18), activebackground = "red", activeforeground = "white", command = lambda: self.game_play2("Rock"))
		but2 = Button(self.master, text = "Paper", bg = "blue", fg = "white", font = ('Helvetica', 18), activebackground = "blue", activeforeground = "white", command = lambda: self.game_play2("Paper"))
		but3 = Button(self.master, text = "Scissors", bg = "yellow", fg = "white", font = ('Helvetica', 18), activebackground = "yellow", activeforeground = "white", command = lambda: self.game_play2("Scissors"))
		but1.place(x = 350, y = 150)
		but2.place(x = 230, y = 220)
		but3.place(x = 460, y = 220)


	#Checking if the required ouput is ok, if not managing it
	def play(self, type_, num):
		self.type_ = type_
		self.limit = num
		if num.isdigit():
			if int(num) >= 1 and int(num) <= 100:
				self.clear()
				self.game_play(type_, num)
			else:
				messagebox.showwarning("Only integers!", "Please only give integers that are between 1 to 100!")
		else:
			messagebox.showwarning("Only integers!", "Please only give integers that are between 1 to 100!")


	#Making the menu of the game
	def set_menu(self):
		#global but
		exit_but = Button(self.master, text = "Exit", bg = "red", fg = "white", activebackground = "red", activeforeground = "white", command = exit, font = ('Helvetica', 18))
		exit_but.place(x = 700, y = 20)
		lab = Label(self.master, text = "How do you want to play?", relief = RAISED, bg = "#ff4000", fg = "green", bd = 3, font = ("Comic Sans MS", 32))
		lab.place(x = 150, y = 50)
		var = StringVar()
		options = ["Best of", "Score limit"]
		var.set(options[0])
		opt = OptionMenu(self.master, var, *options)
		opt.config(width=10, font=('Helvetica', 12))
		opt.place(x = 250, y = 180)
		spin = Spinbox(self.master, from_ = 1, to = 100, width=10, font=('Helvetica', 12))
		spin.place(x = 450, y = 190)
		but = Button(self.master, bg = "blue", fg = "white", text = "Play", command = lambda: self.play(var.get(), spin.get()), font = ('Helvetica', 18), activebackground = "red", activeforeground = "white")
		but.place(x = 390, y = 250)
		

	#Running and combining the code	
	def run(self):
		self.master.protocol("WM_DELETE_WINDOW", self.exit)
		self.set_menu()


#Making instance of the RPS class
win  = Tk()
game = RPS(win)
#Running th program
game.run()
win.mainloop()