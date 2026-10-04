from collections import deque

class AntreanLayanan:
    """Implementasi Struktur Data Queue (FIFO) untuk Antrean Layanan Mahasiswa"""
    def __init__(self):
        self.antrean = deque()

    def is_empty(self):
        """Memeriksa apakah antrean kosong"""
        return len(self.antrean) == 0

    def enqueue(self, mahasiswa):
        """Penambahan data: memasukkan mahasiswa ke barisan paling belakang"""
        self.antrean.append(mahasiswa)

    def dequeue(self):
        """Penghapusan data: melayani mahasiswa di barisan paling depan"""
        if self.is_empty():
            return None
        return self.antrean.popleft()

    def peek(self):
        """Melihat data terdepan tanpa mengeluarkannya"""
        if self.is_empty():
            return None
        return self.antrean[0]

    def get_kondisi(self):
        """Mengembalikan daftar antrean saat ini"""
        return list(self.antrean)


class FiturUndo:
    """Implementasi Struktur Data Stack (LIFO) untuk Pembatalan Aktivitas Petugas"""
    def __init__(self):
        self.stack = []

    def is_empty(self):
        """Memeriksa apakah riwayat aktivitas kosong"""
        return len(self.stack) == 0

    def push(self, aktivitas):
        """Penambahan data: menyimpan aktivitas baru ke posisi teratas riwayat"""
        self.stack.append(aktivitas)

    def pop(self):
        """Penghapusan data: pembatalan/menghapus aktivitas teratas"""
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        """Melihat data teratas (aktivitas terakhir) tanpa menghapusnya"""
        if self.is_empty():
            return None
        return self.stack[-1]

    def get_kondisi(self):
        """Mengembalikan daftar riwayat aktivitas saat ini"""
        return list(self.stack)


# ==========================================
#         BLOK SIMULASI
# ==========================================

def jalankan_simulasi_antrean():
    sistem_antrean = AntreanLayanan()
    print("--- SIMULASI FITUR ANTREAN ---")
    
    # Langkah 1: Penambahan data
    sistem_antrean.enqueue("A-001: Ahmad Dahlan")
    print("Langkah 1 (Enqueue):", sistem_antrean.get_kondisi())
    
    # Langkah 2: Penambahan data
    sistem_antrean.enqueue("A-002: Budi Santoso")
    print("Langkah 2 (Enqueue):", sistem_antrean.get_kondisi())
    
    # Langkah 3: Penambahan data
    sistem_antrean.enqueue("A-003: Citra Dewi")
    print("Langkah 3 (Enqueue):", sistem_antrean.get_kondisi())
    
    # Langkah 4: Penghapusan data
    sistem_antrean.dequeue()
    print("Langkah 4 (Dequeue):", sistem_antrean.get_kondisi())
    
    # Langkah 5: Penambahan data
    sistem_antrean.enqueue("A-004: Doni Prasetya")
    print("Langkah 5 (Enqueue):", sistem_antrean.get_kondisi())
    
    # Langkah 6: Penghapusan data
    sistem_antrean.dequeue()
    print("Langkah 6 (Dequeue):", sistem_antrean.get_kondisi())

    # Langkah 7: Penambahan data
    sistem_antrean.enqueue("A-005: Eka Ratnawati")
    print("Langkah 7 (Enqueue):", sistem_antrean.get_kondisi())
    print("\n")


def jalankan_simulasi_undo():
    fitur_undo = FiturUndo()
    print("--- SIMULASI FITUR UNDO ---")
    
    # Langkah 1: Penambahan data
    fitur_undo.push("03/10/2026 08:00 - Memvalidasi berkas pendaftaran A-001")
    print("Langkah 1 (Push):", fitur_undo.get_kondisi())
    
    # Langkah 2: Penambahan data
    fitur_undo.push("03/10/2026 08:15 - Mencetak Kartu Rencana Studi (KRS)")
    print("Langkah 2 (Push):", fitur_undo.get_kondisi())
    
    # Langkah 3: Penambahan data
    fitur_undo.push("03/10/2026 08:30 - Mengubah status layanan A-002 menjadi Selesai")
    print("Langkah 3 (Push):", fitur_undo.get_kondisi())
    
    # Langkah 4: Penghapusan data (Undo)
    fitur_undo.pop()
    print("Langkah 4 (Pop) :", fitur_undo.get_kondisi())
    
    # Langkah 5: Penambahan data
    fitur_undo.push("03/10/2026 08:45 - Mengunggah dokumen transkrip nilai A-003")
    print("Langkah 5 (Push):", fitur_undo.get_kondisi())
    print("\n")


# Menjalankan simulasi saat file main.py di-run
if __name__ == '__main__':
    jalankan_simulasi_antrean()
    jalankan_simulasi_undo()
