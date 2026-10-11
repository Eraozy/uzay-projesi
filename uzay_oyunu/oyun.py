import json
from uzay_oyunu.galaksi import galaksi_kur
from uzay_oyunu.araclar import hamle_sayaci, en_bagli_gezegenler

def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """Envanterdeki eşyaların durumuna göre metin döndürür."""
    parcalar = []
    if credits:
        parcalar.append("bol kredi")
    if engines:
        parcalar.append("guclu motor")
    if copilot:
        parcalar.append("yetenekli bir pilot")
    
    if not parcalar:
        return ""
    return "Sende: " + ", ".join(parcalar)


def hedef_menusu(hedefler: list[str]) -> str:
    """Verilen hedef listesini numaralandırılmış menü metni olarak döndürür."""
    menu = "Nereye gitmek istersin?\n"
    for i, hedef in enumerate(hedefler, start=1):
        menu += f"[{i}] {hedef}\n"
    return menu.strip()

# JSON dosyasından verileri okuyup galaksiyi kuralım
with open("uzay_oyunu/galaksi.json", "r", encoding="utf-8") as f:
    veri = json.load(f)

g = galaksi_kur(**veri)

# Hamle sayacını başlatıyoruz (Closure)
hamle_artir = hamle_sayaci()

def travel(g: dict) -> None:
    """Gezegenler arası seyahat fonksiyonu, bağlantıları galaksi sözlüğünden alır."""
    # Her yolculukta/hamlede sayacı bir artırıyoruz
    toplam_hamle = hamle_artir()
    
    current_planet = g["konum"]
    destinations = g["baglantilar"].get(current_planet, [])
    
    # Eğer gidilecek yer kalmadıysa oyun biter
    if not destinations:
        print(f"Oyunu {toplam_hamle} hamlede bitirdin!")