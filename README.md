# mgnrega-performance-dashboard
A Django-based web application that visualizes the monthly and historical performance of districts under India’s MGNREGA program. Designed for accessibility and easy understanding by rural citizens with multilingual (Hindi/English) support.

# MGNREGA Performance Dashboard

This project is a **Django-based web application** that helps citizens easily view and understand the **performance of their district** under the Government of India’s **MGNREGA (Mahatma Gandhi National Rural Employment Guarantee Act)** program.

It uses **Open Government Data (API)** to show monthly performance indicators like total workers, average work days, and wages paid — not only for the **current month** but also **past months**, helping users compare progress over time.

---

## 🚀 Features

- 📊 **District Performance Visualization** — View current and past performance in charts and tables.  
- 🌍 **Multilingual Interface** — Supports **English and Hindi** for accessibility in rural India.  
- 🗓️ **Historical Trends** — Compare monthly data and performance changes.  
- 📶 **Offline Caching** — Data stored locally in a database to handle API downtime.  
- 📍 **Auto District Detection (Bonus)** — Detects user’s district using location for personalized view.  
- 💡 **User-Friendly Design** — Simple UI with icons and colors for low-literacy users.  

---

## 🧱 Tech Stack

- **Backend:** Python, Django  
- **Database:** MySQL  
- **Frontend:** HTML, CSS, (minimal) JavaScript  
- **Data Source:** data.gov.in MGNREGA Open API  
- **Hosting:** (Your VM/VPS or server platform)  

---

## ⚙️ Setup Instructions

1. Clone the repo  
   ```bash
   git clone https://github.com/Isoo-Pal/mgnrega-performance-dashboard.git
   cd mgnrega-performance-dashboard
