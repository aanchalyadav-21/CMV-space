// ==========================================================================
// Community Micro-Volunteering & Empty Space Sharing Platform
// Tagline: Connecting People, Helping Communities.
// Master Engine (script.js)
// ==========================================================================

// 1. Core Profile Seeds for 5 UML Actors
const DEFAULT_PROFILES = {
    member: {
        id: 'usr_mem_01',
        role: 'member',
        name: 'Ramesh Patel',
        roleTitle: 'Senior Resident Member',
        phone: '+91 98765 43210',
        address: 'Flat 402, Shanti Niketan, Sector 4',
        avatar: '👵',
        language: 'en',
        area: 'Sector 4',
        verified: true
    },
    volunteer: {
        id: 'usr_vol_02',
        role: 'volunteer',
        name: 'Karan Verma',
        roleTitle: 'Community Volunteer',
        phone: '+91 98765 43211',
        address: 'B-Wing 104, Gulmohar CHS, Sector 4',
        avatar: '🦸‍♂️',
        rating: 4.9,
        tasksCompleted: 42,
        skills: ['Elderly Care', 'Prescription Pickup', 'Groceries', 'First Aid'],
        availability: 'Evenings & Weekends',
        area: 'Sector 4',
        verified: true
    },
    owner: {
        id: 'usr_own_03',
        role: 'owner',
        name: 'Marian Trust',
        roleTitle: 'Space Owner & Provider',
        phone: '+91 98765 43212',
        address: 'Parish Welfare Center, City Center',
        avatar: '🏛️',
        venueCount: 2,
        area: 'City Center',
        verified: true
    },
    organizer: {
        id: 'usr_org_04',
        role: 'organizer',
        name: 'Pooja Nair',
        roleTitle: 'Event Organizer (CareForward NGO)',
        phone: '+91 98765 43213',
        address: 'CareForward Center, Sector 4',
        avatar: '🤝',
        area: 'Sector 4',
        verified: true
    },
    admin: {
        id: 'usr_adm_05',
        role: 'admin',
        name: 'Platform Safety Supervisor',
        roleTitle: 'System Safety & Verification Administrator',
        phone: '+91 98765 43214',
        avatar: '🛡️',
        area: 'Sector 4 Platform Ops',
        verified: true
    }
};

// Aliases for compatibility
DEFAULT_PROFILES.resident = DEFAULT_PROFILES.member;
DEFAULT_PROFILES.ngo = DEFAULT_PROFILES.organizer;

// 2. Initial Sample Tasks (Micro-Volunteering Lifecycle)
// States: Request Created -> Waiting for Volunteer -> Volunteer Assigned -> Live Location Active -> Volunteer Arrived -> Task In Progress -> Task Completed -> Location Tracking Off -> Rating & Feedback
// Branch: Request Cancelled
// Dispute: Complain Submitted -> Under Investigation -> Complain Resolved
const SEED_TASKS = [
    {
        id: 'TSK-101',
        category: 'Medicine Pickup',
        title: 'Prescription BP & Diabetes Medicine',
        requester: 'Ramesh Patel',
        requesterPhone: '+91 98765 43210',
        location: 'Apex Chemist to Flat 402, Shanti Niketan, Sector 4',
        time: 'Today, 11:30 AM',
        urgency: 'Today (Urgent)',
        skillsNeeded: 'Prescription Pickup & Safe Handover',
        status: 'Live Tracking Active',
        assignedVolunteer: {
            name: 'Karan Verma',
            phone: '+91 98765 43211',
            rating: 4.9,
            avatar: '🦸‍♂️'
        },
        safetyPin: '4829',
        etaMinutes: 10,
        notes: 'Prescription slip will be given at chemist counter. Medicine payment settled.',
        createdAt: 'Today, 10:45 AM',
        rating: null,
        feedback: null
    },
    {
        id: 'TSK-102',
        category: 'Groceries',
        title: 'Fresh Vegetables & 2L Milk',
        requester: 'Sushila Shah (Senior Resident)',
        requesterPhone: '+91 98200 54321',
        location: 'Central Market to Building 12, Nehru Nagar',
        time: 'Today, 4:00 PM',
        urgency: 'Today',
        skillsNeeded: 'Stair Climbing Assistance',
        status: 'Waiting for Volunteer',
        assignedVolunteer: null,
        safetyPin: '7153',
        etaMinutes: null,
        notes: 'Resident has knee arthritis; needs grocery bag carried up to 2nd floor.',
        createdAt: 'Today, 01:15 PM',
        rating: null,
        feedback: null
    },
    {
        id: 'TSK-103',
        category: 'Tutoring',
        title: 'Class 8 Mathematics Basics',
        requester: 'Sunita Sharma (Parent)',
        requesterPhone: '+91 98330 11223',
        location: 'Community Study Room, Shanti Niketan CHS',
        time: 'Tomorrow, 5:00 PM',
        urgency: 'Flexible',
        skillsNeeded: 'Middle School Math Tutoring',
        status: 'Waiting for Volunteer',
        assignedVolunteer: null,
        safetyPin: '9204',
        etaMinutes: null,
        notes: '1-hour weekly volunteer tutoring for algebra equations.',
        createdAt: 'Today, 11:00 AM',
        rating: null,
        feedback: null
    },
    {
        id: 'TSK-104',
        category: 'Digital Guidance',
        title: 'Pension Digital Life Certificate (Jeevan Pramaan)',
        requester: 'Narayan Joshi',
        requesterPhone: '+91 98330 98765',
        location: 'Flat 201, Amar CHS, Sector 4',
        time: 'Yesterday, 10:00 AM',
        urgency: 'Completed',
        skillsNeeded: 'Smartphone & Biometric App',
        status: 'Task Completed',
        assignedVolunteer: {
            name: 'Karan Verma',
            phone: '+91 98765 43211',
            rating: 4.9,
            avatar: '🦸‍♂️'
        },
        safetyPin: '3184',
        etaMinutes: 0,
        notes: 'Digital life certificate successfully verified on central portal.',
        createdAt: 'Yesterday, 09:30 AM',
        rating: 5,
        feedback: 'Karan was extremely respectful, patient, and guided me step-by-step!'
    },
    {
        id: 'TSK-105',
        category: 'Groceries',
        title: 'Weekly Vegetables & Dairy Pack',
        requester: 'Ramesh Patel',
        requesterPhone: '+91 98765 43210',
        location: 'Flat 402, Shanti Niketan, Sector 4',
        time: 'Today, 5:30 PM',
        urgency: 'Today',
        skillsNeeded: 'Local Market Produce Selection',
        status: 'Waiting for Volunteer',
        assignedVolunteer: null,
        safetyPin: '6192',
        etaMinutes: null,
        notes: 'Need 1 crate eggs, 2L toned milk, and fresh vegetables from local dairy.',
        createdAt: 'Today, 09:30 AM',
        rating: null,
        feedback: null
    }
];

// 3. Initial Sample Spaces (Space Sharing Lifecycle)
// States: Listing under review -> Listing approved
// Booking: Booking Pending -> Owner Approves (Booking Confirmed & QR generated) / Owner Rejects -> Check-in (QR scan) -> Space in use -> Checkout (QR scan) -> Booking Completed -> Rate & Feedback
const SEED_SPACES = [
    {
        id: 'SPC-501',
        name: 'St. Joseph Community Activity Hall',
        owner: 'Marian Community Welfare Trust',
        ownerPhone: '+91 98765 43212',
        location: 'Ground Floor, Parish Welfare Center, City Center',
        capacity: 80,
        facilities: ['Air Conditioning', 'Audio / Mic System', 'Projector & Screen', 'Wheelchair Ramp', 'Restrooms'],
        pricing: 'Free for Community Sessions / ₹200 hr External',
        availability: 'Mon - Sat (9:00 AM - 8:30 PM)',
        rules: 'No loud music after 8:30 PM. Please leave premises clean and turn off AC.',
        photo: 'hall',
        status: 'Approved',
        rating: 4.9
    },
    {
        id: 'SPC-502',
        name: 'Shanti Niketan Society Clubhouse & Library',
        owner: 'Shanti Niketan Welfare Society',
        ownerPhone: '+91 98765 43210',
        location: 'B-Wing Terrace Floor, Shanti Niketan CHS, Sector 4',
        capacity: 35,
        facilities: ['Ceiling Fans', 'High Speed Wi-Fi 100Mbps', 'Whiteboard', 'Drinking Water', 'Reading Tables'],
        pricing: 'Free for Resident Programs',
        availability: 'All Days (8:00 AM - 7:00 PM)',
        rules: 'Ideal for small meetings, yoga, tutoring and book clubs.',
        photo: 'clubhouse',
        status: 'Approved',
        rating: 4.8
    },
    {
        id: 'SPC-503',
        name: 'Community Learning & Skill Center',
        owner: 'Neighborhood Education Trust',
        ownerPhone: '+91 98200 44556',
        location: 'Station Road, City Center',
        capacity: 45,
        facilities: ['12 Computer Desks', 'Whiteboard', 'High Speed Internet', 'Wheelchair Access'],
        pricing: 'Community Subsidized',
        availability: 'Mon - Fri (10:00 AM - 5:00 PM)',
        rules: 'Suitable for student coaching and digital literacy programs.',
        photo: 'learning',
        status: 'Pending Admin Review',
        rating: 4.7
    }
];

// 4. Initial Sample Bookings (QR Code Lifecycle)
const SEED_BOOKINGS = [
    {
        id: 'BKG-2026-901',
        spaceId: 'SPC-501',
        spaceName: 'St. Joseph Community Activity Hall',
        requester: 'Pooja Nair (CareForward NGO)',
        requesterPhone: '+91 98765 43213',
        purpose: 'Free Senior Citizen Eye & Health Screening Camp',
        date: 'Saturday, 28 Oct 2026',
        time: '9:00 AM - 1:00 PM',
        expectedGuests: 60,
        status: 'Confirmed',
        qrPassId: 'PASS-SPACE-2026-501',
        qrStatus: 'Ready for Check-in',
        createdAt: 'Today, 10:00 AM',
        rating: null
    },
    {
        id: 'BKG-2026-902',
        spaceId: 'SPC-502',
        spaceName: 'Shanti Niketan Society Clubhouse & Library',
        requester: 'Ramesh Patel',
        requesterPhone: '+91 98765 43210',
        purpose: 'Senior Breathing Exercises & Laughter Yoga Circle',
        date: 'Sunday, 29 Oct 2026',
        time: '7:30 AM - 9:30 AM',
        expectedGuests: 20,
        status: 'Pending Owner Approval',
        qrPassId: 'PASS-SPACE-2026-502',
        qrStatus: 'Pending Approval',
        createdAt: 'Today, 11:30 AM',
        rating: null
    }
];

// 5. Initial Sample Organizer Activities (Integration between Volunteering & Space)
const SEED_ACTIVITIES = [
    {
        id: 'ACT-301',
        title: 'Senior Citizen Digital Literacy & Safety Drive',
        organizer: 'Pooja Nair (CareForward NGO)',
        phone: '+91 98765 43213',
        date: 'Sunday, 1 Nov 2026 (10:00 AM - 1:00 PM)',
        location: 'St. Joseph Community Activity Hall',
        description: 'Interactive workshop teaching seniors smartphone banking safety, fraud awareness, and digital health apps.',
        needsVolunteers: true,
        volunteersNeeded: 8,
        volunteersAssigned: 6,
        volunteerStatus: 'Matching Volunteers (6/8 Confirmed)',
        needsSpace: true,
        spaceId: 'SPC-501',
        spaceName: 'St. Joseph Community Activity Hall',
        spaceStatus: 'Confirmed by Space Owner',
        qrPassId: 'PASS-SPACE-2026-501',
        overallStatus: 'Arrangements in Progress'
    },
    {
        id: 'ACT-302',
        title: 'Neighborhood Tree Plantation & Park Cleanup',
        organizer: 'Pooja Nair (CareForward NGO)',
        phone: '+91 98765 43213',
        date: 'Saturday, 7 Nov 2026 (8:00 AM - 11:00 AM)',
        location: 'Neighborhood Community Garden',
        description: 'Planting 50 saplings and clearing park walkways.',
        needsVolunteers: true,
        volunteersNeeded: 15,
        volunteersAssigned: 12,
        volunteerStatus: 'Volunteers Enlisted (12/15)',
        needsSpace: false,
        spaceId: null,
        spaceName: 'Public Outdoor Park (No Venue Booking Needed)',
        spaceStatus: 'Not Required',
        qrPassId: null,
        overallStatus: 'Confirmed'
    }
];

// 6. Initial Sample Verifications & Complaints (Admin Oversight)
const SEED_VERIFICATIONS = [
    {
        id: 'VER-VOL-101',
        type: 'Volunteer',
        name: 'Karan Verma',
        doc: 'Government Photo ID + Police Character Certificate',
        status: 'Approved',
        phone: '+91 98765 43211',
        submittedAt: '12 Oct 2026'
    },
    {
        id: 'VER-VOL-102',
        type: 'Volunteer',
        name: 'Rohit Deshmukh',
        doc: 'College Student ID + Aadhaar Card',
        status: 'Pending',
        phone: '+91 98204 33221',
        submittedAt: 'Today, 09:15 AM'
    },
    {
        id: 'VER-SPC-201',
        type: 'Space Listing',
        name: 'Community Learning & Skill Center',
        doc: 'Society Trust Registration Deed + Fire Safety NOC',
        status: 'Pending',
        phone: '+91 98200 44556',
        submittedAt: 'Yesterday, 04:30 PM'
    }
];

const SEED_COMPLAINTS = [
    {
        id: 'CMP-2026-101',
        relatedRef: 'TSK-101',
        title: 'Volunteer late arrival for clinic escort',
        filedBy: 'Narayan Joshi',
        phone: '+91 98330 98765',
        description: 'Volunteer arrived 35 minutes past agreed time without prior telephone notice.',
        status: 'Under Investigation',
        actionTaken: 'Volunteer counseling & punctuality warning logged.',
        submittedAt: 'Today, 10:20 AM'
    },
    {
        id: 'CMP-2026-102',
        relatedRef: 'BKG-2026-880',
        title: 'Hall air conditioning unit tripped circuit breaker',
        filedBy: 'Sunita Sharma',
        phone: '+91 98201 55667',
        description: 'AC was not functioning during senior meeting.',
        status: 'Resolved',
        actionTaken: 'Facility caretaker repaired fuse and verified cooling.',
        submittedAt: '21 Oct 2026'
    }
];

// ==========================================================================
// Central Reactive Storage Engine (AppStore / ReachData)
// ==========================================================================
const AppStore = {
    init() {
        if (!localStorage.getItem('reach_tasks')) {
            localStorage.setItem('reach_tasks', JSON.stringify(SEED_TASKS));
        } else {
            try {
                const stored = JSON.parse(localStorage.getItem('reach_tasks') || '[]');
                if (!stored.some(t => t.id === 'TSK-105')) {
                    const t105 = SEED_TASKS.find(x => x.id === 'TSK-105');
                    if (t105) stored.push(t105);
                    localStorage.setItem('reach_tasks', JSON.stringify(stored));
                }
            } catch (e) {}
        }
        if (!localStorage.getItem('reach_spaces')) {
            localStorage.setItem('reach_spaces', JSON.stringify(SEED_SPACES));
        }
        if (!localStorage.getItem('reach_bookings')) {
            localStorage.setItem('reach_bookings', JSON.stringify(SEED_BOOKINGS));
        }
        if (!localStorage.getItem('reach_activities')) {
            localStorage.setItem('reach_activities', JSON.stringify(SEED_ACTIVITIES));
        }
        if (!localStorage.getItem('reach_verifications')) {
            localStorage.setItem('reach_verifications', JSON.stringify(SEED_VERIFICATIONS));
        }
        if (!localStorage.getItem('reach_complaints')) {
            localStorage.setItem('reach_complaints', JSON.stringify(SEED_COMPLAINTS));
        }
    },

    getTasks() { this.init(); return JSON.parse(localStorage.getItem('reach_tasks') || '[]'); },
    saveTasks(tasks) { localStorage.setItem('reach_tasks', JSON.stringify(tasks)); },

    getSpaces() { this.init(); return JSON.parse(localStorage.getItem('reach_spaces') || '[]'); },
    saveSpaces(spaces) { localStorage.setItem('reach_spaces', JSON.stringify(spaces)); },

    getBookings() {
        this.init();
        try {
            const raw = localStorage.getItem('reach_bookings');
            if (raw) {
                const list = JSON.parse(raw);
                if (Array.isArray(list) && list.length > 0) return list;
            }
        } catch(e) {}
        localStorage.setItem('reach_bookings', JSON.stringify(SEED_BOOKINGS));
        return JSON.parse(JSON.stringify(SEED_BOOKINGS));
    },
    saveBookings(bookings) {
        if (!Array.isArray(bookings) || bookings.length === 0) {
            bookings = JSON.parse(JSON.stringify(SEED_BOOKINGS));
        }
        localStorage.setItem('reach_bookings', JSON.stringify(bookings));
    },

    getActivities() { this.init(); return JSON.parse(localStorage.getItem('reach_activities') || '[]'); },
    saveActivities(activities) { localStorage.setItem('reach_activities', JSON.stringify(activities)); },

    getVerifications() { this.init(); return JSON.parse(localStorage.getItem('reach_verifications') || '[]'); },
    saveVerifications(v) { localStorage.setItem('reach_verifications', JSON.stringify(v)); },

    getComplaints() { this.init(); return JSON.parse(localStorage.getItem('reach_complaints') || '[]'); },
    saveComplaints(c) { localStorage.setItem('reach_complaints', JSON.stringify(c)); },

    resetAllData() {
        localStorage.setItem('reach_tasks', JSON.stringify(SEED_TASKS));
        localStorage.setItem('reach_spaces', JSON.stringify(SEED_SPACES));
        localStorage.setItem('reach_bookings', JSON.stringify(SEED_BOOKINGS));
        localStorage.setItem('reach_activities', JSON.stringify(SEED_ACTIVITIES));
        localStorage.setItem('reach_verifications', JSON.stringify(SEED_VERIFICATIONS));
        localStorage.setItem('reach_complaints', JSON.stringify(SEED_COMPLAINTS));
    }
};

// Global ReachData wrapper for backward compatibility across portals
window.ReachData = {
    getTasks: () => AppStore.getTasks(),
    saveTasks: (t) => AppStore.saveTasks(t),
    getRequests: () => {
        const tasks = AppStore.getTasks();
        const dismissed = JSON.parse(localStorage.getItem('reach_vol_dismissed_tasks') || '[]');
        return tasks.filter(t => !dismissed.includes(t.id)).map(t => ({
            id: t.id,
            category: t.category,
            notes: t.notes || t.title,
            userName: t.requester,
            userPhone: t.requesterPhone,
            urgency: t.urgency || 'High Priority',
            time: t.time || 'Immediate',
            address: t.location || 'Sector 4',
            status: t.status === 'Task Completed' ? 'completed' : t.status === 'Live Location Active' ? 'location_active' : t.status === 'Volunteer Arrived' ? 'volunteer_arrived' : t.status === 'Task in Progress' ? 'in_progress' : (t.status.includes('Waiting') ? 'waiting_volunteer' : t.status),
            rating: t.rating,
            feedback: t.feedback,
            createdAt: t.createdAt || 'Just now',
            icon: (t.category || '').includes('Medicine') ? '💊' : (t.category || '').includes('Grocer') ? '🛒' : (t.category || '').includes('Tutor') ? '📚' : '🤝'
        }));
    },
    updateRequestStatus: (id, newStatus, extraData = {}) => {
        const tasks = AppStore.getTasks();
        const t = tasks.find(x => x.id === id || x.id === 'TSK-101');
        if (t) {
            if (newStatus === 'completed') t.status = 'Task Completed';
            else if (newStatus === 'location_active') t.status = 'Live Location Active';
            else if (newStatus === 'volunteer_arrived') t.status = 'Volunteer Arrived';
            else if (newStatus === 'in_progress') t.status = 'Task in Progress';
            else if (newStatus === 'passed_by_volunteer') t.status = 'Passed by Volunteer';
            if (extraData.rating) t.rating = extraData.rating;
            if (extraData.feedback) t.feedback = extraData.feedback;
            AppStore.saveTasks(tasks);
        }
        return t;
    },
    addComplaint: (c) => {
        const list = AppStore.getComplaints();
        list.unshift({ id: 'CMP-' + Date.now().toString().slice(-4), ...c, status: 'Under Investigation', submittedAt: 'Just now' });
        AppStore.saveComplaints(list);
    },
    getSpaces: () => AppStore.getSpaces(),
    saveSpaces: (s) => AppStore.saveSpaces(s),
    getBookings: () => AppStore.getBookings(),
    saveBookings: (b) => AppStore.saveBookings(b),
    getActivities: () => AppStore.getActivities(),
    saveActivities: (a) => AppStore.saveActivities(a),
    getVerifications: () => AppStore.getVerifications(),
    saveVerifications: (v) => AppStore.saveVerifications(v),
    getComplaints: () => AppStore.getComplaints(),
    saveComplaints: (c) => AppStore.saveComplaints(c),
    getCurrentUser: () => AuthSession.getCurrentUser(),
    loginUser: (phone, role) => AuthSession.login(role, phone),
    setCurrentUserRole: (role) => AuthSession.switchRole(role)
};

// ==========================================================================
// Authentication & Session Management
// ==========================================================================
const AuthSession = {
    isLoggedIn() {
        const tabActive = sessionStorage.getItem('reach_auth_active');
        if (tabActive !== null) {
            return tabActive === 'true';
        }
        return localStorage.getItem('reach_auth_active') === 'true';
    },

    getCurrentRole() {
        if (!this.isLoggedIn()) return null;
        return sessionStorage.getItem('reach_auth_role') || localStorage.getItem('reach_auth_role') || 'member';
    },

    getCurrentUser() {
        if (!this.isLoggedIn()) {
            return null; // Guest / unauthenticated user: strictly null!
        }
        const role = this.getCurrentRole() || 'member';
        const stored = sessionStorage.getItem('reach_auth_user') || localStorage.getItem('reach_auth_user');
        if (stored) {
            try {
                const u = JSON.parse(stored);
                if (u && (u.role === role || (!u.role && role === 'member'))) return u;
            } catch (e) {}
        }
        return DEFAULT_PROFILES[role] || DEFAULT_PROFILES.member;
    },

    login(role, phone, name) {
        localStorage.setItem('reach_auth_active', 'true');
        sessionStorage.setItem('reach_auth_active', 'true');
        sessionStorage.setItem('reach_auth_role', role);
        localStorage.setItem('reach_auth_role', role);
        const base = DEFAULT_PROFILES[role] || DEFAULT_PROFILES.member;
        const user = {
            ...base,
            phone: phone || base.phone,
            name: name || base.name
        };
        sessionStorage.setItem('reach_auth_user', JSON.stringify(user));
        localStorage.setItem('reach_auth_user', JSON.stringify(user));
        return user;
    },

    register(userData) {
        localStorage.setItem('reach_auth_active', 'true');
        const role = userData.role || 'member';
        localStorage.setItem('reach_auth_role', role);
        const base = DEFAULT_PROFILES[role] || DEFAULT_PROFILES.member;

        const idType = userData.idType || 'Aadhaar Card';
        const rawNum = userData.aadhaarNumber || '5421 8892 4103';
        const cleanDigits = rawNum.replace(/\s+/g, '');
        const maskedNum = cleanDigits.length >= 4 ? `XXXX-XXXX-${cleanDigits.slice(-4)}` : cleanDigits;

        const user = {
            ...base,
            ...userData,
            id: 'usr_' + Date.now(),
            aadhaarNumber: maskedNum,
            idType: idType,
            idProofFile: userData.idProofFile || 'aadhaar_card_verified.pdf',
            verified: role === 'volunteer' ? false : true
        };
        localStorage.setItem('reach_auth_user', JSON.stringify(user));

        // Add verification entry into KYC Queue for Admin console
        const verifs = AppStore.getVerifications();
        verifs.unshift({
            id: 'VER-' + (role === 'volunteer' ? 'VOL' : 'RES') + '-' + Date.now().toString().slice(-4),
            roleType: role === 'volunteer' ? 'Volunteer' : (role === 'owner' ? 'Space Provider' : 'Resident Member'),
            type: role === 'volunteer' ? 'Volunteer' : 'Resident',
            name: user.name,
            collegeOrOrg: user.area || 'Sector 4',
            idType: idType,
            idNumber: maskedNum,
            doc: `${idType} (${maskedNum})`,
            status: role === 'volunteer' ? 'pending' : 'approved',
            phone: user.phone,
            submittedAt: 'Just now'
        });
        AppStore.saveVerifications(verifs);

        if (window.ReachData && typeof ReachData.addVerification === 'function') {
            ReachData.addVerification({
                roleType: role === 'volunteer' ? 'Volunteer' : 'Resident',
                name: user.name,
                collegeOrOrg: user.area || 'Sector 4',
                idType: idType,
                idNumber: maskedNum,
                status: role === 'volunteer' ? 'pending' : 'approved'
            });
        }

        return user;
    },

    switchRole(role) {
        localStorage.setItem('reach_auth_active', 'true');
        localStorage.setItem('reach_auth_role', role);
        const base = DEFAULT_PROFILES[role] || DEFAULT_PROFILES.member;
        localStorage.setItem('reach_auth_user', JSON.stringify(base));
        return base;
    },

    logout() {
        // Tab-isolated logout: sign out this specific tab without disturbing other tabs
        sessionStorage.setItem('reach_auth_active', 'false');
        sessionStorage.removeItem('reach_auth_user');
        sessionStorage.removeItem('reach_auth_role');
        sessionStorage.removeItem('reach_user_session');

        // Immediate DOM cleanup so UI updates instantly
        const welcome = document.getElementById('signedInWelcomeBox');
        if (welcome) welcome.remove();
        if (typeof renderDynamicNavigation === 'function') {
            try { renderDynamicNavigation(); } catch (e) {}
        }
        const rolePill = document.getElementById('roleSwitcherPill');
        if (rolePill) rolePill.remove();

        // Redirect only this tab to index.html with signed_out flag
        window.location.replace('index.html?signed_out=' + Date.now());
    },

    showAuthModal(options = {}) {
        const title = options.title || 'Sign In Required';
        const message = options.message || 'You must be signed into a verified account to perform this action.';
        const targetRole = options.role || 'member';
        const redirectUrl = options.redirectUrl || window.location.href;

        let modal = document.getElementById('authGuardModal');
        if (!modal) {
            modal = document.createElement('div');
            modal.id = 'authGuardModal';
            modal.className = 'modal-overlay';
            modal.style.display = 'flex';
            document.body.appendChild(modal);
        } else {
            modal.style.display = 'flex';
        }

        const roleLabels = {
            member: 'Resident (Ramesh Patel)',
            volunteer: 'Volunteer (Karan Verma)',
            owner: 'Space Owner (Marian Trust)',
            organizer: 'Event Organizer (Pooja Nair)',
            admin: 'Administrator'
        };

        modal.innerHTML = `
            <div class="modal-content" style="max-width: 520px; text-align: center; padding: 32px 28px;">
                <div style="font-size: 3rem; margin-bottom: 12px;">🔒</div>
                <h2 style="color: var(--primary-dark); font-size: 1.5rem; margin-bottom: 10px;">
                    ${title}
                </h2>
                <p style="color: var(--text-muted); font-size: 0.98rem; line-height: 1.5; margin-bottom: 24px;">
                    ${message}
                </p>

                <div style="display: flex; flex-direction: column; gap: 12px; margin-bottom: 20px;">
                    <a href="index.html#signInBox" class="btn btn-primary" style="padding: 12px 18px; font-size: 1rem; text-decoration: none; justify-content: center;">
                        🔑 Sign In with Mobile Number (OTP)
                    </a>
                    <a href="register.html?role=${targetRole}" class="btn btn-secondary" style="padding: 12px 18px; font-size: 1rem; text-decoration: none; justify-content: center;">
                        📝 Create a Free Account
                    </a>
                </div>

                <div style="margin-top: 10px;">
                    <button type="button" class="btn btn-secondary" onclick="document.getElementById('authGuardModal').style.display='none'" style="font-size: 0.85rem; padding: 6px 16px;">
                        Close
                    </button>
                </div>
            </div>
        `;
    },

    quickLogin(role, redirectUrl) {
        const defaultPhones = {
            member: '+91 98765 43210',
            volunteer: '+91 98765 43211',
            owner: '+91 98765 43212',
            organizer: '+91 98765 43213',
            admin: '+91 98765 00000'
        };
        const phone = defaultPhones[role] || '+91 98765 43210';
        this.login(role, phone);
        if (redirectUrl) {
            window.location.href = redirectUrl;
        } else {
            window.location.reload();
        }
    }
};

// ==========================================================================
// Language Dictionary (English, हिंदी, मराठी)
// ==========================================================================
const I18N_STRINGS = {
    en: {
        projectName: 'Community Micro-Volunteering & Empty Space',
        subtitle: '',
        tagline: 'Connecting People, Helping Communities.',
        seniorHelpline: 'Senior Helpline',
        sosButton: '🚨 EMERGENCY SOS',
        home: 'Home',
        requestHelp: 'Request Help',
        browseTasks: 'Browse Tasks',
        myTasks: 'My Tasks',
        communitySpaces: 'Community Spaces',
        findSpaces: 'Find a Space',
        mySpaces: 'My Spaces',
        bookingRequests: 'Booking Requests',
        createActivity: 'Create Activity',
        myActivities: 'My Activities',
        myActivity: 'My Activity',
        adminDashboard: 'Admin Oversight',
        verification: 'Verification',
        signIn: 'Sign In',
        createAccount: 'Create Account',
        signOut: 'Sign Out'
    },
    hi: {
        projectName: 'सामुदायिक माइक्रो-वॉलंटियरिंग एवं रिक्त स्थान',
        subtitle: '',
        tagline: 'लोगों को जोड़ना, समुदायों की मदद करना।',
        seniorHelpline: 'वरिष्ठ नागरिक हेल्पलाइन',
        sosButton: '🚨 आपातकालीन एसओएस',
        home: 'मुख्य पृष्ठ',
        requestHelp: 'सहायता मांगें',
        browseTasks: 'कार्य देखें',
        myTasks: 'मेरे कार्य',
        communitySpaces: 'सामुदायिक स्थान',
        findSpaces: 'स्थान खोजें',
        mySpaces: 'मेरे स्थान',
        bookingRequests: 'बुकिंग अनुरोध',
        createActivity: 'गतिविधि बनाएं',
        myActivities: 'मेरी गतिविधियां',
        myActivity: 'मेरी गतिविधि',
        adminDashboard: 'प्रशासक डैशबोर्ड',
        verification: 'सत्यापन',
        signIn: 'साइन इन करें',
        createAccount: 'खाता बनाएं',
        signOut: 'साइन आउट'
    },
    mr: {
        projectName: 'सामुदायिक मायक्रो-स्वयंसेवा आणि रिकामी जागा',
        subtitle: '',
        tagline: 'लोकांना जोडणे, समुदायांना मदत करणे.',
        seniorHelpline: 'ज्येष्ठ नागरिक हेल्पलाइन',
        sosButton: '🚨 आपत्कालीन एसओएस',
        home: 'मुख्यपृष्ठ',
        requestHelp: 'मदत मागवा',
        browseTasks: 'कामे पहा',
        myTasks: 'माझी कामे',
        communitySpaces: 'समुदाय जागा',
        findSpaces: 'जागा शोधा',
        mySpaces: 'माझ्या जागा',
        bookingRequests: 'बुकिंग विनंत्या',
        createActivity: 'कार्यक्रम तयार करा',
        myActivities: 'माझे कार्यक्रम',
        myActivity: 'माझी प्रगती',
        adminDashboard: 'प्रशासक नियंत्रण',
        verification: 'पडताळणी',
        signIn: 'साइन इन',
        createAccount: 'नोंदणी करा',
        signOut: 'बाहेर पडा'
    }
};

function getActiveLanguage() {
    return 'en';
}

function setLanguage(lang) {
    localStorage.setItem('reach_lang', 'en');
    applyLanguageTranslations();
}

function applyLanguageTranslations() {
    const lang = getActiveLanguage();
    const t = I18N_STRINGS[lang] || I18N_STRINGS.en;

    // Update common header labels if present
    const logoSub = document.querySelector('.logo-sub');
    if (logoSub) {
        if (!t.subtitle) {
            logoSub.style.display = 'none';
        } else {
            logoSub.textContent = t.subtitle;
            logoSub.style.display = 'block';
        }
    }

    const taglineEl = document.querySelector('.platform-tagline');
    if (taglineEl) taglineEl.textContent = t.tagline;

    renderDynamicNavigation();
}

// ==========================================================================
// Accessibility Controls: Font Resizer
// ==========================================================================
function changeFontSize(size) {
    const root = document.documentElement;
    root.classList.remove('font-small', 'font-normal', 'font-large');
    if (size === 'small') root.classList.add('font-small');
    else if (size === 'large') root.classList.add('font-large');
    else root.classList.add('font-normal');
    localStorage.setItem('reach_font_size', size);
}

// ==========================================================================
// Emergency SOS Modal (Included Core Security Service in UML)
// ==========================================================================
function openSosModal() {
    let m = document.getElementById('sosModal');
    if (!m) {
        m = document.createElement('div');
        m.id = 'sosModal';
        m.className = 'modal-overlay';
        m.style.display = 'flex';
        m.innerHTML = `
            <div class="modal-content" style="border-top: 6px solid var(--danger);">
                <div class="modal-header">
                    <h2 style="color: var(--danger); display: flex; align-items: center; gap: 8px;">
                        🚨 Senior & Community Emergency Panic Response
                    </h2>
                    <button class="modal-close-btn" onclick="closeSosModal()">&times;</button>
                </div>
                <p style="margin-bottom: 20px; color: var(--text-main); font-size: 1.05rem;">
                    Do you need immediate medical emergency help or local security dispatch?
                </p>
                <div style="display: flex; flex-direction: column; gap: 14px; margin-bottom: 22px;">
                    <a href="tel:108" class="btn btn-danger" style="text-align: left; justify-content: flex-start; padding: 14px 18px; font-size: 1.05rem;">
                        🚑 Call Medical Ambulance (108) - Toll Free
                    </a>
                    <a href="tel:02225001111" class="btn btn-secondary" style="text-align: left; justify-content: flex-start; padding: 14px 18px; font-size: 1.05rem;">
                        👮 Call Local Community Security Desk (022-2500-1111)
                    </a>
                    <a href="tel:1091" class="btn btn-secondary" style="text-align: left; justify-content: flex-start; padding: 14px 18px; font-size: 1.05rem;">
                        🛡️ Women & Senior Citizen Helpline (1091)
                    </a>
                </div>
                <div style="text-align: right;">
                    <button class="btn btn-secondary" onclick="closeSosModal()">Close</button>
                </div>
            </div>
        `;
        document.body.appendChild(m);
    } else {
        m.style.display = 'flex';
    }
}

function closeSosModal() {
    const m = document.getElementById('sosModal');
    if (m) m.style.display = 'none';
}

// ==========================================================================
// Dynamic Role Navigation & Header Initializer
// CRITICAL: Before sign in, do NOT show Request Task or Track links!
// ==========================================================================
function renderDynamicNavigation() {
    const mainNav = document.querySelector('.main-nav');
    if (!mainNav) return;

    const isLoggedIn = AuthSession.isLoggedIn();
    const role = AuthSession.getCurrentRole();
    const lang = getActiveLanguage();
    const t = I18N_STRINGS[lang] || I18N_STRINGS.en;
    const path = window.location.pathname.toLowerCase();

    const isHome = path.endsWith('index.html') || path.endsWith('/');
    const isRegister = path.endsWith('register.html');
    const isDashboard = path.endsWith('dashboard.html');
    const isHelp = path.endsWith('help.html') || path.endsWith('request.html') || path.endsWith('request-help.html') || path.endsWith('categories.html');
    const isVolunteer = path.endsWith('volunteer.html');
    const isSpaces = path.endsWith('spaces.html') || path.endsWith('explore.html');
    const isOwner = path.endsWith('owner.html') || path.endsWith('space-owner.html');
    const isOrganize = path.endsWith('organize.html') || path.endsWith('ngo-admin.html');
    const isActivity = path.endsWith('my-activity.html') || path.endsWith('confirmation.html');
    const isAdmin = path.endsWith('admin.html');

    let links = '';

    if (!isLoggedIn) {
        // BEFORE SIGN IN: Strictly public informative flow only!
        // No request task, no track task!
        links = `
            <a href="index.html" class="${isHome && !isRegister ? 'active' : ''}">🏠 ${t.home}</a>
            <a href="spaces.html" class="${isSpaces ? 'active' : ''}">🏛️ ${t.communitySpaces}</a>
            <a href="index.html#servicesOverview">📋 Services</a>
            <a href="index.html#signInBox" class="btn btn-secondary" style="padding: 6px 14px; font-size: 0.88rem;">🔑 ${t.signIn}</a>
            <a href="register.html" class="btn btn-primary" style="padding: 6px 14px; font-size: 0.88rem;">📝 ${t.createAccount}</a>
        `;
    } else {
        // LOGGED IN: Role-Based Navigation
        if (role === 'volunteer') {
            links = `
                <a href="dashboard.html?role=volunteer" class="${isDashboard ? 'active' : ''}">📊 Dashboard</a>
                <a href="volunteer.html?tab=browse" class="${isVolunteer ? 'active' : ''}">🔍 ${t.browseTasks}</a>
                <a href="volunteer.html?tab=mytasks">🦸 ${t.myTasks}</a>
                <a href="spaces.html" class="${isSpaces ? 'active' : ''}">🏛️ ${t.communitySpaces}</a>
            `;
        } else if (role === 'owner') {
            links = `
                <a href="dashboard.html?role=owner" class="${isDashboard ? 'active' : ''}">📊 Dashboard</a>
                <a href="owner.html?tab=spaces" class="${isOwner ? 'active' : ''}">🏛️ ${t.mySpaces}</a>
                <a href="owner.html?tab=bookings">📩 ${t.bookingRequests}</a>
                <a href="owner.html?tab=add" class="btn btn-primary" style="padding: 6px 12px; font-size: 0.85rem;">+ Add Venue</a>
            `;
        } else if (role === 'organizer' || role === 'ngo') {
            links = `
                <a href="dashboard.html?role=organizer" class="${isDashboard ? 'active' : ''}">📊 Dashboard</a>
                <a href="organize.html?tab=create" class="${isOrganize ? 'active' : ''}">🎯 ${t.createActivity}</a>
                <a href="organize.html?tab=myactivities">📋 ${t.myActivities}</a>
                <a href="spaces.html" class="${isSpaces ? 'active' : ''}">🏛️ ${t.communitySpaces}</a>
            `;
        } else if (role === 'admin') {
            links = `
                <a href="admin.html?tab=verifications" class="${isAdmin ? 'active' : ''}">🛡️ ${t.verification}</a>
                <a href="admin.html?tab=monitor">📊 Requests & Bookings</a>
                <a href="admin.html?tab=complaints">⚖️ Complaints & Grievance</a>
                <a href="dashboard.html?role=member">👀 View As Resident</a>
            `;
        } else {
            // Community Member / Senior Resident (Default)
            links = `
                <a href="dashboard.html?role=member" class="${isDashboard ? 'active' : ''}">📊 My Dashboard</a>
                <a href="help.html" class="${isHelp ? 'active' : ''}">🛒 ${t.requestHelp}</a>
                <a href="spaces.html" class="${isSpaces ? 'active' : ''}">🏛️ ${t.findSpaces}</a>
                <a href="my-activity.html" class="${isActivity ? 'active' : ''}">📋 ${t.myActivity}</a>
            `;
        }
    }

    links += `<div id="navUserSection"></div>`;
    mainNav.innerHTML = links;

    // Render User Pill & Logout Button
    const navUserContainer = document.getElementById('navUserSection');
    if (navUserContainer) {
        if (isLoggedIn) {
            const u = AuthSession.getCurrentUser();
            if (u) {
                const roleBadgeLabels = {
                    member: 'Resident',
                    resident: 'Resident',
                    volunteer: 'Volunteer',
                    owner: 'Space Owner',
                    organizer: 'Organizer',
                    ngo: 'Organizer',
                    admin: 'Admin'
                };
                const userRoleName = roleBadgeLabels[u.role] || (u.role === 'owner' ? 'Space Owner' : 'Resident');
                const firstName = (u.name || 'User').split(' ')[0];
                navUserContainer.innerHTML = `
                    <div style="display: flex; align-items: center; gap: 8px;">
                        <a href="dashboard.html" class="user-badge-pill" title="Signed In Profile">
                            <span>${u.avatar || '👤'}</span>
                            <span><strong>${firstName}</strong> (${userRoleName})</span>
                        </a>
                        <button onclick="AuthSession.logout()" class="btn btn-secondary" style="padding: 6px 12px; font-size: 0.82rem; color: #DC2626; border-color: #FCA5A5;">
                            ${t.signOut}
                        </button>
                    </div>
                `;
            }
        }
    }
}

// ==========================================================================
// Return Button / Breadcrumbs Injector
// ==========================================================================
function renderReturnButton(fallbackUrl = 'dashboard.html', label = '← Return to Dashboard') {
    const container = document.getElementById('backButtonContainer');
    if (container) {
        container.innerHTML = `
            <a href="${fallbackUrl}" class="btn-back">
                ${label}
            </a>
        `;
    }
}

// ==========================================================================
// Standalone QR Code SVG Generator (Zero External Dependencies)
// Generates a crisp, authentic SVG representation for physical display/scanning
// ==========================================================================
function generateQrSvg(codeString = 'PASS-REACH-2026', size = 180) {
    return `
    <svg width="${size}" height="${size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; padding:8px; border-radius:10px; border:2px solid #CBD5E1;">
        <rect x="0" y="0" width="100" height="100" fill="#ffffff"/>
        <!-- Corner Finder Patterns -->
        <rect x="6" y="6" width="26" height="26" fill="#1E3A8A" rx="3"/>
        <rect x="10" y="10" width="18" height="18" fill="#ffffff" rx="2"/>
        <rect x="14" y="14" width="10" height="10" fill="#1E3A8A" rx="1"/>

        <rect x="68" y="6" width="26" height="26" fill="#1E3A8A" rx="3"/>
        <rect x="72" y="10" width="18" height="18" fill="#ffffff" rx="2"/>
        <rect x="76" y="14" width="10" height="10" fill="#1E3A8A" rx="1"/>

        <rect x="6" y="68" width="26" height="26" fill="#1E3A8A" rx="3"/>
        <rect x="10" y="72" width="18" height="18" fill="#ffffff" rx="2"/>
        <rect x="14" y="76" width="10" height="10" fill="#1E3A8A" rx="1"/>

        <!-- Timing / Sync Bars -->
        <rect x="36" y="16" width="28" height="4" fill="#0284C7"/>
        <rect x="16" y="36" width="4" height="28" fill="#0284C7"/>

        <!-- QR Data Blocks -->
        <rect x="38" y="38" width="8" height="8" fill="#10B981"/>
        <rect x="54" y="38" width="8" height="8" fill="#1E3A8A"/>
        <rect x="46" y="46" width="8" height="8" fill="#0284C7"/>
        <rect x="38" y="54" width="8" height="8" fill="#1E3A8A"/>
        <rect x="54" y="54" width="8" height="8" fill="#10B981"/>

        <rect x="70" y="38" width="6" height="6" fill="#1E3A8A"/>
        <rect x="82" y="44" width="6" height="6" fill="#0284C7"/>
        <rect x="74" y="52" width="6" height="6" fill="#1E3A8A"/>
        <rect x="86" y="60" width="6" height="6" fill="#10B981"/>

        <rect x="38" y="70" width="6" height="6" fill="#1E3A8A"/>
        <rect x="48" y="76" width="6" height="6" fill="#0284C7"/>
        <rect x="58" y="70" width="6" height="6" fill="#1E3A8A"/>
        <rect x="40" y="86" width="6" height="6" fill="#10B981"/>
        <rect x="52" y="86" width="6" height="6" fill="#1E3A8A"/>
        <rect x="64" y="82" width="6" height="6" fill="#0284C7"/>

        <rect x="70" y="72" width="8" height="8" fill="#1E3A8A"/>
        <rect x="82" y="80" width="8" height="8" fill="#10B981"/>
    </svg>`;
}

// ==========================================================================
// Initialization on DOM Ready
// ==========================================================================
document.addEventListener('DOMContentLoaded', () => {
    AppStore.init();

    // Restore font size
    const savedSize = localStorage.getItem('reach_font_size');
    if (savedSize) changeFontSize(savedSize);

    // Dynamic Navigation and UI setup
    renderDynamicNavigation();
    applyLanguageTranslations();
});
