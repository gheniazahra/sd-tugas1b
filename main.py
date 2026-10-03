from collections import deque

class AntreanLayanan:
    #Implementasi Struktur Data Queue (FIFO) untuk Antrean Layanan Mahasiswa
    def __init__(self):
        self.antrean = deque()

    def is_empty(self):
        #Memeriksa apakah antrean kosong
        return len(self.antrean) == 0

    def enqueue(self, mahasiswa):
        #Penambahan data: memasukkan mahasiswa ke barisan paling belakang
        self.antrean.append(mahasiswa)

    def dequeue(self):
        #Penghapusan data: melayani mahasiswa di barisan paling depan
        if self.is_empty():
            return None
        return self.antrean.popleft()

    def peek(self):
        #Melihat data terdepan tanpa mengeluarkannya
        if self.is_empty():
            return None
        return self.antrean[0]

    def get_kondisi(self):
        #Mengembalikan daftar antrean saat ini
        return list(self.antrean)


class FiturUndo:
    #Implementasi Struktur Data Stack (LIFO) untuk Pembatalan Aktivitas Petugas
    def __init__(self):
        self.stack = []

    def is_empty(self):
        #Memeriksa apakah riwayat aktivitas kosong
        return len(self.stack) == 0

    def push(self, aktivitas):
        #Penambahan data: menyimpan aktivitas baru ke posisi teratas riwayat
        self.stack.append(aktivitas)

    def pop(self):
        #Penghapusan data: membatalkan/menghapus aktivitas teratas
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        #Melihat data terdepan (aktivitas terakhir) tanpa menghapusnya
        if self.is_empty():
            return None
        return self.stack[-1]

    def get_kondisi(self):
        #Mengembalikan daftar riwayat aktivitas saat ini
        return list(self.stack)


# Contoh Pengujian Sederhana
if __name__ == "__main__":
    # 1. Pengujian Antrean
    sistem_antrean = AntreanLayanan()
    print("--- PENGUJIEN ANTREAN ---")
    sistem_antrean.enqueue({"no_urut": 1, "nama": "Ahmad"})
    sistem_antrean.enqueue({"no_urut": 2, "nama": "Budi"})
    print("Data Terdepan:", sistem_antrean.peek())
    print("Dilayani:", sistem_antrean.dequeue())
    print("Status Kosong:", sistem_antrean.is_empty())

    # 2. Pengujian Undo
    fitur_undo = FiturUndo()
    print("\n--- PENGUJIAN UNDO ---")
    fitur_undo.push({"id": 101, "aktivitas": "Memproses Berkas Ahmad"})
    fitur_undo.push({"id": 102, "aktivitas": "Mencetak Kartu Budi"})
    print("Aktivitas Terakhir:", fitur_undo.peek())
    print("Dibatalkan:", fitur_undo.pop())
    print("Status Kosong:", fitur_undo.is_empty())