from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from datetime import datetime


def generate_pdf_report(
    patient_name,
    patient_id,
    alpha, beta, gamma,
    alpha_pct, beta_pct, gamma_pct,
    prediction, confidence,
    spectrogram_path
):

    file_name = f"EEG_Report_{patient_id}.pdf"
    doc = SimpleDocTemplate(file_name, pagesize=A4)
    elements = []

    styles = getSampleStyleSheet()
    normal = styles["Normal"]
    title = styles["Heading1"]
    heading = styles["Heading2"]

    # -----------------------------
    # Title
    # -----------------------------
    elements.append(Paragraph("EEG Stress Detection Report", title))
    elements.append(Spacer(1, 0.3 * inch))

    # -----------------------------
    # Patient Details
    # -----------------------------
    elements.append(Paragraph("Patient Information", heading))
    elements.append(Paragraph(f"Patient Name: {patient_name}", normal))
    elements.append(Paragraph(f"Patient ID: {patient_id}", normal))

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    elements.append(Paragraph(f"Report Generated On: {now}", normal))
    elements.append(Spacer(1, 0.3 * inch))

    # -----------------------------
    # Input Values
    # -----------------------------
    elements.append(Paragraph("Input EEG Values", heading))
    elements.append(Paragraph(f"Alpha: {alpha}", normal))
    elements.append(Paragraph(f"Beta: {beta}", normal))
    elements.append(Paragraph(f"Gamma: {gamma}", normal))
    elements.append(Spacer(1, 0.2 * inch))

    # -----------------------------
    # Band Power
    # -----------------------------
    elements.append(Paragraph("Band Power Distribution (%)", heading))
    elements.append(Paragraph(f"Alpha Power: {alpha_pct:.2f}%", normal))
    elements.append(Paragraph(f"Beta Power: {beta_pct:.2f}%", normal))
    elements.append(Paragraph(f"Gamma Power: {gamma_pct:.2f}%", normal))
    elements.append(Spacer(1, 0.2 * inch))

    # -----------------------------
    # Prediction
    # -----------------------------
    elements.append(Paragraph("Prediction Result", heading))
    elements.append(Paragraph(
        f"Mental State: {prediction} (Confidence: {confidence:.2f}%)",
        normal
    ))
    elements.append(Spacer(1, 0.2 * inch))

    # -----------------------------
    # Suggestions
    # -----------------------------
    elements.append(Paragraph("Suggested Action", heading))

    if prediction == "High Stress":
        suggestion = "Stress detected. Recommend meditation, breathing exercises, proper sleep, and workload reduction."
    elif prediction == "Relaxed":
        suggestion = "Calm mental state detected. Maintain healthy routine and hydration."
    else:
        suggestion = "Active cognitive state detected. Maintain balance and take short breaks."

    elements.append(Paragraph(suggestion, normal))
    elements.append(Spacer(1, 0.3 * inch))

    # -----------------------------
    # Spectrogram
    # -----------------------------
    elements.append(Paragraph("EEG Spectrogram", heading))
    elements.append(Spacer(1, 0.2 * inch))
    elements.append(Image(spectrogram_path, width=400, height=250))

    doc.build(elements)

    return file_name