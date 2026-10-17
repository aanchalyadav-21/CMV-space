// ==========================================================================
// Sahyog Community Platform - Shared JavaScript
// Supports Font Resizing, SOS Panic Modal, Complaint Filing, & Demo State
// ==========================================================================

// 1. Accessibility: Font Resizer
function changeFontSize(size) {
    const root = document.documentElement;
    root.classList.remove('font-small', 'font-normal', 'font-large');
    
    if (size === 'small') {
        root.classList.add('font-small');
    } else if (size === 'large') {
        root.classList.add('font-large');
    } else {
        root.classList.add('font-normal');
    }

    localStorage.setItem('sahyog_font_size', size);
}

document.addEventListener('DOMContentLoaded', () => {
    const savedSize = localStorage.getItem('sahyog_font_size');
    if (savedSize) {
        changeFontSize(savedSize);
    }
});

// 2. SOS Panic Button Modal Controls
function openSosModal() {
    const modal = document.getElementById('sosModal');
    if (modal) modal.classList.add('active');
}

function closeSosModal() {
    const modal = document.getElementById('sosModal');
    if (modal) modal.classList.remove('active');
}

// 3. Complaint & Grievance Modal Controls
function openComplaintModal() {
    const modal = document.getElementById('complaintModal');
    if (modal) modal.classList.add('active');
}

function closeComplaintModal() {
    const modal = document.getElementById('complaintModal');
    if (modal) modal.classList.remove('active');
}

function handleComplaintSubmit(e) {
    e.preventDefault();
    const alertBox = document.getElementById('complaintSuccess');
    if (alertBox) {
        alertBox.style.display = 'block';
        setTimeout(() => {
            closeComplaintModal();
            alertBox.style.display = 'none';
        }, 2500);
    } else {
        alert('Your complaint #CMP-2026-104 has been registered with the DBIT Grievance Desk.');
        closeComplaintModal();
    }
}

// 4. Demo State Helper: Stores Volunteer Requests OR Community Space Bookings
function saveHelpRequest(data) {
    localStorage.setItem('sahyog_current_request', JSON.stringify(data));
}

function getHelpRequest() {
    const defaultData = {
        category: 'Grocery & Medicine Delivery',
        name: 'Ramesh Patel',
        phone: '+91 98765 43210',
        address: 'Flat 402, Shanti Niketan, Sector 4, Kurla West',
        time: 'Today, Morning (9:00 AM - 12:00 PM)',
        urgency: 'Today',
        notes: 'Need someone to pick up prescribed blood pressure medicine from Apex Chemist.',
        isSpaceBooking: false,
        hallName: 'St. Joseph Community Activity Hall',
        guestCapacity: '50 People',
        eventType: 'Senior Wellness & Reading Circle'
    };
    
    const saved = localStorage.getItem('sahyog_current_request');
    return saved ? JSON.parse(saved) : defaultData;
}
