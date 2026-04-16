# =============================================================================
# PDFserver.py - FastAPI PDF Generation Server
# 
# This module generates PDF order summaries for QuickBasket
# PDF files are saved in the OrderPDF folder
# =============================================================================

from fastapi import FastAPI
from fastapi.responses import FileResponse
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer,
    Image
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from datetime import datetime
import uuid
import os
import config

# =============================================================================
# FastAPI Application Setup
# =============================================================================

app = FastAPI()

# Create PDF folder if not exists
if not os.path.exists(config.PDF_FOLDER):
    os.makedirs(config.PDF_FOLDER)


# =============================================================================
# PDF Generation Endpoint
# =============================================================================

@app.post("/generate-pdf")
async def generate_pdf(data: dict):
    """
    Generate PDF order summary
    
    Parameters:
    - data: Dictionary containing order items and totals
    
    Returns:
    - FileResponse: PDF file download
    """
    
    print("Incoming Data:", data)
    
    # Generate unique filename
    filename = os.path.join(config.PDF_FOLDER, f"QuickBasket_{uuid.uuid4()}.pdf")
    
    styles = getSampleStyleSheet()
    story = []
    
    # -------- Banner Logo --------
    logo_path = "images/QuickBasketLogo.png"
    
    if os.path.exists(logo_path):
        img = ImageReader(logo_path)
        img_width, img_height = img.getSize()
        aspect = img_height / float(img_width)
        
        banner = Image(
            logo_path,
            width=7.5 * inch,
            height=(7.5 * inch) * aspect
        )
        
        story.append(banner)
        story.append(Spacer(1, 18))
    
    # -------- Modern Title --------
    title_style = ParagraphStyle(
        "ModernTitle",
        parent=styles["Heading1"],
        alignment=TA_CENTER,
        textColor=colors.HexColor("#1F3A5F"),
        spaceAfter=12
    )
    
    story.append(
        Paragraph(
            "<b>QuickBasket Order Summary</b>",
            title_style
        )
    )
    
    story.append(Spacer(1, 10))
    
    # -------- Metadata Card --------
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    metadata = [
        ["Company", "QuickBasket"],
        ["Document", "Order Summary"],
        ["Generated", now],
        ["Status", "Confirmed"]
    ]
    
    meta_table = Table(metadata, colWidths=[200, 300])
    meta_table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#F7F9FC")),
        ("BOX", (0,0), (-1,-1), 1, colors.HexColor("#E5E7EB")),
        ("INNERGRID", (0,0), (-1,-1), 0.5, colors.HexColor("#E5E7EB")),
        ("FONTSIZE", (0,0), (-1,-1), 10),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ]))
    
    story.append(meta_table)
    story.append(Spacer(1, 25))
    
    # -------- Extract Data --------
    items = (
        data.get("items")
        or data.get("data", {}).get("items")
        or []
    )
    
    grand_total = (
        data.get("Grand Total")
        or data.get("data", {}).get("Grand Total")
        or ""
    )
    
    # -------- Modern Table --------
    table_data = [["Product", "Qty", "Unit Price", "Total"]]
    
    if not items:
        table_data.append(["No Items Found", "", "", ""])
    else:
        for item in items:
            table_data.append([
                str(item.get("Product", "")).title(),
                str(item.get("Quantity", "")),
                str(item.get("Unit Price", "")),
                str(item.get("Total", ""))
            ])
    
    table = Table(table_data, colWidths=[240, 60, 100, 110])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#1F3A5F")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,0), 11),
        ("BACKGROUND", (0,1), (-1,-1), colors.HexColor("#FBFCFE")),
        ("FONTSIZE", (0,1), (-1,-1), 10),
        ("GRID", (0,0), (-1,-1), 0.5, colors.HexColor("#E5E7EB")),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ]))
    
    story.append(table)
    story.append(Spacer(1, 25))
    
    # -------- Modern Grand Total Card --------
    if grand_total:
        grand_total_table = Table(
            [["Grand Total", grand_total]],
            colWidths=[380, 130]
        )
        grand_total_table.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#EEF2FF")),
            ("TEXTCOLOR", (0,0), (-1,-1), colors.HexColor("#1F3A5F")),
            ("FONTNAME", (0,0), (-1,-1), "Helvetica-Bold"),
            ("FONTSIZE", (0,0), (-1,-1), 13),
            ("ALIGN", (1,0), (1,0), "RIGHT"),
            ("BOX", (0,0), (-1,-1), 1, colors.HexColor("#CBD5E1")),
            ("LEFTPADDING", (0,0), (-1,-1), 12),
            ("RIGHTPADDING", (0,0), (-1,-1), 12),
            ("TOPPADDING", (0,0), (-1,-1), 10),
            ("BOTTOMPADDING", (0,0), (-1,-1), 10),
        ]))
        
        story.append(grand_total_table)
        story.append(Spacer(1, 35))
    
    # -------- Footer --------
    footer_style = ParagraphStyle(
        "footer",
        alignment=TA_CENTER,
        textColor=colors.grey,
        fontSize=9
    )
    
    footer = Paragraph(
        f"""
        QuickBasket Pvt Ltd<br/>
        Generated Automatically • {now}
        """,
        footer_style
    )
    
    story.append(footer)
    
    # -------- Build PDF --------
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        topMargin=12,
        bottomMargin=20
    )
    
    doc.build(story)
    
    return FileResponse(
        filename,
        media_type="application/pdf",
        filename="QuickBasket_Order.pdf"
    )
