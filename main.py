def matnni_teskari_qil(matn):
    """Matnni orqasidan boshlab yig'uvchi funksiya"""
    indeks = len(matn) - 1
    teskari_matn = ""

    while indeks >= 0:
        teskari_matn += matn[indeks]
        indeks -= 1

    print(f"Asl matn: {matn}")
    print(f"Teskari matn: {teskari_matn}")

matnni_teskari_qil("dasturlash")


def xavfsiz_parol_yarat():
    """Belgilar soni 8 tadan kam bo'lmagan parol so'rovchi funksiya"""
    while True:
        parol = input("Yangi parol kiriting (kamida 8 ta belgi): ")

        if len(parol) >= 8:
            print("Parol muvaffaqiyatli qabul qilindi! ✅")
            break
        else:
            print(f"Xato! Siz kiritgan parol {len(parol)} ta belgidan iborat. Juda qisqa!")

xavfsiz_parol_yarat()


def fibonachchi_seriyasi(maksimal_limit):
    """Maksimal limitgacha bo'lgan Fibonachchi sonlarini chiqaruvchi funksiya"""
    a, b = 0, 1
    print(f"{maksimal_limit} gacha bo'lgan Fibonachchi sonlari:")

    while a <= maksimal_limit:
        print(a, end=" ")
        a, b = b, a + b
    print()

fibonachchi_seriyasi(100)


def dublikatlarni_ochir(royxat):
    """Ro'yxatdagi takrorlangan elementlarni tozalovchi funksiya"""
    toza_royxat = []
    indeks = 0

    while indeks < len(royxat):
        element = royxat[indeks]
        if element not in toza_royxat:
            toza_royxat.append(element)
        indeks += 1

    print(f"Eski ro'yxat: {royxat}")
    print(f"Tozalangan ro'yxat: {toza_royxat}")

sonlar = [1, 2, 2, 3, 4, 4, 4, 5, 1]
dublikatlarni_ochir(sonlar)

def faqat_son_kirit():
    """Foydalanuvchi faqat butun son kiritishini ta'minlovchi funksiya"""
    while True:
        try:
            yosh = int(input("Yoshingizni kiriting: "))
            print(f"Rahmat! Tizim yoshingizni {yosh} deb qabul qildi.")
            break
        except ValueError:
            print("Xato! Iltimos, harf emas, faqat raqam kiriting.\n")

faqat_son_kirit()

def harf_filtri(soz):
    """So'z ichidagi 'a' harflarini o'chirib tashlovchi funksiya"""
    indeks = 0
    yangi_soz = ""

    while indeks < len(soz):
        harf = soz[indeks]
        indeks += 1

        if harf.lower() == 'a':
            continue

        yangi_soz += harf

    print(f"Asl so'z: {soz} -> Filtrdan keyin: {yangi_soz}")

harf_filtri("Alisher")
harf_filtri("Dasturlash")
import random

def oyin_tosh_qaychi():
    """Kompyuterga qarshi 1 ochkogacha o'yin"""
    ochko = 0
    variantlar = ["tosh", "qaychi", "qogoz"]

    print("--- TOSh-QAYChI-QOG‘OZ O‘YINI ---")
    print("Ketma-ket 1 ochko to'plashingiz kerak!")

    while ochko < 1:
        kompyuter = random.choice(variantlar)
        taktika = input("Tosh, Qaychi yoki Qogoz? (Tanlang): ").lower()

        if taktika not in variantlar:
            print("Bunday variant yo'q, qayta kiriting!")
            continue

        print(f"Kompyuter tanlovi: {kompyuter}")

        if taktika == kompyuter:
            print("Durang!")
        elif (taktika == "tosh" and kompyuter == "qaychi") or \
                (taktika == "qaychi" and kompyuter == "qogoz") or \
                (taktika == "qogoz" and kompyuter == "tosh"):
            ochko += 1
            print(f"Siz yutdingiz! 🎉 Hozirgi ochkongiz: {ochko}/1")
        else:
            ochko = 0
            print("Kompyuter yutdi! Ochkolaringiz nolga tushdi. 😔")

    print("Tabriklaymiz! Siz ketma-ket 1 marta yutib, o'yinda g'olib bo'ldingiz! 🏆")

oyin_tosh_qaychi()