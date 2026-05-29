# Veri Açıklaması

Bu klasörde ham uydu görüntülerinin tamamı yerine proje kapsamında üretilmiş işlenmiş veri tabloları bulunmaktadır.

## Dosyalar

- `processed/yillik_su_alanlari.csv`: 1984-2024 dönemi için pilot göllerin yıllık su yüzey alanı hesapları.
- `processed/iklim_verisi.csv`: NASA POWER tabanlı iklim değişkenleri.
- `processed/iklim_su_birlesik.csv`: İklim değişkenleri ile yıllık su alanı serilerinin birleştirilmiş tablosu.

## Ham Veri Kaynakları

Ham uydu verileri boyut nedeniyle pakete dahil edilmemiştir. Kullanılan kaynaklar:

- Landsat ve Sentinel-2 görüntüleri: Microsoft Planetary Computer üzerinden erişilmiştir.
- İklim verileri: NASA POWER servisinden alınmıştır.
- Su maskeleri: NDWI tabanlı eşikleme ile üretilmiştir.
