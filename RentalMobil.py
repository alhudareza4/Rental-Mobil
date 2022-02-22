
# Define Data
'''
primary key

nama mobil
tipe mobil
harga perhari
jumlah hari
'''
dictMobil= {"10A":{"Nama Mobil":"Avanza",
                    "Tipe Kendaraan":"MPV",
                    "Sewa per Hari": 300000,
                    "Jumlah Mobil":30},
            "11A":{"Nama Mobil":"Fortuner",
                    "Tipe Kendaraan":"SUV",
                    "Sewa per Hari": 500000,
                    "Jumlah Mobil":30}
            }

cart = []

# Define function menampilkan daftar 
'''
1. menampilkan seluruh data
2. menampilkan data tertentu
3. kembali ke menu utama
'''
def reportRentalMobil():
    
    while (True):
        pilihanReport= int(input('''
        ===== Report Rental Mobil =====

        1. Report Seluruh Data Kendaraan
        2. Report Data Tertentu
        3. Kembali ke Menu Utama
        
        Silahkan Pilih Menu yang ingin Ditampilkan [1-3] :
        '''))
        if (pilihanReport == 1):
            menampilkanReport()

        elif(pilihanReport == 2):
            while (True):
                inputPrimKey = input("Masukan Primary Key Data Yang ingin anda Tampilkan : ")
                if (inputPrimKey not in dictMobil.keys()):
                    print("Primary Key Yang anda Masukan Salah")
                    while True:
                        val1 = input("Apakah anda ingin Kembali ? [Y/N] : ")
                        if val1 == "Y":
                            break
                        elif val1 == "N":
                            continue
                        else:
                            print("Pilihan Menu yang anda Masukan Salah !")
                    break
                elif (inputPrimKey in dictMobil.keys()):
                    print(dictMobil[inputPrimKey])
                    break
        elif(pilihanReport ==3):
            break
        else:
            print("Pilihan Menu yang anda Masukan Salah !")

def menampilkanReport():
    if len(dictMobil) == 0:
        print("Data Rental Mobil Kosong")
    elif len(dictMobil) > 0:
        print("Daftar Rental Mobil")
        for key, val3 in dictMobil.items():
            print("Index : {}, Nama Mobil : {}, Tipe Kendaraan : {}, Sewa per Hari : {}, Jumlah Mobil : {}".format(key, dictMobil[key]["Nama Mobil"], dictMobil[key]["Tipe Kendaraan"], dictMobil[key]["Sewa per Hari"], dictMobil[key]["Jumlah Mobil"] ))


# Define function menambah data mobil rental

# Define function mengubah Data Rental Mobil

# Define function Menghapus Data Rental Mobil
def deleteRentalMobil():
    
    menampilkanReport()

    while (True):
        inputPilihanDelete = input("Masukan Primary Key Data yang ingin dihapus : ")
        if inputPilihanDelete in dictMobil.keys():
            del dictMobil[inputPilihanDelete]
            menampilkanReport()


        elif inputPilihanDelete not in dictMobil.keys():
            print("Primary yang anda Masukan tidak ada di Data Rental mobil")
            break
        
        option2 = input("Apakah anda ingin menghapus Data lainnya ? [Y/N] : ")
        if option2 == "Y":
            continue
        elif option2 == "N":
            break
        else:
            print("Pilihan Menu yang anda Masukan Salah !")



while True:
    pilihanMenu = int(input('''
    ======== Selamat datang dirental Mobil ========

    List Menu:
    1. Report Data Rental Mobil
    2. Menambah Data Mobil Rental
    3. Mengubah Data Rental Mobil 
    4. Menghapus Data Rental Mobil
    5. Exit Program

    Masukan angka Menu yang ingin dijalankan : '''))

    if(pilihanMenu == 1):
        reportRentalMobil()
    elif(pilihanMenu == 2):
        print("2")
    elif(pilihanMenu == 3):
        print("3")
    elif(pilihanMenu == 4):
        deleteRentalMobil()
    elif(pilihanMenu == 5):
        break
    else:
        print("pilihan menu yang anda masukan salah!")
