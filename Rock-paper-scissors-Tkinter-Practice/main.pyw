#!/usr/bin/python3

# Images by: https://www.vecteezy.com/free-vector/rock-paper-Scissorss
# file by: https://github.com/Jean-carje


from random import choice
import tkinter as tk


class GameScreen(tk.Tk):
    def __init__(self):
        super().__init__()

        # Image Object
        self.rock = tk.PhotoImage(file="./images/rock.png")
        self.paper = tk.PhotoImage(file="./images/paper.png")
        self.Scissors = tk.PhotoImage(file="./images/Scissors.png")
        self.blank = tk.PhotoImage(file="./images/blank.png")
        self.center = tk.PhotoImage(file="./images/center.png")
        self.reset = tk.PhotoImage(file="./images/reset.png")
        
        # Counter Wins
        self.playerWins = 0
        self.computerWins = 0

        # title, background, size, icon
        self.title("Rock, Paper, Scissors Game")
        self.iconphoto(False, tk.PhotoImage(file='./images/icon.png'))
        self.configure(bg="#cfdfff")
        self.geometry("800x540")
        self.resizable(False, False)
  
        # Padding
        self.padX = (5, 5)
        self.padY = (5, 5)

        # ----------------------- Text ----------------------- 
        # Wins Text
        # self.compLabel: Computer
        # self.plaLabel: Player
        self.compLabel = tk.Label(self, text=self.computerWins, font=("Helvetica", "38"), bg="#cfdfff")
        self.plaLabel = tk.Label(self, text=self.playerWins, font=("Helvetica", "38"), bg="#cfdfff")
        self.plaLabel.grid(column=3, row=1, padx=self.padX, pady=self.padY)
        self.compLabel.grid(column=1, row=1, padx=self.padX, pady=self.padY)

        # Computer Text
        self.computer = tk.Label(self, text="Computer!", font=("Helvetica", "25"), bg="#cfdfff")
        self.computer.grid(column=0, row=0, padx=self.padX, pady=(20, 10))

        # Player Text
        self.player = tk.Label(self, text="You!", font=("Helvetica", "25"), bg="#cfdfff")
        self.player.grid(column=4, row=0, padx=self.padX, pady=(20, 10))

        # Size control (text center space)
        tk.Label(self, image=self.center, width="150", relief="flat", borderwidth=0).grid(column=2, row=1)

        # Draw initial values
        self.welcome()

        # ----------------------- Label Computer items ----------------------- 
        self.rockComp = tk.Label(self, image=self.rock, width="150", borderwidth=0)
        self.paperComp = tk.Label(self, image=self.paper, width="150", borderwidth=0)
        self.ScissorsComp = tk.Label(self, image=self.Scissors, width="150", borderwidth=0)
        
        self.rockComp.grid(column=0, row=1)
        self.paperComp.grid(column=0, row=2)
        self.ScissorsComp.grid(column=0, row=3)

        # ----------------------- Button Player items ----------------------- 
        self.rockButton = tk.Button(self, image=self.rock, width="150", borderwidth=0, command=lambda: self.playGame("Rock"))
        self.paperButton = tk.Button(self, image=self.paper, width="150", borderwidth=0, command=lambda: self.playGame("Paper"))
        self.ScissorsButton = tk.Button(self, image=self.Scissors, width="150", borderwidth=0, command=lambda: self.playGame("Scissors"))

        self.rockButton.grid(column=4, row=1)
        self.paperButton.grid(column=4, row=2)
        self.ScissorsButton.grid(column=4, row=3)

        # ----------------------- reset button ----------------------- 
        self.restartButton = tk.Button(self, image=self.reset, text=" Reset!", compound=tk.LEFT, font=("Helvetica", "15"), width="150")
        self.restartButton.configure(bg="#cfdfff", fg="#E31C1C", borderwidth=0, activebackground="#cfdfff", pady=10, command=self.restart)
        self.restartButton.grid(column=2, row=3)



    def playGame(self, user):
        selections = {
            "Rock": ["Scissors", self.rock],
            "Scissors": ["Paper", self.Scissors],
            "Paper": ["Rock", self.paper]
        }

        choiceComp = choice(list(selections.keys()))

        if choiceComp == user:
            # Draw
            self.textCenter.configure(text="There is\na draw.")
            self.textCenter.grid(column=2, row=2)

            self.blankPlayer = tk.Label(self, image=selections[user][1], width="150", borderwidth=0)
            self.blankComp = tk.Label(self, text="Computer", image=selections[choiceComp][1], width="150", borderwidth=0)
            self.blankPlayer.grid(column=3, row=2)
            self.blankComp.grid(column=1, row=2)

        elif selections[user][0] == choiceComp:
            # Player Win
            self.playerWins += 1
            self.textCenter.configure(text="Well done!")
            self.plaLabel.configure(text=self.playerWins)
            self.plaLabel.grid(column=3, row=1, padx=self.padX, pady=self.padY)
            self.textCenter.grid(column=2, row=2, padx=(2, 2))

            self.blankPlayer = tk.Label(self, image=selections[user][1], width="150", borderwidth=0)
            self.blankComp = tk.Label(self, text="Computer", image=selections[choiceComp][1], width="150", borderwidth=0)
            self.blankPlayer.grid(column=3, row=2)
            self.blankComp.grid(column=1, row=2)

        else:
            # Computer Win
            self.computerWins += 1
            self.textCenter.configure(text="Sorry,\nbut the\ncomputer\nwin.")
            self.compLabel.configure(text=self.computerWins)
            self.compLabel.grid(column=1, row=1, padx=self.padX, pady=self.padY)
            self.textCenter.grid(column=2, row=2)

            self.blankPlayer = tk.Label(self, image=selections[user][1], width="150", borderwidth=0)
            self.blankComp = tk.Label(self, text="Computer", image=selections[choiceComp][1], width="150", borderwidth=0)
            self.blankPlayer.grid(column=3, row=2)
            self.blankComp.grid(column=1, row=2)

    def welcome(self):
        """ Draw Initial """
        self.configure(bg="#cfdfff")
        # Text center
        self.textCenter = tk.Label(self, text="Choose\nan item!", font=("Helvetica", 18), bg="#cfdfff")
        self.textCenter.grid(column=2, row=2, padx=(7, 7))

        self.blankComp = tk.Label(self, image=self.blank, width="150", borderwidth=0)
        self.blankPlayer = tk.Label(self, image=self.blank, width="150", borderwidth=0)
        self.blankPlayer.grid(column=3, row=2, padx=self.padX, pady=self.padY)
        self.blankComp.grid(column=1, row=2, padx=self.padX, pady=self.padY)

    def restart(self):
        # Counter Wins
        self.playerWins = 0
        self.computerWins = 0

        # Wins Text
        self.compLabel = tk.Label(self, text=self.computerWins, font=("Helvetica", "38"), bg="#cfdfff")
        self.plaLabel = tk.Label(self, text=self.playerWins, font=("Helvetica", "38"), bg="#cfdfff")

        self.welcome()
        self.plaLabel.grid(column=3, row=1, padx=self.padX, pady=self.padY)
        self.compLabel.grid(column=1, row=1, padx=self.padX, pady=self.padY)



if __name__ == "__main__":
    Gs = GameScreen()
    Gs.mainloop()
