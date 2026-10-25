# 🤝 Community Micro-Volunteering & Empty Space
### Platform Documentation & Architecture
**Tagline:** *Connecting People, Helping Communities.*

🔗 **Live Deployed Web Application:** [https://aanchalyadav-21.github.io/CMV-space/](https://aanchalyadav-21.github.io/CMV-space/)

---

## 🌟 Overview & Platform Mission

**Community Micro-Volunteering & Empty Space** is a neighborhood-driven web platform designed to foster community mutual aid and optimize local space sharing:

1. **Community Micro-Volunteering (Primary Service):** Everyday errand and assistance requests for seniors and residents — prescription medicine pickup, grocery assistance, tutoring, tech guidance, and companion walks — fulfilled by verified neighborhood volunteers.
2. **Community Empty Space Sharing (Secondary Service):** Discovering, scheduling, and reserving local community spaces, society clubhouses, and activity halls for educational workshops, health camps, and neighborhood gatherings.
3. **Integrated Event Organizing:** Enables community NGOs and group organizers to organize neighborhood events that seamlessly pair an empty venue with verified volunteer support.
4. **Safety & Supervisor Verification:** Dedicated administrative oversight for identity checks, space audit, live task monitoring, and community grievance resolution.
5. **Privacy-First Design:** Unauthenticated visitors can explore community services, browse spaces, and learn about the platform. Creating requests or tracking tasks strictly requires secure sign-in.

---

## 📁 File Structure & Core Components

| File | Purpose | Description |
| :--- | :--- | :--- |
| `index.html` | Welcome & Portal Gateway | Main homepage, service overview, sign-in & registration portal, accessibility controls. |
| `register.html` | Account Registration | User onboarding with role selection (Resident, Volunteer, Space Provider, Organizer). |
| `dashboard.html` | User Hub | Dynamic role-based dashboard for residents, volunteers, owners, and organizers. |
| `help.html` | Request Help | Errand request creation form with category selection, urgency, and accessibility voice support. |
| `review.html` | Review & Submit | Summary review step before final submission, preventing accidental duplicate requests. |
| `confirmation.html` | Request Tracker | Live operational status tracking, safety PIN verification, and volunteer contact. |
| `volunteer.html` | Volunteer Operations Hub | Dedicated volunteer desk to browse nearby errands, accept/pass tasks, and enter completion PIN. |
| `spaces.html` | Empty Spaces Directory | Public directory to discover and request reservations for community halls and clubhouses. |
| `pass.html` | Space Digital Entry Pass | Dedicated facility entry pass with SVG QR gate verification, caretaker contact, and venue rules. |
| `owner.html` | Space Provider Portal | Facility management hub to approve booking requests and generate passes. |
| `organize.html` | Event Organizer Desk | Platform integration module to run community activities utilizing volunteers and venues. |
| `my-activity.html` | Activity History | Comprehensive history of errand requests, venue reservations, and completed tasks. |
| `admin.html` | Supervisor Console | Administrative console for KYC verifications, space audits, and safety complaints. |
| `complaints.html` | Safety Grievance Desk | Dispute reporting portal for residents and volunteers to ensure community safety. |
| `style.css` | Unified Design System | High-contrast WCAG AA accessible design system with tailored fonts and responsive layout. |
| `script.js` | Master Engine | Reactive storage engine (`AppStore`), session management, and multi-language support. |

---

## 🚀 Running the Web Platform

1. Open `index.html` in any modern web browser.
2. Sign in with any role using demo credentials or register a new community account.
3. Enjoy an authentic, community-first mutual aid experience!
