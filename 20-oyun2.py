print("Aklından 1 ile 100 arasında bir sayı tut.")
print("Cevap olarak:")
print("b -> Sayım daha BÜYÜK")
print("k -> Sayım daha KÜÇÜK")
print("d -> DOĞRU")

alt = 1
ust = 100
deneme = 0
max_deneme = 7

while True:
    if alt > ust:
        print("Cevaplar tutarsız. Oyun bitirildi.")
        break

    if deneme >= max_deneme:
        print("Deneme sınırına ulaşıldı.")
        break

    tahmin = (alt + ust) // 2
    deneme += 1

    print(f"Tahminim: {tahmin}")
    cevap = input("Cevabın (b/k/d): ").lower()

    if cevap == "d":
        print(f"Bildim! {deneme} denemede buldum.")
        break
    elif cevap == "b":
        alt = tahmin + 1
    elif cevap == "k":
        ust = tahmin - 1
    else:
        print("Geçersiz giriş. Lütfen b, k veya d gir.")
        