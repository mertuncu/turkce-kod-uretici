💻 Türkçe Kod Üretici ve Açıklayıcı
Yapay zeka destekli, Türkçe problem anlayan ve Python kodu üreten web uygulaması.
📖 Proje Hakkında
Bu proje, Python öğrenen öğrencilere ve geliştiricilere Türkçe dilinde destek sağlayan bir yapay zeka asistanıdır. Kullanıcılar Türkçe olarak problemlerini yazabilir, sistem otomatik olarak Python kodu üretir ve her satırı detaylı şekilde açıklar.
✨ Özellikler

🇹🇷 Türkçe Destek: Problemlerinizi kendi dilinizde yazın
🤖 AI Destekli: OpenAI GPT-4o-mini ile güçlendirilmiş
📝 Kod Açıklama: Her satır detaylı Türkçe açıklama
🌐 Web Arayüzü: Kullanıcı dostu, modern tasarım
📥 Kod İndirme: Üretilen kodu kolayca kaydedin
💡 Örnek Problemler: Hızlı başlangıç için hazır örnekler

🚀 Kurulum
Gereksinimler

Python 3.10 veya üzeri
OpenAI API anahtarı (buradan alın)

Adımlar

Projeyi klonlayın:

bashgit clone https://github.com/mertuncu/turkce-kod-uretici.git
cd turkce-kod-uretici

Gerekli paketleri yükleyin:

bashpip install -r requirements.txt

API anahtarınızı ayarlayın:

.env dosyası oluşturun ve içine ekleyin:
envOPENAI_API_KEY=sk-proj-your-api-key-here

Uygulamayı çalıştırın:

bashstreamlit run TurkceKodUretici.py
Tarayıcınızda http://localhost:8501 adresinde uygulama açılacak!
📚 Kullanım

Sol taraftaki Problem Tanımı alanına Türkçe probleminizi yazın
🚀 Kod Üret butonuna tıklayın
Sağ tarafta üretilen Python kodunu ve açıklamasını görün
İsterseniz 📥 Kodu İndir butonu ile kaydedin

Örnek Problemler
Bir listedeki çift sayıları bulan Python fonksiyonu yaz
İki sayının en büyük ortak bölenini (EBOB) bulan algoritma yaz
Fibonacci serisinin ilk 10 terimini yazdıran program yaz
🛠️ Teknolojiler

Python 3.13 - Programlama dili
Streamlit - Web framework
OpenAI API - GPT-4o-mini modeli
python-dotenv - Ortam değişkenleri yönetimi

📁 Proje Yapısı
turkce-kod-uretici/
│
├── TurkceKodUretici.py    # Ana uygulama
├── .env                    # API anahtarı (GİZLİ - paylaşılmaz!)
├── .gitignore             # Git ignore
├── requirements.txt        # Bağımlılıklar
└── README.md              # Bu dosya
⚠️ Önemli Notlar

.env dosyasını asla GitHub'a yüklemeyin
OpenAI API kullanımı ücretlidir (test için $5 yeterli)
İnternet bağlantısı gereklidir

🤝 Katkıda Bulunma

Bu repo'yu fork edin
Yeni bir branch oluşturun (git checkout -b feature/yeniOzellik)
Değişikliklerinizi commit edin (git commit -m 'Yeni özellik eklendi')
Branch'inizi push edin (git push origin feature/yeniOzellik)
Pull Request oluşturun

📝 Lisans
Bu proje MIT lisansı altında lisanslanmıştır.
👨‍💻 Geliştirici
Mert Uncu

Üniversite: İskenderun Teknik Üniversitesi 
Ders: Mühendislikte Bilgisayar Uygulamaları 1
Yıl: 2025


⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!
