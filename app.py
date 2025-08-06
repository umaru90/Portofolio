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
    st.markdown("<h1 class='main-header'>Halo, Saya Rivaldo Elia</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>Machine Learning | Cloud Computing | Problem Solver | Lifelong Learner</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2,1])
    with col1:
        st.write("""
        ### Selamat Datang di Portofolio Saya
        I am an Electrical Engineering graduate with a keen interest in Technology and Programming. During my studies and various project experiences, I developed technical skills in programming (mainly using Python and C), Computer Networking, Cloud Computing, Artificial Intelligence (AI), and Internet of Things (IoT). 
        Besides hard skills, I also have strong soft skills, such as Data Analysis, Problem Solving, and Critical Thinking. I am used to managing my time effectively, quick to learn new things, and able to work collaboratively in a team.
        I am constantly eager to develop myself in the field of technology and am open to new opportunities that are challenging and impactful.
        """)
        
        st.write("### Quick Stats")
        col_stats1, col_stats2, col_stats3 = st.columns(3)
        with col_stats1:
            st.metric("Proyek Selesai", "8")
        with col_stats2:
            st.metric("Tahun Pengalaman", "4")
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
        - **Nama**: Rivaldo Elia
        - **Profesi**: Engineering
        - **Lokasi**: Sidikalang, Sumatera Utara, Indonesia
        - **Email**: eliarivaldo225@gmail.com
        
        ### Keahlian
        - 🐍 **Python**: Data Science
        - 🌐 **Web Development**: Streamlit
        - 📊 **Data**: Analysis, Visualization, Machine Learning
        
        ### Minat
        - Teknologi terbaru dan AI
        - Fotografi dan videografi
        - Listening Music
        - Drifting & Otomotive Enthusiast
        """)
    
    st.write("---")
    st.write("### Timeline Karier")
    timeline_data = [
        {"Tahun": "2021", "Event": "Mulai Perkuliahan di Institut Teknologi Del"},
        {"Tahun": "2024", "Event": "Studi Independent Bangkit Academy 2024 & Intern PT.Pelabuhan Indonesia (Pelindo)"}
    ]
    
    for item in timeline_data:
        with st.expander(f"{item['Tahun']}"):
            st.write(item["Event"])

elif menu == "💼 Proyek":
    st.header("Proyek Saya")
    
    projects = [
        {
            "nama": "Car-Dealer-in-Python",
            "deskripsi": "Car Dealer Application using Python as my project for the Programming 2 (Python) course.",
            "teknologi": ["Python"],
            "link": "https://github.com/umaru90/Car-Dealer-in-Python.git"
        },
        {
            "nama": "Air Quality Data Analytics ",
            "deskripsi": "Simulasi menjadi Data Analytics menggunakan Python selama MBKM Independent Study at Bangkit Academy 2024.",
            "teknologi": ["Python", "Pandas", "Matplotlib", "Streamlit", "Seaborn", "Numpy", "Babel"],
            "link": "https://github.com/umaru90/Air-Quality-Dataset.git"
        },
        {
            "nama": "Brazillian E-Commerce Public Data Analytics",
            "deskripsi": "Simulasi menjadi Data Analytics menggunakan Python selama MBKM Independent Study at Bangkit Academy 2024.",
            "teknologi": ["Python", "Pandas", "Matplotlib", "Streamlit", "Seaborn", "Numpy", "Babel"],
            "link": "https://github.com/umaru90/Brazillian-E-Commerce-Public-Dataset.git"
        },
        {
            "nama": "Digital Thermometer using Atmega 8535",
            "deskripsi": "Digital Thermometer using LM35 Based on ATMega8535 as my project in the microcontroller systems course.",
            "teknologi": ["C", "AtMega8535"],
            "link": "https://github.com/umaru90/Digital-Thermometer-Atmega8535.git"
        },
        {
            "nama": "Traffict Light Simulator Using VHDL",
            "deskripsi": "Traffic Light Simulation using VHDL as my project in the computer system architecture course.",
            "teknologi": ["VHDL"],
            "link": "https://github.com/umaru90/Traffict-Light-Using-VHDL.git"
        },
        {
            "nama": "OSPF using MikroTik RB951 and GNS3",
            "deskripsi": "Network Performance Testing with OSPF and Network Topology Implementation using GNS3 and Mikrotik RB951 Router as my project in the Computer Network 2 course.",
            "teknologi": ["Mikrotik", "GNS3", "OSPF"],
            "link": "https://github.com/umaru90/OSPF-using-MikroTik-RB951-and-GNS3.git"
        },
        {
            "nama": "Catedium App",
            "deskripsi": "Cat Identification using CNN Tensorflow (The Capstone Project that our group made during the Independent Study of Bangkit Academy 2024)",
            "teknologi": ["Python", "Kotlin", "Tensorflow", "CNN", ],
            "link": "https://github.com/umaru90/Catedium.git"
        },
        {
            "nama": "M-Bot Robot with Hand-Gesture-Controller",
            "deskripsi": "-",
            "teknologi": ["Python", "Leap Motion", "A* Algorithm", "Manhattan", "Pyserial", "MATLAB"],
            "link": "https://github.com/umaru90/M-Bot_Robot_with_Leap_Motion_Controller.git"
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
        - 📧 **Email**: [eliarivaldo225@gmail.com](mailto:namaanda@email.com)
        - 💼 **LinkedIn**: [linkedin.com/in/Rivaldo Elia](https://linkedin.com/in/username)
        - 🐙 **GitHub**: [github.com/umaru90](https://github.com/username)
        - 📱 **WhatsApp**: [+62-858-0979-3305](https://wa.me/62xxxxxxxx)
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
st.sidebar.markdown("© 2024 Rivaldo Elia")

# Tambahan: Download CV
with st.sidebar:
    st.markdown("### 📄 Download CV")
    st.download_button(
        label="Download CV (PDF)",
        data="Ini adalah contoh CV. Ganti dengan file PDF Anda yang sebenarnya.",
        file_name="Elia Rivaldo Pasaribu-resume.pdf",
        mime="application/pdf"
    )
