from uzay_oyunu.oyun import envanter_metni, hedef_menusu

def test_envanter_metni():
    # Eşyaların varlık durumunu test ediyoruz
    sonuc = envanter_metni(True, False, True)
    assert "bol kredi" in sonuc
    assert "yetenekli bir pilot" in sonuc

def test_hedef_menusu():
    hedefler = ["centauri", "sirius"]
    menusu = hedef_menusu(hedefler)
    assert "[1] centauri" in menusu
    assert "[2] sirius" in menusu