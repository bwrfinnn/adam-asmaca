import random
from colorama import Fore, Style


#Adam asmaca çizimi
def adam_asmaca_ciz(yanlis_hak):
     asma = [
         """
         -----
         |   |
             |
             |
             |
             |
        """, """
         -----
         |   |
         O   |
             |
             |
             |
        """, """
         -----
         |   |
         O   |
         |   |
             |
             |
        """, """
         -----
         |   |
         O   |
        /|   |
             |
             |
        """, """
         -----
         |   |
         O   |
        /|\\  |
             |
             |
        """, """
         -----
         |   |
         O   |
        /|\\  |
        /    |
             |
        """, """
         -----
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        """
     ]
     print(asma[6 - yanlis_hak])


#Kategori ve kelimeler
Kelimeler = {
    "Hayvan": ["kedi", "köpek", "aslan", "kaplan", "zürafa", "kuş", "balık", "kanguru", "kaplumbağa", "rakun"],
    "Eşya": ["bilgisayar", "telefon", "defter", "kalem", "tarak", "silgi", "kalemlik", "çanta", "ruj"],
    "Şehir": ["istanbul", "ankara", "izmir", "antalya", "bursa", "balıkesir", "konya", "adana", "mersin", "eskişehir", "kocaeli"],
    "Yiyecekler": ["hamburger", "makarna", "pizza", "pilav", "kek", "çorba", "mantı", "köfte", "lahmacun", "çiğ köfte"],
    "Meyveler": ["elma", "armut", "kiraz", "kavun", "kivi", "muz", "çilek", "portakal", "karpuz", "nar", "üzüm", "kayısı"],
    "Renkler": ["mor", "pembe", "mavi", "yeşil", "turuncu", "kırmızı", "siyah", "beyaz", "sarı", "lacivert", "kahverengi", "gri"], 
}

#Seviye seçimi
print("Zorluk seviyeleri: Kolay(6 hak),Orta(4 hak),Zor(2 hak)")
seviye = input("Zorluk seviyesini seçin (kolay/orta/zor):").lower()
if seviye == "kolay":
     yanlis_tahmin_hakki = 6
elif seviye == "orta":
     yanlis_tahmin_hakki = 4
elif seviye == "zor":
     yanlis_tahmin_hakki = 2

#Rastgele kategori ve kelime seçimi
kategori = random.choice(list(Kelimeler.keys()))
gizli_kelime = random.choice(Kelimeler[kategori])
gizli_kelime_tahmin = ["_"] * len(gizli_kelime)
tahmin_edilen_harfler = []
puan = 0

print(Fore.GREEN + f"Kategori: {kategori}" + Style.RESET_ALL)
print("Adam Asmaca oyununa hoş geldiniz!")
print(" ".join(gizli_kelime_tahmin))

while yanlis_tahmin_hakki > 0 and "_" in gizli_kelime_tahmin:
     tahmin = input("Bir harf ya da kelime tahmin edin: ").lower()

     # Tüm kelime tahmini
     if len(tahmin) > 1:
          if tahmin == gizli_kelime:
               print(Fore.GREEN + "Tebrikler! Kelimeyi doğru tahmin ettiniz." +
                     Style.RESET_ALL)
               puan += 50
               gizli_kelime_tahmin = list(gizli_kelime)
               break
          else:
               print(Fore.RED +
                     "Yanlış tahmin! Tüm kelimeyi yanlış tahmin ettiniz." +
                     Style.RESET_ALL)
               yanlis_tahmin_hakki -= 1
               adam_asmaca_ciz(yanlis_tahmin_hakki)
               continue

     # Daha önce tahmin edilmiş mi kontrolü
     if tahmin in tahmin_edilen_harfler:
          print(Fore.YELLOW +
                "Bu harfi zaten tahmin ettiniz. Başka bir harf deneyin." +
                Style.RESET_ALL)
          continue

     tahmin_edilen_harfler.append(tahmin)

     # Doğru tahmin
     if tahmin in gizli_kelime:
          print(Fore.GREEN + f"Doğru! '{tahmin}' kelimede var." +
                Style.RESET_ALL)
          puan += 10
          for i in range(len(gizli_kelime)):
               if gizli_kelime[i] == tahmin:
                    gizli_kelime_tahmin[i] = tahmin
     else:
          # Yanlış tahmin
          yanlis_tahmin_hakki -= 1
          print(
              Fore.RED +
              f"Yanlış! '{tahmin}' kelimede yok. Kalan hakkınız: {yanlis_tahmin_hakki}"
              + Style.RESET_ALL)
          adam_asmaca_ciz(yanlis_tahmin_hakki)

     print(" ".join(gizli_kelime_tahmin))
     print(Fore.CYAN + f"Toplam Puan: {puan}" + Style.RESET_ALL)

if "_" not in gizli_kelime_tahmin:
     print(Fore.GREEN + "Tebrikler! Kelimeyi tamamen doğru tahmin ettiniz!" +
           Style.RESET_ALL)
else:
     print(Fore.RED +
           f"Hakkınız bitti. Kaybettiniz! Kelime şuydu: {gizli_kelime}" +
           Style.RESET_ALL)

print(Fore.MAGENTA + f"Oyun bitti! Toplam puanınız: {puan}" + Style.RESET_ALL)
