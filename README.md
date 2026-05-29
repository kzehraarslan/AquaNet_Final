# AquaNet

**Türkiye İç Göllerinde Derin Öğrenme ile Yüzey Suyu Değişimi Tespiti, Çevresel Etki Analizi ve Kuraklık Tahmini**

Bu depo, Derin Öğrenme final projesi kapsamında geliştirilen AquaNet çalışmasının teslim paketidir. Proje; Türkiye'deki dört pilot iç gölde yüzey suyu değişimini izlemek, çevresel değişkenlerin göreli etkilerini analiz etmek ve 2035/2040/2050 dönemleri için kuraklık senaryoları üretmek amacıyla hazırlanmıştır.

## Çalışma Alanları

- Tuz Gölü
- Burdur Gölü
- Beyşehir Gölü
- Salda Gölü

## Modüller

1. **Modül 1 — Yüzey Suyu Segmentasyonu**  
   EfficientNet-B4 kodlayıcı ve U-Net tabanlı segmentasyon yapısı kullanılmıştır. NDWI tabanlı su maskeleri referans çıktı olarak değerlendirilmiştir.

2. **Modül 2 — Çevresel Değişken Analizi**  
   Sıcaklık, yağış, evapotranspirasyon, nem ve su dengesi değişkenlerinin su yüzey alanı üzerindeki göreli etkileri Cross-Attention yaklaşımıyla analiz edilmiştir.

3. **Modül 3 — Kuraklık Senaryo Tahmini**  
   BiLSTM tabanlı zaman serisi modeli ile mevcut trend, RCP 4.5 benzeri ve RCP 8.5 benzeri senaryolar altında 2035, 2040 ve 2050 tahminleri üretilmiştir.

## Klasör Yapısı

```text
AquaNet_Final_Teslim_Paketi/
├── notebooks/                 # Ana notebook
├── src/                       # Yardımcı Python modülleri
├── scripts/                   # Kontrol ve özet tablo üretim scriptleri
├── config/                    # Örnek proje konfigürasyonu
├── data/
│   ├── processed/             # Teslim edilen CSV veri çıktıları
│   └── external/              # Ham/veri kaynağı notları
├── outputs/
│   ├── figures/               # Makale ve deney görselleri
│   ├── maps/                  # Folium HTML harita çıktısı
│   └── metrics/               # JSON/NPY metrik çıktıları
├── docs/                      # Final makale PDF'i ve öneri raporu
├── models/                    # Büyük model ağırlıkları için ayrılmış klasör
└── archive/                   # İlk ham notebook kaydı
```

## Hızlı Başlangıç

Paket içeriğini kontrol etmek için:

```bash
pip install -r requirements.txt
python scripts/quick_validate_outputs.py
```

Özet tabloları yeniden üretmek için:

```bash
python scripts/make_summary_tables.py
```

Ana deney akışı için:

```bash
jupyter notebook notebooks/AquaNet_Main.ipynb
```

## Teslim Notu

Ham uydu görüntüleri büyük boyutlu olduğu için ZIP paketine eklenmemiştir. Notebook, Microsoft Planetary Computer ve NASA POWER kaynaklarından veriyi yeniden çekebilecek şekilde düzenlenmiştir. Teslim paketinde nihai CSV/JSON sonuçları, görseller, interaktif harita çıktısı ve final makale PDF'i bulunmaktadır.

## Öne Çıkan Sonuçlar

- Burdur Gölü segmentasyon IoU: 0,989
- Beyşehir Gölü segmentasyon IoU: 0,959
- Salda Gölü segmentasyon IoU: 0,984
- Tuz Gölü 2024 segmentasyon IoU: 0,036
- RCP 8.5 senaryosunda 2050 tahmini kayıp:
  - Tuz Gölü: yaklaşık %30,98
  - Burdur Gölü: yaklaşık %34,35

## Yazar

Kamile Zehra ARSLAN  
Kahramanmaraş Sütçü İmam Üniversitesi, Bilgisayar Mühendisliği Bölümü  
ORCID: 0009-0000-2079-0124
