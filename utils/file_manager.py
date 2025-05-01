import csv
from models.item import Item

class FileManager:
    """
    Class untuk mengatur penyimpanan dan pembacaan data ke file CSV.
    """

    @staticmethod
    def save_inventory(filename, inventory):
        """
        Menyimpan semua data inventory ke file CSV.
        """
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["id_barang", "nama", "kategori", "harga", "stok"])  # Header
            current = inventory.head
            while current:
                writer.writerow([current.id_barang, current.nama, current.kategori, current.harga, current.stok])
                current = current.next

    @staticmethod
    def load_inventory(filename, inventory):
        """
        Membaca data dari file CSV ke inventory.
        """
        try:
            with open(filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    inventory.add_item(
                        id_barang=row['id_barang'],
                        nama=row['nama'],
                        kategori=row['kategori'],
                        harga=int(row['harga']),
                        stok=int(row['stok'])
                    )
        except FileNotFoundError:
            print(f"File {filename} tidak ditemukan. Membuat file baru saat menyimpan.")
