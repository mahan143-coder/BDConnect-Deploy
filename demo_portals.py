from flask import Blueprint, render_template, abort

demo_bp = Blueprint("demo", __name__)

PATIENT_TESTS = [
    {"name": "Complete Blood Count", "code": "CBC", "price": 350, "category": "Hematology"},
    {"name": "Lipid Profile", "code": "LIPID", "price": 650, "category": "Biochemistry"},
    {"name": "Thyroid Profile", "code": "TFT", "price": 750, "category": "Endocrinology"},
    {"name": "HbA1c", "code": "HBA1C", "price": 500, "category": "Diabetes"},
]

PATIENT_BOOKINGS = [
    {"id": "DEMO-1042", "tests": "CBC, Lipid Profile", "date": "Sample appointment", "status": "Sample collected", "tone": "green"},
    {"id": "DEMO-1043", "tests": "Thyroid Profile", "date": "Sample appointment", "status": "Technician assigned", "tone": "blue"},
    {"id": "DEMO-1044", "tests": "HbA1c", "date": "Sample appointment", "status": "Report ready", "tone": "green"},
]

TECHNICIAN_JOBS = [
    {"id": "DEMO-1042", "patient": "Demo Patient A", "location": "Demo Zone A", "time": "08:30 AM", "tests": "CBC + Lipid", "status": "Completed", "tone": "green"},
    {"id": "DEMO-1043", "patient": "Demo Patient B", "location": "Demo Zone B", "time": "10:00 AM", "tests": "Thyroid Profile", "status": "Assigned", "tone": "blue"},
    {"id": "DEMO-1045", "patient": "Demo Patient C", "location": "Demo Zone C", "time": "11:30 AM", "tests": "HbA1c", "status": "Pending", "tone": "amber"},
]

LAB_SAMPLES = [
    {"id": "SPEC-2001", "booking": "DEMO-1042", "sample": "EDTA / Serum", "test": "CBC + Lipid", "status": "Processing", "tone": "blue"},
    {"id": "SPEC-2002", "booking": "DEMO-1043", "sample": "Serum", "test": "Thyroid Profile", "status": "Received", "tone": "amber"},
    {"id": "SPEC-2003", "booking": "DEMO-1044", "sample": "EDTA", "test": "HbA1c", "status": "Verified", "tone": "green"},
    {"id": "SPEC-2004", "booking": "DEMO-1046", "sample": "Serum", "test": "Lipid Profile", "status": "Quality review", "tone": "violet"},
]

ADMIN_BOOKINGS = [
    {"id": "DEMO-1042", "patient": "Demo Patient A", "tests": "CBC + Lipid", "technician": "Collector Alpha", "status": "Collected", "tone": "green"},
    {"id": "DEMO-1043", "patient": "Demo Patient B", "tests": "Thyroid Profile", "technician": "Collector Beta", "status": "Assigned", "tone": "blue"},
    {"id": "DEMO-1044", "patient": "Demo Patient C", "tests": "HbA1c", "technician": "Collector Gamma", "status": "Completed", "tone": "green"},
    {"id": "DEMO-1045", "patient": "Demo Patient D", "tests": "CBC", "technician": "Unassigned", "status": "Pending", "tone": "amber"},
]

PORTALS = {
    "patient": {
        "title": "Patient Portal",
        "subtitle": "Discover tests, review sample appointments and follow diagnostic milestones.",
        "icon": "P",
        "metrics": [
            ("Available Tests", "24+", "Illustrative catalogue"),
            ("Demo Bookings", "03", "Fictional records"),
            ("Reports Ready", "01", "Preview status"),
            ("Home Collection", "Available", "Concept only"),
        ],
    },
    "technician": {
        "title": "Technician Workspace",
        "subtitle": "Collection assignments, field operations and specimen handover.",
        "icon": "T",
        "metrics": [
            ("Assigned Jobs", "08", "Illustrative workload"),
            ("Completed", "05", "Sample assignments"),
            ("Pending", "03", "Sample assignments"),
            ("Samples Handed Over", "05", "Fictional tracking"),
        ],
    },
    "lab": {
        "title": "Partner Laboratory",
        "subtitle": "Specimen accession, processing queues and report verification.",
        "icon": "L",
        "metrics": [
            ("Samples Received", "18", "Sample workload"),
            ("In Processing", "07", "Illustrative count"),
            ("Quality Review", "03", "Illustrative count"),
            ("Verified", "08", "Sample records"),
        ],
    },
    "admin": {
        "title": "Admin Command Center",
        "subtitle": "A consolidated view of bookings, collection operations and laboratory coordination.",
        "icon": "A",
        "metrics": [
            ("Total Bookings", "128", "Fictional activity"),
            ("Collections Done", "94", "Illustrative total"),
            ("Active Collectors", "12", "Demo personnel"),
            ("Sample Revenue", "₹48,650", "Not actual earnings"),
        ],
    },
}

@demo_bp.get("/demo")
def demo_index():
    return render_template(
        "demo_portal.html",
        role="admin",
        portal=PORTALS["admin"],
        portals=PORTALS,
        tests=PATIENT_TESTS,
        bookings=PATIENT_BOOKINGS,
        jobs=TECHNICIAN_JOBS,
        samples=LAB_SAMPLES,
        admin_bookings=ADMIN_BOOKINGS,
    )

@demo_bp.get("/demo/<role>")
def demo_portal(role):
    if role not in PORTALS:
        abort(404)

    return render_template(
        "demo_portal.html",
        role=role,
        portal=PORTALS[role],
        portals=PORTALS,
        tests=PATIENT_TESTS,
        bookings=PATIENT_BOOKINGS,
        jobs=TECHNICIAN_JOBS,
        samples=LAB_SAMPLES,
        admin_bookings=ADMIN_BOOKINGS,
    )
