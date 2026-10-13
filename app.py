import os
from flask import Flask, render_template, abort

app = Flask(__name__)

SECTIONS = {
    "booking": {
        "title": "Patient Booking Journey",
        "subtitle": "From booking request to sample collection",
        "steps": [
            ("01", "Choose diagnostic tests", "Select investigations from a sample catalogue."),
            ("02", "Choose collection details", "Review a fictional home-collection appointment."),
            ("03", "Technician assignment", "See how a collector would be assigned."),
            ("04", "Sample collection", "Preview collection and barcode tracking."),
            ("05", "Lab processing", "Follow the simulated laboratory workflow."),
            ("06", "Digital report", "View the final delivery stage without real reports.")
        ]
    },
    "technician": {
        "title": "Technician Workspace",
        "subtitle": "Mobile-first collection operations",
        "steps": [
            ("01", "Assignment received", "A fictional home-collection job appears."),
            ("02", "Route planning", "Collection locations are represented by demo labels."),
            ("03", "Patient verification", "OTP verification is described but not performed."),
            ("04", "Sample labeling", "Barcode and specimen handling are previewed."),
            ("05", "Handover", "The specimen moves to a simulated partner lab."),
            ("06", "Job completion", "The fictional job is marked complete.")
        ]
    },
    "lab": {
        "title": "Partner Laboratory Portal",
        "subtitle": "Sample receipt to report delivery",
        "steps": [
            ("01", "Sample received", "A fictional specimen enters the workflow."),
            ("02", "Accession", "Sample identity and requested tests are reviewed."),
            ("03", "Processing", "Laboratory processing is simulated."),
            ("04", "Quality review", "Results move through a sample approval stage."),
            ("05", "Report readiness", "A fictional report status is displayed."),
            ("06", "Completion", "The sample workflow is closed.")
        ]
    },
    "admin": {
        "title": "Operations Command Center",
        "subtitle": "A preview of the BDConnect admin experience",
        "steps": [
            ("01", "Booking overview", "View fictional appointment activity."),
            ("02", "Technician allocation", "Review a sample assignment workflow."),
            ("03", "Sample tracking", "Preview collection and lab milestones."),
            ("04", "Partner coordination", "Understand the laboratory handoff."),
            ("05", "Financial overview", "Review illustrative figures only."),
            ("06", "Operational reporting", "Explore the proposed management workflow.")
        ]
    }
}

@app.after_request
def secure_response(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "style-src 'self'; "
        "img-src 'self' data:; "
        "script-src 'none'; "
        "object-src 'none'; "
        "base-uri 'none'; "
        "form-action 'none'; "
        "frame-ancestors 'none'"
    )
    response.headers["Cache-Control"] = "public, max-age=300"
    return response

@app.get("/")
def home():
    return render_template("home.html")

@app.get("/preview/<section>")
def preview(section):
    item = SECTIONS.get(section)
    if item is None:
        abort(404)
    return render_template(
        "preview.html",
        section=section,
        item=item
    )

@app.get("/health")
def health():
    return {"status": "ok", "mode": "read-only-showcase"}

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=int(os.environ.get("PORT", "5000")),
        debug=False
    )
