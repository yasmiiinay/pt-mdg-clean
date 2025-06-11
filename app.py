from flask import Flask, render_template, request, flash, redirect
import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

app = Flask(__name__)

# Ortam değişkenlerinden ayarları al
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['DEBUG'] = os.getenv('DEBUG', 'False').lower() == 'true'

# Static folder yapılandırması
app = Flask(__name__, static_folder='static', static_url_path='/static')

# Blog postları örneği
posts = [
    {
        "id": 1,
        "title": "Kilo Vermek İçin Bilinmesi Gerekenler",
        "summary": "Kilo vermek yalnızca az yemekle olmaz. Bu yazıda metabolizmayı nasıl hızlandıracağınızı keşfedin.",
        "content": "...",
        "date": "2025-06-01",
        "kategori": "Beslenme",
        "image": "/static/1.jpg"
    },
    {
        "id": 2,
        "title": "Kas Yapmanın Altın Kuralları",
        "summary": "Kas gelişimi yalnızca sporla değil, doğru beslenme ve dinlenmeyle mümkündür.",
        "content": "Kas yapmak sadece spor salonunda geçirdiğin saatlere bağlı değildir. Antrenman kadar, hatta bazen daha da önemli olan başka bir faktör var: uyku. Peki neden uyku kas gelişiminde bu kadar kritik? Öncelikle, vücudumuz uyku sırasında kendini tamir eder ve yeniler. Kaslarımız da antrenman sonrası yıpranır; işte uyku, bu yıpranan kasların onarımı ve güçlenmesi için olmazsa olmazdır. Yeterince uyumayan biri, kaslarının tam anlamıyla toparlanmasına fırsat vermez.Ayrıca, uyku hormon dengemizi düzenler. Özellikle büyüme hormonu, kas yapımında ve yağ yakımında önemli rol oynar. Bu hormonun en yüksek seviyede salgılandığı zaman, derin uyku evresidir. Yani kaliteli uyku, doğal kas gelişimini destekleyen bir hormonal denge sağlar.Son olarak, uyku eksikliği sadece kasları değil, motivasyonunu, enerjini ve genel performansını da olumsuz etkiler. Antrenmanlarda istediğin verimi alamaz, kendini yorgun hissedersen, hedeflerine ulaşman zorlaşır. Özetle; iyi bir uyku, kas gelişiminin temel taşıdır. Spor salonunda harcadığın emek kadar, yatağında geçirdiğin saatlere de değer ver. Vücuduna saygı göster, dinlen ve büyümesini destekle. Çünkü kasların, sen uyurken büyür.",
        "date": "2025-06-02",
        "kategori": "Antrenman",
        "image": "/static/2.jpg"
    },
    {
        "id": 3,
        "title": "Esnekliğin Önemi ve Mobilite",
        "summary": "Daha esnek bir vücut için öneriler: mobilite çalışmalarıyla performansını artır.",
        "content": "...",
        "date": "2025-06-03",
        "kategori": "Sağlık",
        "image": "/static/3.jpg"
    },
    {
        "id": 4,
        "title": "Spor Öncesi ve Sonrası Beslenme",
        "summary": "Antrenmandan maksimum verim alman için beslenme önerileri.",
        "content": "...",
        "date": "2025-06-04",
        "kategori": "Beslenme",
        "image": "/static/4.jpg"
    },
    {
        "id": 5,
        "title": "Kardiyo mu, Ağırlık mı?",
        "summary": "Hedefine göre en uygun antrenman tipini seç.",
        "content": "...",
        "date": "2025-06-05",
        "kategori": "Antrenman",
        "image": "/static/5.jpg"
    },
    {
        "id": 6,
        "title": "Uyku ve Kas Gelişimi",
        "summary": "Yeterli uyku neden kas gelişiminde bu kadar önemli?",
        "content": "Kas yapmak sadece spor salonunda geçirdiğin saatlere bağlı değildir. Antrenman kadar, hatta bazen daha da önemli olan başka bir faktör var: uyku. Peki neden uyku kas gelişiminde bu kadar kritik? Öncelikle, vücudumuz uyku sırasında kendini tamir eder ve yeniler. Kaslarımız da antrenman sonrası yıpranır; işte uyku, bu yıpranan kasların onarımı ve güçlenmesi için olmazsa olmazdır. Yeterince uyumayan biri, kaslarının tam anlamıyla toparlanmasına fırsat vermez.Ayrıca, uyku hormon dengemizi düzenler. Özellikle büyüme hormonu, kas yapımında ve yağ yakımında önemli rol oynar. Bu hormonun en yüksek seviyede salgılandığı zaman, derin uyku evresidir. Yani kaliteli uyku, doğal kas gelişimini destekleyen bir hormonal denge sağlar.Son olarak, uyku eksikliği sadece kasları değil, motivasyonunu, enerjini ve genel performansını da olumsuz etkiler. Antrenmanlarda istediğin verimi alamaz, kendini yorgun hissedersen, hedeflerine ulaşman zorlaşır. Özetle; iyi bir uyku, kas gelişiminin temel taşıdır. Spor salonunda harcadığın emek kadar, yatağında geçirdiğin saatlere de değer ver. Vücuduna saygı göster, dinlen ve büyümesini destekle. Çünkü kasların, sen uyurken büyür.",
        "date": "2025-06-06",
        "kategori": "Sağlık",
        "image": "/static/6.jpg"
    },
    {
        "id": 7,
        "title": "Mental Sağlık ve Egzersiz",
        "summary": "Egzersizin ruh haline olan etkileri üzerine.",
        "content": "...",
        "date": "2025-06-08",
        "kategori": "Sağlık",
        "image": "/static/7.jpg"
    }
]


# Anasayfa
@app.route('/')
def home():
    return render_template("home.html")

# Hakkımda sayfası
@app.route('/about')
def about():
    return render_template("about.html")

# Hizmetler sayfası
@app.route('/services')
def services():
    return render_template("services.html")

# Blog liste sayfası
@app.route("/blog")
def blog():
    category = request.args.get("kategori")
    if category:
        filtered_posts = [p for p in posts if p["kategori"] == category]
    else:
        filtered_posts = posts
    return render_template("blog.html", posts=filtered_posts, selected_category=category)


# Blog detay sayfası
@app.route("/blog/<int:post_id>")
def blog_detail(post_id):
    post = next((p for p in posts if p["id"] == post_id), None)
    if post:
        return render_template("blog_detail.html", post=post)
    else:
        return "Blog yazısı bulunamadı", 404

# İletişim sayfası
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        print(f"Gelen mesaj:\nAd: {name}\nEmail: {email}\nMesaj: {message}\n")
        flash('Mesajınız başarıyla gönderildi. Teşekkürler!', 'success')
        return redirect('/contact')

    return render_template("contact.html")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=False)
