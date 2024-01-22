from bs4 import BeautifulSoup
import requests

def ekstraksi_data():
    url = "https://bmkg.go.id/"
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',}

    try:
        content = requests.get(url, headers=headers)
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(', ')

        tanggal = result[0]
        waktu = result[1]
        # print(soup.prettify())

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None


        for res in result:
            
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
                
            i = i + 1

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['ls'] = ls
        hasil['bt'] = bt
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan
        print('----------------------')
        # print(hasil)
        return hasil
    else:
        return None



def tampilkan_data(result):
    if result is None:
        print('Server Masih Perbaikan')
        return
    
    print('Last info gempa')
    print('Tanggal : ', result['tanggal'])
    print('Waktu : ', result['waktu'])
    print('Magnitudo : ', result['magnitudo'])
    print('Kedalaman : ', result['kedalaman'])
    print(f"Koordinat : {result['ls']} , {result['bt']}")
    print('Pusat : ', result['lokasi'])
    print('Dirasakan : ', result['dirasakan'])
if __name__ == '__MAIN__':
    print("haiii")
