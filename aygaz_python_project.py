import tkinter as tk
from tkinter import messagebox
import random

class GameApp:
    def __init__(self, root):
        """Launcher: Launches the game application and creates the interface."""
        self.root = root
        self.root.title("Taş Kağıt Makas Oyunu")
        self.root.geometry("700x500")

        # Creates the main framework
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Creates and centers a title tag
        self.label = tk.Label(
            self.main_frame,
            text="Taş Kağıt Makas Oyunu",
            font=("Arial", 14, "bold")
        )
        self.label.place(relx=0.5, rely=0.2, anchor="center")

        # Creates and centers the start game button
        self.start_game_button = tk.Button(
            self.main_frame,
            text="Oyna",
            command=self.tas_kagit_makas_iremnur_akalin,
            font=("Arial", 14, "bold"),
            width=15,
            height=2,
            padx=10,
            pady=10
        )
        self.start_game_button.place(relx=0.5, rely=0.4, anchor="center")

        # Creates Rock, Paper, Scissors buttons and hides them at startup
        self.rock_button = tk.Button(
            self.main_frame,
            text="Taş",
            command=lambda: self.make_move("taş")
        )
        self.paper_button = tk.Button(
            self.main_frame,
            text="Kağıt",
            command=lambda: self.make_move("kağıt")
        )
        self.scissors_button = tk.Button(
            self.main_frame,
            text="Makas",
            command=lambda: self.make_move("makas")
        )

        # Creates a game info tag and is initially empty
        self.game_info_label = tk.Label(
            self.main_frame,
            text=(
                "Siz ve bilgisayar taş, kağıt veya makas seçeneklerinden birini seçersiniz.\n"
                "Taş makası yener, makas kağıdı yener, kağıt taşı yener.\n"
                "Her turda iki eli kazanan turu kazanır.\n"
                "Oyunu kazanmak için toplamda iki turu kazanmanız gerekir.\n"
                "Çarpı işaretine basarak oyundan çıkabilirsiniz."
            ),
            font=("Arial", 11, "bold")
        )
        self.game_info_label.place(relx=0.5, rely=0.7, anchor="center")

        # Label to show tour results
        self.tour_results_label = tk.Label(
            self.main_frame,
            text="",
            font=("Arial", 11, "bold")
        )
        self.tour_results_label.place(relx=0.5, rely=0.8, anchor="center")

        # Variables to track game state and number of rounds
        self.player_tour_scores = [0, 0, 0]  # Player scores in each round
        self.computer_tour_scores = [0, 0, 0]  # Computer scores in each round
        self.current_tour = 0
        self.rounds_left = 3
        self.tour_results = [""] * 3  # List to store the result of each round


    def make_move(self, player_move):
            """Processes the player's move and updates the game.

            Args:
                player_move (str): Player's chosen move (rock, paper or scissors).

            Returns:
                None
            """
            if player_move not in ["taş", "kağıt", "makas"]:
                messagebox.showerror("Geçersiz Seçim", "Lütfen geçerli bir seçim yapın!")
                return

            options = ["taş", "kağıt", "makas"]
            computer_move = random.choice(options)

            if player_move == computer_move:
                result = "Beraberlik!"
                result_color = "black"  # Black for a draw
            elif (player_move == "taş" and computer_move == "makas") or \
                (player_move == "makas" and computer_move == "kağıt") or \
                (player_move == "kağıt" and computer_move == "taş"):
                result = "Kazandınız!"
                result_color = "green"  # Green for winning
                self.player_tour_scores[self.current_tour] += 1
            else:
                result = "Bilgisayar kazandı!"
                result_color = "red"  # Red for losing
                self.computer_tour_scores[self.current_tour] += 1

            self.update_game_info(player_move, computer_move, result, result_color)

            if self.player_tour_scores[self.current_tour] >= 2 or \
            self.computer_tour_scores[self.current_tour] >= 2:
                self.end_tour()
            elif self.rounds_left <= 0:
                self.end_game()


    def update_game_info(self, player_move, computer_move, result, result_color):
        """Updates game information and shows the result in color.

        Args:
            player_move (str): Player's chosen move.
            computer_move (str): The move the computer chooses.
            result (str): The result of the game (You won, Computer won, etc.)).
            result_color (str): Color name indicating the result color.

        Returns:
            None
        """
        game_info_text = (
            f"Bilgisayarın seçimi: {computer_move}\n"
            f"Sizin seçiminiz: {player_move}\n"
            f"{result}"
        )
        
        self.game_info_label.config(
            text=game_info_text,
            fg=result_color  # Sets the result color
        )
        
        # position game_info_label
        self.game_info_label.place(relx=0.5, rely=0.65, anchor="center")


    def tas_kagit_makas_iremnur_akalin(self):
        """Launches the game and updates the interface.

        This method starts the game and presents the user with options. 
        It also resets the scores and updates the current tour.
        
        Args:
            None

        Returns:
            None
        """
        # Hides the start game button
        self.start_game_button.place_forget()

        # Shows Rock, Paper, Scissors buttons centered
        self.rock_button.place(relx=0.3, rely=0.5, anchor="center")
        self.paper_button.place(relx=0.5, rely=0.5, anchor="center")
        self.scissors_button.place(relx=0.7, rely=0.5, anchor="center")

        # Resets scores and starts the game
        self.player_tour_scores = [0, 0, 0]
        self.computer_tour_scores = [0, 0, 0]
        self.current_tour = 0
        self.tour_results = [""] * 3

        self.update_tour_results()


    def update_tour_results(self):
        """Updates lap results.

        This method updates the results of the 
        current lap and shows the result on the screen.

        Args:
            None

        Returns:
            None
        """
        # Updates the results of the current round
        self.tour_results_label.config(
            text=self.tour_results[self.current_tour]
        )
        self.tour_results_label.place(
            relx=0.5, 
            rely=0.8, 
            anchor="center"  # Label's location
        )


    def end_tour(self):
        """Processes the end of a round and shows the result.

        This method evaluates the result of the current round, updates the result and
        checks whether the game continues. Checks the round results and 
        shows the game information on the screen.

        Args:
            None

        Returns:
            None
        """
        if self.player_tour_scores[self.current_tour] >= 2:
            result = "Turu kazandınız!"
            result_color = "green"  # Green for winning
        else:
            result = "Bilgisayar turu kazandı!"
            result_color = "red"  # Red for losing

        # Updates the round result
        self.tour_results[self.current_tour] = f"{self.current_tour + 1}. Tur Kazananı: {result}"
        self.update_tour_results()

        # Setting the choice of PC and player as an example
        # These values are replaced by real choices
        player_move = "Taş"  # Sample casting
        computer_move = "Makas"  # Sample computer selection

        # Updates game information
        self.update_game_info(player_move, computer_move, result, result_color)

        self.current_tour += 1

        # Checks whether the game is over
        if self.current_tour >= 3 or \
        (self.player_tour_scores.count(2) >= 2 or self.computer_tour_scores.count(2) >= 2):
            self.end_game()
        else:
            # Informs about starting a new round
            self.game_info_label.config(
                text=f"{self.tour_results[self.current_tour - 1]}\nYeni tura geçildi.",
                fg="black"  # Black for other information
            )
            self.game_info_label.place(
                relx=0.5,
                rely=0.9,
                anchor="center"  # Location of the information label
            )


    def end_game(self):
        """At the end of the game, it shows the result and offers a new game option.

        This method evaluates the outcome of the game and shows the 
        results on the screen.
        It also gives the user the option to start a new game.

        Args:
            None

        Returns:
            None
        """
        if self.player_tour_scores.count(2) >= 2:
            result = "Tebrikler! Oyunu kazandınız!"
        else:
            result = "Bilgisayar oyunu kazandı."

        # Updates the game result
        self.game_info_label.config(
            text="\n".join(self.tour_results) + "\n\n" + result
        )
        
        # Offers the option to start a new game
        self.ask_to_play_again()


    def ask_to_play_again(self):
        """It asks the user and the computer if they want to play a new game.

        This method asks the user if they want to continue the game and
        also randomizes the computer's response. Resets the game according to the answers
        or closes the application.

        Args:
            None

        Returns:
            None
        """
        # Asks the user if he/she wants to continue
        continue_user = messagebox.askyesno("Oyun Bitti", "Oyuna devam etmek ister misiniz?")

        # Computer randomly determines if it wants to continue
        continue_computer = random.choice([True, False])

        if continue_user and continue_computer:
            self.reset_game()
        elif not continue_user:
            self.root.quit()
        elif not continue_computer:
            messagebox.showinfo("Bilgisayar Yanıtı", "Bilgisayar oyun oynamak istemiyor.")
            self.root.quit()


    def reset_game(self):
        """Resets and restarts the game.

        This method resets the entire game state and starts a new game.
        
        Args:
            None
        
        Returns:
            None
        """
        # Clears game information
        self.game_info_label.config(text="")
        
        # Resets scores and game status
        self.player_tour_scores = [0, 0, 0]
        self.computer_tour_scores = [0, 0, 0]
        self.current_tour = 0
        self.rounds_left = 3
        self.tour_results = [""] * 3
        
        # Starts new game
        self.tas_kagit_makas_iremnur_akalin()


if __name__ == "__main__":

    # Creates the main window
    root = tk.Tk()
    
    # Initializes the application object
    app = GameApp(root)
    
    # Starts the main loop
    root.mainloop()