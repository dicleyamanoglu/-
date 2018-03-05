x=int(input("Finansman gelirini giriniz."))
y=int(input("Pazar gelirini giriniz."))
z=int(input("Kira gelirini giriniz."))
a=int(input("Ücreti giriniz."))
b=int(input("finansman giderini giriniz."))
c=int(input("Kira giderini giriniz."))
d=int(input("Muhasebe gideriniz giriniz."))
toplamGelir=(x+y+z)
toplamGider=(a+b+c+d)
kar=toplamGelir-toplamGider
if kar>1000:
    print("Şirketiniz karlı.")
else:
    print("Şirketiniz zararda.")


def kul(x,y,z):
    kullanilabilirlik=(x-y)/z
    return kullanilabilirlik

def perf(a,b,x,y):
    performans=(a*b)/(x-y)
    return performans

def kal(e,f):
    kalite=e/f
    return kalite

def oeeHesapla(x,y,z,a,b,e,f):
    oee=kul(x,y,z)*perf(a,b,x,y)*kal(e,f)
    print("%",oee)



def ciroHesapla(x,y):
    ciro=x*y
    return ciro
toplamCalisan=25
def adambasiCiro(x,y,toplamCalisan):
    adambasi=ciroHesapla(x,y)/toplamCalisan
    return adambasi
