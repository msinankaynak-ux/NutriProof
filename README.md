# NutriProof
Scientific Supplement Analysis &amp; Biopharmaceutical Data Ecosystem.
# NutriProof: Global Supplement Intelligence & Regulatory Ecosystem

NutriProof, gıda takviyelerini biyofarmasötik kriterler (BCS/SPIP), klinik kanıtlar ve uluslararası kalite standartları (USP/FDA) çerçevesinde analiz eden akademik tabanlı bir dijital otorite platformudur.

## 🔬 Bilimsel Temel (Scientific Core)
Projenin merkezinde, takviye içeriklerinin emilim ve etkinlik profillerini belirleyen iki ana parametre bulunur:
- **BCS (Biopharmaceutics Classification System):** İçeriklerin çözünürlük ve geçirgenlik sınıflandırması.
- **SPIP (Single Pass Intestinal Permeability):** Bağırsak geçirgenlik katsayıları üzerinden biyoyararlanım tahmini.

## 🛠️ Modüller ve Özellikler

### 1. Tüketici Modülü (ProofCheck)
- **Kamera & Barkod:** Ürün barkodunu tarayarak anlık analiz sunar.
- **Kişiselleştirilmiş Uyarı:** Kullanıcının sağlık profili ve kullandığı ilaçlar (Rx) ile takviye etkileşimlerini denetler.
- **ProofScore:** Biyoyararlanım teknolojilerine (Fitosom, Lipozomal, Time-Release vb.) göre hesaplanan kalite puanı.

### 2. Üretici Portalı (NutriProof Gold)
- **Verified Data:** Üreticilerin kendi analiz sertifikalarını (CoA) ve yüksek çözünürlüklü görsellerini yükleyebileceği ücretsiz arayüz.
- **Transparency Dashboard:** Ürünlerin kalite skorlarını iyileştirmek için üreticilere sunulan akademik geri bildirim paneli.

### 3. Veri Kazıma (Scraper) Stratejisi
- **Birincil Kaynak:** Orijinal Marka Web Siteleri (Nutraxin, Orzax, New Life vb.).
- **İkincil Kaynak:** Vitaminler.com (Barkod ve görsel eşleşmesi için).
- **Akademik Kaynak:** Examine.com & ClinicalTrials.gov.

## 🎨 Görsel Kimlik (UI/UX)
- **Tema:** Digital Laboratory / High-Contrast
- **Renk Paleti:** - Arka Plan: `#0A1628` (Derin Gece Mavisi)
  - Vurgu: `#FFBF00` (Gold / Amber Sarısı)

## 📁 Proje Klasör Yapısı
```text
NutriProof/
├── scrapers/            # Marka bazlı Python veri kazıma botları
├── data/                # Ham ve işlenmiş JSON/CSV veritabanı
├── backend/             # Analitik motor ve API katmanı
├── frontend/            # React/Next.js tabanlı kullanıcı arayüzü
└── docs/                # Akademik makaleler, BCS ve SPIP tabloları
