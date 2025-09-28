def app_penjumlahan():
    print("=== PROGRAM PENJUMLAHAN ===")
    try:
        angka1 = int(input("angka1: "))
        angka2 = int(input("angka2: "))
        hasil = angka1 + angka2
        print("hasil penjumlahan", hasil)
        print("=== Program penjumlahan selesai ===")
        input("Enter untuk lanjut")
    except ValueError:
        print("Input harus berupa angka!")
    print("=== Program perkalian selesai ===")
    input("Enter untuk lanjut")

def app_pengurangan():
    print("=== PROGRAM PENGURANGAN ===")
    try:
        angka1 = int(input("angka1: "))
        angka2 = int(input("angka2: "))
        hasil = angka1 - angka2
        print("hasil pengurangan", hasil)
    except ValueError:
        print("Input harus berupa angka!")
    print("=== Program pengurangan selesai ===")
    input("Enter untuk lanjut")

def app_perkalian():
    print("=== PROGRAM PERKALIAN ===")
    try:
        angka1 = int(input("angka1: "))
        angka2 = int(input("angka2: "))
        hasil = angka1 * angka2
        print("hasil perkalian", hasil)
    except ValueError:
        print("Input harus berupa angka!")
    print("=== Program perkalian selesai ===")
    input("Enter untuk lanjut")

def app_pembagian():
    print("=== PROGRAM PEMBAGIAN ===")
    try:
        angka1 = int(input("angka1: "))
        angka2 = int(input("angka2: "))
        hasil = angka1 / angka2
        print("hasil pembagian", hasil)
    except ValueError:
        print("Input harus berupa angka!")
    print("=== Program pembagian selesai ===")
    input("Enter untuk lanjut")

def menu():
    while True:
        print("=== PROGRAM KALKULATOR SEDERHANA ===")
        print("1. Penjumlahan")
        print("2. pengurangan")
        print("3. perkalian")
        print("4. pembagian")
        print("5. keluar")
        print("=== PROGRAM KALKULATOR SERDEHANA")
    
        pilihan = int(input("Pilihan: "))

        if pilihan == 1:
            app_penjumlahan()
        elif pilihan == 2:
            app_pengurangan()
        elif pilihan == 3:
            app_perkalian()
        elif pilihan == 4:
            app_pembagian()
        elif pilihan == 5:
            print("==+ SAMPAI JUMPA LAGI ===")
            break
menu()