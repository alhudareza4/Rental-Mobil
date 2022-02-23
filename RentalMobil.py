
# Define Data


dictMobil= {"10A":{"Nama Mobil":"Avanza",
                    "Tipe Kendaraan":"MPV",
                    "Biaya": 300000,
                    "Penyewa":"Udin"},
            "11A":{"Nama Mobil":"Fortuner",
                    "Tipe Kendaraan":"SUV",
                    "Biaya": 500000,
                    "Penyewa":"Asep"}
            }



# Define function menampilkan daftar 

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
                if len(inputPrimKey) == 0:
                    print("Primary key yang dimasukan tidak boleh kosong !")
                    break
                elif (inputPrimKey not in dictMobil.keys()):
                    print("Primary Key Yang anda Masukan Salah")
                    break
                elif (inputPrimKey in dictMobil.keys()):
                    print(dictMobil[inputPrimKey])
                    break
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
            print("Index : {}, Nama Mobil : {}, Tipe Kendaraan : {}, Biaya : {}, Penyewa : {}".format(key, 
                                                                                                            dictMobil[key]["Nama Mobil"], 
                                                                                                            dictMobil[key]["Tipe Kendaraan"], 
                                                                                                            dictMobil[key]["Biaya"], 
                                                                                                            dictMobil[key]["Penyewa"] ))


# Define function menambah data mobil rental
def menambahRentalMobil():
    while True:
        pilihanMenambah = int(input('''
        =======Menambah Data Rental Mobil=======
        1. Menambah Data Rental Mobil
        2. Kembali Ke Menu Utama
        Silahkan pilih sub menu Menambah data [1-2] : '''))

        if pilihanMenambah == 1:
            while True:
                primKey = input("Masukan Nomor Indeks : ")
                if primKey in dictMobil.keys():
                    print("Primary key yang anda masukan tidak boleh sama dengan yang sudah ada !")
                    continue
                elif len(primKey) == 0:
                    print("Primary Key tidak Boleh Kosong !")
                    continue
                else:
                    print("Input Primary key Berhasil !")
                    break

            while True:
                NM = input("Masukan Nama Mobil : ")
                if len(NM) == 0:
                    print("Nama Mobil Tidak boleh Kosong !")
                    continue
                else:
                    print("Input Nama Mobil berhasil !")
                    break
            
            while True:
                TK = input("Masukan Tipe Kendaraan : ")
                if len(TK) == 0:
                    print("Tipe Kendaraan Tidak boleh Kosong !")
                    continue
                else:
                    print("Input Tipe Kendaraan berhasil !")
                    break            
            
            while True:
                try:
                    B = int(input("Masukan Biaya yang dikeluarkan : "))
                except:
                    print("Input yang dimasukan haruslah bilangan !")
                    continue
                print("Input Biaya Sewa Kendaraan berhasil !")
                break                 
            
            while True:
                P = input("Masukan Penyewa Mobil : ")
                if len(P) == 0:
                    print("Penyewa Tidak boleh Kosong !")
                    continue
                else:
                    print("Input Penyewa Mobil berhasil !")
                    break          
            
            dictMobil[primKey] = {"Nama Mobil": NM, "Tipe Kendaraan": TK, "Biaya": B, "Penyewa": P}
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
        
        pilihanMengubah = int(input('''
        =======Mengubah Data Rental Mobil=======
        1. Index Data
        2. Nama Mobil
        3. Tipe Mobil
        4. Biaya
        5. Penyewa
        6. Kembali ke menu utama
        Silahkan pilih data yang akan diubah [1-6] : '''))

        if pilihanMengubah == 1:
            while True:
                PrimKey = input("Masukan Indeks Data yang ingin anda Ubah : ")
                if len(PrimKey) == 0:
                    print("Index yang dimasukan tidak boleh kosong !")
                    break
                elif PrimKey not in dictMobil.keys():
                    print("Index yang anda Masukan tidak ada")
                    break
                elif PrimKey in dictMobil.keys():
                    while True:
                        newPrimKey = input("Masukan Indeks Data Yang Baru : ")
                        if len(newPrimKey) == 0:
                            print("data yang anda Masukan tidak Boleh Kosong ! ")
                        elif newPrimKey in dictMobil.keys():
                            print("Indeks baru yang anda masukan tidak boleh sama dengan yang sudah ada !")
                        else:
                            dictMobil[newPrimKey] = dictMobil[PrimKey]
                            del dictMobil[PrimKey]
                            print("\nProses Mengubah Data Berhasil ! \n")
                            menampilkanReport()
                            break
                    break
            
                        

        elif pilihanMengubah == 2:
            while True:
                PrimKey = input("Masukan Indeks Data yang ingin anda Ubah : ")
                if len(PrimKey) == 0:
                    print("Index yang dimasukan tidak boleh kosong !")
                    break
                elif PrimKey not in dictMobil.keys():
                    print("Index yang anda Masukan tidak ada")
                    break               
                elif PrimKey in dictMobil.keys():
                    while True:
                        newNM = input("Masukan Nama Mobil yang Baru : ")
                        if len(newNM) == 0:
                            print("data yang anda Masukan tidak Boleh Kosong ! ")
                        elif newNM == dictMobil[PrimKey]["Nama Mobil"]:
                            print("Nama Mobil baru yang anda masukan tidak boleh sama !")
                        else:
                            dictMobil[PrimKey]["Nama Mobil"] = newNM      
                            print("\nProses Mengubah Data Berhasil ! \n")
                            menampilkanReport()
                            break
                break
            
        elif pilihanMengubah == 3:
            while True:
                PrimKey = input("Masukan Indeks Data yang ingin anda Ubah : ")
                if len(PrimKey) == 0:
                    print("Index yang dimasukan tidak boleh kosong !")
                    break
                elif PrimKey not in dictMobil.keys():
                    print("Index yang anda Masukan tidak ada")
                    break
                elif PrimKey in dictMobil.keys():
                    while True:
                        newTK = input("Masukan Tipe Mobil yang Baru : ")
                        if len(newTK) == 0:
                            print("data yang anda Masukan tidak Boleh Kosong ! ")
                        elif newTK == dictMobil[PrimKey]["Tipe Kendaraan"]:
                            print("Tipe Mobil baru yang anda masukan tidak boleh sama !")
                        else:
                            dictMobil[PrimKey]["Tipe Kendaraan"] = newTK    
                            print("\nProses Mengubah Data Berhasil ! \n")
                            menampilkanReport()
                            break
                break
            
        elif pilihanMengubah == 4:
            while True:
                PrimKey = input("Masukan Indeks Data yang ingin anda Ubah : ")
                if len(PrimKey) == 0:
                    print("Index yang dimasukan tidak boleh kosong !")
                    break
                elif PrimKey not in dictMobil.keys():
                    print("Index yang anda Masukan tidak ada")
                    break
                elif PrimKey in dictMobil.keys():
                    while True:
                        newB = input("Masukan Biaya yang Baru : ")
                        if len(newB) == 0:
                            print("data yang anda Masukan tidak Boleh Kosong ! ")
                        elif int(newB) == dictMobil[PrimKey]["Biaya"]:
                            print("Biaya baru yang anda masukan tidak boleh sama !")
                        else:
                            dictMobil[PrimKey]["Biaya"] = int(newB)  
                            print("\nProses Mengubah Data Berhasil ! \n")
                            menampilkanReport()
                            break
                break
            
        elif pilihanMengubah == 5:
            while True:
                PrimKey = input("Masukan Indeks Data yang ingin anda Ubah : ")
                if len(PrimKey) == 0:
                    print("Index yang dimasukan tidak boleh kosong !")
                    break
                elif PrimKey not in dictMobil.keys():
                    print("Index yang anda Masukan tidak ada")
                    break
                elif PrimKey in dictMobil.keys():
                    while True:
                        newP = input("Masukan Penyewa yang Baru : ")
                        if len(newP) == 0:
                            print("data yang anda Masukan tidak Boleh Kosong ! ")
                        elif newP == dictMobil[PrimKey]["Penyewa"]:
                            print("Jumlah Mobil baru yang anda masukan tidak boleh sama !")
                        else:
                            dictMobil[PrimKey]["Penyewa"] = newP 
                            print("\nProses Mengubah Data Berhasil ! \n")
                            menampilkanReport()
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
            elif len(inputPilihanDelete) == 0:
                print("Primary Key tidak Boleh Kosong !")
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

    Masukan angka Menu yang ingin dijalankan [1-5] : '''))

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
