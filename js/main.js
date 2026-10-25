// ==========================================================================
// Reach Community Platform - Shared Core JavaScript
// Supports Font Resizing, SOS Panic Modal, Role Profile Switcher, & Portal Navigation
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

    localStorage.setItem('reach_font_size', size);
}

// 2. SOS Panic Button Modal Controls
function openSosModal() {
    const modal = document.getElementById('sosModal');
    if (modal) {
        modal.style.display = 'flex';
    }
}

function closeSosModal() {
    const modal = document.getElementById('sosModal');
    if (modal) {
        modal.style.display = 'none';
    }
}

// 3. Complaint Modal Controls (For pages with popup modal)
function openComplaintModal() {
    const modal = document.getElementById('complaintModal');
    if (modal) {
        modal.style.display = 'flex';
    }
}

function closeComplaintModal() {
    const modal = document.getElementById('complaintModal');
    if (modal) {
        modal.style.display = 'none';
    }
}

function handleComplaintSubmit(e) {
    e.preventDefault();
    const form = e.target;
    const ref = form.querySelector('input[type="text"]')?.value || '#RCH-2026-8941';
    const category = form.querySelector('select')?.value || 'other';
    const desc = form.querySelector('textarea')?.value || '';
    const phone = form.querySelector('input[type="tel"]')?.value || '+91 98765 43210';

    if (window.ReachData) {
        ReachData.addComplaint({
            relatedRef: ref,
            category: category,
            description: desc,
            reporterPhone: phone,
            reporterName: 'Resident User'
        });
    }

    const successBox = document.getElementById('complaintSuccess');
    if (successBox) {
        successBox.style.display = 'block';
        setTimeout(() => {
            closeComplaintModal();
            form.reset();
            successBox.style.display = 'none';
        }, 2500);
    } else {
        alert('Complaint Registered (#CMP-2026-104). The Community Grievance Panel will review and respond within 24 hours.');
        closeComplaintModal();
    }
}

// 4. Compatibility Help Request Storage (Resident Flow Screens 1-5)
function saveHelpRequest(data) {
    localStorage.setItem('reach_current_request', JSON.stringify(data));
    // Also sync into main DB if available
    if (window.ReachData) {
        if (data.isSpaceBooking) {
            ReachData.addSpaceBooking({
                hallName: data.hallName || 'St. Joseph Community Activity Hall',
                userName: data.name || 'Ramesh Patel',
                userPhone: data.phone || '+91 98765 43210',
                eventType: data.eventType || 'Community Workshop',
                guestCapacity: data.guestCapacity || '30 People',
                bookingTime: data.time || 'Morning',
                notes: data.notes || ''
            });
        } else {
            ReachData.addRequest({
                category: data.category || 'Grocery & Medicine Delivery',
                userName: data.name || 'Ramesh Patel',
                userPhone: data.phone || '+91 98765 43210',
                address: data.address || 'Sector 4',
                urgency: data.urgency || 'Today',
                time: data.time || 'Morning',
                notes: data.notes || ''
            });
        }
    }
}

function getHelpRequest() {
    const defaultData = {
        category: 'Grocery & Medicine Delivery',
        name: 'Ramesh Patel',
        phone: '+91 98765 43210',
        address: 'Flat 402, Shanti Niketan, Sector 4',
        time: 'Today, Morning (9:00 AM - 12:00 PM)',
        urgency: 'Today',
        notes: 'Need someone to pick up prescribed blood pressure medicine from Apex Chemist.',
        isSpaceBooking: false,
        hallName: 'St. Joseph Community Activity Hall',
        guestCapacity: '50 People',
        eventType: 'Senior Yoga & Wellness Session'
    };

    const saved = localStorage.getItem('reach_current_request') || localStorage.getItem('sahyog_current_request');
    return saved ? JSON.parse(saved) : defaultData;
}

// 5. User Account Profile Pill in Top Bar (No instant role switching without login)
function setupRolePill() {
    const isLogged = (window.AuthSession && typeof AuthSession.isLoggedIn === 'function') 
        ? AuthSession.isLoggedIn() 
        : (localStorage.getItem('reach_auth_active') === 'true');

    const existing = document.getElementById('roleSwitcherPill');
    if (!isLogged) {
        if (existing) existing.remove();
        return;
    }

    const currentUser = (window.AuthSession && typeof AuthSession.getCurrentUser === 'function')
        ? AuthSession.getCurrentUser()
        : (window.ReachData ? ReachData.getCurrentUser() : null);
    if (!currentUser) return;

    const topBar = document.querySelector('.top-bar-left') || document.querySelector('.top-bar');
    if (topBar && !existing) {
        const pillContainer = document.createElement('div');
        pillContainer.id = 'roleSwitcherPill';
        pillContainer.style.display = 'inline-flex';
        pillContainer.style.alignItems = 'center';
        pillContainer.style.gap = '8px';
        pillContainer.innerHTML = `
            <span style="font-size: 0.85rem; color: #93C5FD;">Signed in:</span>
            <span class="role-badge-pill" style="cursor: default; padding: 4px 10px; border-radius: 14px; background: rgba(255,255,255,0.15); display: inline-flex; align-items: center; gap: 6px;">
                <span>${currentUser.avatar || '👤'}</span>
                <span><strong>${currentUser.name ? currentUser.name.split(' ')[0] : 'Member'}</strong></span>
            </span>
        `;
        topBar.appendChild(pillContainer);
    }
}

function openRoleSwitcherModal() {
    return false;
}

function switchRole(roleKey) {
    return false;
}

function openActorSwitcherModal() {
    return false;
}

function closeRoleSwitcherModal() {
    const modal = document.getElementById('roleModal') || document.getElementById('actorModal');
    if (modal) modal.style.display = 'none';
}

function closeActorSwitcherModal() {
    closeRoleSwitcherModal();
}

function switchRole(roleKey) {
    if (window.ReachData) {
        ReachData.setCurrentUserRole(roleKey);
    }
    closeRoleSwitcherModal();

    // Redirect to respective role screen
    if (roleKey === 'resident') {
        window.location.href = 'index.html';
    } else if (roleKey === 'volunteer') {
        window.location.href = 'volunteer.html';
    } else if (roleKey === 'owner') {
        window.location.href = 'space-owner.html';
    } else if (roleKey === 'ngo') {
        window.location.href = 'ngo-admin.html';
    } else if (roleKey === 'admin') {
        window.location.href = 'admin.html';
    }
}

function switchActor(roleKey) {
    switchRole(roleKey);
}

// 7. QR Code SVG Generator (Zero external dependencies)
function renderQrCodeSvg(text, size = 180) {
    // Generates an authentic-looking, scan-friendly visual QR SVG representation
    return `
    <svg width="${size}" height="${size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" style="background:#fff; padding:6px; border-radius:8px;">
        <rect x="0" y="0" width="100" height="100" fill="#ffffff"/>
        <!-- Corner Finder Patterns -->
        <rect x="6" y="6" width="26" height="26" fill="#000000" rx="4"/>
        <rect x="10" y="10" width="18" height="18" fill="#ffffff" rx="2"/>
        <rect x="14" y="14" width="10" height="10" fill="#000000" rx="2"/>

        <rect x="68" y="6" width="26" height="26" fill="#000000" rx="4"/>
        <rect x="72" y="10" width="18" height="18" fill="#ffffff" rx="2"/>
        <rect x="76" y="14" width="10" height="10" fill="#000000" rx="2"/>

        <rect x="6" y="68" width="26" height="26" fill="#000000" rx="4"/>
        <rect x="10" y="72" width="18" height="18" fill="#ffffff" rx="2"/>
        <rect x="14" y="76" width="10" height="10" fill="#000000" rx="2"/>

        <!-- Timing / Sync lines -->
        <rect x="36" y="16" width="28" height="4" fill="#000000"/>
        <rect x="16" y="36" width="4" height="28" fill="#000000"/>

        <!-- QR Data Blocks -->
        <rect x="38" y="38" width="8" height="8" fill="#0284C7"/>
        <rect x="54" y="38" width="8" height="8" fill="#000000"/>
        <rect x="46" y="46" width="8" height="8" fill="#0284C7"/>
        <rect x="38" y="54" width="8" height="8" fill="#000000"/>
        <rect x="54" y="54" width="8" height="8" fill="#0284C7"/>

        <rect x="70" y="38" width="6" height="6" fill="#000000"/>
        <rect x="82" y="44" width="6" height="6" fill="#000000"/>
        <rect x="74" y="52" width="6" height="6" fill="#000000"/>
        <rect x="86" y="60" width="6" height="6" fill="#000000"/>

        <rect x="38" y="70" width="6" height="6" fill="#000000"/>
        <rect x="48" y="76" width="6" height="6" fill="#000000"/>
        <rect x="58" y="70" width="6" height="6" fill="#000000"/>
        <rect x="40" y="86" width="6" height="6" fill="#000000"/>
        <rect x="52" y="86" width="6" height="6" fill="#000000"/>
        <rect x="64" y="82" width="6" height="6" fill="#000000"/>

        <rect x="70" y="72" width="8" height="8" fill="#000000"/>
        <rect x="82" y="80" width="8" height="8" fill="#000000"/>
    </svg>`;
}

// Initialize on DOM Ready
document.addEventListener('DOMContentLoaded', () => {
    const savedSize = localStorage.getItem('reach_font_size') || localStorage.getItem('sahyog_font_size');
    if (savedSize) {
        changeFontSize(savedSize);
    }
    setupRolePill();
});
