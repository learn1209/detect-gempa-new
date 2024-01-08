# Aplikasi deteksi gempa terkini

def ekstraksi_data():
    hasil = dict()
    hasil['tanggal'] = '5 January 2024'
    hasil['waktu'] = '23:19:23 WIB'
    print(hasil)
    return hasil



def tampilkan_data(result):
    print('Last info gempa')
    print('Tanggal', result['tanggal'])
    print('waktu', result['waktu'])    



if __name__ == '__main__':
    print("Aplikasi Utama")
    result = ekstraksi_data()
    tampilkan_data(result)