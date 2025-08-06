import streamlit as st
from datetime import datetime

# Konfigurasi halaman
st.set_page_config(
    page_title="Portofolio Saya",
    page_icon="👤",
    layout="wide"
)

# CSS Custom
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f2937;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #6b7280;
        text-align: center;
    }
    .project-card {
        padding: 1.5rem;
        border-radius: 10px;
        background: #f9fafb;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .contact-form {
        background: #f3f4f6;
        padding: 2rem;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigasi
menu = st.sidebar.radio(
    "Navigasi",
    ["🏠 Beranda", "👤 Tentang Saya", "💼 Proyek", "📞 Kontak"]
)

if menu == "🏠 Beranda":
    st.markdown("<h1 class='main-header'>Halo, Saya [Nama Anda]</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>Web Developer | Problem Solver | Lifelong Learner</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2,1])
    with col1:
        st.write("""
        ### Selamat Datang di Dunia Saya
        Website ini adalah refleksi pribadi tentang perjalanan saya sebagai developer. 
        Di sini Anda akan menemukan proyek-proyek yang telah saya kerjakan, 
        keahlian yang saya miliki, dan cerita di balik setiap langkah yang saya ambil.
        """)
        
        st.write("### Quick Stats")
        col_stats1, col_stats2, col_stats3 = st.columns(3)
        with col_stats1:
            st.metric("Proyek Selesai", "5+")
        with col_stats2:
            st.metric("Tahun Pengalaman", "3")
        with col_stats3:
            st.metric("Bahasa Pemrograman", "4")
    
    with col2:
        st.image("https://placehold.co/300x300?text=Foto+Profil", use_column_width=True)

elif menu == "👤 Tentang Saya":
    st.header("Tentang Saya")
    
    col1, col2 = st.columns([1,2])
    with col1:
        st.image("https://placehold.co/400x400?text=About+Me", use_column_width=True)
    
    with col2:
        st.write("""
        ### Background
        - **Nama**: [Nama Lengkap Anda]
        - **Profesi**: [Pekerjaan/Role Anda]
        - **Lokasi**: [Kota, Negara]
        - **Email**: [nama@email.com]
        
        ### Keahlian
        - 🐍 **Python**: Data Science, Web Development
        - 🌐 **Web Development**: React, Node.js, Streamlit
        - 📊 **Data**: Analysis, Visualization, Machine Learning
        - 🎨 **Design**: UI/UX, Responsive Design
        
        ### Minat
        - Teknologi terbaru dan AI
        - Fotografi dan videografi
        - Membaca buku teknologi
        - Berkontribusi pada open source
        """)
    
    st.write("---")
    st.write("### Timeline Karier")
    timeline_data = [
        {"Tahun": "2021", "Event": "Mulai belajar programming & web development"},
        {"Tahun": "2022", "Event": "First freelance project & portfolio website"},
        {"Tahun": "2023", "Event": "Full-time developer role & team projects"},
        {"Tahun": "2024", "Event": "Lead developer & advanced projects"}
    ]
    
    for item in timeline_data:
        with st.expander(f"{item['Tahun']}"):
            st.write(item["Event"])

elif menu == "💼 Proyek":
    st.header("Proyek Saya")
    
    projects = [
        {
            "nama": "E-commerce Analytics Dashboard",
            "deskripsi": "Dashboard interaktif untuk analisis penjualan dengan visualisasi data real-time menggunakan Python dan Streamlit",
            "teknologi": ["Python", "Pandas", "Plotly", "Streamlit", "SQL"],
            "link": "https://github.com/username/ecommerce-dashboard"
        },
        {
            "nama": "Personal Blog Platform",
            "deskripsi": "Blog pribadi dengan tema minimalis, responsive design, dan optimasi SEO menggunakan React dan Next.js",
            "teknologi": ["React", "Next.js", "Tailwind CSS", "Markdown"],
            "link": "https://github.com/username/personal-blog"
        },
        {
            "nama": "Weather Forecast App",
            "deskripsi": "Aplikasi cuaca real-time dengan prediksi 7 hari ke depan menggunakan API eksternal",
            "teknologi": ["JavaScript", "React", "OpenWeather API", "Chart.js"],
            "link": "https://github.com/username/weather-app"
        },
        {
            "nama": "Task Management System",
            "deskripsi": "Sistem manajemen tugas dengan fitur kolaborasi tim dan notifikasi real-time",
            "teknologi": ["Python", "Flask", "PostgreSQL", "Socket.io"],
            "link": "https://github.com/username/task-manager"
        }
    ]
    
    for project in projects:
        with st.container():
            st.markdown("<div class='project-card'>", unsafe_allow_html=True)
            st.subheader(project["nama"])
            st.write(project["deskripsi"])
            
            col1, col2 = st.columns([3,1])
            with col1:
                st.write("**Teknologi:**", ", ".join([f"`{tech}`" for tech in project["teknologi"]]))
            with col2:
                st.link_button("Lihat Proyek", project["link"])
            
            st.image("https://placehold.co/600x400?text=" + project["nama"].replace(" ", "+"), use_column_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

elif menu == "📞 Kontak":
    st.header("Hubungi Saya")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### Informasi Kontak")
        st.write("""
        - 📧 **Email**: [namaanda@email.com](mailto:namaanda@email.com)
        - 💼 **LinkedIn**: [linkedin.com/in/username](https://linkedin.com/in/username)
        - 🐦 **Twitter**: [@username](https://twitter.com/username)
        - 🐙 **GitHub**: [github.com/username](https://github.com/username)
        - 📱 **WhatsApp**: [+62xxx-xxxx-xxxx](https://wa.me/62xxxxxxxx)
        """)
    
    with col2:
        st.write("### Kirim Pesan Langsung")
        with st.form("contact_form"):
            name = st.text_input("Nama Lengkap", placeholder="Masukkan nama Anda")
            email = st.text_input("Email", placeholder="email@domain.com")
            subject = st.text_input("Subjek", placeholder="Tentang apa pesan ini?")
            message = st.text_area("Pesan", height=150, placeholder="Tulis pesan Anda di sini...")
            
            if st.form_submit_button("Kirim Pesan", use_container_width=True):
                if name and email and message:
                    st.success("✅ Pesan berhasil dikirim! Saya akan segera merespons.")
                    st.balloons()
                else:
                    st.error("⚠️ Mohon isi semua field yang wajib!")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("### Dibuat dengan ❤️ menggunakan Streamlit")
st.sidebar.markdown("© 2024 [Nama Anda]")

# Tambahan: Download CV
with st.sidebar:
    st.markdown("### 📄 Download CV")
    st.download_button(
        label="Download CV (PDF)",
        data="Ini adalah contoh CV. Ganti dengan file PDF Anda yang sebenarnya.",
        file_name="CV_[Nama Anda].pdf",
        mime="application/pdf"
    )
