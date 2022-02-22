
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
def menambahRentalMobil():
    while True:
        pilihanMenambah = int(input('''
        =======Menambah Data Rental Mobil=======
        1. Menambah Data Rental Mobil
        2. Kembali Ke Menu Utama
        Silahkan pilih sub menu Menambah data [1-2] : '''))

        if pilihanMenambah == 1:
            primKey = input("Masukan Nomor Indeks : ")
            NM = input("Masukan Nama Mobil : ")
            TK = input("Masukan Tipe Kendaraan : ")
            SPH = input("Masukan Harga Sewa per Hari : ")
            JM = int(input("Masukan Jumlah Mobil : "))
            dictMobil[primKey] = {"Nama Mobil": NM, "Tipe Kendaraan": TK, "Sewa per Hari": SPH, "Jumlah Mobil": JM}
            print("Proses input Data Berhasil ! ")
            menampilkanReport()
            continue
        elif pilihanMenambah == 2:
            break
        else:
            print("Pilihan Menu yang anda Masukan Salah !")
# Define function mengubah Data Rental Mobil
def mengubahRentalMobil():
    while True:
        #menampilkanReport()
        pilihanMengubah = int(input('''
        =======Mengubah Data Rental Mobil=======
        1. Index Data
        2. Nama Mobil
        3. Tipe Mobil
        4. Sewa per Hari
        5. Jumlah Mobil
        6. Kembali ke menu utama
        Silahkan pilih data yang akan diubah [1-6] : '''))

        if pilihanMengubah == 1:
            while True:
                PrimKey = input("Masukan Indeks Data yang ingin anda Ubah : ")
                if PrimKey not in dictMobil.keys():
                    print("Index yang anda Masukan tidak ada")
                elif PrimKey in dictMobil.keys():
                    while True:
                        newPrimKey = input("Masukan Indeks Data Yang Baru : ")
                        if len(newPrimKey) == 0:
                            print("data yang anda Masukan tidak Boleh Kosong ! ")
                        elif newPrimKey in dictMobil.keys():
                            print("Indeks baru yang anda masukan tidak boleh sama !")
                        else:
                            dictMobil[newPrimKey] = dictMobil[PrimKey]
                            del dictMobil[PrimKey]
                            print("\nProses Mengubah Data Berhasil ! \n")
                            break
                    break
                        

        elif pilihanMengubah == 2:
            while True:
                PrimKey = input("Masukan Indeks Data yang ingin anda Ubah : ")
                if PrimKey not in dictMobil.keys():
                    print("Index yang anda Masukan tidak ada")
                elif PrimKey in dictMobil.keys():
                    while True:
                        newNM = input("Masukan Nama Mobil yang Baru : ")
                        if len(newNM) == 0:
                            print("data yang anda Masukan tidak Boleh Kosong ! ")
                        elif newNM == dictMobil[PrimKey]["Nama Mobil"]:
                            print("Nama Mobil baru yang anda masukan tidak boleh sama !")
                        else:
                            dictMobil["Nama Mobil"] = newNM      
                            print("\nProses Mengubah Data Berhasil ! \n")
                            break
                break
        elif pilihanMengubah == 3:
            while True:
                PrimKey = input("Masukan Indeks Data yang ingin anda Ubah : ")
                if PrimKey not in dictMobil.keys():
                    print("Index yang anda Masukan tidak ada")
                elif PrimKey in dictMobil.keys():
                    while True:
                        newTK = input("Masukan Tipe Mobil yang Baru : ")
                        if len(newTK) == 0:
                            print("data yang anda Masukan tidak Boleh Kosong ! ")
                        elif newTK == dictMobil[PrimKey]["Tipe Kendaraan"]:
                            print("Tipe Mobil baru yang anda masukan tidak boleh sama !")
                        else:
                            dictMobil["Tipe Kendaraan"] = newTK    
                            print("\nProses Mengubah Data Berhasil ! \n")
                            break
                break
        elif pilihanMengubah == 4:
            while True:
                PrimKey = input("Masukan Indeks Data yang ingin anda Ubah : ")
                if PrimKey not in dictMobil.keys():
                    print("Index yang anda Masukan tidak ada")
                elif PrimKey in dictMobil.keys():
                    while True:
                        newSWP = input("Masukan Sewa per Hari yang Baru : ")
                        if len(newSWP) == 0:
                            print("data yang anda Masukan tidak Boleh Kosong ! ")
                        elif int(newSWP) == dictMobil[PrimKey]["Sewa per Hari"]:
                            print("Sewa per Hari baru yang anda masukan tidak boleh sama !")
                        else:
                            dictMobil["Sewa per Hari"] = int(newSWP)    
                            print("\nProses Mengubah Data Berhasil ! \n")
                            break
                break
        elif pilihanMengubah == 5:
            while True:
                PrimKey = input("Masukan Indeks Data yang ingin anda Ubah : ")
                if PrimKey not in dictMobil.keys():
                    print("Index yang anda Masukan tidak ada")
                elif PrimKey in dictMobil.keys():
                    while True:
                        newJM = input("Masukan Jumlah Mobil yang Baru : ")
                        if len(newJM) == 0:
                            print("data yang anda Masukan tidak Boleh Kosong ! ")
                        elif int(newJM) == dictMobil[PrimKey]["Jumlah Mobil"]:
                            print("Jumlah Mobil baru yang anda masukan tidak boleh sama !")
                        else:
                            dictMobil["Jumlah Mobil"] = int(newJM)   
                            print("\nProses Mengubah Data Berhasil ! \n")
                            break
                break
        elif pilihanMengubah == 6:
            break
        else:
            print("Pilihan Menu yang anda Masukan Salah !")

# Define function Menghapus Data Rental Mobil
def deleteRentalMobil():
    #menampilkanReport()
    while True:
    
        pilihanDelete=int(input('''
        =======Menghapus Data Rental Mobil=======
        1. Hapus Data Rental Mobil
        2. Kembali Ke Menu Utama
        Silahkan pilih sub menu hapus data [1-2] : '''))

        if pilihanDelete == 1:
            inputPilihanDelete = input("Masukan Primary Key Data yang ingin dihapus : ")
            if inputPilihanDelete in dictMobil.keys():
                del dictMobil[inputPilihanDelete]
                print("Menghapus Data Berhasil !")
                menampilkanReport()
            elif inputPilihanDelete not in dictMobil.keys():
                print("Primary yang anda Masukan tidak ada di Data Rental mobil")
            
        elif pilihanDelete == 2:
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
        menambahRentalMobil()
    elif(pilihanMenu == 3):
        mengubahRentalMobil()
    elif(pilihanMenu == 4):
        deleteRentalMobil()
    elif(pilihanMenu == 5):
        break
    else:
        print("pilihan menu yang anda masukan salah!")
