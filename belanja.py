import csv
import os

csv_filename = 'Barang.csv'
import time

#fungsi untuk membersihkan tampilan
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Menampilkan menu program
def show_menu():

    clear_screen()
#   Baris kode untuk jumlah total data
    Barang = []
    with open('Barang.csv', "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Barang.append(row)
    row_count = sum(1 for row in Barang)

    print("=== Program Inventory Barang === \n")
    print("============ Menu =============")
    print("* Total Barang : ",row_count)  
    print("===============================")
    print("[1] Lihat Daftar Barang")
    print("[2] Tambah Barang")
    print("[3] Hapus Barang")
    print("[0] Exit \n")
    print("===============================")
    selected_menu = input("Pilih menu> ")
    
    #menampilkan percabangan pada menu
    if(selected_menu == "1"):
        show_barang()
    elif(selected_menu == "2"):
        tambah_barang()
    elif(selected_menu == "3"):
        delete_barang()
    elif(selected_menu == "0"):
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()

#fungsi yang berguna untuk mengembalikan ke menu
def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()

# fungsi menampilkan barang 
def show_barang():
    clear_screen()
    Barang = []
# buka file CSV dengan mode R / Baca
    with open('Barang.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Barang.append(row)

    row_count = sum(1 for row in Barang)

    print("-" * 55)
    print("\t\tDaftar Barang di Inventory")
    print("-" * 55)

    print("kode \t NAMA \t\t harga")
    print("-" * 55)

    # Looping untuk mengeluarkan datanyna
    for data in Barang:
        print(f"{data['Kode']} \t {data['NAMA']} \t Rp.{data['HARGA']}|")
    print("-" * 55)
    print("Total Data: ",row_count)
    print("-" * 55)
    
    back_to_menu()



#  fungsi tambah barang 
def tambah_barang():
    clear_screen()
    with open('Barang.csv', 'a',newline='') as csv_file:
        fieldnames = ['kode', 'NAMA', 'harga']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        print("===============================")
        print("======== Tambah Barang ========")
        print("===============================\n")
        
        kode = input("kode: ")
        nama = input("Nama Barang: ")
        harga = input("Harga Barang: ")

        print("===============================")


        writer.writerow({'kode': kode, 'NAMA': nama, 'harga': harga})  
        print('Data berhasil ditambahkan')  
    back_to_menu()

#fungsi hapus barang
def delete_barang():
    clear_screen()
    Barang = []

    with open('Barang.csv', mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Barang.append(row)

    print("kode \t NAMA \t\t harga")
    print("-" * 55)

    for data in Barang:
        print(f"{data['Kode']} \t {data['NAMA']} \t {data['HARGA']}")

    print("-----------------------")
    kode = input("Hapus Barang dengan KODE : ")

    indeks = 0
    for data in Barang:
        if (data['Kode'] == kode):
            Barang.remove(Barang[indeks])
        indeks = indeks + 1

    # Menulis data baru ke file CSV (tulis ulang)
    with open('Barang.csv', mode="w") as csv_file:
        fieldnames = ['Kode', 'NAMA', 'HARGA']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in Barang:
            writer.writerows({'Kode': new_data['Kode'], 'NAMA': new_data['NAMA'], 'HARGA': new_data['HARGA']}) 

    print("Data sudah terhapus")
    back_to_menu()

if __name__ == "__main__":
    while True:
        show_menu()