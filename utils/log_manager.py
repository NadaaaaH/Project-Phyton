import csv
import os

class LogManager:
    @staticmethod
    def save_log(filename, action, nama_barang, jumlah):
        file_exists = os.path.isfile(filename)

        with open(filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(['Action', 'Nama Barang', 'Jumlah'])

            writer.writerow([action, nama_barang, jumlah])
