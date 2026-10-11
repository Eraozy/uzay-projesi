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