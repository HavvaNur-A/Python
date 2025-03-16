import requests
import json

while True:
    sehir=input("Lütfen Hava Durumunu Öğrenmek İstediğiniz Şehri Giriniz:")
    apiKey="ebf38ccf3f71beedd18c9cfba0dc0eeb"
    adres="https://api.openweathermap.org/data/2.5/weather?q={}&lang=tr&appid={}&units=metric".format(sehir,apiKey)
    baglan=requests.get(adres)
    sorgu=baglan.json()
 #   print(sorgu)
    
    havaDurumu=sorgu["weather"][0]["description"]
    havasicaklik=sorgu["main"]["temp"]
    hissedilenSic=sorgu["main"]["feels_like"]
    minSicaklik=sorgu["main"]["temp_min"]
    maxSicaklik=sorgu["main"]["temp_max"]
    basinc=sorgu["main"]["pressure"]
    nem=sorgu["main"]["humidity"]
    
    print("{} için Hava Durumu Bilgileri Aşağıdaki Gibidir\n\n".format(sehir.capitalize()))
    print("Sıcaklık:{} derece\nDurum:{}\nHissedilen Sıcaklık:{} derece\nEn Düşük Sıcaklık:{} derece\nEn Yüksek Sıcaklık:{} derece\nBasınç:{}\nNem:{} %\n"
          .format(havasicaklik,havaDurumu,hissedilenSic,minSicaklik,maxSicaklik,basinc,nem))