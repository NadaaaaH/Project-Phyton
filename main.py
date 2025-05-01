from models.inventory import InventoryList
from utils.file_manager import FileManager
from models.queue import Queue
from utils.log_manager import LogManager

RIWAYAT_FILENAME = 'riwayat_stok.csv'
FILENAME = "data_inventory.csv"  # Nama file untuk simpan data

def menu_kasir(inventory):
    transaksi_queue = Queue()

    while True:
        print("\n==== MENU KASIR ====")
        print("1. Lihat Daftar Barang")
        print("2. Cari Barang")
        print("3. Lakukan Transaksi")
        print("4. Lihat Antrian Transaksi")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            inventory.display_items()
        elif pilihan == '2':
            nama = input("Nama Barang yang dicari: ")
            item = inventory.find_item_by_name(nama)
            if item:
                print(f"ID: {item.id_barang} | Nama: {item.nama} | Harga: {item.harga} | Stok: {item.stok}")
            else:
                print("Barang tidak ditemukan.")
        elif pilihan == '3':
            nama = input("Masukkan Nama Barang yang dibeli: ")
            item = inventory.find_item_by_name(nama)
            if item:
                jumlah = int(input("Masukkan jumlah pembelian: "))
                if item.stok >= jumlah:
                    total_harga = item.harga * jumlah
                    item.stok -= jumlah

                    transaksi = f"{item.nama} x {jumlah} = Rp{total_harga}"
                    transaksi_queue.enqueue(transaksi)

                    LogManager.save_log(RIWAYAT_FILENAME, 'Update Stok', item.nama, item.stok)

                    print("Transaksi berhasil!")
                    print(f"Total Harga: Rp{total_harga}")
                    print("Struk:")
                    print("======================")
                    print(f"Barang: {item.nama}")
                    print(f"Jumlah: {jumlah}")
                    print(f"Total: Rp{total_harga}")
                    print("======================")
                else:
                    print("Stok tidak mencukupi.")
            else:
                print("Barang tidak ditemukan.")
        elif pilihan == '4':
            transaksi_queue.display_queue()
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

def menu_admin(inventory):
    while True:
        print("\n==== MENU ADMIN ====")
        print("1. Tambah Barang")
        print("2. Lihat Daftar Barang")
        print("3. Cari Barang")
        print("4. Update Barang")
        print("5. Hapus Barang")
        print("6. Simpan Data")
        print("7. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            id_barang = input("ID Barang: ")
            nama = input("Nama Barang: ")
            kategori = input("Kategori: ")
            harga = int(input("Harga: "))
            stok = int(input("Stok: "))
            inventory.add_item(id_barang, nama, kategori, harga, stok)
            print("Barang berhasil ditambahkan!")
            LogManager.save_log(RIWAYAT_FILENAME, 'Update Stok', item.nama, item.stok)
            
        elif pilihan == '2':
            inventory.display_items()
        elif pilihan == '3':
            nama = input("Nama Barang yang dicari: ")
            item = inventory.find_item_by_name(nama)
            if item:
                print(f"ID: {item.id_barang} | Nama: {item.nama} | Harga: {item.harga} | Stok: {item.stok}")
            else:
                print("Barang tidak ditemukan.")
        elif pilihan == '4':
            id_barang = input("ID Barang yang mau diupdate: ")
            nama = input("Nama baru (kosongkan jika tidak mau ubah): ")
            kategori = input("Kategori baru (kosongkan jika tidak mau ubah): ")
            harga = input("Harga baru (kosongkan jika tidak mau ubah): ")
            stok = input("Stok baru (kosongkan jika tidak mau ubah): ")

            result = inventory.update_item(
                id_barang,
                nama if nama else None,
                kategori if kategori else None,
                int(harga) if harga else None,
                int(stok) if stok else None
            )
            if result:
                print("Barang berhasil diupdate.")
            else:
                print("Barang tidak ditemukan.")

            LogManager.save_log(RIWAYAT_FILENAME, 'Update Stok', item.nama, item.stok)
        
        elif pilihan == '5':
            id_barang = input("ID Barang yang mau dihapus: ")
            if inventory.delete_item(id_barang):
                print("Barang berhasil dihapus.")
            else:
                print("Barang tidak ditemukan.")
        elif pilihan == '6':
             print("\nSortir berdasarkan:")
             print("1. Nama")
             print("2. Harga")
             print("3. Stok")
             kunci_sortir = input("Pilih kunci sortir: ")
             if kunci_sortir == '1':
                inventory.sortir_barang('nama')
             elif kunci_sortir == '2':
                inventory.sortir_barang('harga')
             elif kunci_sortir == '3':
                inventory.sortir_barang('stok')
             else:
                print("Pilihan tidak valid.")
             FileManager.save_inventory(FILENAME, inventory)
             print("Data berhasil disimpan ke file.")
        elif pilihan == '7':
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

        LogManager.save_log(RIWAYAT_FILENAME, 'Update Stok', item.nama, item.stok)
        

def main():
    inventory = InventoryList()

    # Load data saat aplikasi dibuka
    FileManager.load_inventory(FILENAME, inventory)

    while True:
        print("\n=== SELAMAT DATANG DI SISTEM INVENTORI ===")
        print("1. Login sebagai Admin")
        print("2. Login sebagai Kasir")
        print("3. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            menu_admin(inventory)
        elif pilihan == '2':
            menu_kasir(inventory)
        elif pilihan == '3':
            FileManager.save_inventory(FILENAME, inventory)
            print("Data berhasil disimpan. Terima kasih telah menggunakan sistem ini.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
