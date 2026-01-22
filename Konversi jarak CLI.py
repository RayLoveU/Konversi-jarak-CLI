def konversi(jarak, dari_satuan, ke_satuan):
    satuan_ke_meter = {
        'milimeter' : 10,
        'sentimeter' : 100,
        'meter' : 1,
        'kilometer' : 0.001,
    }

    if dari_satuan not in satuan_ke_meter or ke_satuan not in satuan_ke_meter:
        raise ValueError("Satuan tidak valid. Pilih dari 'milimeter', 'sentimeter', 'meter', atau 'kilometer'.")

    jarak_meter = jarak / satuan_ke_meter[dari_satuan]
    hasil = jarak_meter * satuan_ke_meter[ke_satuan]
    return hasil
if __name__ == "__main__":
    print("Konversi Jarak CLI")
    print("Satuan yang tersedia: milimeter, sentimeter, meter, kilometer")
    
    jarak = float(input("Masukkan jarak yang akan dikonversi: "))
    dari_satuan = input("Masukkan satuan asal: ").lower()
    ke_satuan = input("Masukkan satuan tujuan: ").lower()
    
    try:
        hasil = konversi(jarak, dari_satuan, ke_satuan)
        print(f"{jarak} {dari_satuan} sama dengan {hasil} {ke_satuan}")
    except ValueError as e:
        print(e)