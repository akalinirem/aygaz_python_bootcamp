Taş Kağıt Makas Oyunu
Bu Python uygulaması, klasik "Taş Kağıt Makas" oyununu Tkinter kullanarak grafiksel bir kullanıcı arayüzü ile oynamanızı sağlar. Oyunda, siz ve bilgisayar sırayla seçimler yaparak birbirinize karşı yarışırsınız. Kazanan, toplamda iki turu kazanan taraf olacaktır.

Özellikler
Oyun Başlatma: "Oyna" butonuna tıklayarak oyunu başlatabilirsiniz.
Seçimler: Taş, Kağıt veya Makas seçimleri yapabilirsiniz.
Tur Sonuçları: Her turun sonucunu ve kazananı gösterir.
Oyun Sonu: Oyun bittikten sonra kazananı bildirir ve yeni bir oyun oynayıp oynamak istemediğinizi sorar.

Gereksinimler
Python 3.x
Tkinter (Python ile birlikte gelir)

Kod Açıklamaları \n
GameApp Sınıfı \n
__init__(self, root): Uygulamanın başlatıcı fonksiyonudur. Arayüz bileşenlerini oluşturur.
make_move(self, player_move): Oyuncunun hamlesini işler ve oyunu günceller.
update_game_info(self, player_move, computer_move, result, result_color): Oyun bilgilerini günceller ve sonucu renkli olarak gösterir.
tas_kagit_makas_iremnur_akalin(self): Oyunu başlatır ve kullanıcıya seçenekleri sunar.
update_tour_results(self): Tur sonuçlarını günceller.
end_tour(self): Bir turun sonunu işler ve sonucu gösterir.
end_game(self): Oyun sonucunu değerlendirir ve sonuçları ekranda gösterir.
ask_to_play_again(self): Kullanıcıya yeni bir oyun oynayıp oynamak istemediğini sorar.
reset_game(self): Oyunu sıfırlar ve tekrar başlatır.