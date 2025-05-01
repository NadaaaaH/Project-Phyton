class Node:
    def __init__(self, transaksi):
        self.transaksi = transaksi
        self.next = None

class Queue:
    """
    Struktur data antrian (Queue) untuk transaksi kasir.
    Menggunakan prinsip FIFO (First In First Out).
    """
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, transaksi):
        new_node = Node(transaksi)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None
        return temp.transaksi

    def is_empty(self):
        return self.front is None

    def display_queue(self):
        if self.is_empty():
            print("Tidak ada transaksi.")
        else:
            current = self.front
            print("=== Antrian Transaksi ===")
            while current:
                print(f"Transaksi: {current.transaksi}")
                current = current.next
