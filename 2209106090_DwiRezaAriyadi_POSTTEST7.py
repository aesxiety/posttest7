import os
os.system ("cls")
from prettytable import PrettyTable


barang = {
    "barang_elektronik" : ['KIPAS','SETRIKA','SPEAKER'],
    "harga" :  [500,250,50]
    }


table=PrettyTable()
judul = ["Barang Elektronik","Harga"]
table.field_names = judul

def buat_table():
    table.clear_rows()
    for i in range(len(barang.get("barang_elektronik"))):
        table.add_row([barang.get("barang_elektronik")[i], barang.get("harga")[i]])

def program_user():
    while True:
        print("""
        ========================
        |       MENU USER      |
        |======================|
        | 1. Tampilkan Barang  |
        | 2. Beli Barang       |
        | 3. Exit              |
        ========================
        """)
        menu_user= input('\n masukan pilihan : ')
        
        if menu_user=='1':
            print()
            print("-"*25)
            buat_table()
            print(table)
            print("-"*25)
            print()
            continue
        elif menu_user == '2':
            menu2 ="y"
            while menu2 == "y":
                print("***** SELAMAT BERBELANJA *****")
                buat_table()
                print(table)
                while True :
                    nama_barang = input("masukan nama barang : ").upper()
                    try:
                        cari = barang.get("barang_elektronik")
                        hasil_index = cari.index(nama_barang)
                        break 

                    except ValueError:
                        print("ERROR-> Masukan kembali nama barang anda")
        
                while True:
                    total = int(input("masukkan jumlah barang yang ingin dibeli: "))
                    if total > 0 :
                        totalharga = (barang.get("harga")[hasil_index]*total)
                        print("="*40, "\n")
                        print("\tBarang yang Ingin Dibeli\t")
                        print("barang: ",(barang.get("barang_elektronik")[hasil_index]))
                        print("harga : ",(barang.get("harga")[hasil_index]))
                        print("total harga :",totalharga)
                        print("\n", "="*40)
                        break
                    else:
                        print("inputan tidak valid")
                        continue

                menu2 = input('Beli lagi ? [y/t] : ').lower()
                if menu2 == "t":
                    break

        elif menu_user == '3':
            break

        else :
            continue

def program_admin():
    while True :
        print("""
            =========================================
            | ----------  PILIHAN ADMIN  ---------- |
            |  1.Menambahkan barang dan harga       |
            |  2.Melihat barang dan harga           |
            |  3.Memperbarui nama barang            |
            |  4.Menghapus barang tertentu          |
            |  5.Logout Admin                       |
            =========================================
            """)
        print()
        menu = input("Masukan menu [1-5] : ")
        if menu == '1':
            menu1 ='y'
            print("Menambahkan barang dan harga ")
            while menu1 == 'y':
                print()
                print("-"*25)
                print()
                buat_table()
                print(table)
                print()
                print("-"*25)
                BarangBaru = input("Masukan nama barang : ").upper()
                #eror handling inputan berupa sring
                while True:
                    try:
                        HargaBaru =int(input("Masukan harga barang : "))
                        break
                    except ValueError :
                        print("hanya masukan angka broo")
                print()
                print("-"*25)
                print()
                barang.get("barang_elektronik").append(BarangBaru)
                barang.get("harga").append(HargaBaru)
                print()
                buat_table()
                print(table)
                menu1 = input('Tambahkan Data Lagi ? [y/t] : ').lower()
                if menu1 == "t":
                    break
            
        elif menu == '2':
            print("Melihat barang dan harga")
            print("-"*25)
            buat_table()
            print(table)
            print("-"*25)
            print()

        elif menu == '3':
            menu3 = 'y'
            print("Memperbarui Nama Barang")
            while menu3 == 'y':
                while True:
                    print()
                    print("-"*25)
                    print()
                    buat_table()
                    print(table)
                    print()
                    nama_barang = input("masukan nama barang : ").upper()
                    try:
                        cari = barang.get("barang_elektronik")
                        hasil_index = cari.index(nama_barang.upper())
                        break 

                    except ValueError:
                        print("Periksa kembali penulisan anda")

                a =input("masukan barang baru : ").upper()
                print()
                #eror handling inputan berupa sring
                while True:
                    try:
                        b = input("masukan harga barang baru :")
                        break
                    except ValueError :
                        print("hanya masukan angka broo")

                barang.get("barang_elektronik")[hasil_index] = a
                barang.get("harga")[hasil_index]= b
                buat_table()
                print(table)
                
                menu3 = input('Update/ubah Data Lagi ?  [y/t]: ').lower()
                if menu3 == "t":
                        break
                
        elif menu == '4':
            menu4 = 'y'
            print("Menghapus barang tertentu")
            while menu4 == 'y' :
                while True:
                    buat_table()
                    print(table)
                    print()
                    nama_barang = input("masukan nama barang : ").upper()
                    try:
                        cari = barang.get("barang_elektronik")
                        hasil_index = cari.index(nama_barang)
                        break 

                    except ValueError:
                        print("Periksa kembali penulisan anda")

                a = barang.get("barang_elektronik")
                c = a.index(nama_barang)
                a.pop(c)
                buat_table()
                print(table)

                menu4 = input('Delete Data Lagi ? [y/t]: ')
                if menu4 == "t":
                        break

        elif menu == '5':
            break
            
        else :
            print("input Not Found")
            continue
    
def admin():
    us_admin = "admin"
    pw_admin = "admin123"   

    i = 0  
    while i < 3 :
        print('='*24)
        print('halo admin, silahkan login\n')  
        us_admin =input("Username : ")
        pw_admin = input("Password : ")
        if us_admin == "admin" and pw_admin == "admin123":
            print()
            print("LOGIN SUKSESS")
            break
        else :
            print()
            print('LOGIN GAGAL')
            i+=1 
            continue 
    if i <3 :
        program_admin()
    elif i==3:
        exit

     
def login_user(username,password):

    print()
    print("SILAHKAN LOGIN")
    i = 0  
    while i < 3 :  
        us_user =input("Username : ")
        pw_user = input("Password : ")  
        if us_user == username and pw_user == password:
            print()
            print("LOGIN SUKSESS\n")
            break
        else :
            print()
            print('LOGIN GAGAL')
            i+=1 
            continue 
    if i < 3 :
        program_user()
    elif i==3:
        exit()       
   
menu ='y'
while menu== 'y':
    print('Login Sebagai : \n1.admin \n2.user')
    sebagai =input('\nmasukan opsi: ') 
    if sebagai == '1' or sebagai == 'admin':
        admin()

    elif sebagai == '2' or sebagai == 'user':
        
        while True:
            account = input("Sudah punya akun [y/t] : ").lower()
            if account == "t" :
                print('REGISTRASI AKUN TERLEBIH DAHULU')
                username = input("Username : ")
                password = input("Password : ")
                break
            elif account == "y":
                break
            else:
                continue
        
        try:
            login_user(username,password)
            
        except :
            print("akun belum dibuat")


    else:
        print('eror')

    menu = input('ke menu login?[y/t] : ').lower()
    if menu == 't':
        break    












