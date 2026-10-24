// ==========================================================================
// Reach Community Platform - Unified Data Store & Account Management
// Supports: Senior Citizens, Volunteers, Space Providers, NGOs, and Support Staff
// ==========================================================================

const REACH_STORAGE_KEYS = {
    USER_SESSION: 'reach_user_session',
    REQUESTS: 'reach_requests_db',
    SPACES: 'reach_spaces_db',
    SPACE_BOOKINGS: 'reach_space_bookings_db',
    COMPLAINTS: 'reach_complaints_db',
    EVENTS: 'reach_events_db',
    VERIFICATIONS: 'reach_verifications_db'
};

// 1. Initial Sample Community Profiles (Realistic neighborhood members)
const SEED_PROFILES = {
    resident: {
        id: 'usr_res_01',
        name: 'Ramesh Patel',
        role: 'resident',
        roleTitle: 'Senior Citizen Resident',
        phone: '+91 98765 43210',
        address: 'Flat 402, Shanti Niketan, Sector 4',
        avatar: '👴',
        verified: true,
        seniorCitizen: true
    },
    volunteer: {
        id: 'usr_vol_02',
        name: 'Karan Verma',
        role: 'volunteer',
        roleTitle: 'Verified Community Volunteer',
        phone: '+91 98765 43211',
        rating: 4.9,
        reviewsCount: 38,
        tasksCompleted: 42,
        skills: ['Elderly Care', 'Grocery Pickup', 'Tech Help', 'First Aid'],
        avatar: '🦸‍♂️',
        isAvailable: true,
        verified: true
    },
    owner: {
        id: 'usr_own_03',
        name: 'Marian Community Welfare Trust',
        role: 'owner',
        roleTitle: 'Community Space Provider',
        phone: '+91 98765 43212',
        society: 'St. Joseph Welfare Trust',
        venuesManaged: 2,
        avatar: '🏛️',
        verified: true
    },
    ngo: {
        id: 'usr_ngo_04',
        name: 'CareForward Community Welfare Foundation',
        role: 'ngo',
        roleTitle: 'Community Welfare NGO',
        organization: 'CareForward Foundation',
        phone: '+91 98765 43213',
        avatar: '🤝',
        verified: true
    },
    admin: {
        id: 'usr_adm_05',
        name: 'Reach Community Support Desk',
        role: 'admin',
        roleTitle: 'Community Support & Safety Team',
        department: 'Neighborhood Safety & Grievance Panel',
        phone: '+91 98765 43214',
        avatar: '🛡️',
        verified: true
    }
};

const SEED_SPACES = [
    {
        id: 'spc_101',
        name: 'St. Joseph Community Activity Hall',
        ownerName: 'Marian Welfare Trust',
        ownerPhone: '+91 98765 43212',
        capacity: 60,
        address: 'Ground Floor, Parish Welfare Center, City Center',
        amenities: ['Air Conditioning', 'Audio / Mic System', 'Projector & Screen', 'Wheelchair Ramp', 'Restrooms'],
        hourlyRate: 'Free (Community Sponsored)',
        photos: 'hall1.jpg',
        rules: 'No loud music after 8:30 PM. Please leave the hall clean.',
        slots: ['Morning (9:00 AM - 12:00 PM)', 'Afternoon (2:00 PM - 5:00 PM)', 'Evening (6:00 PM - 9:00 PM)'],
        status: 'verified',
        rating: 4.8
    },
    {
        id: 'spc_102',
        name: 'Shanti Niketan Society Clubhouse & Library',
        ownerName: 'Society Welfare Committee',
        ownerPhone: '+91 98765 43210',
        capacity: 35,
        address: 'B-Wing Terrace Floor, Shanti Niketan CHS, Sector 4',
        amenities: ['Wi-Fi 100Mbps', 'Whiteboard', 'Ceiling Fans', 'Drinking Water', 'Reading Tables'],
        hourlyRate: 'Free for Residents / ₹150/hr External',
        photos: 'clubhouse.jpg',
        rules: 'Keep quiet in reading corner. Maximum 35 attendees.',
        slots: ['Morning (10:00 AM - 1:00 PM)', 'Evening (4:00 PM - 7:00 PM)'],
        status: 'verified',
        rating: 4.6
    },
    {
        id: 'spc_103',
        name: 'Neighborhood Learning Center & Hall',
        ownerName: 'Neighborhood Care Trust',
        ownerPhone: '+91 022 2504 2000',
        capacity: 90,
        address: '1st Floor, Premier Community Center, City Center',
        amenities: ['High-Def Projector', 'Air Conditioned', 'Stage & Podium', 'Lapel Microphones', 'Wheelchair Ramp'],
        hourlyRate: 'Community Welfare Sponsoring Available',
        photos: 'community_hall.jpg',
        rules: 'Community premises. Advance booking reservation required.',
        slots: ['Saturday (10:00 AM - 2:00 PM)', 'Sunday (2:00 PM - 6:00 PM)'],
        status: 'verified',
        rating: 4.9
    }
];

const SEED_REQUESTS = [
    {
        id: 'RCH-2026-8941',
        category: 'Grocery & Medicine Delivery',
        icon: '🛒',
        userName: 'Ramesh Patel',
        userPhone: '+91 98765 43210',
        address: 'Flat 402, Shanti Niketan, Sector 4',
        urgency: 'Today (Urgent)',
        time: 'Morning (9:00 AM - 12:00 PM)',
        notes: 'Need someone to pick up prescribed blood pressure medicine (Amlodipine 5mg) from Apex Chemist.',
        status: 'waiting_volunteer',
        createdAt: 'Today, 09:30 AM',
        assignedVolunteer: null,
        etaMinutes: 15,
        otpCode: '4829',
        rating: null,
        feedback: null
    },
    {
        id: 'RCH-2026-8942',
        category: 'Smartphone & Digital Help',
        icon: '📱',
        userName: 'Mrs. Leela Joshi (Age 74)',
        userPhone: '+91 98201 12345',
        address: 'Flat 201, Rosewood Apts, Near Station Road',
        urgency: 'Flexible',
        time: 'Today (3:00 PM - 5:00 PM)',
        notes: 'Help needed to submit online Digital Life Certificate (Jeevan Pramaan) on government pension portal.',
        status: 'in_progress',
        createdAt: 'Today, 10:15 AM',
        assignedVolunteer: {
            name: 'Karan Verma',
            phone: '+91 98765 43211',
            rating: 4.9,
            avatar: '🦸‍♂️'
        },
        etaMinutes: 0,
        otpCode: '6192',
        rating: null,
        feedback: null
    },
    {
        id: 'RCH-2026-8943',
        category: 'Clinic Companion & Walking',
        icon: '🩺',
        userName: 'Mr. Anthony D\'Souza',
        userPhone: '+91 98334 77889',
        address: 'Bunglow 12, St. Anthony Society, Sector 4',
        urgency: 'Tomorrow',
        time: 'Tomorrow, Morning (8:00 AM - 10:00 AM)',
        notes: 'Need walking partner to accompany to Holy Family Clinic for routine blood check and return safely.',
        status: 'completed',
        createdAt: 'Yesterday, 04:00 PM',
        assignedVolunteer: {
            name: 'Karan Verma',
            phone: '+91 98765 43211',
            rating: 4.9,
            avatar: '🦸‍♂️'
        },
        rating: 5,
        feedback: 'Karan was extremely courteous, patient, and on time. Felt very safe.'
    }
];

const SEED_SPACE_BOOKINGS = [
    {
        id: 'SPACE-2026-502',
        hallId: 'spc_101',
        hallName: 'St. Joseph Community Activity Hall',
        userName: 'Ramesh Patel',
        userPhone: '+91 98765 43210',
        eventType: 'Senior Citizen Morning Yoga & Wellness Circle',
        guestCapacity: '25-30 Elders',
        bookingDate: 'Tomorrow',
        bookingTime: 'Morning (9:00 AM - 11:30 AM)',
        notes: 'Sound system needed for calm meditation audio.',
        status: 'confirmed',
        qrCodeToken: 'QR-PASS-SJ-2026-502',
        checkInTime: null,
        checkOutTime: null,
        ownerDecisionBy: 'Marian Welfare Trust',
        createdAt: 'Today, 11:00 AM'
    },
    {
        id: 'SPACE-2026-503',
        hallId: 'spc_102',
        hallName: 'Shanti Niketan Society Clubhouse & Library',
        userName: 'CareForward Foundation',
        userPhone: '+91 98765 43213',
        eventType: 'Free Community Health & Diabetes Screening',
        guestCapacity: '40 Attendees',
        bookingDate: 'Sunday, 26 Oct 2026',
        bookingTime: 'Morning (10:00 AM - 1:00 PM)',
        notes: 'Volunteer doctors attending from local health center.',
        status: 'pending_approval',
        qrCodeToken: 'QR-PASS-SN-2026-503',
        ownerDecisionBy: null,
        createdAt: 'Today, 01:20 PM'
    }
];

const SEED_COMPLAINTS = [
    {
        id: 'CMP-2026-104',
        relatedRef: 'RCH-2026-8941',
        category: 'no-show',
        description: 'Assigned volunteer was delayed by 40 minutes without prior telephone notification.',
        reporterPhone: '+91 98765 43210',
        reporterName: 'Ramesh Patel',
        status: 'under_investigation',
        actionTaken: 'Contacted volunteer; formal reminder and protocol advisory issued.',
        createdAt: 'Today, 11:30 AM'
    },
    {
        id: 'CMP-2026-105',
        relatedRef: 'SPACE-2026-499',
        category: 'space',
        description: 'Sound system microphone battery was depleted in clubhouse.',
        reporterPhone: '+91 98201 55667',
        reporterName: 'Sunita Sharma',
        status: 'resolved',
        actionTaken: 'Facility caretaker replaced batteries and instituted pre-booking check protocol.',
        createdAt: '20 Oct 2026, 02:15 PM'
    }
];

const SEED_EVENTS = [
    {
        id: 'EVT-2026-01',
        title: 'Monsoon Clean Neighborhood & Health Awareness Drive',
        ngoName: 'CareForward Community Welfare Foundation',
        date: 'Sunday, 26 Oct 2026',
        time: '8:00 AM - 11:30 AM',
        venue: 'St. Joseph Hall & Neighboring Streets',
        volunteersNeeded: 15,
        volunteersRegistered: 11,
        description: 'Distributing mosquito prevention kits and educating senior residents about health precautions.'
    },
    {
        id: 'EVT-2026-02',
        title: 'Senior Citizen Digital Literacy & UPI Safety Workshop',
        ngoName: 'Neighborhood Care Trust',
        date: 'Saturday, 01 Nov 2026',
        time: '3:00 PM - 5:30 PM',
        venue: 'Neighborhood Learning Center',
        volunteersNeeded: 10,
        volunteersRegistered: 8,
        description: 'One-on-one coaching for elderly residents to safely use payment apps and avoid digital fraud.'
    }
];

const SEED_VERIFICATIONS = [
    {
        id: 'VER-VOL-101',
        roleType: 'Volunteer',
        name: 'Karan Verma',
        collegeOrOrg: 'Youth Volunteer Guild',
        idType: 'Government ID + Aadhaar Card',
        idNumber: 'VER-2026-KRL45',
        status: 'approved',
        submittedAt: '15 Oct 2026'
    },
    {
        id: 'VER-OWN-102',
        roleType: 'Space Provider',
        name: 'Marian Welfare Trust',
        collegeOrOrg: 'St. Joseph Welfare Trust',
        idType: 'Society Registration Certificate',
        idNumber: 'SOC-MAH-2024-KRL',
        status: 'approved',
        submittedAt: '16 Oct 2026'
    },
    {
        id: 'VER-VOL-103',
        roleType: 'Volunteer',
        name: 'Rohit Deshmukh',
        collegeOrOrg: 'Community Volunteer Pool',
        idType: 'Photo ID Card',
        idNumber: 'VER-2026-RD28',
        status: 'pending',
        submittedAt: '22 Oct 2026'
    }
];

// 2. Data Store Helper API
const ReachData = {
    init() {
        if (!localStorage.getItem(REACH_STORAGE_KEYS.REQUESTS)) {
            localStorage.setItem(REACH_STORAGE_KEYS.REQUESTS, JSON.stringify(SEED_REQUESTS));
        }
        if (!localStorage.getItem(REACH_STORAGE_KEYS.SPACES)) {
            localStorage.setItem(REACH_STORAGE_KEYS.SPACES, JSON.stringify(SEED_SPACES));
        }
        if (!localStorage.getItem(REACH_STORAGE_KEYS.SPACE_BOOKINGS)) {
            localStorage.setItem(REACH_STORAGE_KEYS.SPACE_BOOKINGS, JSON.stringify(SEED_SPACE_BOOKINGS));
        }
        if (!localStorage.getItem(REACH_STORAGE_KEYS.COMPLAINTS)) {
            localStorage.setItem(REACH_STORAGE_KEYS.COMPLAINTS, JSON.stringify(SEED_COMPLAINTS));
        }
        if (!localStorage.getItem(REACH_STORAGE_KEYS.EVENTS)) {
            localStorage.setItem(REACH_STORAGE_KEYS.EVENTS, JSON.stringify(SEED_EVENTS));
        }
        if (!localStorage.getItem(REACH_STORAGE_KEYS.VERIFICATIONS)) {
            localStorage.setItem(REACH_STORAGE_KEYS.VERIFICATIONS, JSON.stringify(SEED_VERIFICATIONS));
        }
    },

    // Session & Authentication
    isLoggedIn() {
        if (localStorage.getItem('reach_auth_active') === 'false') return false;
        return localStorage.getItem('reach_is_logged_in') === 'true' || localStorage.getItem('reach_auth_active') === 'true';
    },

    getCurrentUser() {
        if (!this.isLoggedIn()) return null;
        const saved = localStorage.getItem(REACH_STORAGE_KEYS.USER_SESSION);
        if (saved) {
            try { return JSON.parse(saved); } catch (e) {}
        }
        if (window.AuthSession && typeof AuthSession.getCurrentUser === 'function') {
            return AuthSession.getCurrentUser();
        }
        return null;
    },

    setCurrentUserRole(roleKey) {
        if (SEED_PROFILES[roleKey]) {
            localStorage.setItem(REACH_STORAGE_KEYS.USER_SESSION, JSON.stringify(SEED_PROFILES[roleKey]));
            localStorage.setItem('reach_is_logged_in', 'true');
            localStorage.setItem('reach_auth_active', 'true');
            return SEED_PROFILES[roleKey];
        }
        return null;
    },

    loginUser(phone, roleKey) {
        this.init();
        let profile = SEED_PROFILES[roleKey] || SEED_PROFILES.resident;
        const customUsers = JSON.parse(localStorage.getItem('reach_custom_users') || '[]');
        const matched = customUsers.find(u => u.phone === phone);
        if (matched) profile = matched;

        localStorage.setItem(REACH_STORAGE_KEYS.USER_SESSION, JSON.stringify(profile));
        localStorage.setItem('reach_is_logged_in', 'true');
        return profile;
    },

    registerUser(userData) {
        this.init();
        const customUsers = JSON.parse(localStorage.getItem('reach_custom_users') || '[]');
        const newProfile = {
            id: 'usr_' + Date.now(),
            name: userData.name,
            phone: userData.phone,
            role: userData.role || 'resident',
            roleTitle: {
                resident: 'Senior Citizen / Resident',
                volunteer: 'Community Volunteer',
                owner: 'Space Provider',
                ngo: 'NGO Partner',
                admin: 'Platform Support'
            }[userData.role] || 'Community Resident',
            address: userData.address || 'Sector 4',
            avatar: userData.role === 'volunteer' ? '🦸‍♂️' : (userData.role === 'owner' ? '🏛️' : (userData.role === 'ngo' ? '🤝' : '👤')),
            verified: true,
            createdAt: new Date().toLocaleDateString('en-GB')
        };
        customUsers.push(newProfile);
        localStorage.setItem('reach_custom_users', JSON.stringify(customUsers));
        localStorage.setItem(REACH_STORAGE_KEYS.USER_SESSION, JSON.stringify(newProfile));
        localStorage.setItem('reach_is_logged_in', 'true');
        return newProfile;
    },

    logoutUser() {
        localStorage.setItem('reach_is_logged_in', 'false');
        localStorage.removeItem(REACH_STORAGE_KEYS.USER_SESSION);
        if (window.AuthSession && typeof AuthSession.logout === 'function') {
            AuthSession.logout();
        } else {
            localStorage.setItem('reach_auth_active', 'false');
            localStorage.removeItem('reach_auth_user');
            localStorage.removeItem('reach_auth_role');
            window.location.replace('index.html');
        }
    },

    // Requests (Micro-Volunteering)
    getRequests() {
        this.init();
        const list = JSON.parse(localStorage.getItem(REACH_STORAGE_KEYS.REQUESTS) || '[]');
        try {
            const rawTasks = JSON.parse(localStorage.getItem('reach_tasks') || '[]');
            rawTasks.forEach(t => {
                if (!list.some(r => r.id === t.id)) {
                    list.push({
                        id: t.id,
                        category: t.category || t.title || 'Everyday Help',
                        icon: (t.category || '').includes('Medicine') ? '💊' : (t.category || '').includes('Grocer') ? '🛒' : '🤝',
                        userName: t.requester || 'Resident Member',
                        userPhone: t.requesterPhone || '+91 98765 43210',
                        address: t.location || 'Sector 4',
                        urgency: t.urgency || 'Normal',
                        time: t.time || 'Today',
                        notes: t.notes || t.title || 'Help requested by senior member',
                        status: t.status === 'Task Completed' ? 'completed' : (t.status === 'Live Location Active' || t.status === 'Accepted') ? 'location_active' : 'waiting_volunteer',
                        otpCode: t.safetyPin || '4829',
                        assignedVolunteer: t.assignedVolunteer || null,
                        createdAt: t.createdAt || 'Today'
                    });
                }
            });
        } catch (e) {}
        return list;
    },

    getRequestById(id) {
        return this.getRequests().find(r => r.id === id);
    },

    addRequest(newReq) {
        const list = this.getRequests();
        const id = newReq.id || ('RCH-2026-' + Math.floor(1000 + Math.random() * 9000));
        const reqRecord = {
            id,
            createdAt: 'Just now',
            status: 'waiting_volunteer',
            otpCode: newReq.safetyPin || Math.floor(1000 + Math.random() * 9000).toString(),
            assignedVolunteer: null,
            etaMinutes: 15,
            ...newReq
        };
        list.unshift(reqRecord);
        localStorage.setItem(REACH_STORAGE_KEYS.REQUESTS, JSON.stringify(list));
        return reqRecord;
    },

    updateRequestStatus(id, newStatus, extraData = {}) {
        const list = this.getRequests();
        const item = list.find(r => r.id === id);
        if (item) {
            item.status = newStatus;
            Object.assign(item, extraData);
            localStorage.setItem(REACH_STORAGE_KEYS.REQUESTS, JSON.stringify(list));
        }

        // Also update reach_tasks in sync
        try {
            const tasks = JSON.parse(localStorage.getItem('reach_tasks') || '[]');
            let matched = tasks.find(t => t.id === id);
            if (!matched && (newStatus === 'location_active' || newStatus === 'accepted')) {
                const lastStr = localStorage.getItem('reach_last_confirmed');
                if (lastStr) {
                    try {
                        const lastItem = JSON.parse(lastStr);
                        if (lastItem && lastItem.id) matched = tasks.find(t => t.id === lastItem.id);
                    } catch (e) {}
                }
                if (!matched) matched = tasks.find(t => t.status === 'Waiting for Volunteer');
            }
            if (matched) {
                if (newStatus === 'location_active' || newStatus === 'accepted') {
                    matched.status = 'Live Location Active';
                    matched.assignedVolunteer = extraData.assignedVolunteer || {
                        name: 'Karan Verma',
                        phone: '+91 98765 43211',
                        rating: 4.9,
                        avatar: '🦸‍♂️'
                    };
                } else if (newStatus === 'completed') {
                    matched.status = 'Task Completed';
                }
                localStorage.setItem('reach_tasks', JSON.stringify(tasks));
            }
        } catch (e) {}

        // Also update reach_last_confirmed in sync
        try {
            const lastStr = localStorage.getItem('reach_last_confirmed');
            if (lastStr) {
                const lastItem = JSON.parse(lastStr);
                if (newStatus === 'location_active' || newStatus === 'accepted') {
                    lastItem.status = 'Live Location Active';
                    lastItem.assignedVolunteer = 'Karan Verma';
                    lastItem.assignedVolunteerPhone = '+91 98765 43211';
                } else if (newStatus === 'completed') {
                    lastItem.status = 'Task Completed';
                }
                localStorage.setItem('reach_last_confirmed', JSON.stringify(lastItem));
            }
        } catch (e) {}

        return item;
    },

    // Spaces & Bookings
    getSpaces() {
        this.init();
        return JSON.parse(localStorage.getItem(REACH_STORAGE_KEYS.SPACES) || '[]');
    },

    addSpace(space) {
        const list = this.getSpaces();
        const id = 'spc_' + Math.floor(100 + Math.random() * 900);
        const record = { id, status: 'verified', rating: 5.0, ...space };
        list.push(record);
        localStorage.setItem(REACH_STORAGE_KEYS.SPACES, JSON.stringify(list));
        return record;
    },

    getSpaceBookings() {
        this.init();
        return JSON.parse(localStorage.getItem(REACH_STORAGE_KEYS.SPACE_BOOKINGS) || '[]');
    },

    addSpaceBooking(booking) {
        const list = this.getSpaceBookings();
        const id = 'SPACE-2026-' + Math.floor(500 + Math.random() * 499);
        const record = {
            id,
            status: 'pending_approval',
            qrCodeToken: 'QR-PASS-' + id,
            createdAt: 'Just now',
            checkInTime: null,
            checkOutTime: null,
            ...booking
        };
        list.unshift(record);
        localStorage.setItem(REACH_STORAGE_KEYS.SPACE_BOOKINGS, JSON.stringify(list));
        return record;
    },

    updateSpaceBookingStatus(id, newStatus, extraData = {}) {
        const list = this.getSpaceBookings();
        const item = list.find(b => b.id === id);
        if (item) {
            item.status = newStatus;
            Object.assign(item, extraData);
            localStorage.setItem(REACH_STORAGE_KEYS.SPACE_BOOKINGS, JSON.stringify(list));
        }
        return item;
    },

    // Complaints / Grievance Redressal
    getComplaints() {
        this.init();
        return JSON.parse(localStorage.getItem(REACH_STORAGE_KEYS.COMPLAINTS) || '[]');
    },

    addComplaint(complaint) {
        const list = this.getComplaints();
        const id = 'CMP-2026-' + Math.floor(100 + Math.random() * 900);
        const record = {
            id,
            status: 'under_investigation',
            createdAt: 'Just now',
            ...complaint
        };
        list.unshift(record);
        localStorage.setItem(REACH_STORAGE_KEYS.COMPLAINTS, JSON.stringify(list));
        return record;
    },

    updateComplaintStatus(id, newStatus, actionTaken = '') {
        const list = this.getComplaints();
        const item = list.find(c => c.id === id);
        if (item) {
            item.status = newStatus;
            if (actionTaken) item.actionTaken = actionTaken;
            localStorage.setItem(REACH_STORAGE_KEYS.COMPLAINTS, JSON.stringify(list));
        }
        return item;
    },

    // Events
    getEvents() {
        this.init();
        return JSON.parse(localStorage.getItem(REACH_STORAGE_KEYS.EVENTS) || '[]');
    },

    addEvent(eventData) {
        const list = this.getEvents();
        const id = 'EVT-2026-' + (list.length + 1).toString().padStart(2, '0');
        const record = { id, volunteersRegistered: 0, ...eventData };
        list.unshift(record);
        localStorage.setItem(REACH_STORAGE_KEYS.EVENTS, JSON.stringify(list));
        return record;
    },

    // Verifications
    getVerifications() {
        this.init();
        return JSON.parse(localStorage.getItem(REACH_STORAGE_KEYS.VERIFICATIONS) || '[]');
    },

    updateVerificationStatus(id, newStatus) {
        const list = this.getVerifications();
        const item = list.find(v => v.id === id);
        if (item) {
            item.status = newStatus;
            localStorage.setItem(REACH_STORAGE_KEYS.VERIFICATIONS, JSON.stringify(list));
        }
        return item;
    }
};

// Initialize immediately
ReachData.init();
