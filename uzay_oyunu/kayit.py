def gorev_kaydi(baslik: str, *adimlar: str, oncelik: str = "normal", **ekler: str) -> str:
    """Görev başlığını, adımlarını, önceliğini ve ek bilgileri biçimlendirerek döndürür."""
    # Önceliği büyük harfe çevirelim (örn: YÜKSEK)
    sonuc = [f"[{oncelik.upper()}] {baslik}"]
    
    # Adımları numaralandırarak ekleyelim
    for i, adim in enumerate(adimlar, 1):
        sonuc.append(f"{i}. {adim}")
        
    # Ek sözlük parametrelerini ekleyelim (örn: sorumlu: Ayşe)
    for anahtar, deger in ekler.items():
        sonuc.append(f"{anahtar}: {deger}")
        
    return "\n".join(sonuc)


if __name__ == "__main__":
    # Liste ve sözlük açarak (*) ve (**) test çağrıları
    liste_adimlar = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    sozluk_ekler = {"sorumlu": "Ayşe"}
    
    print(gorev_kaydi("Kara deliğe atla", *liste_adimlar, oncelik="yüksek", **sozluk_ekler))