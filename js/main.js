// ==========================================================================
// Sahyog Community Platform - Shared JavaScript
// Supports Font Resizing (Senior Accessibility) and Simple Demo State
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

    // Save user preference
    localStorage.setItem('sahyog_font_size', size);
}

// Restore user font size preference on page load
document.addEventListener('DOMContentLoaded', () => {
    const savedSize = localStorage.getItem('sahyog_font_size');
    if (savedSize) {
        changeFontSize(savedSize);
    }
});

// 2. Demo State Helper: Passes form data across Screen 3 -> Screen 4 -> Screen 5
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
        notes: 'Need someone to pick up prescribed blood pressure medicine from Apex Chemist.'
    };
    
    const saved = localStorage.getItem('sahyog_current_request');
    return saved ? JSON.parse(saved) : defaultData;
}
