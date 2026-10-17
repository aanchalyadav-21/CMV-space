# 🤝 Sahyog Community Platform

> **DBIT Department of Computer Engineering — AY 26-27**  
> **Course:** 25CE3CEP01 Community Engagement Project  
> **Experiment No. 5:** Prototype Development Using Software Tools (Front-End Prototype)

---

## 📌 Project Overview
**Sahyog** is an accessible, community-driven micro-volunteering and shared space platform. It allows local residents and senior citizens to request quick help (grocery/medicine pickup, digital tech assistance, walking companion) and reserve shared community halls for workshops and neighborhood activities.

---

## 👥 Team Work Division (5 Members)

Each team member is assigned **one screen** and its corresponding stylesheet. **Do not edit another member's files** to prevent merge conflicts!

| Member | Role / Screen | HTML File | CSS File | Responsibility |
| :--- | :--- | :--- | :--- | :--- |
| **Member 1** | **Screen 1:** Landing / Entry Screen | `index.html` | `css/screen1.css` | Hero section, welcome message, accessibility banner, CTA to Screen 2 |
| **Member 2** | **Screen 2:** Service Category Selection | `categories.html` | `css/screen2.css` | Category cards (Groceries, Tech Help, Companion, Community Spaces) |
| **Member 3** | **Screen 3:** Help Request Input Form | `request-help.html` | `css/screen3.css` | Senior-accessible form (name, phone, landmark, preferred time slot) |
| **Member 4** | **Screen 4:** Summary Review Screen | `review.html` | `css/screen4.css` | Verification card, senior safety guarantee, Edit & Confirm buttons |
| **Member 5** | **Screen 5:** Success & Tracking Screen | `confirmation.html` | `css/screen5.css` | Tracking ID (#SYG-2026-8941), status badge, Return to Home button |

---

## 🚀 How to Run the Prototype Locally

No installation or server setup is required!
1. Double-click `index.html` in your file explorer to open it in Chrome, Edge, or Firefox.
2. Click **"Request Volunteer Help Now →"** to test the entire 5-screen interactive user flow.
3. Test the **A- / A / A+** font resizer in the top blue banner.

---

## 📁 Repository Structure
```text
sahyog-community-platform/
│
├── index.html           # Screen 1 (Member 1)
├── categories.html      # Screen 2 (Member 2)
├── request-help.html    # Screen 3 (Member 3)
├── review.html          # Screen 4 (Member 4)
├── confirmation.html    # Screen 5 (Member 5)
│
├── css/
│   ├── base.css         # Shared design tokens, header, footer, accessible buttons
│   ├── screen1.css      # Member 1 custom styles
│   ├── screen2.css      # Member 2 custom styles
│   ├── screen3.css      # Member 3 custom styles
│   ├── screen4.css      # Member 4 custom styles
│   └── screen5.css      # Member 5 custom styles
│
├── js/
│   └── main.js          # Shared JavaScript (font resizer & demo state)
│
└── README.md            # Team guide & submission reference
```

---

## 📝 Information for Experiment 5 Word Report

- **Tool Selected:** Basic Front-End Web Development (HTML5 / CSS3 / JavaScript)
- **Public View / Prototype URL:** `https://<github-username>.github.io/sahyog-community-platform/`
- **GitHub Repository URL:** `https://github.com/<github-username>/sahyog-community-platform`
- **Core User Journey Sequence:**
  1. `index.html` (Landing)
  2. `categories.html` (Service Directory)
  3. `request-help.html` (Request Input Form)
  4. `review.html` (Summary Verification)
  5. `confirmation.html` (Status & Tracking)
