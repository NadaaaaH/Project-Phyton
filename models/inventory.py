from models.item import Item
import csv

class InventoryList:
    """
    Class untuk manajemen linked list inventory.
    """
    def __init__(self):
        self.head = None

    def add_item(self, id_barang, nama, kategori, harga, stok):
        new_item = Item(id_barang, nama, kategori, harga, stok)
        if self.head is None:
            self.head = new_item
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_item

        self.simpan_ke_csv()  # ← Langsung simpan setelah tambah

    def simpan_ke_csv(self, filename="data_barang.csv"):
        current = self.head
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Nama', 'Kategori', 'Harga', 'Stok'])
            while current:
                writer.writerow([
                    current.id_barang,
                    current.nama,
                    current.kategori,
                    current.harga,
                    current.stok
                ])
                current = current.next

    def display_items(self):
        """
        Menampilkan semua barang yang ada di inventory.
        """
        if self.head is None:
            print("Tidak ada barang di inventory.")
            return
        current = self.head
        while current:
            print(f"ID: {current.id_barang} | Nama: {current.nama} | Kategori: {current.kategori} | Harga: {current.harga} | Stok: {current.stok}")
            current = current.next

    def find_item_by_name(self, nama):
        """
        Mencari barang berdasarkan nama (linear search).
        """
        current = self.head
        while current:
            if current.nama.lower() == nama.lower():
                return current
            current = current.next
        return None

    def update_item(self, id_barang, nama=None, kategori=None, harga=None, stok=None):
        """
        Memperbarui informasi item berdasarkan ID.
        """
        current = self.head
        while current:
            if current.id_barang == id_barang:
                if nama:
                    current.nama = nama
                if kategori:
                    current.kategori = kategori
                if harga is not None:
                    current.harga = harga
                if stok is not None:
                    current.stok = stok
                self.simpan_ke_csv()
                return True
            current = current.next
        return False

    def delete_item(self, id_barang):
        """
        Menghapus item berdasarkan ID.
        """
        current = self.head
        prev = None
        while current:
            if current.id_barang == id_barang:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                self.simpan_ke_csv()
                return True
            prev = current
            current = current.next
        return False

    def cek_stok_rendah(self, ambang_batas=5):
        current = self.head
        print("\n=== NOTIFIKASI STOK RENDAH ===")
        stok_rendah = False
        while current:
            if current.stok <= ambang_batas:
                print(f"⚠️  {current.nama} stok tersisa {current.stok}")
                stok_rendah = True
            current = current.next
        if not stok_rendah:
            print("Semua stok dalam kondisi aman.")


    def sortir_barang(self, kunci='nama'):
        data = []
        current = self.head
        while current:
            data.append(current)
            current = current.next

        if kunci == 'nama':
            data.sort(key=lambda x: x.nama.lower())
        elif kunci == 'harga':
            data.sort(key=lambda x: x.harga)
        elif kunci == 'stok':
            data.sort(key=lambda x: x.stok)

        print(f"\n=== Daftar Barang diurutkan berdasarkan {kunci.capitalize()} ===")
        for item in data:
            print(f"ID: {item.id_barang} | Nama: {item.nama} | Harga: {item.harga} | Stok: {item.stok}")
