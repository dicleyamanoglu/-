# soru1
satisM = 500
birimS = 20
ciro = 5000
i = 0
while (ciro <= 500000):
    ciro = ciro + (satisM * birimS)
    satisM = satisM + 200
    birimS = birimS + 10
    i = i + 1
print("500.000den fazla ciro", i, ".ayda tamamlanmıştır.")

# soru2
# x=2017 yılı stok miktarı
x = 10000
i = 0
while True:
    x = x - 500
    x = x + 100
    i = i + 1
    if (x == 0):
        print("Stokların sıfırlandığı ay:", i)
        break

#soru3
kalanlarToplam=0
while True:
    print("Bir sayı giriniz.Çıkmak için 0(Sıfır) giriniz.")
    sayi=int(input("Girilen sayı:"))
    if sayi!=0:
        kalan=sayi%3
        kalanlarToplam=kalan+kalanlarToplam
        print("Toplam:",kalanlarToplam)
    else:
        print("Çıkış yapıldı.")
        break

# soru4
calisan = 50
yevmiye = 90
haftalikMaas = 450
aylikMaas = 0
while True:
    haftalikMesai = int(input("Haftalık mesai saati:"))
    aylikMesai = haftalikMesai * 4
    haftalikMaas = haftalikMaas + (haftalikMesai * yevmiye * 0.10)
    aylikMaas = haftalikMaas * 4 + aylikMaas
    calisanToplamMaas = aylikMaas * calisan
    if aylikMesai <= 22:
        print("Ödenen toplam maaş:", calisanToplamMaas)
    else:
        print("Aylık çalışma sınırı aşıldı.")
    break

# soru5
gunlukUretim = 200
gunlukDefoluUrun = 0
toplamDefUrun = 0
i = 0
while (gunlukDefoluUrun <= gunlukUretim * 0.20):
    gunlukDefoluUrun = int(input("Günlük Defolu ürün miktarı:"))
    toplamDefUrun = toplamDefUrun + gunlukDefoluUrun
    i = i + 1
    if (gunlukDefoluUrun > gunlukUretim * 0.20):
        print("Defolu ürün sayısı limiti aşıldı.")
        break
    print(i, "Günlük Defolu ürün sayısı:", toplamDefUrun)
