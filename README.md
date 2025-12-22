df_raw = pd.read_csv("oyuncular.csv")
# ⚽ Premier League Kadro Optimizasyonu - Karar Destek Sistemi

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![PuLP](https://img.shields.io/badge/PuLP-2.7+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Tamamı Streamlit üzerinde çalışan bu uygulama, Premier League oyuncu verisi ile **binary integer programming** kullanarak optimal 11'i kurar, senaryo ve duyarlılık analizleri yapar, uyumluluk skorları üretir, Pareto sınırı çizer ve bench/yedek analizleri sunar. Bu doküman, uygulamayı ilk kez açan birinin tüm sekmeleri ve veri beklentilerini anlaması için hazırlandı.

## 🚀 Hızlı Başlangıç

```bash
# 1) Sanal ortam (önerilir)
python -m venv venv
venv\Scripts\activate   # Windows

# 2) Bağımlılıklar
pip install -r requirements.txt

# 3) Uygulamayı başlat
streamlit run main.py
```

Tarayıcıdan `http://localhost:8501` adresine gidin.

## 📂 Veri ve Yapı

- `data/playerstats_2025.csv`: Ana oyuncu istatistikleri (rating, ofans, defans, form, fiyat, sakatlık, alt pozisyon).
- `data/premier_league_players_tf.csv`: Pozisyon/flex bilgisini destekler (Alt_Pozisyon vs. Atanan_Pozisyon).
- `data/Player-positions.csv`: Ek pozisyon detayları.
- Kaynak kod: `src/` altındaki modüller (optimizer, visualizer, decision_analyzer, sensitivity_analyzer, alternative_solutions, explainability, compatibility, pareto_analysis, narrative_builder, bench_analyzer).

## 🧭 Arayüz Rehberi (Sekmeler)

**Kontrol Paneli (sol sidebar)**
- Takım seçimi: Veriyi kulüp bazında filtreler.
- Formasyon: 4-4-2, 4-3-3, 3-5-2, 5-3-2, 4-2-3-1, 3-4-3.
- Bütçe slider’ı: Maksimum toplam maliyet.
- Strateji: Dengeli, Ofansif, Defansif (ağırlık setlerini etkiler).

**Tab 1 – Optimal 11**
- LP çözümüyle seçilen ilk 11; saha yerleşimi (Plotly pitch) ve detaylı tablo.
- Kadro skorları ve metrik kartları.

**Tab 2 – Karar Destek Raporu**
- `decision_analyzer`: Ağırlıklı skor, risk uyarıları, seçilen/alternatif oyuncular, pozisyon bazlı özetler.

**Tab 3 – Tüm Kadro**
- Pozisyon filtreleri, sakatlık filtresi, sıralama; takımın tüm oyuncu havuzu.

**Tab 4 – Duyarlılık Analizi**
- `sensitivity_analyzer`: Tornado (parametre etki sıralaması) ve seçili parametre için yüzde değişim vs skor tablosu ve çizgi grafiği.

**Tab 5 – What-If Senaryoları**
- Bütçe değişimi, minimum rating seviyesi, formasyon değişikliği senaryoları (`alternative_solutions`).

**Tab 6 – Oyuncu Uyumluluğu**
- `compatibility`: Kimya/uyum skorları, pozisyon eşleşmeleri ve öneriler.

**Tab 7 – Pareto Analizi**
- `pareto_analysis`: Ofans/defans (veya maliyet) için Pareto frontier; grafik ve tablo.

**Tab 8 – Kadro Raporu (Narrative)**
- `narrative_builder`: Yönetici özeti, formasyon seçimi açıklaması, güçlü/zayıf yönler ve öneriler. Markdown indirme butonu.

**Tab 9 – Bench & Yedekler**
- `bench_analyzer`: Pozisyon başına yedekler, kadro derinliği, sakatlık senaryosu simülasyonu.

## 🔢 Optimizasyon Modeli (özet)

Karar değişkeni: $x_i \in \{0,1\}$ oyuncu i seçildiyse 1.

Amaç fonksiyonu (örnek):
$$\max \sum_i (w_{rating} r_i + w_{form} f_i + w_{off} o_i + w_{def} d_i - w_{cost} c_i) x_i$$

Ana kısıtlar:
- Pozisyona göre gerekli oyuncu sayıları (formasyon). 
- Toplam 11 oyuncu.
- Bütçe üst limiti.
- Sakat oyuncu seçilmez.
- Esnek pozisyonlar `config.POSITION_CAN_BE_FILLED_BY` ile kontrol edilir.

Solver: PuLP CBC (varsayılan).

## ⚙️ Konfigürasyon

- `src/config.py`: Formasyonlar, pozisyon esneklikleri, renkler, ikonlar, varsayılan ağırlıklar.
- `src/data_handler.py`: Veri yükleme ve normalizasyon.
- `src/optimizer.py`: PuLP modeli ve skor hesaplama.

## 📦 Bağımlılıklar

| Kütüphane | Versiyon | Not |
|-----------|----------|-----|
| streamlit | ≥1.28.0 | UI |
| pandas | ≥2.0.0 | Veri işleme |
| numpy | ≥1.24.0 | Sayısal işlemler |
| pulp | ≥2.7.0 | BIP çözücü |
| plotly | ≥5.18.0 | Grafik |

## 🛠️ Geliştirici Notları

- Yeni veri kaynağı eklerken `data_handler.py` içindeki kolon adlarıyla uyumlu hale getirin (Oyuncu_Adi/Oyuncu, Alt_Pozisyon, Fiyat_M, Form, Ofans_Gucu, Defans_Gucu, Sakatlik).
- Bench sekmesi isim kolonu fallback’i destekler (Oyuncu_Adi yoksa Oyuncu). 
- İkonlar HTML olarak `DISPLAY_ICONS` sözlüğünde; selectbox’larda ham HTML görünmemesi için `format_position_display` sade metin döndürür.

## 📄 Lisans

MIT Lisansı.

---

⚽ *"En iyi kadro, matematiksel olarak optimal olandır."*

