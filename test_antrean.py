import unittest
# Memanggil class dari file main.py
from main import AntreanLayanan, FiturUndo

class TestAntreanLayanan(unittest.TestCase):
    def setUp(self):
        # Dijalankan sebelum setiap test pada antrean dimulai
        self.sistem = AntreanLayanan()

    # 1. Test Penambahan Data (Antrean)
    def test_penambahan_data(self):
        self.sistem.enqueue("Z-999: Test Mahasiswa 1")
        self.assertEqual(self.sistem.get_kondisi(), ["Z-999: Test Mahasiswa 1"])

    # 2. Test Penghapusan Data (Antrean)
    def test_penghapusan_data(self):
        self.sistem.enqueue("Z-999: Test Mahasiswa 1")
        self.sistem.enqueue("Z-888: Test Mahasiswa 2")
        dihapus = self.sistem.dequeue()
        
        # Mahasiswa 1 harusnya terhapus (FIFO)
        self.assertEqual(dihapus, "Z-999: Test Mahasiswa 1")
        self.assertEqual(self.sistem.get_kondisi(), ["Z-888: Test Mahasiswa 2"])

    # 3. Test Melihat Data Terdepan (Antrean)
    def test_melihat_data_terdepan(self):
        self.sistem.enqueue("Z-777: Test Mahasiswa 3")
        terdepan = self.sistem.peek()
        
        self.assertEqual(terdepan, "Z-777: Test Mahasiswa 3")
        # Pastikan data tidak terhapus setelah di-peek
        self.assertEqual(self.sistem.get_kondisi(), ["Z-777: Test Mahasiswa 3"]) 

    # 4. Test Memeriksa Kondisi Kosong (Antrean)
    def test_memeriksa_kondisi_kosong(self):
        self.assertTrue(self.sistem.is_empty()) # Harus True saat baru inisialisasi
        self.sistem.enqueue("Z-666: Test Mahasiswa 4")
        self.assertFalse(self.sistem.is_empty()) # Harus False setelah diisi


class TestFiturUndo(unittest.TestCase):
    def setUp(self):
        # Dijalankan sebelum setiap test pada fitur undo dimulai
        self.fitur = FiturUndo()

    # 1. Test Penambahan Data (Undo)
    def test_penambahan_data(self):
        self.fitur.push("Aktivitas 1: Mengubah status dokumen")
        self.assertEqual(self.fitur.get_kondisi(), ["Aktivitas 1: Mengubah status dokumen"])

    # 2. Test Penghapusan Data (Undo)
    def test_penghapusan_data(self):
        self.fitur.push("Aktivitas 1: Mengubah status dokumen")
        self.fitur.push("Aktivitas 2: Mencetak kartu")
        dibatalkan = self.fitur.pop()
        
        # Yang dibatalkan/dihapus harus aktivitas yang terakhir dimasukkan (LIFO)
        self.assertEqual(dibatalkan, "Aktivitas 2: Mencetak kartu")
        self.assertEqual(self.fitur.get_kondisi(), ["Aktivitas 1: Mengubah status dokumen"])

    # 3. Test Melihat Data Teratas (Undo)
    def test_melihat_data_teratas(self):
        self.fitur.push("Aktivitas 3: Menghapus data pendaftar")
        teratas = self.fitur.peek()
        
        self.assertEqual(teratas, "Aktivitas 3: Menghapus data pendaftar")
        # Pastikan aktivitas tidak terhapus dari riwayat
        self.assertEqual(self.fitur.get_kondisi(), ["Aktivitas 3: Menghapus data pendaftar"])

    # 4. Test Memeriksa Kondisi Kosong (Undo)
    def test_memeriksa_kondisi_kosong(self):
        self.assertTrue(self.fitur.is_empty()) 
        self.fitur.push("Aktivitas 4: Memasukkan data baru")
        self.assertFalse(self.fitur.is_empty())


# Menjalankan unit test saat file test_antrean.py di-run
if __name__ == '__main__':
    unittest.main()