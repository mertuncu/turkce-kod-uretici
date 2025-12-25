import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# .env dosyasından API anahtarını yükle
load_dotenv()

# OpenAI client oluştur
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Sayfa yapılandırması
st.set_page_config(
    page_title="Türkçe Kod Üretici",
    page_icon="💻",
    layout="wide"
)

# Başlık
st.title("💻 Türkçe Kod Üretici ve Açıklayıcı")
st.markdown("Türkçe probleminizi yazın, Python kodu üretelim!")

# Sidebar - Örnek problemler
with st.sidebar:
    st.header("📚 Örnek Problemler")
    st.markdown("""
    - Bir listedeki çift sayıları bulan fonksiyon
    - İki sayının EBOB'unu bulan kod
    - Fibonacci serisinin ilk 10 terimi
    - Bir metindeki sesli harfleri sayan program
    - Liste içindeki en büyük sayıyı bulan fonksiyon
    """)

    st.markdown("---")
    st.markdown("### ℹ️ Nasıl Çalışır?")
    st.markdown("""
    1. Probleminizi Türkçe yazın
    2. 'Kod Üret' butonuna basın
    3. AI sizin için Python kodu üretir
    4. Kodun açıklamasını görün
    """)

# Ana alan
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 Problem Tanımı")
    problem = st.text_area(
        "Probleminizi Türkçe olarak yazın:",
        height=200,
        placeholder="Örnek: Bir listedeki çift sayıları bulan bir Python fonksiyonu yaz"
    )

    if st.button("🚀 Kod Üret", type="primary", use_container_width=True):
        if not problem.strip():
            st.error("⚠️ Lütfen bir problem tanımı girin!")
        else:
            with st.spinner("🤖 Kod üretiliyor..."):
                try:
                    # OpenAI API çağrısı
                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[
                            {
                                "role": "system",
                                "content": "Sen bir Python programlama uzmanısın. Kullanıcının Türkçe olarak verdiği problemi anlayıp Python kodu üret. Kodu açıklama ile birlikte ver."
                            },
                            {
                                "role": "user",
                                "content": f"Şu problemi çözen Python kodu yaz ve kodun ne yaptığını satır satır Türkçe açıkla:\n\n{problem}"
                            }
                        ],
                        temperature=0.7,
                        max_tokens=1500
                    )

                    # Yanıtı al
                    ai_response = response.choices[0].message.content

                    # Session state'e kaydet
                    st.session_state['generated_code'] = ai_response
                    st.session_state['problem'] = problem

                    st.success("✅ Kod başarıyla üretildi!")

                except Exception as e:
                    st.error(f"❌ Hata oluştu: {str(e)}")
                    st.info("💡 API anahtarınızı kontrol edin ve kredi ekleyin.")

with col2:
    st.subheader("💻 Üretilen Kod ve Açıklama")

    if 'generated_code' in st.session_state:
        st.markdown(st.session_state['generated_code'])

        # Kopyalama butonu
        st.download_button(
            label="📥 Kodu İndir",
            data=st.session_state['generated_code'],
            file_name="uretilen_kod.txt",
            mime="text/plain"
        )
    else:
        st.info("👈 Sol taraftan bir problem girin ve 'Kod Üret' butonuna basın")

# Alt bilgi
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <small>🎓 Mühendislikte Bilgisayar Uygulamaları Projesi | Powered by OpenAI GPT-4</small>
</div>
""", unsafe_allow_html=True)
