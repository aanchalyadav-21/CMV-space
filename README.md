# 🤝 Reach Community Platform

> **DBIT Department of Computer Engineering — AY 26-27**  
> **Course:** 25CE3CEP01 Community Engagement Project  
> **Experiment No. 5:** Prototype Development Using Software Tools (Front-End Prototype)

---

## 📌 Project Overview
**Reach** is an accessible, community-driven micro-volunteering and shared space platform. It allows local residents and senior citizens to request urgent help (grocery/medicine pickup, digital tech assistance, clinic companion) and reserve shared community halls for workshops and neighborhood activities.

### 🌟 Key Human-Centric Safety Features:
1. **🚨 Senior Emergency SOS Panic Button:** One-touch emergency assistance modal in the top header connecting elders directly to medical ambulance (108) and society security.
2. **⚠️ Grievance Redressal / Complaint Filing:** Accessible link in the footer allowing residents to file complaints (#CMP-2026) regarding volunteer conduct or facility maintenance.
3. **🏛️ Dedicated Space Booking Pass:** If a user reserves a community space (e.g., St. Joseph Community Hall), Screen 5 generates an official **Community Space Booking Pass (#SPACE-2026-502)** with key-handover instructions instead of a volunteer delivery receipt.
4. **👓 Senior Citizen Accessibility:** Top-bar font size toggle (`A-` / `A` / `A+`), high-contrast colors, and large touch targets.

---

## 👥 Team Work Division (5 Members)

Each team member is assigned **one screen** and its corresponding stylesheet.

| Member | Role / Screen | HTML File | CSS File | Responsibility |
| :--- | :--- | :--- | :--- | :--- |
| **Member 1** | **Screen 1:** Landing / Entry Screen | `index.html` | `css/screen1.css` | Hero section, welcome message, accessibility banner, CTA to Screen 2 |
| **Member 2** | **Screen 2:** Service Category Selection | `categories.html` | `css/screen2.css` | Category cards (Groceries, Tech Help, Companion, Community Spaces) |
| **Member 3** | **Screen 3:** Help & Space Request Form | `request-help.html` | `css/screen3.css` | Form with dynamic hall & capacity selector when Community Space is chosen |
| **Member 4** | **Screen 4:** Summary Review Screen | `review.html` | `css/screen4.css` | Verification card, senior safety guarantee, Edit & Confirm buttons |
| **Member 5** | **Screen 5:** Success & Tracking Screen | `confirmation.html` | `css/screen5.css` | Generates Volunteer Match Tracking ID or Community Space Booking Pass |

---

## 🚀 How to Run the Prototype Locally

1. Double-click `index.html` in your file explorer to open it in Chrome, Edge, or Firefox.
2. Click **"Request Volunteer Help Now →"** to test the 5-screen volunteer flow.
3. OR click **"Browse Community Spaces 🏛️"** to see how the form and Screen 5 dynamically generate a **Community Space Booking Pass**!
4. Click **"🚨 EMERGENCY SOS"** in the top blue banner to test the senior emergency modal.
5. Click **"⚠️ Report an Issue"** in the footer to test the complaint filing system.

---

## 📝 Information for Experiment 5 Word Report

- **Tool Selected:** `Basic Front-End Web Development (HTML5 / CSS3 / JavaScript)`
- **Public View / Prototype URL:** `https://aanchalyadav-21.github.io/sahyog-community-platform/`
- **GitHub Repository URL:** `https://github.com/aanchalyadav-21/sahyog-community-platform`
- **Core User Journey Sequence:**
  1. `index.html` (Landing)
  2. `categories.html` (Service Directory)
  3. `request-help.html` (Request & Space Booking Form)
  4. `review.html` (Summary Verification)
  5. `confirmation.html` (Status & Tracking Pass)
