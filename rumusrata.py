def rata_rata(*data):
    banyak_data = len(data)
    jumlah_data = sum(data)
    nilai_rata_rata = float(jumlah_data) / float(banyak_data)
    return nilai_rata_rata

print("Rata-rata: ",rata_rata(84,99,86,85,94,88,84,81,92,86,96,94,93,79,80,91))