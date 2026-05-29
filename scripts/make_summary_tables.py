"""Generate compact CSV summary tables from AquaNet JSON outputs.

Run from the repository root:
    python scripts/make_summary_tables.py
"""

from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
METRICS = ROOT / "outputs" / "metrics"
SUMMARY = ROOT / "outputs" / "summary_tables"
SUMMARY.mkdir(exist_ok=True)

lake_names = {
    "tuz": "Tuz Gölü",
    "burdur": "Burdur Gölü",
    "beysehir": "Beyşehir Gölü",
    "salda": "Salda Gölü",
}

with open(METRICS / "modul1_test_metrics.json", encoding="utf-8") as f:
    m1 = json.load(f)
rows = [
    {"Göl": lake_names[k], "Yıl": v["yil"], "IoU": v["iou"], "F1-score": v["f1"]}
    for k, v in m1.items()
]
pd.DataFrame(rows).to_csv(SUMMARY / "modul1_test_metrics_summary.csv", index=False)

with open(METRICS / "modul3_tahminler.json", encoding="utf-8") as f:
    m3 = json.load(f)
rows = []
for lake_key, scenarios in m3.items():
    rcp85 = scenarios["RCP 8.5 (+3.0°C)"]
    rows.append({
        "Göl": lake_names[lake_key],
        "2024 Su Alanı (km2)": rcp85["2024"],
        "2050 RCP 8.5 (km2)": rcp85["2050"],
        "Değişim (%)": rcp85["delta_2050_pct"],
    })
pd.DataFrame(rows).to_csv(SUMMARY / "modul3_rcp85_2050_summary.csv", index=False)

print(f"Summary tables written to: {SUMMARY}")
