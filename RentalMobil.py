


cart = []




while True:
    pilihanMenu = int(input('''
    Selamat datang dirental Mobil

    List Menu:
    1. Menampilkan Daftar Mobil
    2. Menambah Mobil
    3. Menghapus
    4. Membeli
    5. Exit Program

    Masukan angka Menu yang ingin dijalankan : '''))

    if(pilihanMenu == 1):
        print("1")
    elif(pilihanMenu == 2):
        print("2")
    elif(pilihanMenu == 3):
        print("3")
    elif(pilihanMenu == 4):
        print("4")
    elif(pilihanMenu == 5):
        break
    else:
        print("pilihan menu yang anda masukan salah!")
