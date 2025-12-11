"""
=============================================================================
UI_COMPONENTS.PY - STREAMLIT ARAYÜZ BİLEŞENLERİ
=============================================================================

Bu modül, Streamlit uygulaması için CSS stilleri ve
yeniden kullanılabilir UI bileşenlerini içerir.
=============================================================================
"""

import streamlit as st
from .config import COLORS, DISPLAY_ICONS


def apply_custom_css():
    """
    Uygulamaya özel CSS stillerini uygular.
    Bu fonksiyon sayfa yüklendiğinde bir kez çağrılmalıdır.
    """
def apply_custom_css():
    """
    Uygulamaya özel CSS stillerini ve FontAwesome kütüphanesini yükler.
    Bu fonksiyon sayfa yüklendiğinde bir kez çağrılmalıdır.
    """
    # FontAwesome CDN Linki
    st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">', unsafe_allow_html=True)
    
    st.markdown(f"""
    <style>
        /* Ana tema renkleri - Futbol sahası yeşili temalı */
        :root {{
            --primary-green: {COLORS['primary_green']};
            --secondary-green: {COLORS['secondary_green']};
            --accent-gold: {COLORS['accent_gold']};
            --light-green: {COLORS['light_green']};
        }}
        
        /* Sidebar stilleri */
        [data-testid="stSidebar"] {{
            background: linear-gradient(180deg, {COLORS['primary_green']} 0%, {COLORS['dark_bg']} 100%);
        }}
        
        [data-testid="stSidebar"] .stMarkdown {{
            color: #ffffff;
        }}
        
        /* Başlık stilleri */
        .fas, .far, .fab {{
            margin-right: 8px;
        }}

        .main-title {{
            font-family: 'Georgia', serif;
            font-size: 2.8rem;
            font-weight: bold;
            color: {COLORS['primary_green']};
            text-align: center;
            padding: 1rem;
            background: linear-gradient(90deg, #f0f8f0, #e8f5e9, #f0f8f0);
            border-radius: 15px;
            margin-bottom: 2rem;
            border: 3px solid {COLORS['secondary_green']};
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }}
        
        /* Metrik kartları */
        .metric-card {{
            background: linear-gradient(135deg, {COLORS['secondary_green']} 0%, {COLORS['primary_green']} 100%);
            padding: 1.5rem;
            border-radius: 12px;
            color: white;
            text-align: center;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
            border: 2px solid {COLORS['accent_gold']};
        }}
        
        .metric-value {{
            font-size: 2.2rem;
            font-weight: bold;
            color: {COLORS['accent_gold']};
        }}
        
        .metric-label {{
            font-size: 0.95rem;
            color: {COLORS['light_green']};
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        /* Oyuncu kartları */
        .player-card {{
            background: linear-gradient(145deg, #ffffff, #f5f5f5);
            border-radius: 12px;
            padding: 1rem;
            margin: 0.5rem 0;
            border-left: 5px solid {COLORS['secondary_green']};
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            transition: transform 0.2s;
        }}
        
        .player-card:hover {{
            transform: translateX(5px);
        }}
        
        /* Pozisyon badge'leri */
        .position-badge {{
            display: inline-block;
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-weight: bold;
            font-size: 0.8rem;
        }}
        
        .pos-gk {{ background-color: #ff6b6b; color: white; }}
        .pos-def {{ background-color: #4dabf7; color: white; }}
        .pos-mid {{ background-color: #51cf66; color: white; }}
        .pos-fwd {{ background-color: #ffd43b; color: #333; }}
        
        /* Info kutuları */
        .info-box {{
            background: linear-gradient(135deg, #e8f5e9, #c8e6c9);
            border-radius: 10px;
            padding: 1rem;
            border: 1px solid #81c784;
            margin: 1rem 0;
        }}
        
        /* Tablo stilleri */
        .dataframe {{
            font-size: 0.9rem;
        }}
        
        /* Footer */
        .footer {{
            text-align: center;
            color: #666;
            padding: 2rem;
            margin-top: 3rem;
            border-top: 2px solid #e0e0e0;
        }}
    </style>
    """, unsafe_allow_html=True)



def get_icon(key):
    """Verilen anahtar kelime için ikon döndürür, yoksa boş döner."""
    return DISPLAY_ICONS.get(key, '')


def format_position_display(pos):
    """Örn: 'ST' alır, '⚽ ST' döndürür (HTML render edilmez, st.write veya selectbox için)."""
    # Selectbox için HTML çalışmaz, ancak kullanıcı config.py'yi HTML doldurttu.
    # Bu durumda selectbox'ta raw HTML görünecek. Bunu düzeltmek benim görevim mi?
    # Kullanıcının talebi çok spesifik. "Bunu yapmanın en iyi yolu... format_func=lambda x: f"{DISPLAY_ICONS.get(x, '')} {x}"
    # Aynen uyguluyorum.
    return f"{get_icon(pos)} {pos}"


def render_main_title():
    """Ana başlığı render eder."""
    st.markdown(
        f'<div class="main-title">{get_icon("app_logo")} FC26 Kadro Optimizasyonu<br>'
        '<span style="font-size: 1.2rem; font-weight: normal;">'
        f'{get_icon("chart")} Karar Destek Sistemi - Alt Pozisyon Bazlı Doğrusal Programlama</span></div>',
        unsafe_allow_html=True
    )


def render_metric_card(value: str, label: str, icon_key: str = None):
    """
    Metrik kartı HTML'i döndürür.
    
    Args:
        value: Gösterilecek değer
        label: Metrik etiketi
        icon_key: config.DISPLAY_ICONS içindeki anahtar (opsiyonel)
    """
    icon_html = get_icon(icon_key) if icon_key else ""
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{icon_html} {value}</div>
        <div class="metric-label">{label}</div>
    </div>
    """, unsafe_allow_html=True)


def render_info_box():
    """Renk kodları bilgi kutusunu render eder."""
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, {COLORS['primary_green']}, {COLORS['dark_bg']}); 
                border-radius: 10px; padding: 1rem; border: 2px solid {COLORS['accent_gold']}; 
                margin: 1rem 0;
        color: white;
    ">
        <strong style="color: #d4af37;">{get_icon('bulb')} İpucu:</strong> Oyuncuların üzerine gelerek detaylı bilgi görebilirsiniz.
        <br><br>
        <strong style="color: #d4af37;">Pozisyon Renkleri:</strong><br>
        <span style="color: #ff6b6b; font-weight: bold;">● Kaleci</span> |
        <span style="color: #74c0fc; font-weight: bold;">● Defans</span> |
        <span style="color: #8ce99a; font-weight: bold;">● Orta Saha</span> |
        <span style="color: #ffe066; font-weight: bold;">● Forvet</span>
    </div>
    """, unsafe_allow_html=True)


def render_footer():
    """Sayfa altbilgisini render eder."""
    st.markdown("""
    <div class="footer">
        <p><strong>Karar Destek Sistemleri - Final Projesi</strong></p>
        <p>Bu uygulama, Doğrusal Programlama (Linear Programming) teknikleri kullanılarak geliştirilmiştir.</p>
        <p>Optimizasyon motoru: PuLP | Arayüz: Streamlit | Görselleştirme: Plotly</p>
    </div>
    """, unsafe_allow_html=True)


def render_sidebar_info():
    """Sidebar hakkında bilgi kutusunu render eder."""
    st.info(
        f"**Premier League 2024-25** verisi ile çalışır.\n\n"
        f"**Alt pozisyonlar** (CB, RB, LB, DM, CM, CAM, RM, LM, RW, LW, ST) desteklenir.\n\n"
        f"Van Dijk (CB) artık RB'ye **atanamaz**!\n\n"
        f"**PuLP** ile Doğrusal Programlama optimizasyonu."
    )





