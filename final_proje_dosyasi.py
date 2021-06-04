#Algoritma II Proje Ödevi
#Kişisel Yapılacaklar Listesi Programı
#Edip Güvenç ÇEKİÇ
import sys,os,time
import sqlite3 as sql

########################### Genel Fonksiyonlar ##############################################
def sayfa_temizle():
    os.system('cls')

def bekle():
    bekle=input("Devam etmek için bir tuşa basınız.")
########################## Kullanıcı İşlemi Fonksiyonlar ####################################
def kullanıcı_vt():
    vt = sql.connect('user.sqlite3')
    im = vt.cursor()
    im.execute("""CREATE TABLE IF NOT EXISTS user (ad,sifre)""")
    vt.commit()
    vt.close()

def search_user(name):
    vt = sql.connect('user.sqlite3')
    im = vt.cursor()
    im.execute("""SELECT * FROM user""")
    veriler = im.fetchall()
    vt.close()
    for i in range(len(veriler)):
        if veriler[i][0] == name:
            return True
    return False

def parola_sorgula(s_ad,parola_s):
    vt = sql.connect('user.sqlite3')
    im = vt.cursor()
    im.execute("""SELECT * FROM user WHERE ad = '{}'""".format(s_ad, parola_s))
    veriler = im.fetchall()
    vt.close()
    for i in range(len(veriler)):
        if veriler[i][1] == parola_s:
            return True
    return False

def kayıt_sil(ad):
    vt = sql.connect('user.sqlite3')
    im = vt.cursor()
    im.execute("""DELETE FROM user WHERE ad = '{}'""".format(ad))
    vt.commit()
    vt.close()

def parola_düzenle(ad, parola):
    vt = sql.connect('user.sqlite3')
    im = vt.cursor()
    im.execute("""UPDATE user SET sifre = '{}' WHERE ad = '{}'""".format(parola, ad))
    vt.commit()
    vt.close()

def c_user(ad_t,sifre_t):
    vt = sql.connect('user.sqlite3')
    im = vt.cursor()
    im.execute("""INSERT INTO user VALUES ('{}','{}')""".format(ad_t,sifre_t))
    vt.commit()
    vt.close()
    print("Yeni kayıt oluşturuldu.")

def l_user():
    vt = sql.connect('user.sqlite3')
    im = vt.cursor()
    im.execute("""SELECT * FROM user""")
    veriler = im.fetchall()
    vt.close()
    print("Kullanıcılar:")
    for i in range(len(veriler)):
        print("{}.".format(i+1) + veriler[i][0])
########################## Yapılacak Listesi Fonksiyonları ####################################
def kayıtlar_vt():
    vt2 = sql.connect('kayitlar.sqlite3')
    im = vt2.cursor()
    im.execute("""CREATE TABLE IF NOT EXISTS kayitlar (Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,ad,kayıt_e,tarih,yapıldı)""")
    vt2.commit()
    vt2.close()

def olustur(ad, kayit, tarih):
    vt2 = sql.connect('kayitlar.sqlite3')
    im = vt2.cursor()
    im.execute("""INSERT INTO kayitlar (ad, kayıt_e,tarih,yapıldı) VALUES('{}','{}','{}','F')""".format(ad,kayit,tarih))
    vt2.commit()
    vt2.close()
    print("Yeni kayıt oluşturuldu.")
def kayit_listele(ad_s):
    vt2 = sql.connect('kayitlar.sqlite3')
    im = vt2.cursor()
    im.execute("""SELECT * FROM kayitlar WHERE ad = '{}'""".format(ad_s))
    veriler = im.fetchall()
    vt2.close()
    print("Kayıtlar: ")
    for i in range(len(veriler)):
        if veriler[i][4] == "F":
           durum = "YAPILMADI"
        else:
            durum = "yapıldı"
        print("Sıra \t\t\t:"+ str((i+1)))
        print("Yapılacak listesi \t:"+veriler[i][2]) 
        print("Tarih \t\t\t:" +veriler[i][3])
        print("Durum \t\t\t:"+durum)
        print("")

def id_sec(ad_s,sira):
    sira = int(sira)
    vt2 = sql.connect('kayitlar.sqlite3')
    im = vt2.cursor()
    im.execute("""SELECT * FROM kayitlar WHERE ad = '{}'""".format(ad_s))
    veriler = im.fetchall()
    vt2.close()
    return veriler[sira-1][0]

def kayitlar_sil(ad):
    vt2 = sql.connect('kayitlar.sqlite3')
    im = vt2.cursor()
    im.execute("""DELETE FROM kayitlar WHERE ad = '{}'""".format(ad))
    vt2.commit()
    vt2.close()

def kayitlar_düzenle(sira_i, kayit_d):
    vt2 = sql.connect('kayitlar.sqlite3')
    im = vt2.cursor()
    #im.execute("""SELECT * FROM kayitlar""")
    im.execute("""UPDATE kayitlar SET kayıt_e = '{}' WHERE Id = {}""".format(kayit_d, sira_i))
    vt2.commit()
    vt2.close()

def kayitlar_sil(sira_i):
    vt2 = sql.connect('kayitlar.sqlite3')
    im = vt2.cursor()
    #im.execute("""SELECT * FROM kayitlar""")
    im.execute("""DELETE FROM kayitlar WHERE Id = {}""".format(sira_i))
    vt2.commit()
    vt2.close()

def kayıtlar_menu(ad):
    sayfa_temizle()
    print("""{} Hoşgeldiniz.
    Yapılacaklar Listesi: """.format(ad))
    print("""
Kayıtları görüntülemek için     1'e basınız.
Kayıt eklemek için              2'e basınız.
Kayıt silmek için               3'e basınız.
Kayıt güncellemek için          4'e basınız.
Çıkış için                      (q)'ya basınız. """)

#####################Akış Bölümü

print("Yapılacaklar listesi programı")
kullanıcı_vt()
sor1 = "a"
while sor1 != 'q':
    sor1 = input(""" 
 ---------  Kullanıcı İşlemleri-----------------------------
 |  Yeni Kullanıcı Oluşturmak için          1'e basınız,   |
 |  Kayıtlı Kullanıcıları listelemek için   2'ye basınız,  |
 |  Kullanıcı silmek için                   3'e basınız    |
 |  Kullanıcı şifresini değiştirmek için    4'e basınız    |
 |  Kullanıcı kayıtları için                (y)'e basınız. |
 |  Çıkış için                              (q)'ya basınız.|
 |---------------------------------------------------------|
                        """)   
    if sor1 == "1":
        sayfa_temizle()
        user_name = input("Kullanıcı adı giriniz: ")
        if search_user(user_name) == False:
            sifre_gir = input("Şifre oluşturunuz: ")
            c_user(user_name,sifre_gir)
            print("Kullanıcı oluşturuldu.")
            bekle()
            sayfa_temizle()
        else:
            print("""Böyle bir kayıt var. Lütfen başka bir kullanıcı adı giriniz.""")
            bekle()
            sayfa_temizle()
    elif sor1 == "2":
        l_user()
        bekle()
        sayfa_temizle()
    elif sor1 == "3":
        l_user()
        silkayıt = input("Silinecek kullanıcının adını giriniz: ")
        if search_user(silkayıt) == True:
            sifresor = input("Silmek istediğiniz kullancının parolasını giriniz: ")
            if parola_sorgula(silkayıt, sifresor) == True:
                kayıt_sil(silkayıt)
                print("Kayıt silindi.")
                bekle()
                sayfa_temizle()
            else:
                print("Girdiğiniz parola yanlış. Kayıt silinemedi.")
                bekle()
                sayfa_temizle()
        else:
            print("Böyle bir kullanıcı yok.")
            bekle()
            sayfa_temizle()
    elif sor1 == "4":
        l_user()
        düz_parola = input("Parolasını yenilemek istediğiniz kaydı giriniz: ")
        if search_user(düz_parola) == True:
            sifresor = input("Eski parolayı giriniz: ")
            if parola_sorgula(düz_parola,sifresor) == True:
                yeni_parola = input("Yeni parolayı giriniz: ")
                parola_düzenle(düz_parola, yeni_parola)
                print("Yeni parola oluşturuldu.")
                bekle()
                sayfa_temizle()
            else:
                print("Girdiğiniz parola yanlış. Kayıt silinemedi.")
                bekle()
                sayfa_temizle()
        elif search_user(düz_parola) == False:
            print("Böyle bir kullanıcı yok.")
            bekle()
            sayfa_temizle()
    elif sor1 == "q":
        print("Programdan çıkılıyor")
        break
    elif sor1 == "y":
        l_user()
        listesec = 'a'
        kullanıcı = input("Yapılacak listesini görebilmek için\nKullanıcı adını seçiniz: ")
        if search_user(kullanıcı) == True:
            sifresor = input("Parola giriniz: ")
            if parola_sorgula(kullanıcı,sifresor) == True:
                kayıtlar_vt()
                while True:
                    kayıtlar_menu(kullanıcı)
                    listesec = input(" ")
                    if listesec == "1":
                        print("kayıt listele")
                        kayit_listele(kullanıcı)
                        bekle()
                        sayfa_temizle()
                    elif listesec == "2":
                        kayıt_ek = input("Yapılacak listesine kayıt ekleyiniz: ")
                        tarih = time.strftime('%c')
                        olustur(kullanıcı, kayıt_ek, tarih)
                        print("Yeni kayıt oluştu.")
                        listesec = 'a'
                        bekle()
                        sayfa_temizle()
                    elif listesec == "3":
                        print("kayıt sil")
                        kayit_listele(kullanıcı)
                        kayit_sec_sil = input("Silinmesini istediğiniz kaydın sıra numarasını giriniz: ")
                        sil_kayit = id_sec(kullanıcı,kayit_sec_sil)
                        kayitlar_sil(sil_kayit)
                        bekle()
                        sayfa_temizle()
                    elif listesec == "4":
                        kayit_listele(kullanıcı)
                        kayit_sec = input("Güncellenmesini istediğiniz kaydın sıra numarasını giriniz: ")
                        degis = id_sec(kullanıcı,kayit_sec)
                        düzen_kayit=input("Yeni kaydı giriniz: ")
                        kayitlar_düzenle(degis, düzen_kayit)
                        bekle()
                        sayfa_temizle()
                    elif listesec == "q":
                        print("Programdan çıkılıyor")
                        bekle()
                        sor1 = 'q'
                        break
            else:
                print("Girdiğiniz parola yanlış.")
                bekle()
                sayfa_temizle()
        else:
            print("Böyle bir kullanıcı yok.")
            bekle()
            sayfa_temizle()