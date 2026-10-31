import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_cell_borders(cell, top="single", bottom="single", left="single", right="single", color="000000", sz="4"):
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'<w:tcBorders {nsdecls("w")}>'
                        f'<w:top w:val="{top}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                        f'<w:left w:val="{left}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                        f'<w:bottom w:val="{bottom}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                        f'<w:right w:val="{right}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                        f'</w:tcBorders>')
    tcPr.append(borders)

def set_table_borders(table, color="000000", sz="4"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'<w:tblBorders {nsdecls("w")}>'
                        f'<w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                        f'<w:left w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                        f'<w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                        f'<w:right w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                        f'<w:insideH w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                        f'<w:insideV w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                        f'</w:tblBorders>')
    tblPr.append(borders)

def build_exp5_doc():
    doc = Document()

    # 1. Page Margins (1 inch)
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        section.different_first_page_header_footer = False

        # Header: DBIT/CE/B.E./SEM-III/CEP/2026-27 (Right aligned)
        hdr = section.header
        hdr_p = hdr.paragraphs[0]
        hdr_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hdr_p.paragraph_format.space_after = Pt(0)
        r = hdr_p.add_run("DBIT/CE/B.E./SEM-III/CEP/2026-27")
        r.font.name = "Times New Roman"
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(50, 50, 50)

    # Base styling
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(11)
    normal_style.font.color.rgb = RGBColor(0, 0, 0)
    normal_style.paragraph_format.line_spacing = 1.15
    normal_style.paragraph_format.space_after = Pt(4)

    # ---------------------------------------------------------
    # PAGE 1: HEADER, METADATA TABLES, AIM, THEORY, PROTOTYPING
    # ---------------------------------------------------------

    # Institution Header (Table with logo on left, text in center)
    header_tbl = doc.add_table(rows=1, cols=2)
    header_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    header_tbl.autofit = False
    header_tbl.columns[0].width = Inches(1.3)
    header_tbl.columns[1].width = Inches(5.2)

    cell_logo = header_tbl.cell(0, 0)
    cell_logo.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    if os.path.exists('dbit_logo.png'):
        p_logo = cell_logo.paragraphs[0]
        p_logo.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_logo.paragraph_format.space_after = Pt(0)
        p_logo.add_run().add_picture('dbit_logo.png', width=Inches(1.15))

    cell_txt = header_tbl.cell(0, 1)
    cell_txt.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    p_inst = cell_txt.paragraphs[0]
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_after = Pt(1)

    r1 = p_inst.add_run("The Bombay Salesian Society’s\n")
    r1.font.size = Pt(11)
    
    r2 = p_inst.add_run("DON BOSCO INSTITUTE OF TECHNOLOGY\n")
    r2.font.bold = True
    r2.font.size = Pt(14)
    
    r3 = p_inst.add_run("Department of Computer Engineering AY 26-27\n")
    r3.font.size = Pt(11)
    
    r4 = p_inst.add_run("25CE3CEP01 Community Engagement Project")
    r4.font.bold = True
    r4.font.size = Pt(11.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # Class / Batch / Group No. Table
    tbl_meta = doc.add_table(rows=1, cols=3)
    tbl_meta.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_meta, sz="4")
    tbl_meta.columns[0].width = Inches(2.1)
    tbl_meta.columns[1].width = Inches(2.1)
    tbl_meta.columns[2].width = Inches(2.3)

    c0 = tbl_meta.cell(0, 0)
    c0.paragraphs[0].add_run("Class:").font.bold = True
    set_cell_margins(c0, 60, 60, 100, 100)

    c1 = tbl_meta.cell(0, 1)
    c1.paragraphs[0].add_run("Batch: Batch C").font.bold = True
    set_cell_margins(c1, 60, 60, 100, 100)

    c2 = tbl_meta.cell(0, 2)
    c2.paragraphs[0].add_run("Group No.: Grp 04").font.bold = True
    set_cell_margins(c2, 60, 60, 100, 100)

    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_after = Pt(2)

    # Group Details Table
    tbl_grp = doc.add_table(rows=6, cols=3)
    tbl_grp.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_grp, sz="4")
    tbl_grp.columns[0].width = Inches(1.1)
    tbl_grp.columns[1].width = Inches(2.2)
    tbl_grp.columns[2].width = Inches(3.2)

    # Row 0: Merged Header
    c_m = tbl_grp.cell(0, 0)
    c_m.merge(tbl_grp.cell(0, 2))
    p_gm = c_m.paragraphs[0]
    p_gm.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_gm.add_run("Group Details:").font.bold = True
    set_cell_margins(c_m, 60, 60, 100, 100)

    # Row 1: Columns
    headers = ["S. No.", "Roll No.", "Name"]
    for j, h in enumerate(headers):
        cell = tbl_grp.cell(1, j)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if j < 2 else WD_ALIGN_PARAGRAPH.LEFT
        p.add_run(h).font.bold = True
        set_cell_margins(cell, 60, 60, 100, 100)

    # Rows 2 to 5: Blank rows for student names
    for i in range(2, 6):
        cell_num = tbl_grp.cell(i, 0)
        cell_num.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        cell_num.paragraphs[0].add_run(str(i - 1))
        set_cell_margins(cell_num, 70, 70, 100, 100)
        set_cell_margins(tbl_grp.cell(i, 1), 70, 70, 100, 100)
        set_cell_margins(tbl_grp.cell(i, 2), 70, 70, 100, 100)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # Experiment Title
    p_exp = doc.add_paragraph()
    p_exp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_exp.paragraph_format.space_after = Pt(2)
    r_exp = p_exp.add_run("Experiment No. 5")
    r_exp.font.bold = True
    r_exp.font.underline = True
    r_exp.font.size = Pt(13)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_sub.paragraph_format.space_after = Pt(8)
    r_sub = p_sub.add_run("Prototype development using software tools")
    r_sub.font.bold = True
    r_sub.font.underline = True
    r_sub.font.size = Pt(11.5)

    # Aim
    p_aim = doc.add_paragraph()
    p_aim.paragraph_format.space_after = Pt(6)
    r_aim_lbl = p_aim.add_run("Aim: ")
    r_aim_lbl.font.bold = True
    r_aim_lbl.font.underline = True
    p_aim.add_run("To develop a prototype of the solution as sections and provide proof of concept.")

    # Theory
    p_theory = doc.add_paragraph()
    p_theory.paragraph_format.space_after = Pt(6)
    r_th_lbl = p_theory.add_run("Theory: ")
    r_th_lbl.font.bold = True
    r_th_lbl.font.underline = True
    p_theory.add_run("In Experiment No. 4, potential solutions were structured using UML modeling (Use Case, Activity, and State diagrams) along with a planned project timeline. Building upon the structural workflows established in the Activity and State diagrams, Experiment No. 5 transitions from logical architecture into visual implementation and human-computer interface design.")

    # Prototyping
    p_proto_lbl = doc.add_paragraph()
    p_proto_lbl.paragraph_format.space_after = Pt(3)
    r_pr = p_proto_lbl.add_run("Prototyping:")
    r_pr.font.bold = True
    r_pr.font.underline = True

    p_proto = doc.add_paragraph()
    p_proto.paragraph_format.space_after = Pt(4)
    p_proto.add_run("Prototyping serves as a tangible Proof of Concept (PoC). The primary focus of this experiment is visual user interface (UI) design and interactive forward user flows (ensuring that clicking key action buttons advances the user sequentially through the service journey).")

    p_tools_intro = doc.add_paragraph()
    p_tools_intro.paragraph_format.space_after = Pt(3)
    p_tools_intro.add_run("Students may implement their prototype using any one of the following tools:")

    tools_items = [
        ("1. Figma (Recommended for UI/UX): ", "Utilizing components, frames, and interactive click-to-navigate prototyping connections."),
        ("2. Canva (Visual Mockup): ", "Designing multi-page user journeys and linking interactive button elements directly to subsequent pages using the internal page hyperlinking feature."),
        ("3. Basic Front-End Web Development: ", "Static multi-page HTML5/CSS3/JavaScript connected via hyperlinks (<a> tags) or simple view-switching logic.")
    ]
    for prefix, body in tools_items:
        p_t = doc.add_paragraph()
        p_t.paragraph_format.left_indent = Inches(0.25)
        p_t.paragraph_format.space_after = Pt(2)
        r_pre = p_t.add_run(prefix)
        r_pre.font.bold = True
        p_t.add_run(body)

    # Page Break to Page 2
    doc.add_page_break()

    # ---------------------------------------------------------
    # PAGE 2: SOLUTION FLOW & ARCHITECTURE + SCREENS 1 & 2
    # ---------------------------------------------------------

    p_sec1 = doc.add_paragraph()
    p_sec1.paragraph_format.space_after = Pt(6)
    r_sec1 = p_sec1.add_run("1. Solution Flow and Architecture")
    r_sec1.font.bold = True
    r_sec1.font.size = Pt(12)

    p_cuj = doc.add_paragraph()
    p_cuj.paragraph_format.space_after = Pt(3)
    r_cuj = p_cuj.add_run("Core User Journey (Step-by-step screen sequence):")
    r_cuj.font.bold = True

    screens_list = [
        ("Screen 1: ", "Landing / Entry Screen (ConnectSphere Home Portal & Multi-Role Gateway)"),
        ("Screen 2: ", "Core Feature / Selection Screen (Problem Category Directory & Shared Spaces Hub)"),
        ("Screen 3: ", "Input / Action / Form Screen (Unified Assistance Request & Society Delivery Logistics)"),
        ("Screen 4: ", "Confirmation / Detail Review Screen (Pre-Dispatch Verification & Senior PIN Code Generation)"),
        ("Screen 5 / Success Screen: ", "Live Lifecycle Status & Real-Time Tracking Screen (Live Status Stepper & GPS Tracker)")
    ]
    for s_pre, s_desc in screens_list:
        p_sc = doc.add_paragraph()
        p_sc.paragraph_format.left_indent = Inches(0.25)
        p_sc.paragraph_format.space_after = Pt(2)
        p_sc.add_run(s_pre).font.bold = True
        p_sc.add_run(s_desc)

    p_cta_lbl = doc.add_paragraph()
    p_cta_lbl.paragraph_format.space_before = Pt(6)
    p_cta_lbl.paragraph_format.space_after = Pt(3)
    p_cta_lbl.add_run("Key Call-to-Action (CTA) Buttons & Forward Interactions:").font.bold = True

    cta_items = [
        ("• 'Explore Tasks & Spaces' / 'Request Assistance' CTA ", "→ Navigates from Landing Screen to Service Category Directory (Screen 2)."),
        ("• 'Request Assistance' on Category Card ", "→ Carries preselected category into the Unified Assistance Form (Screen 3)."),
        ("• 'Proceed to Review Details →' Button ", "→ Validates form inputs, serializes session data, and advances to Order Review (Screen 4)."),
        ("• 'Confirm & Broadcast to Community →' Button ", "→ Commits errand, generates Senior Safety PIN, broadcasts to volunteers, and opens Live Tracker (Screen 5)."),
        ("• 'Return to Dashboard' / 'Track My Errand' Button ", "→ Provides continuous real-time state feedback and returns senior to their home desk.")
    ]
    for c_pre, c_desc in cta_items:
        p_c = doc.add_paragraph()
        p_c.paragraph_format.left_indent = Inches(0.25)
        p_c.paragraph_format.space_after = Pt(2)
        p_c.add_run(c_pre).font.bold = True
        p_c.add_run(c_desc)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # Prototype Design & Walkthrough
    p_sec2 = doc.add_paragraph()
    p_sec2.paragraph_format.space_after = Pt(6)
    r_sec2 = p_sec2.add_run("2. Prototype Design & Walkthrough")
    r_sec2.font.bold = True
    r_sec2.font.size = Pt(12)

    # --- Screen 1 Walkthrough ---
    p_s1_lbl = doc.add_paragraph()
    p_s1_lbl.paragraph_format.space_after = Pt(3)
    p_s1_lbl.add_run("Screen 1: Landing / Entry Screen").font.bold = True

    # Screenshot 1
    if os.path.exists('screen1_landing.png'):
        p_img1 = doc.add_paragraph()
        p_img1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img1.paragraph_format.space_after = Pt(3)
        p_img1.add_run().add_picture('screen1_landing.png', width=Inches(5.4))

    p_s1_desc = doc.add_paragraph()
    p_s1_desc.paragraph_format.space_after = Pt(2)
    p_s1_desc.add_run("Description & Forward Interaction:").font.bold = True

    p_s1_pur = doc.add_paragraph()
    p_s1_pur.paragraph_format.space_after = Pt(2)
    p_s1_pur.add_run("Purpose: ").font.bold = True
    p_s1_pur.add_run("This screen serves as the community gateway for ConnectSphere, introducing residents, senior citizens, and neighborhood volunteers to the dual-purpose platform. It provides quick emergency SOS access, senior helpline details, live community activity metrics, and immediate navigation to browse errands or reserve empty shared spaces.")

    p_s1_trig = doc.add_paragraph()
    p_s1_trig.paragraph_format.space_after = Pt(6)
    p_s1_trig.add_run("Forward Trigger: ").font.bold = True
    p_s1_trig.add_run("Clicking the primary button ")
    p_s1_trig.add_run('"Explore Tasks & Shared Spaces"').font.bold = True
    p_s1_trig.add_run(' or selecting ')
    p_s1_trig.add_run('"Request Daily Assistance"').font.bold = True
    p_s1_trig.add_run(" navigates the user forward to Screen 2 (Categories & Service Directory).")

    # --- Screen 2 Walkthrough ---
    p_s2_lbl = doc.add_paragraph()
    p_s2_lbl.paragraph_format.space_after = Pt(3)
    p_s2_lbl.add_run("Screen 2: Core Feature / Selection Screen").font.bold = True

    # Screenshot 2
    if os.path.exists('screen2_categories.png'):
        p_img2 = doc.add_paragraph()
        p_img2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img2.paragraph_format.space_after = Pt(3)
        p_img2.add_run().add_picture('screen2_categories.png', width=Inches(5.4))

    p_s2_desc = doc.add_paragraph()
    p_s2_desc.paragraph_format.space_after = Pt(2)
    p_s2_desc.add_run("Description & Forward Interaction:").font.bold = True

    p_s2_pur = doc.add_paragraph()
    p_s2_pur.paragraph_format.space_after = Pt(2)
    p_s2_pur.add_run("Purpose: ").font.bold = True
    p_s2_pur.add_run("Displays the core service categories organized into structured neighborhood assistance cards: Prescription Medicine Pickup, Fresh Groceries & Dairy, Student Tutoring, Pension App & Digital Life Certificate Guidance, and Companion Walks, alongside shared community space reservations.")

    p_s2_trig = doc.add_paragraph()
    p_s2_trig.paragraph_format.space_after = Pt(4)
    p_s2_trig.add_run("Forward Trigger: ").font.bold = True
    p_s2_trig.add_run("Clicking on any dedicated category card button (e.g., ")
    p_s2_trig.add_run('"Request Medicine Help →"').font.bold = True
    p_s2_trig.add_run(' or ')
    p_s2_trig.add_run('"Request Grocery Help →"').font.bold = True
    p_s2_trig.add_run(") captures the category context and forwards the resident to Screen 3 (Input Request Form).")

    # Page Break to Page 3
    doc.add_page_break()

    # ---------------------------------------------------------
    # PAGE 3: SCREENS 3, 4, 5
    # ---------------------------------------------------------

    # --- Screen 3 Walkthrough ---
    p_s3_lbl = doc.add_paragraph()
    p_s3_lbl.paragraph_format.space_after = Pt(3)
    p_s3_lbl.add_run("Screen 3: Input / Action / Form Screen").font.bold = True

    # Screenshot 3
    if os.path.exists('screen3_request_form.png'):
        p_img3 = doc.add_paragraph()
        p_img3.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img3.paragraph_format.space_after = Pt(3)
        p_img3.add_run().add_picture('screen3_request_form.png', width=Inches(5.4))

    p_s3_desc = doc.add_paragraph()
    p_s3_desc.paragraph_format.space_after = Pt(2)
    p_s3_desc.add_run("Description & Forward Interaction:").font.bold = True

    p_s3_pur = doc.add_paragraph()
    p_s3_pur.paragraph_format.space_after = Pt(2)
    p_s3_pur.add_run("Purpose: ").font.bold = True
    p_s3_pur.add_run("Captures essential operational data required by neighborhood volunteers: resident contact details, building/flat address, preferred assistance time, urgency level, and specific notes (e.g., prescription slip details or stair climbing support).")

    p_s3_trig = doc.add_paragraph()
    p_s3_trig.paragraph_format.space_after = Pt(6)
    p_s3_trig.add_run("Forward Trigger: ").font.bold = True
    p_s3_trig.add_run("Submitting the validated form via the ")
    p_s3_trig.add_run('"Proceed to Review Details →"').font.bold = True
    p_s3_trig.add_run(" button saves the active request draft and advances the flow to Screen 4 (Detail Review Screen).")

    # --- Screen 4 Walkthrough ---
    p_s4_lbl = doc.add_paragraph()
    p_s4_lbl.paragraph_format.space_after = Pt(3)
    p_s4_lbl.add_run("Screen 4: Confirmation / Detail Review Screen").font.bold = True

    # Screenshot 4
    if os.path.exists('screen4_review.png'):
        p_img4 = doc.add_paragraph()
        p_img4.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img4.paragraph_format.space_after = Pt(3)
        p_img4.add_run().add_picture('screen4_review.png', width=Inches(5.4))

    p_s4_desc = doc.add_paragraph()
    p_s4_desc.paragraph_format.space_after = Pt(2)
    p_s4_desc.add_run("Description & Forward Interaction:").font.bold = True

    p_s4_pur = doc.add_paragraph()
    p_s4_pur.paragraph_format.space_after = Pt(2)
    p_s4_pur.add_run("Purpose: ").font.bold = True
    p_s4_pur.add_run("Presents a comprehensive review slip displaying requester name, phone number, destination address, scheduled delivery window, and safety guidelines. It enables seniors to double-check their errand specifics or edit details prior to broadcast.")

    p_s4_trig = doc.add_paragraph()
    p_s4_trig.paragraph_format.space_after = Pt(6)
    p_s4_trig.add_run("Forward Trigger: ").font.bold = True
    p_s4_trig.add_run("Clicking the prominent green button ")
    p_s4_trig.add_run('"Confirm & Broadcast to Community →"').font.bold = True
    p_s4_trig.add_run(" commits the request to the neighborhood pool, generates a 4-digit Senior Safety PIN, dispatches real-time broadcast pings, and opens Screen 5 (Real-Time Tracker).")

    # --- Screen 5 Walkthrough ---
    p_s5_lbl = doc.add_paragraph()
    p_s5_lbl.paragraph_format.space_after = Pt(3)
    p_s5_lbl.add_run("Screen 5: Success / Status / Completion Screen").font.bold = True

    # Screenshot 5
    if os.path.exists('screen5_tracker.png'):
        p_img5 = doc.add_paragraph()
        p_img5.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img5.paragraph_format.space_after = Pt(3)
        p_img5.add_run().add_picture('screen5_tracker.png', width=Inches(5.4))

    p_s5_desc = doc.add_paragraph()
    p_s5_desc.paragraph_format.space_after = Pt(2)
    p_s5_desc.add_run("Description & Forward Interaction:").font.bold = True

    p_s5_pur = doc.add_paragraph()
    p_s5_pur.paragraph_format.space_after = Pt(2)
    p_s5_pur.add_run("Purpose: ").font.bold = True
    p_s5_pur.add_run("Serves as the persistent live execution dashboard. It features an active 8-step lifecycle status tracker (Request Created → Waiting for Volunteer → Volunteer Assigned → Live Location Active → Arrived at Location → Task in Progress → PIN Verification → Feedback), dynamic live ETA, and the 4-digit Senior Safety Handover PIN.")

    p_s5_final = doc.add_paragraph()
    p_s5_final.paragraph_format.space_after = Pt(4)
    p_s5_final.add_run("Final State Displayed: ").font.bold = True
    p_s5_final.add_run("Displays the unique tracking reference (e.g., ")
    p_s5_final.add_run("#TSK-102").font.bold = True
    p_s5_final.add_run("), dynamic status badge (")
    p_s5_final.add_run("⏳ Status: Waiting for Nearby Volunteer").font.bold = True
    p_s5_final.add_run(" transitioning dynamically upon acceptance to ")
    p_s5_final.add_run("🟢 Status: Volunteer Assigned & En Route").font.bold = True
    p_s5_final.add_run("), volunteer phone contact CTA, Senior Safety PIN code (e.g., 7153), and a ")
    p_s5_final.add_run('"← Return to Dashboard"').font.bold = True
    p_s5_final.add_run(" navigation button.")

    # Page Break to Page 4
    doc.add_page_break()

    # ---------------------------------------------------------
    # PAGE 4: PROTOTYPE ACCESS LINKS & RESOURCES
    # ---------------------------------------------------------

    p_links_hdr = doc.add_paragraph()
    p_links_hdr.paragraph_format.space_after = Pt(6)
    r_lh = p_links_hdr.add_run("Prototype Access & Proof of Concept Links")
    r_lh.font.bold = True
    r_lh.font.underline = True
    r_lh.font.size = Pt(12)

    p_tool = doc.add_paragraph()
    p_tool.paragraph_format.space_after = Pt(4)
    p_tool.add_run("Tool Selected (Figma / Canva / Front-End): ").font.bold = True
    p_tool.add_run("Basic Front-End Web Development (HTML5, CSS3, JavaScript)")

    p_url = doc.add_paragraph()
    p_url.paragraph_format.space_after = Pt(1)
    p_url.add_run("Public View/Prototype URL:").font.bold = True

    p_url_val = doc.add_paragraph()
    p_url_val.paragraph_format.left_indent = Inches(0.25)
    p_url_val.paragraph_format.space_after = Pt(2)
    r_u = p_url_val.add_run("https://aanchalyadav-21.github.io/CMV-space/")
    r_u.font.color.rgb = RGBColor(0, 70, 180)
    r_u.font.underline = True

    p_perm = doc.add_paragraph()
    p_perm.paragraph_format.space_after = Pt(6)
    r_pm = p_perm.add_run("(Ensure public access permissions are enabled: Fully accessible publicly via GitHub Pages)")
    r_pm.font.size = Pt(9.5)
    r_pm.font.italic = True
    r_pm.font.color.rgb = RGBColor(80, 80, 80)

    p_repo = doc.add_paragraph()
    p_repo.paragraph_format.space_after = Pt(2)
    p_repo.add_run("Github Repository URL (if Front-End):").font.bold = True

    p_repo_val = doc.add_paragraph()
    p_repo_val.paragraph_format.left_indent = Inches(0.25)
    p_repo_val.paragraph_format.space_after = Pt(12)
    r_rp = p_repo_val.add_run("https://github.com/aanchalyadav-21/CMV-space")
    r_rp.font.color.rgb = RGBColor(0, 70, 180)
    r_rp.font.underline = True

    # Resources Heading
    p_res_hdr = doc.add_paragraph()
    p_res_hdr.paragraph_format.space_after = Pt(6)
    r_rh = p_res_hdr.add_run("Resources")
    r_rh.font.bold = True
    r_rh.font.size = Pt(11.5)

    # Resources Table (5 rows matching PDF template exactly)
    tbl_res = doc.add_table(rows=6, cols=3)
    tbl_res.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_res, sz="4")
    tbl_res.columns[0].width = Inches(0.8)
    tbl_res.columns[1].width = Inches(2.3)
    tbl_res.columns[2].width = Inches(3.4)

    # Header Row
    res_headers = ["Sr. No.", "Title", "Link"]
    for j, h in enumerate(res_headers):
        cell = tbl_res.cell(0, j)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if j == 0 else WD_ALIGN_PARAGRAPH.LEFT
        p.add_run(h).font.bold = True
        set_cell_margins(cell, 60, 60, 80, 80)

    resources_data = [
        ("1", "Figma Beginner Prototyping Guide", "https://help.figma.com/hc/en-us/articles/360040314193-Guide-to-prototyping-in-Figma"),
        ("2", "Video Tutorial: Figma Prototyping Basics", "https://www.youtube.com/watch?v=1ucLq6JTxac"),
        ("3", "Canva Interactive Hyperlinking Guide", "https://www.canva.com/help/add-links/"),
        ("4", "Video Tutorial: Clickable Presentations in Canva", "https://www.youtube.com/watch?v=qO2Qfqz1Hks"),
        ("5", "Web Basics: Multi-Page HTML/CSS Navigation", "https://www.youtube.com/watch?v=iXSSHlOe47s")
    ]

    for i, (sr, title, link) in enumerate(resources_data):
        row_idx = i + 1
        c_sr = tbl_res.cell(row_idx, 0)
        c_sr.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        c_sr.paragraphs[0].add_run(sr)
        set_cell_margins(c_sr, 60, 60, 80, 80)

        c_tit = tbl_res.cell(row_idx, 1)
        c_tit.paragraphs[0].add_run(title)
        set_cell_margins(c_tit, 60, 60, 80, 80)

        c_lnk = tbl_res.cell(row_idx, 2)
        r_l = c_lnk.paragraphs[0].add_run(link)
        r_l.font.size = Pt(9.5)
        r_l.font.color.rgb = RGBColor(0, 70, 180)
        r_l.font.underline = True
        set_cell_margins(c_lnk, 60, 60, 80, 80)

    # Save output document
    output_filename = "Experiment_5_ConnectSphere_Prototype_Report.docx"
    doc.save(output_filename)
    print(f"SUCCESS: Saved {output_filename} successfully!")

if __name__ == "__main__":
    build_exp5_doc()

