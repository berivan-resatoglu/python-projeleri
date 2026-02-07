import random

print("🎮 SAYI AVCISI OYUNU 🎮")
print("Aklından 1 ile 100 arasında bir sayı tut 🤫")
print("İlk tahminim sürpriz olacak 🎲 ama sonra zekâm konuşur 😎\n")

print("Komutlar:")
print("⬆️  b : Sayım DAHA BÜYÜK")
print("⬇️  k : Sayım DAHA KÜÇÜK")
print("🎯 d : EVET BULDUN!")

alt = 1
ust = 100
deneme = 0
max_deneme = 7

# 🎲 İlk tahmin rastgele
tahmin = random.randint(alt, ust)

while True:
    if alt > ust:
        print("\n🚨 Hop! Bir yerde beni kandırdın 😅")
        print("Matematik buna itiraz ediyor.")
        break

    if deneme >= max_deneme:
        print("\n⏰ Deneme hakkım bitti!")
        print("Bu raundu sen kazandın 😄")
        break

    deneme += 1

    print(f"\n🤖 Deneme {deneme}")
    print(f"🧠 Tahminim 👉 {tahmin}")
    cevap = input("Ne diyorsun? (b/k/d): ").lower()

    if cevap == "d":
        print(f"\n🎉 YAKALADIM! {deneme} denemede buldum!")
        print("🏆 Yapay zekâ asla pes etmez 😎")
        break

    elif cevap == "b":
        print("⬆️ O zaman biraz yükseliyorum...")
        alt = tahmin + 1
        tahmin = (alt + ust) // 2

    elif cevap == "k":
        print("⬇️ Tamam, aşağı iniyorum...")
        ust = tahmin - 1
        tahmin = (alt + ust) // 2

    else:
        print("🙃 b, k ya da d yazman lazım ama deniyorum seni affetmeye 😅")