"""Utilities for loading AquaNet result artifacts."""

import json
from pathlib import Path
import pandas as pd
from .aquanet_config import DATA_DIR, METRICS_DIR


def load_yearly_water_area(path=None):
    path = Path(path) if path else DATA_DIR / "yillik_su_alanlari.csv"
    return pd.read_csv(path)


def load_climate_water_table(path=None):
    path = Path(path) if path else DATA_DIR / "iklim_su_birlesik.csv"
    return pd.read_csv(path)


def load_json_result(filename):
    with open(METRICS_DIR / filename, "r", encoding="utf-8") as f:
        return json.load(f)


def load_module1_metrics():
    return load_json_result("modul1_test_metrics.json")


def load_module2_results():
    return load_json_result("modul2_sonuclar.json")


def load_module3_predictions():
    return load_json_result("modul3_tahminler.json")
