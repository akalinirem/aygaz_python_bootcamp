import tkinter as tk
from tkinter import messagebox
import random

class GameApp:
    def __init__(self, root):
        """Başlatıcı: Oyun uygulamasını başlatır ve arayüzü oluşturur."""
        self.root = root
        self.root.title("Taş Kağıt Makas Oyunu")
        self.root.geometry("700x500")

        # Ana çerçeve oluşturur
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Başlık etiketi oluşturur ve ortalar
        self.label = tk.Label(
            self.main_frame,
            text="Taş Kağıt Makas Oyunu",
            font=("Arial", 14, "bold")
        )
        self.label.place(relx=0.5, rely=0.2, anchor="center")

        # Oyuna başlama butonu oluşturur ve ortalar
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

        # Taş, Kağıt, Makas butonları oluşturur ve başlangıçta gizler
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

        # Oyun bilgisi etiketi oluşturur ve başlangıçta boş kalır
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

        # Tur sonuçlarını gösterecek etiket
        self.tour_results_label = tk.Label(
            self.main_frame,
            text="",
            font=("Arial", 11, "bold")
        )
        self.tour_results_label.place(relx=0.5, rely=0.8, anchor="center")

        # Oyun durumunu ve tur sayısını takip etmek için değişkenler
        self.player_tour_scores = [0, 0, 0]  # Her turdaki oyuncu skorları
        self.computer_tour_scores = [0, 0, 0]  # Her turdaki bilgisayar skorları
        self.current_tour = 0
        self.rounds_left = 3
        self.tour_results = [""] * 3  # Her turun sonucunu saklamak için liste


    def make_move(self, player_move):
            """Oyuncunun hamlesini işleme koyar ve oyunu günceller.

            Args:
                player_move (str): Oyuncunun seçtiği hamle (taş, kağıt veya makas).

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
                result_color = "black"  # Beraberlik için siyah
            elif (player_move == "taş" and computer_move == "makas") or \
                (player_move == "makas" and computer_move == "kağıt") or \
                (player_move == "kağıt" and computer_move == "taş"):
                result = "Kazandınız!"
                result_color = "green"  # Kazanma için yeşil
                self.player_tour_scores[self.current_tour] += 1
            else:
                result = "Bilgisayar kazandı!"
                result_color = "red"  # Kaybetme için kırmızı
                self.computer_tour_scores[self.current_tour] += 1

            self.update_game_info(player_move, computer_move, result, result_color)

            if self.player_tour_scores[self.current_tour] >= 2 or \
            self.computer_tour_scores[self.current_tour] >= 2:
                self.end_tour()
            elif self.rounds_left <= 0:
                self.end_game()


    def update_game_info(self, player_move, computer_move, result, result_color):
        """Oyun bilgisini günceller ve sonucu renkli olarak gösterir.

        Args:
            player_move (str): Oyuncunun seçtiği hamle.
            computer_move (str): Bilgisayarın seçtiği hamle.
            result (str): Oyunun sonucu (Kazandınız, Bilgisayar kazandı, vb.).
            result_color (str): Sonuç rengini belirten renk adı.

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
            fg=result_color  # Sonuç rengini ayarlıyor
        )
        
        # game_info_label'ı konumlandır
        # Butonları yerleştirdikten sonra burayı ayarlayabilirsiniz
        self.game_info_label.place(relx=0.5, rely=0.65, anchor="center")


    def tas_kagit_makas_iremnur_akalin(self):
        """Oyunu başlatır ve arayüzü günceller.

        Bu yöntem, oyunu başlatır ve kullanıcıya seçenekleri sunar. Ayrıca, skorları sıfırlar
        ve mevcut turu günceller.
        
        Args:
            None

        Returns:
            None
        """
        # Oyuna başlama butonunu gizler
        self.start_game_button.place_forget()

        # Taş, Kağıt, Makas butonlarını ortalanmış şekilde gösterir
        self.rock_button.place(relx=0.3, rely=0.5, anchor="center")
        self.paper_button.place(relx=0.5, rely=0.5, anchor="center")
        self.scissors_button.place(relx=0.7, rely=0.5, anchor="center")

        # Skorları sıfırlar ve oyunu başlatır
        self.player_tour_scores = [0, 0, 0]
        self.computer_tour_scores = [0, 0, 0]
        self.current_tour = 0
        self.tour_results = [""] * 3

        self.update_tour_results()


    def update_tour_results(self):
        """Tur sonuçlarını günceller.

        Bu yöntem, mevcut turun sonuçlarını günceller ve sonucu ekranda gösterir.

        Args:
            None

        Returns:
            None
        """
        # Mevcut turun sonuçlarını günceller
        self.tour_results_label.config(
            text=self.tour_results[self.current_tour]
        )
        self.tour_results_label.place(
            relx=0.5, 
            rely=0.8, 
            anchor="center"  # Label'ın konumu
        )


    def end_tour(self):
        """Bir turun sonunu işleme alır ve sonucu gösterir.

        Bu yöntem, mevcut turun sonucunu değerlendirir, sonucu günceller ve
        oyunun devam edip etmediğini kontrol eder. Tur sonuçlarını ve 
        oyun bilgisini ekranda gösterir.

        Args:
            None

        Returns:
            None
        """
        if self.player_tour_scores[self.current_tour] >= 2:
            result = "Turu kazandınız!"
            result_color = "green"  # Kazanma için yeşil
        else:
            result = "Bilgisayar turu kazandı!"
            result_color = "red"  # Kaybetme için kırmızı

        # Tur sonucunu günceller
        self.tour_results[self.current_tour] = f"{self.current_tour + 1}. Tur Kazananı: {result}"
        self.update_tour_results()

        # Bilgisayarın ve oyuncunun seçimini örnek olarak ayarlanıyor
        # Bu değerler gerçek seçimlerle değiştiriliyor
        player_move = "Taş"  # Örnek oyuncu seçimi
        computer_move = "Makas"  # Örnek bilgisayar seçimi

        # Oyun bilgisini günceller
        self.update_game_info(player_move, computer_move, result, result_color)

        self.current_tour += 1

        # Oyunun bitip bitmediğini kontrol eder
        if self.current_tour >= 3 or \
        (self.player_tour_scores.count(2) >= 2 or self.computer_tour_scores.count(2) >= 2):
            self.end_game()
        else:
            # Yeni tur başlatılmasıyla ilgili bilgi verir
            self.game_info_label.config(
                text=f"{self.tour_results[self.current_tour - 1]}\nYeni tura geçildi.",
                fg="black"  # Diğer bilgiler için siyah
            )
            self.game_info_label.place(
                relx=0.5,
                rely=0.9,
                anchor="center"  # Bilgi label'ının konumu
            )


    def end_game(self):
        """Oyun sonunda sonucu gösterir ve yeni oyun seçeneği sunar.

        Bu yöntem, oyunun sonucunu değerlendirir ve sonuçları ekranda gösterir.
        Ayrıca, kullanıcıya yeni bir oyun başlatma seçeneği sunar.

        Args:
            None

        Returns:
            None
        """
        if self.player_tour_scores.count(2) >= 2:
            result = "Tebrikler! Oyunu kazandınız!"
        else:
            result = "Bilgisayar oyunu kazandı."

        # Oyun sonucunu günceller
        self.game_info_label.config(
            text="\n".join(self.tour_results) + "\n\n" + result
        )
        
        # Yeni oyun başlatma seçeneğini sunar
        self.ask_to_play_again()


    def ask_to_play_again(self):
        """Kullanıcıya ve bilgisayara yeni bir oyun oynayıp oynamak istemediğini sorar.

        Bu yöntem, kullanıcıya oyuna devam etmek isteyip istemediğini sorar ve
        bilgisayarın da yanıtını rastgele belirler. Yanıtlara göre oyunu sıfırlar
        veya uygulamayı kapatır.

        Args:
            None

        Returns:
            None
        """
        # Kullanıcıya devam etmek isteyip istemediğini sorar
        continue_user = messagebox.askyesno("Oyun Bitti", "Oyuna devam etmek ister misiniz?")

        # Bilgisayar devam etmek isteyip istemediğini rastgele belirler
        continue_computer = random.choice([True, False])

        if continue_user and continue_computer:
            self.reset_game()
        elif not continue_user:
            self.root.quit()
        elif not continue_computer:
            messagebox.showinfo("Bilgisayar Yanıtı", "Bilgisayar oyun oynamak istemiyor.")
            self.root.quit()


    def reset_game(self):
        """Oyunu sıfırlar ve tekrar başlatır.

        Bu yöntem, oyunun tüm durumunu sıfırlar ve yeni bir oyun başlatır.
        
        Args:
            None
        
        Returns:
            None
        """
        # Oyun bilgilerini temizler
        self.game_info_label.config(text="")
        
        # Skorları ve oyun durumunu sıfırlar
        self.player_tour_scores = [0, 0, 0]
        self.computer_tour_scores = [0, 0, 0]
        self.current_tour = 0
        self.rounds_left = 3
        self.tour_results = [""] * 3
        
        # Yeni oyunu başlatır
        self.tas_kagit_makas_iremnur_akalin()


if __name__ == "__main__":

    # Ana pencereyi oluşturur
    root = tk.Tk()
    
    # Uygulama nesnesini başlatır
    app = GameApp(root)
    
    # Ana döngüyü başlatır
    root.mainloop()

