from gettext import translation
import streamlit as st
from pathlib import Path
import base64

st.set_page_config(page_title="MAHALAKSHMI S — Portfolio", layout="wide")

PHOTO_PATH = Path("photo.jpg")

def image_to_data_url(path: Path) -> str:
    if not path.exists():
        return ""
    with path.open("rb") as f:
        data = f.read()
    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
    b64 = base64.b64encode(data).decode("utf-8")
    return f"data:{mime};base64,{b64}"

photo_data_url = image_to_data_url(PHOTO_PATH)
transparent_gif = "data:image/gif;base64,R0lGODlhAQABAIAAAP///////ywAAAAAAQABAAACAUwAOw=="
photo_src = photo_data_url if photo_data_url else transparent_gif

html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<!-- FONT ADDED (ONLY CHANGE) -->
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">

<title>Portfolio — MAHALAKSHMI S</title>

<style>
  *{{margin:0;padding:0;box-sizing:border-box;}}

  /* FONT APPLIED HERE */
  body{{
    font-family:'Poppins', Arial, sans-serif;
    background:#f5f0ff;
    color:#232129;
    overflow-x:hidden;
    line-height:1.7;
  }}

  a{{text-decoration:none;}}
  .container{{max-width:1100px;margin:0 auto;padding:20px;}}
  header{{position:sticky;top:0;background:rgba(255,255,255,0.85);backdrop-filter:blur(6px);z-index:50;padding:10px 0;border-bottom:1px solid #ddd;}}
  nav{{display:flex;justify-content:space-between;align-items:center;}}
  .brand{{display:flex;align-items:center;gap:12px;font-weight:700;}}
  .brand .logo{{width:44px;height:44px;border-radius:10px;background:linear-gradient(135deg,#6b5ce7,#b497ff);color:white;display:flex;align-items:center;justify-content:center;font-size:22px;font-weight:800;}}
  .nav-links{{display:flex;gap:16px;}}
  .nav-links a{{font-weight:600;color:#333;transition:0.3s;}}
  .nav-links a:hover{{color:#6b5ce7;}}
  .hero{{display:grid;grid-template-columns:1fr 350px;gap:30px;padding:80px 0;align-items:center;}}
  .card{{background:white;padding:20px;border-radius:14px;box-shadow:0 6px 20px rgba(80,70,120,0.1);opacity:0;transform:translateY(30px);transition:all 0.8s ease-in-out;}}
  .card.visible{{opacity:1;transform:translateY(0);}}
  .card:hover{{transform:scale(1.05);box-shadow: 0 14px 35px rgba(107, 92, 231, 0.25);}}
  .card{{transition:transform 0.35s ease,box-shadow 0.35s ease;}}
  .avatar{{width:140px;height:140px;border-radius:50%;overflow:hidden;margin:0 auto 12px;}}
  .avatar img{{width:100%;height:100%;object-fit:cover;}}
  section{{padding:40px 0;}}
  .section-title{{font-size:24px;font-weight:800;margin-bottom:16px;color:#2b2350;}}
  .projects-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;}}
  
  .skill{{padding:6px 12px;border-radius:8px;background:#d6c9f5;font-weight:600;font-size:14px;transition:0.3s;}}
  .skill:hover{{background:#6b5ce7;color:white;transform:scale(1.05);}}
  .button{{padding:10px 16px;background:#6b5ce7;color:white;border-radius:10px;font-weight:700;transition:0.3s;}}
  .button:hover{{background:#5741b3;}}
  footer{{margin-top:40px;padding:20px;text-align:center;color:#555;}}
  @media(max-width:900px){{.hero{{grid-template-columns:1fr}}.projects-grid{{grid-template-columns:repeat(2,1fr);}}}}
  @media(max-width:600px){{.projects-grid{{grid-template-columns:1fr;}}}}
  .typed-text {{border-right: .15em solid #6b5ce7;white-space: nowrap;overflow: hidden;}}
</style>
</head>


<body>

<header>
  <div class="container">
    <nav>
      <div class="brand">
        <div class="logo">MS</div>
        <div>
          <div style="font-weight:800">MAHALAKSHMI S</div>
        </div>
      </div>
      <div class="nav-links">
        <a href="#about">About</a>
        <a href="#skills">Skills</a>
        <a href="#projects">Projects</a>
        <a href="#timeline">Timeline</a>
        <a href="#contact">Contact</a>
      </div>
    </nav>
  </div>
</header>

<main class="container">

<section class="hero">
  <div class="card">
    <h1 style="font-size:32px;color:#2b2350;font-weight:900">
      <span style="color:#6b5ce7">MAHALAKSHMI S</span>
    </h1>
    <p style="margin-top:10px;color:#444;max-width:700px" class="typed-text" id="typed"></p>
    <div style="margin-top:18px;display:flex;gap:12px">
      <a href="#projects" class="button">Projects</a>
      <a href="#contact" class="button" style="background:white;color:#6b5ce7;border:1px solid #6b5ce7;">Contact</a>
    </div>
  </div>

  <div class="card" style="text-align:center">
    <div class="avatar">
      <img src="{photo_src}" alt="profile"/>
    </div>
    <div style="font-weight:800">MAHALAKSHMI S</div>
    <div style="color:#555;font-size:14px">
      Dhanalakshmi Srinivasan Engineering College • Batch 2022–2026
    </div>
  </div>
</section>

<section id="about">
  <div class="section-title">About</div>
  <div class="card">
    I am an enthusiastic learner with a genuine passion for exploring new technologies and solving real-world problems. I constantly seek opportunities to expand my knowledge, strengthen my technical skills, and apply creative thinking to challenges. With a strong commitment to continuous learning, I enjoy working on projects that push me to grow, adapt, and innovate.
    <br><br>
    I am aspiring to secure an entry-level role where I can put my skills into action and contribute to the success of an organization. I aim to bring dedication, curiosity, and a positive mindset to every task I take on. My goal is to learn from experienced professionals, take on meaningful responsibilities, and build a strong foundation for my career while adding value through hard work and problem-solving abilities.
  </div>
</section>

<section id="skills">
  <div class="section-title">Skills & Expertise</div>

  <div class="projects-grid">
    <div class="card">
      <strong>Data Analysis</strong>
      <p style="margin-top:8px;color:#555;font-size:14px;">
        Excel · Google Sheets · Exploratory Data Analysis (EDA) · Statistics
      </p>
    </div>

    <div class="card">
      <strong>Programming</strong>
      <p style="margin-top:8px;color:#555;font-size:14px;">
        Python · R · SQL
      </p>
    </div>

    <div class="card">
      <strong>Databases</strong>
      <p style="margin-top:8px;color:#555;font-size:14px;">
        MySQL · PostgreSQL · MongoDB
      </p>
    </div>

    <div class="card">
      <strong>Data Visualization</strong>
      <p style="margin-top:8px;color:#555;font-size:14px;">
        Power BI · Tableau · Excel Dashboards
      </p>
    </div>

    <div class="card">
      <strong>Business & Analytics</strong>
      <p style="margin-top:8px;color:#555;font-size:14px;">
        KPI Analysis · A/B Testing · Reporting
      </p>
    </div>

    <div class="card">
      <strong>Tools & Platforms</strong>
      <p style="margin-top:8px;color:#555;font-size:14px;">
        Git · GitHub
      </p>
    </div>
  </div>
</section>


<section id="projects">
  <div class="section-title">Projects</div>
  <div class="projects-grid">
    <div class="card">
      <strong>Banking Console App</strong>
      <p class="muted">Python · MySQL</p>
      <p>CRUD banking system with transactions and logging.</p>
      <a href="https://github.com/mowriyaathl-comp/SQL--Query-Project/blob/main/bk.py" target="_blank">View on GitHub</a>
    </div>

    <div class="card">
      <strong>Medical Appointment Scheduler</strong>
      <p class="muted">Python · MySQL</p>
      <p>Patient record management + appointment booking system.</p>
      <a href="https://github.com/mowriyaathl-comp/SQL--Query-Project/blob/main/patient.py" target="_blank">View on GitHub</a>
    </div>

    <div class="card">
      <strong>More Projects</strong>
      <p class="muted">GitHub</p>
      <p>Explore additional repositories.</p>
      <a href="https://github.com/mowriyaathl-comp" target="_blank">github.com/mowriyaathl-comp</a>
    </div>
  </div>
</section>

<section id="timeline" class="hidden">
  <div class="card">
    <h2>Timeline</h2>
    <p><strong>Education:</strong><br>
    Bachelor of Technology in Information Technology<br>
    Dhanalakshmi Srinivasan Engineering College, Perambalur<br>
    2022 - 2026
    </p>
    <p><strong>Workshops & Courses:</strong><br>
      - Data Science — Workshop<br>
      - NPTEL: Data Analytics with Python — 60%<br>
      - AI Programming — Intel<br>
      
    </p>
  </div>
</section>


<section id="contact">
  <div class="section-title">Contact Me</div>
  <p style="margin-bottom:20px;color:#555;max-width:600px;">
    I’m open to opportunities and collaborations. Feel free to reach out via email or the form below. I’ll get back to you as soon as possible.
  </p>
  <div class="card" style="display:grid;grid-template-columns:1fr 1fr;gap:20px">
    <div>
      <p>Email: <a href="mailto:mowriyaathl@gmail.com">mowriyaathl@gmail.com</a></p>
      <p>Phone: <a href="tel:+917418285969">+91 7418285969</a></p>
      <p>GitHub: <a href="https://github.com/mowriyaathl-comp" target="_blank">github.com/mowriyaathl-comp</a></p>
      <p>LinkedIn: <a href="https://www.linkedin.com/in/mahalakshmi-s-454497281/" target="_blank">linkedin.com/in/mahalakshmi-s</a></p>
    </div>
    <div>
      <input placeholder="Your name" style="padding:10px;margin-bottom:10px;width:100%;border-radius:8px;border:1px solid #ccc;">
      <input placeholder="Your email" style="padding:10px;margin-bottom:10px;width:100%;border-radius:8px;border:1px solid #ccc;">
      <textarea placeholder="Message" style="padding:10px;width:100%;height:120px;border-radius:8px;border:1px solid #ccc;"></textarea>
      <div style="margin-top:10px">
        <a href="mailto:mowriyaathl@gmail.com" class="button">Send</a>
      </div>
    </div>
  </div>
</section>

<footer>
© 2025 MAHALAKSHMI S
</footer>

<script>
  // Scroll animation
  function reveal(){{
    var cards = document.querySelectorAll('.card');
    for(var i=0;i<cards.length;i++){{
      var windowHeight = window.innerHeight;
      var elementTop = cards[i].getBoundingClientRect().top;
      var elementVisible = 100;
      if(elementTop < windowHeight - elementVisible){{
        cards[i].classList.add("visible");
      }}
    }}
  }}
  window.addEventListener("scroll", reveal);
  window.addEventListener("load", reveal);

  // Typing effect
  const typedText = "Passionate learner with strong fundamentals in coding, databases and real-world problem solving.";
  let i=0;
  function typeWriter(){{
    if(i < typedText.length){{
      document.getElementById("typed").innerHTML += typedText.charAt(i);
      i++;
      setTimeout(typeWriter,50);
    }}
  }}
  window.addEventListener("load", typeWriter);
</script>

</body>
</html>
"""

st.components.v1.html(html_template, height=7500, scrolling=True)