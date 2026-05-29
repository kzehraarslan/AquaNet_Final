"""Quick integrity check for the AquaNet delivery package.

Run from the repository root:
    python scripts/quick_validate_outputs.py
"""

from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    "notebooks/AquaNet_Main.ipynb",
    "data/processed/yillik_su_alanlari.csv",
    "data/processed/iklim_verisi.csv",
    "data/processed/iklim_su_birlesik.csv",
    "outputs/metrics/modul1_test_metrics.json",
    "outputs/metrics/modul2_sonuclar.json",
    "outputs/metrics/modul3_tahminler.json",
    "outputs/figures/modul1_tahminler.png",
    "outputs/figures/zaman_serisi_4gol.png",
    "outputs/figures/modul3_tahmin_2050.png",
    "outputs/maps/aquanet_interaktif_harita.html",
    "docs/AQUANET_Proje_Makalesi.pdf",
]


def main():
    print("AquaNet teslim paketi kontrolü")
    missing = []
    for rel in REQUIRED_FILES:
        path = ROOT / rel
        status = "OK" if path.exists() else "MISSING"
        print(f"[{status}] {rel}")
        if not path.exists():
            missing.append(rel)

    if missing:
        raise SystemExit(f"Eksik dosya sayısı: {len(missing)}")

    water = pd.read_csv(ROOT / "data/processed/yillik_su_alanlari.csv")
    print(f"Yıllık su alanı kaydı: {len(water)} satır")

    with open(ROOT / "outputs/metrics/modul1_test_metrics.json", encoding="utf-8") as f:
        metrics = json.load(f)
    print("Modül 1 test gölleri:", ", ".join(metrics.keys()))
    print("Kontrol tamamlandı.")


if __name__ == "__main__":
    main()
