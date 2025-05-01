class Item:
    """
    Class untuk merepresentasikan satu barang di dalam linked list.
    """
    def __init__(self, id_barang, nama, kategori, harga, stok):
        self.id_barang = id_barang
        self.nama = nama
        self.kategori = kategori
        self.harga = harga
        self.stok = stok
        self.next = None  # Pointer ke barang berikutnya (linked list)
