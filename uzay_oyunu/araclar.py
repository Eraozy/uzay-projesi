import time
from functools import wraps

def hamle_sayaci():
    """Her çağrıldığında sayacı 1 artıran bir closure fonksiyonu döndürür."""
    sayac = 0
    def say():
        nonlocal sayac
        sayac += 1
        return sayac
    return say

def en_bagli_gezegenler(galaksi: dict) -> list[str]:
    """Gezegenleri bağlantı sayısına göre azalan, eşitlikte alfabetik sırayla döndürür."""
    baglantilar = galaksi.get("baglantilar", {})
    # Bağlantı sayısına göre azalan (-len), isime göre alfabetik (gezegen adı) sıralama
    return sorted(galaksi.get("gezegenler", []), key=lambda g: (-len(baglantilar.get(g, [])), g))

def sure_olc(fonksiyon):
    """Bonus: Verilen fonksiyonun çalışma süresini ölçen sarmalayıcı."""
    @wraps(fonksiyon)
    def sarmalayici(*args, **kwargs):
        baslangic = time.time()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.time()
        print(f"[{fonksiyon.__name__}] Çalışma süresi: {bitis - baslangic:.6f} saniye")
        return sonuc
    return sarmalayici