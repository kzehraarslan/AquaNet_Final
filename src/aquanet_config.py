"""Central configuration for AquaNet.

This file keeps lake metadata and commonly used feature names in one place so
notebook cells and scripts remain readable.
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"
FIGURES_DIR = OUTPUTS_DIR / "figures"
METRICS_DIR = OUTPUTS_DIR / "metrics"
MAPS_DIR = OUTPUTS_DIR / "maps"

LAKES = {
    "tuz": {"name": "Tuz Gölü", "color": "#d62728"},
    "burdur": {"name": "Burdur Gölü", "color": "#1f77b4"},
    "beysehir": {"name": "Beyşehir Gölü", "color": "#2ca02c"},
    "salda": {"name": "Salda Gölü", "color": "#9467bd"},
}

CLIMATE_FEATURES = [
    "sicaklik_ort",
    "yagis_toplam",
    "evapotrans_toplam",
    "nem_ort",
    "su_dengesi",
]
