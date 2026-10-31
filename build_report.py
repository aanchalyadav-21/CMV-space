# Comprehensive DBIT Community Engagement Project 1 Report Generator
# Name: ConnectSphere: Community Micro-Volunteering & Empty Space Sharing
# Alignment: Fully Justified (Body & Tables)
# Page Numbering: Native Dynamic Word Fields (Page X of Y)

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def create_full_report():
    doc = docx.Document()
    
    # Page setup - A4 conforming to DBIT formatting guidelines
    # Margins: Left 2.5 cm (0.98 in), Right 2.0 cm (0.79 in), Top 2.0 cm (0.79 in), Bottom 2.0 cm (0.79 in)
    section = doc.sections[0]
    section.page_width = Inches(8.27)
    section.page_height = Inches(11.69)
    section.top_margin = Inches(0.79)
    section.bottom_margin = Inches(0.79)
    section.left_margin = Inches(0.98)
    section.right_margin = Inches(0.79)
    
    # Base Normal Style: 12pt Times New Roman, Justified, 1.25 line spacing
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(12)
    normal_style.font.color.rgb = RGBColor(0, 0, 0)
    normal_style.paragraph_format.line_spacing = 1.25
    normal_style.paragraph_format.space_after = Pt(6)
    normal_style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    # Running Footer with native dynamic Word Page Numbers: "Page X of Y"
    footer = section.footer
    p_ftr = footer.paragraphs[0]
    p_ftr.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    
    r_ftr_lbl = p_ftr.add_run("ConnectSphere  |  Course Code: 25CE3CEP01  |  Page ")
    r_ftr_lbl.font.name = 'Times New Roman'
    r_ftr_lbl.font.size = Pt(9.5)
    r_ftr_lbl.font.italic = True
    r_ftr_lbl.font.color.rgb = RGBColor(100, 116, 139)

    def append_page_field(p, field_name):
        run = p.add_run()
        run.font.name = 'Times New Roman'
        run.font.size = Pt(9.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(30, 41, 59)
        fldChar1 = OxmlElement('w:fldChar')
        fldChar1.set(qn('w:fldCharType'), 'begin')
        instrText = OxmlElement('w:instrText')
        instrText.set(qn('xml:space'), 'preserve')
        instrText.text = field_name
        fldChar2 = OxmlElement('w:fldChar')
        fldChar2.set(qn('w:fldCharType'), 'separate')
        fldChar3 = OxmlElement('w:fldChar')
        fldChar3.set(qn('w:fldCharType'), 'end')
        run._r.append(fldChar1)
        run._r.append(instrText)
        run._r.append(fldChar2)
        run._r.append(fldChar3)

    append_page_field(p_ftr, 'PAGE')
    r_of = p_ftr.add_run(" of ")
    r_of.font.name = 'Times New Roman'
    r_of.font.size = Pt(9.5)
    r_of.font.italic = True
    r_of.font.color.rgb = RGBColor(100, 116, 139)
    append_page_field(p_ftr, 'NUMPAGES')

    # Word Compatibility Settings: Prevent expanding shift-returns
    try:
        settings_elm = doc.settings.element
        compat = parse_xml(f'<w:compat {nsdecls("w")}><w:doNotExpandShiftReturn/></w:compat>')
        settings_elm.append(compat)
    except Exception as e:
        print("Notice on compat:", e)

    # Helper Paragraph Functions
    def add_title(text, size=16, space_before=12, space_after=12, align=WD_ALIGN_PARAGRAPH.CENTER, color=RGBColor(0,0,0)):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.space_before = Pt(space_before)
        p.paragraph_format.space_after = Pt(space_after)
        run = p.add_run(text)
        run.bold = True
        run.font.name = 'Times New Roman'
        run.font.size = Pt(size)
        run.font.color.rgb = color
        return p

    def add_h1(text, space_before=18, space_after=8):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(space_before)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.bold = True
        run.font.name = 'Times New Roman'
        run.font.size = Pt(14)
        run.font.color.rgb = RGBColor(15, 23, 42)
        return p

    def add_h2(text, space_before=14, space_after=6):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(space_before)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.bold = True
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        run.font.color.rgb = RGBColor(30, 41, 59)
        return p

    def add_p(text, bold_prefix="", italic_prefix="", space_after=6, align=WD_ALIGN_PARAGRAPH.JUSTIFY):
        # Split text into separate paragraphs if it contains newlines
        # This completely eliminates awkward stretched line justification!
        raw_lines = text.split('\n')
        lines = [l.strip() for l in raw_lines if l.strip()]
        if not lines:
            p = doc.add_paragraph()
            p.alignment = align
            p.paragraph_format.space_after = Pt(space_after)
            p.paragraph_format.line_spacing = 1.25
            return p

        created_p = None
        for i, line in enumerate(lines):
            p = doc.add_paragraph()
            
            # Short headings ending with ':' should be left-aligned so Word never expands them
            is_header_lead = (line.endswith(':') and len(line) < 85) or line.startswith(('1. Likes', '2. Criticisms', '3. Questions', '4. Ideas', 'Scope Boundaries:'))
            if is_header_lead:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            else:
                p.alignment = align
                
            p.paragraph_format.space_after = Pt(space_after if i == len(lines)-1 else 3)
            p.paragraph_format.line_spacing = 1.25

            # Apply bold/italic prefix only on the first line if supplied to add_p
            if i == 0:
                if bold_prefix:
                    r_b = p.add_run(bold_prefix)
                    r_b.bold = True
                    r_b.font.name = 'Times New Roman'
                    r_b.font.size = Pt(12)
                if italic_prefix:
                    r_i = p.add_run(italic_prefix)
                    r_i.italic = True
                    r_i.font.name = 'Times New Roman'
                    r_i.font.size = Pt(12)

            line_to_process = line

            # Check if line is a bullet item starting with '• ' or '- '
            if line_to_process.startswith('• ') or line_to_process.startswith('- '):
                line_to_process = line_to_process[2:].strip()
                r_sym = p.add_run('•  ')
                r_sym.font.name = 'Times New Roman'
                r_sym.font.size = Pt(12)
                r_sym.bold = True
                p.paragraph_format.left_indent = Inches(0.25)
                p.paragraph_format.first_line_indent = Inches(-0.25)

            # Check if line has a key label before a colon (e.g. '• Purpose: ...' or '1. Presentation Layer: ...')
            colon_pos = line_to_process.find(':')
            if 0 < colon_pos <= 60 and not line_to_process.endswith(':'):
                prefix = line_to_process[:colon_pos+1]
                rest = line_to_process[colon_pos+1:]

                r_pref = p.add_run(prefix)
                r_pref.bold = True
                r_pref.font.name = 'Times New Roman'
                r_pref.font.size = Pt(12)

                r_rest = p.add_run(rest)
                r_rest.font.name = 'Times New Roman'
                r_rest.font.size = Pt(12)
            else:
                r_main = p.add_run(line_to_process)
                r_main.font.name = 'Times New Roman'
                r_main.font.size = Pt(12)
                if is_header_lead:
                    r_main.bold = True

            if created_p is None:
                created_p = p

        return created_p

    def add_bullet(text, bold_prefix="", space_after=4):
        p = doc.add_paragraph(style='List Bullet')
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.25
        if bold_prefix:
            r_b = p.add_run(bold_prefix)
            r_b.bold = True
            r_b.font.name = 'Times New Roman'
            r_b.font.size = Pt(12)
        r = p.add_run(text)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)
        return p

    def set_cell_background(cell, fill_hex):
        tcPr = cell._tc.get_or_add_tcPr()
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
        tcPr.append(shd)

    def set_table_styling(table, col_widths=None):
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        tblPr = table._tbl.tblPr
        borders = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>'
            f'<w:top w:val="single" w:sz="6" w:space="0" w:color="94A3B8"/>'
            f'<w:bottom w:val="single" w:sz="6" w:space="0" w:color="94A3B8"/>'
            f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>'
            f'<w:insideV w:val="none"/>'
            f'<w:left w:val="none"/>'
            f'<w:right w:val="none"/>'
            f'</w:tblBorders>'
        )
        tblPr.append(borders)
        
        # Style header row
        hdr_row = table.rows[0]
        for cell in hdr_row.cells:
            set_cell_background(cell, "F1F5F9")
            for p in cell.paragraphs:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.space_before = Pt(4)
                p.paragraph_format.space_after = Pt(4)
                for r in p.runs:
                    r.bold = True
                    r.font.name = 'Times New Roman'
                    r.font.size = Pt(10)
                    r.font.color.rgb = RGBColor(15, 23, 42)
                    
        # Style content rows: Clean left alignment for table text cells to eliminate awkward spacing
        for row in table.rows[1:]:
            for cell_idx, cell in enumerate(row.cells):
                col_header = table.rows[0].cells[cell_idx].text.strip() if len(table.rows[0].cells) > cell_idx else ""
                for p in cell.paragraphs:
                    # Center code, number, score, and percentage columns
                    if (cell_idx == 0 and len(row.cells) >= 3) or any(k in col_header for k in ["Score", "Max", "Mean", "%", "CO", "PO", "Sr."]):
                        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    else:
                        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                    p.paragraph_format.space_before = Pt(3)
                    p.paragraph_format.space_after = Pt(3)
                    p.paragraph_format.line_spacing = 1.15
                    for r in p.runs:
                        r.font.name = 'Times New Roman'
                        r.font.size = Pt(9.5)
                        
        if col_widths:
            for row in table.rows:
                for i, w in enumerate(col_widths):
                    if i < len(row.cells):
                        row.cells[i].width = w

    def add_image_with_caption(img_path, caption, width=Inches(6.0)):
        if os.path.exists(img_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(10)
            p_img.paragraph_format.space_after = Pt(4)
            p_img.add_run().add_picture(img_path, width=width)
            
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_before = Pt(2)
            p_cap.paragraph_format.space_after = Pt(12)
            r = p_cap.add_run(caption)
            r.bold = True
            r.italic = True
            r.font.name = 'Times New Roman'
            r.font.size = Pt(10)
            r.font.color.rgb = RGBColor(51, 65, 85)
        else:
            print(f"Notice: Image {img_path} not found.")

    print("Building fully justified ConnectSphere report with dynamic page numbering...")

    # ==========================================
    # 1. FRONT MATTER: COVER PAGE
    # ==========================================
    add_title("Don Bosco Institute of Technology, Mumbai", size=16, space_before=0, space_after=2)
    p_inst = doc.add_paragraph("(An Autonomous Institute Affiliated to the University of Mumbai)\nMumbai - 400070")
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_after = Pt(14)
    for r in p_inst.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)

    p_dept = doc.add_paragraph("Department of Computer Engineering")
    p_dept.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_dept.paragraph_format.space_after = Pt(16)
    for r in p_dept.runs:
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(13)

    if os.path.exists("extracted_images/exp4_img_1.jpg"):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_after = Pt(16)
        p_logo.add_run().add_picture("extracted_images/exp4_img_1.jpg", width=Inches(1.5))

    add_title("CONNECTSPHERE: COMMUNITY MICRO-VOLUNTEERING & EMPTY SPACE SHARING", size=15, space_before=6, space_after=8, color=RGBColor(2, 132, 199))
    add_p("A Hyperlocal Mutual-Aid and Community Infrastructure Sharing Platform with Offline-First State Synchronization, Verifiable Gate Access Passes, and Doorstep PIN Verification", space_after=18, align=WD_ALIGN_PARAGRAPH.CENTER)

    p_sub = doc.add_paragraph("A Report Submitted in partial fulfillment of the requirements for\nCOMMUNITY ENGAGEMENT PROJECT 1\nCourse Code: 25CE3CEP01\nSemester III, Academic Year 2026-27")
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(16)
    for r in p_sub.runs:
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)

    p_by = doc.add_paragraph("Submitted by Group No.: 04 (Batch: Comps C)")
    p_by.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_by.paragraph_format.space_after = Pt(8)
    p_by.runs[0].bold = True

    # Student Table
    table_students = doc.add_table(rows=6, cols=3)
    hdr = table_students.rows[0].cells
    hdr[0].text = "Name of Student"
    hdr[1].text = "Roll No."
    hdr[2].text = "Student ID / UID"
    
    students_data = [
        ("Ansley Rayen", "45", "202401045"),
        ("Simone Rodrigues", "46", "202401046"),
        ("Disha Ganesh Shetty", "50", "202401050"),
        ("Aanchal Yadav", "54", "202401054"),
        ("Kritika Singh", "56", "202401056")
    ]
    for idx, (name, roll, uid) in enumerate(students_data):
        row_cells = table_students.rows[idx+1].cells
        row_cells[0].text = name
        row_cells[1].text = roll
        row_cells[2].text = uid
    set_table_styling(table_students, [Inches(3.2), Inches(1.3), Inches(2.0)])

    p_sup = doc.add_paragraph("\nSupervised by\nProf. [Name of Faculty Mentor]\nDepartment of Computer Engineering\n\nAY 2026-27")
    p_sup.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sup.paragraph_format.space_before = Pt(12)
    p_sup.paragraph_format.space_after = Pt(0)
    for r in p_sup.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)
        r.bold = True

    doc.add_page_break()

    # ==========================================
    # 2. CERTIFICATE, APPROVAL, DECLARATION
    # ==========================================
    add_title("CERTIFICATE", size=16, space_before=12, space_after=14)
    add_p('This is to certify that the Community Engagement Project 1 entitled "ConnectSphere: Community Micro-Volunteering & Empty Space Sharing" is a bona fide work carried out by the following students of Second Year Computer Engineering, Semester III, during Academic Year 2026-27, in partial fulfillment of the requirements of the course Community Engagement Project 1 (25CE3CEP01).')
    
    table_cert = doc.add_table(rows=6, cols=3)
    table_cert.rows[0].cells[0].text = "Student Name"
    table_cert.rows[0].cells[1].text = "Roll No."
    table_cert.rows[0].cells[2].text = "Signature"
    for idx, (name, roll, _) in enumerate(students_data):
        row_cells = table_cert.rows[idx+1].cells
        row_cells[0].text = name
        row_cells[1].text = roll
        row_cells[2].text = "____________________"
    set_table_styling(table_cert, [Inches(3.2), Inches(1.3), Inches(2.0)])

    p_sigs = doc.add_paragraph("\n\n\n________________________            ________________________            ________________________\n     Signature                                Signature                                 Signature\n   Faculty Guide                         Head of Department                             Principal")
    p_sigs.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in p_sigs.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10.5)
        r.bold = True

    doc.add_page_break()

    add_title("COMMUNITY ENGAGEMENT PROJECT 1 REPORT APPROVAL", size=15, space_before=12, space_after=14)
    add_p('This report titled "ConnectSphere: Community Micro-Volunteering & Empty Space Sharing" submitted by:')
    for idx, (name, roll, _) in enumerate(students_data):
        add_p(f"{idx+1}. {name} (Roll No.: {roll})", space_after=2)
    add_p('is approved for completion of Community Engagement Project 1 (25CE3CEP01), Semester III, Academic Year 2026-27, Department of Computer Engineering, Don Bosco Institute of Technology, Mumbai.', space_after=14)

    p_exam = doc.add_paragraph("\n\nExaminers:\n\n1. ___________________________________________________\n\n2. ___________________________________________________\n\nDate: ____________________\nPlace: Kurla, Mumbai")
    for r in p_exam.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)
        r.bold = True

    doc.add_page_break()

    add_title("DECLARATION", size=16, space_before=12, space_after=14)
    add_p('We hereby declare that the project report titled "ConnectSphere: Community Micro-Volunteering & Empty Space Sharing" is our original work carried out under the guidance of our Faculty Mentor. The work has not been submitted elsewhere for the award of any degree or academic credit. All sources of information, data, images, code, standards and published material used in this report have been appropriately acknowledged.')

    table_dec = doc.add_table(rows=6, cols=3)
    table_dec.rows[0].cells[0].text = "Student Name"
    table_dec.rows[0].cells[1].text = "Roll No."
    table_dec.rows[0].cells[2].text = "Signature"
    for idx, (name, roll, _) in enumerate(students_data):
        row_cells = table_dec.rows[idx+1].cells
        row_cells[0].text = name
        row_cells[1].text = roll
        row_cells[2].text = "____________________"
    set_table_styling(table_dec, [Inches(3.2), Inches(1.3), Inches(2.0)])

    doc.add_page_break()

    # ==========================================
    # 3. VISION, MISSION, PSOS & ABSTRACT
    # ==========================================
    add_title("VISION, MISSION AND PROGRAMME SPECIFIC OUTCOMES", size=14, space_before=10, space_after=10)
    add_h2("Institute Vision")
    add_p("Shaping a sustainable tomorrow - DBIT will be known to have an innovative, enjoyable and holistic learning environment that transforms individuals into socially conscious citizens the Don Bosco way and will lead in research and entrepreneurship in the area of sustainable technologies.")
    
    add_h2("Institute Mission: Engineering Excellence with Purpose")
    add_bullet("To create future engineers who work with honesty and integrity and excel in the use of technology for the benefit of the underprivileged.")
    add_bullet("To train engineers to be innovative problem solvers and entrepreneurs who engage in research and life-long learning.")
    add_bullet("To provide a diverse and stimulating environment for staff and students to grow holistically.")

    add_h2("Department Vision")
    add_p("To become a center of academic excellence in the field of computer science and engineering for developing technically competent professionals in the service of society.")

    add_h2("Department Mission")
    add_bullet("Develop an academic system towards effective teaching learning process by ensuring enthusiastic participation from the stakeholders for consistent improvement through evaluation and feedback.")
    add_bullet("Promote undergraduate collaborative research in the emerging areas of computer science.")
    add_bullet("Provide learning environment for the students to enhance problem solving skills with professional and ethical responsibilities.")
    add_bullet("Prepare industry ready professionals with social commitment.")

    add_h2("Programme Specific Outcomes (PSOs)")
    add_bullet("The Computer Engineering graduate will be able to demonstrate the ability to understand, analyze and develop computer applications in the field of Computer Science and Engineering.", bold_prefix="PSO 1: ")
    add_bullet("The Computer Engineering graduate will be able to demonstrate leadership, professional communication, ethical practices, teamwork and social commitment.", bold_prefix="PSO 2: ")
    add_bullet("The Computer Engineering graduate will be able to demonstrate research skills and utilize modern computing tools to solve real life problems.", bold_prefix="PSO 3: ")

    doc.add_page_break()

    add_title("ABSTRACT", size=16, space_before=12, space_after=14)
    abstract_text = (
        "Urban residential communities face two intertwined socio-technical challenges: elderly and vulnerable residents "
        "frequently struggle with time-critical, small-scale errands (such as prescription medicine collection, grocery assistance, "
        "and emergency clinic visits) due to isolated nuclear family structures, while communal physical infrastructure "
        "(society clubhouses, parish halls, and educational rooms) remains severely underutilized due to opaque, bureaucratic "
        "reservation procedures. Existing commercial gig platforms neglect low-margin micro-tasks, lack volunteer safety "
        "verification, and completely segregate errand assistance from civic venue booking.\n\n"
        "To resolve this, the 'ConnectSphere: Community Micro-Volunteering & Empty Space Sharing' platform was engineered as a "
        "hyperlocal, full-featured progressive web ecosystem. The methodology adopted human-centered design thinking—grounded "
        "in an empirical field survey of N = 102 community respondents across Kurla, Mumbai, paired with in-depth empathy mapping "
        "and UML behavioral modeling. The resulting architecture integrates five role-based portals (Resident, Volunteer, Space Owner, "
        "NGO Organizer, and System Admin), powered by a decoupled state machine, peer-to-peer BroadcastChannel reactivity, and an "
        "offline-resilient HTML5 AppStore.\n\n"
        "Key innovations include: (1) a secure 4-digit doorstep Safety Verification PIN (e.g., #4829) that safeguards vulnerable "
        "residents before completing medicine deliveries; (2) a dynamic SVG Gate Access Pass with verifiable QR tokens for "
        "approved community space bookings; and (3) an integrated Organizer Desk enabling NGOs to co-recruit volunteers and reserve "
        "civic halls within a unified workflow. The system was validated through peer heuristic walkthroughs, achieving a 28/35 "
        "usability score (80.0% benchmark on the DBIT evaluation rubric) and 100% task completion across test scenarios. The live application is publicly deployed and operational "
        "at https://aanchalyadav-21.github.io/CMV-space/, demonstrating tangible societal impact by bridging civic isolation and "
        "democratizing access to shared neighborhood resources."
    )
    add_p(abstract_text)

    doc.add_page_break()

    # ==========================================
    # 4. TABLE OF CONTENTS, LIST OF FIGURES & TABLES
    # ==========================================
    add_title("CONTENTS", size=16, space_before=10, space_after=10)
    
    toc_table = doc.add_table(rows=1, cols=3)
    toc_table.rows[0].cells[0].text = "Chapter / Section"
    toc_table.rows[0].cells[1].text = "Title"
    toc_table.rows[0].cells[2].text = "Page"
    
    toc_entries = [
        ("", "List of Figures", "viii"),
        ("", "List of Tables", "ix"),
        ("1", "Introduction", "1"),
        ("1.1", "Problem Identification and Selection", "1"),
        ("1.2", "Empathy Study and Stakeholder Analysis", "2"),
        ("1.3", "Motivation", "4"),
        ("1.4", "Problem Statement", "4"),
        ("1.5", "Objectives and Scope", "5"),
        ("2", "Literature Review and Existing Solutions", "6"),
        ("2.1", "Literature Survey on Current Trends", "6"),
        ("2.2", "Comparative Analysis of Existing Products / Systems", "8"),
        ("2.3", "Research Gaps and Identified Limitations", "9"),
        ("2.4", "Feature List and Justification", "10"),
        ("3", "Field Research and Survey Methodology", "12"),
        ("3.1", "Methodology and Data Collection Plan", "12"),
        ("3.2", "Questionnaire and Interview Design", "13"),
        ("3.3", "Survey and Interview Findings Analysis", "15"),
        ("3.4", "Finalized Feature List Based on Empirical Findings", "18"),
        ("4", "System Design and Creative Ideation", "20"),
        ("4.1", "Proposed System Architecture and Solution Approach", "20"),
        ("4.2", "UML Modeling", "21"),
        ("4.2.1", "Use Case Diagram and Actor Descriptions", "21"),
        ("4.2.2", "Activity Diagram and Process Flow", "23"),
        ("4.2.3", "State Diagram and Transitions", "25"),
        ("4.3", "Project Timeline and Work Breakdown", "27"),
        ("5", "Prototype Implementation and Proof of Concept", "28"),
        ("5.1", "Prototype Development Environment and Software Tools Selected", "28"),
        ("5.2", "Screen-by-Screen Walkthrough and Visual Design", "29"),
        ("6", "User Testing, Peer Review, and Design Evaluation", "35"),
        ("6.1", "Testing Methodology and Task Scenarios", "35"),
        ("6.2", "Usability Walkthrough Evaluation (35-Point Rubric)", "36"),
        ("6.3", "Peer Constructive Feedback Analysis", "38"),
        ("7", "Conclusion: Societal Impact and Future Scope", "39"),
        ("7.1", "Community Impact and Societal Value Created", "39"),
        ("7.2", "Future Enhancements and Deployment Roadmap", "40"),
        ("", "References", "42"),
        ("", "Appendix A: Stakeholder Interaction & Community Survey Evidence", "43"),
        ("", "Appendix B: Course Outcomes, CO-PO-PSO Mapping and Justification", "45")
    ]
    for sec_num, sec_title, p_num in toc_entries:
        r = toc_table.add_row()
        r.cells[0].text = sec_num
        r.cells[1].text = sec_title
        r.cells[2].text = p_num
    set_table_styling(toc_table, [Inches(1.2), Inches(4.5), Inches(0.8)])

    doc.add_page_break()

    add_title("LIST OF FIGURES", size=16, space_before=10, space_after=10)
    fig_table = doc.add_table(rows=1, cols=3)
    fig_table.rows[0].cells[0].text = "Figure No."
    fig_table.rows[0].cells[1].text = "Name of Figure"
    fig_table.rows[0].cells[2].text = "Page"
    
    figures_data = [
        ("Figure 1.1", "Five Iterative Stages of the Design Thinking Process", "2"),
        ("Figure 1.2", "4-Quadrant Empathy Map (Says, Thinks, Does, Feels) for Elderly Residents", "3"),
        ("Figure 1.3", "User Persona Profile: Mrs. Sharda (68-Year-Old Retired Teacher)", "4"),
        ("Figure 3.1", "Distribution of Survey Respondents by Demographic Category (N = 102)", "15"),
        ("Figure 3.2", "Empirical Evaluation of Community Challenges Observed on the Ground", "16"),
        ("Figure 3.3", "Priority Community Services Requested by Survey Respondents", "16"),
        ("Figure 3.4", "Respondent Willingness to Contribute Volunteer Time vs Shared Spaces", "17"),
        ("Figure 3.5", "Validation of Platform Security (PIN/Aadhaar) and Dual Architecture", "18"),
        ("Figure 4.1", "Proposed Layered Architectural Model for the ConnectSphere Platform", "21"),
        ("Figure 4.2", "UML Use Case Diagram Depicting 5 Primary System Actors and Security Kernels", "22"),
        ("Figure 4.3", "UML Activity Diagram: Hyperlocal Micro-Volunteering Errand Workflow", "24"),
        ("Figure 4.4", "UML Activity Diagram: Community Empty Space Discovery and Booking Workflow", "25"),
        ("Figure 4.5", "UML State Machine Diagram: Micro-Volunteering Errand Lifecycle", "26"),
        ("Figure 4.6", "UML State Machine Diagram: Community Space Pass Reservation & QR Lifecycle", "27"),
        ("Figure 4.7", "Gantt Chart: Work Breakdown Structure and Phased Project Execution", "28"),
        ("Figure 5.1", "Landing & Entry Screen Interface (index.html) with Emergency SOS & Helpline", "30"),
        ("Figure 5.2", "Resident Core Service Selection Hub (dashboard.html)", "30"),
        ("Figure 5.3", "Structured Errand Request Form with Urgency Selector (help.html)", "31"),
        ("Figure 5.4", "Pre-Submission Summary Review & Verification Checkpoint (review.html)", "31"),
        ("Figure 5.5", "Live Operational Status Tracker with 4-Digit Doorstep PIN (confirmation.html)", "32"),
        ("Figure 5.6", "Volunteer Operations Hub & Field Mission Desk (volunteer.html)", "32"),
        ("Figure 5.7", "Community Empty Space Directory with Capacity & Amenity Filters (spaces.html)", "33"),
        ("Figure 5.8", "Space Digital Gate Entry Pass with Real-Time SVG QR Code (pass.html)", "33"),
        ("Figure 5.9", "Space Provider Facility Management & Decision Portal (owner.html)", "34"),
        ("Figure 5.10", "Community Event Organizer Hub with Dual-Resource Pairing (organize.html)", "34"),
        ("Figure 5.11", "Safety Grievance & Dispute Resolution Desk (complaints.html)", "35"),
        ("Figure 5.12", "Platform Governance & Supervisor Admin Console (admin.html)", "35")
    ]
    for f_num, f_name, p_num in figures_data:
        r = fig_table.add_row()
        r.cells[0].text = f_num
        r.cells[1].text = f_name
        r.cells[2].text = p_num
    set_table_styling(fig_table, [Inches(1.2), Inches(4.5), Inches(0.8)])

    doc.add_page_break()

    add_title("LIST OF TABLES", size=16, space_before=10, space_after=10)
    tbl_table = doc.add_table(rows=1, cols=3)
    tbl_table.rows[0].cells[0].text = "Table No."
    tbl_table.rows[0].cells[1].text = "Name of Table"
    tbl_table.rows[0].cells[2].text = "Page"
    
    tables_list = [
        ("Table 2.1", "Literature Survey on Current Trends and Academic Benchmark Solutions", "7"),
        ("Table 2.2", "Comparative Feature Matrix of Existing Commercial & Non-Profit Systems", "8"),
        ("Table 2.3", "System Feature List and Engineering Justification Matrix", "11"),
        ("Table 3.1", "Structured 20-Question Survey Questionnaire and Design Rationale", "13"),
        ("Table 3.2", "Demographic Breakdown of Field Survey Respondents (N = 102)", "15"),
        ("Table 3.3", "Empirical Feedback-to-Improvement Engineering Matrix", "19"),
        ("Table 3.4", "Synthesized Dual-Resource Architecture Working Model", "20"),
        ("Table 6.1", "Peer Usability Walkthrough Evaluation (35-Point Heuristic Rubric)", "37"),
        ("Table 6.2", "Peer Constructive Feedback Classification and Architectural Response", "38")
    ]
    for t_num, t_name, p_num in tables_list:
        r = tbl_table.add_row()
        r.cells[0].text = t_num
        r.cells[1].text = t_name
        r.cells[2].text = p_num
    set_table_styling(tbl_table, [Inches(1.2), Inches(4.5), Inches(0.8)])

    doc.add_page_break()

    # ==========================================
    # CHAPTER 1: INTRODUCTION
    # ==========================================
    add_title("CHAPTER 1\nINTRODUCTION", size=16, space_before=12, space_after=14)
    
    add_h1("1.1 Problem Identification and Selection")
    add_p(
        "Modern urban residential ecosystems present an acute socio-technical paradox. In densely populated metropolitan "
        "areas such as Mumbai, the rapid expansion of nuclear households, corporate migration, and changing social fabrics "
        "have left elderly citizens, single patients, and vulnerable residents increasingly isolated. Everyday essential "
        "errands—including obtaining prescription refills from neighborhood chemists, purchasing fresh groceries, collecting "
        "laboratory diagnostic reports, attending medical appointments, or resolving smartphone digital utility queries—pose "
        "severe physical strain and cognitive anxiety for seniors. Although these errands require relatively modest time "
        "commitments (typically 15 to 45 minutes), commercial hyper-convenience and gig-economy applications (such as Dunzo, "
        "Blinkit, or Swiggy Instamart) operate strictly on algorithmic delivery fees, minimum cart value thresholds, and "
        "profit-driven margins. Commercial riders lack background-verified elder-care training, cannot accompany a frail "
        "senior down a flight of stairs, and offer zero interpersonal trust."
    )
    add_p(
        "Simultaneously, neighborhood communities possess significant latent resources that remain disconnected. Urban "
        "housing societies, residential welfare associations (RWAs), charitable trusts, and parish institutions frequently "
        "own community clubhouses, library halls, and activity centers. However, an estimated 65% of these shared communal "
        "spaces remain physically locked and unoccupied during weekday hours and weekends. The existing booking process "
        "is plagued by manual paper registers, informal gatekeeper bias, and a total absence of transparent scheduling. "
        "Grassroots welfare organizations, student tutors, and local youth groups seeking affordable venues to host free "
        "health screening camps, blood donation drives, educational workshops, or senior wellness circles cannot easily "
        "discover or reserve these spaces."
    )
    add_p(
        "This project, ConnectSphere: Community Micro-Volunteering & Empty Space Sharing, identifies this critical gap and "
        "pioneers a unified, community-driven digital platform. By intertwining informal, short-duration mutual-aid volunteering "
        "with transparent, automated community hall reservations, the platform establishes a sustainable neighborhood care network."
    )

    add_h1("1.2 Empathy Study and Stakeholder Analysis")
    add_p(
        "To ground the system architecture in real human needs rather than technical assumptions, the team conducted an "
        "exhaustive design thinking study following the five iterative stages: Empathize, Define, Ideate, Prototype, and Test "
        "(Figure 1.1). Qualitative immersion sessions, observational studies in housing societies, and semi-structured interviews "
        "were conducted with primary stakeholders across Mumbai's suburban localities."
    )

    add_image_with_caption("extracted_images/exp1_img_1.jpg", "Figure 1.1: Five Iterative Stages of the Design Thinking Process (Experiment 1)", width=Inches(5.0))

    add_p(
        "The primary stakeholder groups identified include:\n"
        "1. Senior Citizens & Vulnerable Residents: Suffer from physical mobility limitations, chronic health ailments, "
        "and digital literacy barriers. They desire independence without becoming a financial or logistical burden to their families.\n"
        "2. Student & Youth Volunteers: College and university students possessing spare hours, high digital fluency, and a "
        "strong desire to contribute civic service, but who are dissuaded by cumbersome long-term NGO commitments.\n"
        "3. Community Space Owners & Society Committees: RWA secretaries and trustees who manage society premises. They require "
        "verified credentials, accountable visitor gate-entry tracking, and noise/safety compliance without administrative overhead.\n"
        "4. Grassroots NGOs & Welfare Organizers: Small charitable organizations and teachers requiring reliable volunteer "
        "staffing and affordable venue infrastructure to execute social upliftment drives."
    )

    add_h2("Empathy Mapping: Senior Resident Mindset")
    add_p(
        "The empathy mapping process synthesized field observations across four fundamental human quadrants: Says, Thinks, "
        "Does, and Feels (Figure 1.2):\n"
        "• Says: 'I need someone trustworthy to accompany me for appointments.' 'I don’t want to trouble my working children every day.' 'I just need minor help with heavy groceries.'\n"
        "• Thinks: 'Can I truly trust a stranger entering my building?' 'Will a volunteer be punctual, or will I be stranded?' 'What if something goes wrong during the handover?'\n"
        "• Does: Postpones medical checkups when children are busy; relies hesitantly on domestic maids or neighborhood watchmen; uses basic phone dialers but avoids complex smartphone user interfaces.\n"
        "• Feels: Anxious regarding personal safety; embarrassed to repeatedly ask for favors; lonely and sidelined by modern fast-paced technology; immensely relieved when warm, trustworthy assistance arrives."
    )

    add_image_with_caption("extracted_images/exp1_img_3.jpg", "Figure 1.2: 4-Quadrant Empathy Map and User Persona (Mrs. Sharda, 68) Developed in Experiment 1", width=Inches(5.8))

    add_h2("Detailed User Persona: Mrs. Sharda (Senior Resident)")
    add_p(
        "• Demographics: 68-year-old retired schoolteacher living in Shanti Niketan Society, Sector 4. Her adult children are "
        "working in separate corporate hubs and cannot assist with daytime errands.\n"
        "• Daily Frustrations: Difficulty carrying heavy medicine packages up society staircases; prolonged waiting times at "
        "local chemist counters; intimidation by complex commercial applications with small fonts and high delivery fees.\n"
        "• Functional Needs: A high-contrast, uncluttered interface; one-touch emergency SOS helpline; background-checked "
        "neighborhood volunteers; and a foolproof security mechanism to verify the identity of the volunteer prior to doorstep handover."
    )

    add_h1("1.3 Motivation")
    add_p(
        "The impetus for this project stems from ethical, social, and academic imperatives:\n"
        "1. Social Commitment: Senior citizens and economically vulnerable groups represent the demographic backbone of our "
        "society yet face severe technological exclusion. Engineering solutions must prioritize social good over monetization.\n"
        "2. Civic Asset Optimization: Leaving public and society halls vacant while educational workshops and blood donation "
        "drives struggle for space represents a massive structural inefficiency. Software engineering provides the scheduling "
        "mechanisms to unlock this unused physical capacity.\n"
        "3. Academic & Technical Rigor: Building an offline-resilient, role-isolated, real-time reactive web ecosystem provides "
        "practical mastery over client-side event loops, cross-tab synchronization channels, security cryptography, and responsive UI design."
    )

    add_h1("1.4 Problem Statement")
    add_p(
        '"To develop an accessible, human-centric web platform that seamlessly connects senior citizens and residents needing '
        'small-scale everyday assistance with background-verified neighborhood volunteers, while simultaneously enabling community '
        'members and NGOs to discover, reserve, and verify underutilized civic spaces for welfare activities through automated, '
        'verifiable digital QR gate passes."',
        bold_prefix="Formal Problem Statement: "
    )

    add_h1("1.5 Objectives and Scope")
    add_p("The project aims to achieve the following specific, measurable engineering objectives:")
    add_bullet("Develop a high-contrast, WCAG-compliant multi-role web application supporting five isolated operational personas (Resident, Volunteer, Space Provider, Organizer, and Admin).")
    add_bullet("Implement a 3-step streamlined micro-volunteering dispatch workflow with 4-digit security PIN verification at doorstep delivery.")
    add_bullet("Construct an interactive Community Space Directory with dynamic filtering by capacity, price, and amenities, paired with a verifiable SVG QR gate access slip.")
    add_bullet("Engineer a real-time cross-tab state synchronization architecture using the BroadcastChannel API and storage event listeners to ensure instant decision reactivity (<50 ms).")
    add_bullet("Incorporate safety grievance reporting and administrative KYC audit consoles to ensure complete community accountability.")

    add_p("Scope Boundaries:\n"
          "• In-Scope (Phase 1): Client-side prototype architecture, persistent local/session storage simulation, dynamic SVG QR generation, 4-digit PIN verification, responsive CSS styling, and live GitHub Pages deployment.\n"
          "• Out-of-Scope (Future Phase): Backend SQL/NoSQL clustering, live GPS satellite tracking integration, SMS cellular OTP gateway integration, and financial payment gateway processing."
    )

    doc.add_page_break()

    # ==========================================
    # CHAPTER 2: LITERATURE REVIEW
    # ==========================================
    add_title("CHAPTER 2\nLITERATURE REVIEW AND EXISTING SOLUTIONS", size=16, space_before=12, space_after=14)
    
    add_h1("2.1 Literature Survey on Current Trends")
    add_p(
        "To establish a solid academic foundation, recent peer-reviewed literature in the domains of digital social engagement, "
        "micro-volunteering ergonomics, space utilization analytics, and fifteen-minute community circles was surveyed (Table 2.1)."
    )

    lit_table = doc.add_table(rows=6, cols=5)
    lit_table.rows[0].cells[0].text = "Ref."
    lit_table.rows[0].cells[1].text = "Paper Title & Year"
    lit_table.rows[0].cells[2].text = "Authors"
    lit_table.rows[0].cells[3].text = "Methodology & Key Findings"
    lit_table.rows[0].cells[4].text = "Research Gap & Relation to Project"

    lit_data = [
        ("[1]", "Towards design recommendations for social engagement platforms supporting volunteering targeting older people (2023)",
         "Renny S.N. Lindberg, Beat Signer, Olga De Troyer",
         "Evaluated 10 digital platforms via user interviews. Found usability, high-contrast text, transparent identity verification, and panic helplines are critical for elderly adoption.",
         "Limited evaluation with real-time field deployments. Directly inspired ConnectSphere's font sizing (A-, A, A+), helpline banner, and verified Aadhaar profiles."),
        ("[2]", "Digital volunteering through a volunteering crowdsourcing platform: lessons from TuDu.org.pl (2022)",
         "Aleksandra Belina",
         "Analyzed crowdsourced volunteer micro-tasks. Demonstrated that breaking civic aid into short, flexible micro-tasks dramatically boosts youth participation.",
         "Focused solely on virtual tasks (translation, graphic design). ConnectSphere adapts micro-tasks to physical, localized neighborhood errands."),
        ("[3]", "The role of volunteer experience on performance on online volunteering platforms (2023)",
         "Gloria Urrea, Eunae Yoo",
         "Applied statistical regression on large humanitarian volunteering datasets. Proved gamified recognition (points, badges, verified hours) boosts volunteer retention by 42%.",
         "Neglected physical safety mechanisms during task execution. Inspired ConnectSphere's Volunteer Desk service hours tracker and badge recognition."),
        ("[4]", "Future workspace needs flexibility and diversity: Machine learning-driven behavioural analysis of co-working space (2023)",
         "Maoran Sun, Ramit Debnath, Ronita Bardhan, et al.",
         "Used IoT sensor occupancy logs to cluster space preferences. Concluded that multi-functional, flexible spatial layouts maximize utilization efficiency.",
         "Confined to commercial co-working desks. ConnectSphere extends space sharing to residential society clubhouses and community welfare halls."),
        ("[5]", "Spatial Inequality and Shared Accessibility in the Fifteen-Minute Community Life Circle (2026)",
         "Li Yue, Hongbo Zhao, Yehua Dennis Wei, et al.",
         "Spatial GIS accessibility modeling combined with supply-demand mismatch analysis across urban neighborhoods.",
         "Macro-level policy analysis without an executable software platform. ConnectSphere implements the localized digital platform connecting nearby residents within walking radius.")
    ]
    for idx, (ref, title, authors, meth, gap) in enumerate(lit_data):
        row = lit_table.rows[idx+1].cells
        row[0].text = ref
        row[1].text = title
        row[2].text = authors
        row[3].text = meth
        row[4].text = gap
    set_table_styling(lit_table, [Inches(0.6), Inches(1.8), Inches(1.3), Inches(1.8), Inches(1.5)])

    add_h1("2.2 Comparative Analysis of Existing Products / Systems")
    add_p(
        "Commercial and non-profit mobile applications attempting to solve community challenges were evaluated against "
        "operational pros, cons, and functional capabilities (Table 2.2)."
    )

    comp_table = doc.add_table(rows=6, cols=5)
    comp_table.rows[0].cells[0].text = "Ref."
    comp_table.rows[0].cells[1].text = "Product / System"
    comp_table.rows[0].cells[2].text = "Operational Features"
    comp_table.rows[0].cells[3].text = "Identified Missing Features"
    comp_table.rows[0].cells[4].text = "Comparison with Proposed ConnectSphere"

    comp_data = [
        ("[6]", "Be My Eyes", "Live video assistance connecting visually impaired users with global volunteers for simple reading tasks.",
         "No physical doorstep assistance, no local neighborhood task dispatch, no facility space booking.",
         "ConnectSphere operates hyperlocally for physical errands (medicine, groceries) and incorporates doorstep PIN security."),
        ("[7]", "Catchafire", "Professional skill-based volunteer matching for registered non-profit organizations.",
         "Requires high time commitments (weeks/months); ignores rapid physical micro-errands for individual citizens.",
         "ConnectSphere facilitates 15-minute everyday micro-tasks without corporate barriers."),
        ("[8]", "Idealist", "Global social-impact directory publishing formal internships, full-time jobs, and volunteer events.",
         "Zero live operational tracking, no security PIN verification, lacks community hall discovery.",
         "ConnectSphere provides live status lifecycles, emergency escalation, and gate entry passes."),
        ("[9]", "Peerspace", "Commercial peer-to-peer marketplace for renting private event venues, photo studios, and halls.",
         "Exorbitant commercial rental pricing; strictly profit-driven; completely detached from volunteering.",
         "ConnectSphere democratizes unused society clubhouses for non-profit and welfare use at zero or nominal cost."),
        ("[10]", "VolunteerMatch", "Web-based portal matching volunteers with local non-profit organizations based on location and cause.",
         "Lacks real-time reactivity, no doorstep delivery verification, cannot co-book physical spaces for events.",
         "ConnectSphere uniquely bundles volunteer recruitment with civic venue reservation on a single platform.")
    ]
    for idx, (ref, name, feats, missing, comp) in enumerate(comp_data):
        row = comp_table.rows[idx+1].cells
        row[0].text = ref
        row[1].text = name
        row[2].text = feats
        row[3].text = missing
        row[4].text = comp
    set_table_styling(comp_table, [Inches(0.6), Inches(1.2), Inches(1.8), Inches(1.6), Inches(1.8)])

    add_h1("2.3 Research Gaps and Identified Limitations")
    add_p(
        "The critical examination of academic literature and existing market solutions highlights three fundamental research gaps:\n"
        "1. The Micro-Task / Senior Safety Disconnect: While digital volunteering platforms exist, they remain virtual. Physical "
        "errand platforms fail to provide elderly-appropriate verification protocols (such as physical handover PINs) to prevent "
        "impersonation or theft at the resident's doorstep.\n"
        "2. The Spatial-Civic Isolation Gap: Venue booking engines (e.g., Peerspace) are aggressively commercialized, whereas civic "
        "volunteering hubs ignore spatial needs. An NGO wishing to organize an eye-screening camp must navigate fragmented channels "
        "to separately book a hall and recruit volunteers.\n"
        "3. Cognitive Barrier and Accessibility Neglect: Mainstream platforms feature crowded user interfaces, aggressive commercial "
        "upselling, and micro-interactions that alienate senior citizens with deteriorating eyesight or motor skills."
    )

    add_h1("2.4 Feature List and Justification")
    add_p(
        "To directly address the identified gaps, a preliminary feature set was engineered with rigorous design justifications (Table 2.3)."
    )

    feat_table = doc.add_table(rows=6, cols=3)
    feat_table.rows[0].cells[0].text = "Sr."
    feat_table.rows[0].cells[1].text = "System Feature"
    feat_table.rows[0].cells[2].text = "Engineering Justification Based on Gaps"

    feat_data = [
        ("1", "Location-Based Micro-Task Dispatch", "Enables senior citizens to broadcast small tasks (medicine pickup, groceries) to nearby verified youth within a 1-km radius, ensuring rapid turnaround."),
        ("2", "Doorstep Safety PIN Verification", "A 4-digit code generated exclusively on the senior's screen that the volunteer must input to complete the task, eliminating fraud and false completion."),
        ("3", "Community Space Discovery & Booking", "Unlocks underutilized society clubhouses and parish halls with transparent calendar slots, pricing filters, and amenity tags."),
        ("4", "Verifiable SVG QR Gate Access Slip", "Generates an official digital pass with an embedded QR code upon space owner approval, allowing building security guards to verify attendees without paper passes."),
        ("5", "Dual-Resource NGO Organizer Desk", "Allows welfare organizers to seamlessly request volunteer teams and book a community venue in a unified step, ensuring successful civic drives.")
    ]
    for idx, (sr, feat, just) in enumerate(feat_data):
        row = feat_table.rows[idx+1].cells
        row[0].text = sr
        row[1].text = feat
        row[2].text = just
    set_table_styling(feat_table, [Inches(0.6), Inches(2.2), Inches(4.2)])

    doc.add_page_break()

    # ==========================================
    # CHAPTER 3: FIELD RESEARCH & SURVEY METHODOLOGY
    # ==========================================
    add_title("CHAPTER 3\nFIELD RESEARCH AND SURVEY METHODOLOGY", size=16, space_before=12, space_after=14)
    
    add_h1("3.1 Methodology and Data Collection Plan")
    add_p(
        "To empirically validate the identified problem and prioritize platform features, a rigorous field survey was conducted "
        "across urban residential neighborhoods in Mumbai (Kurla, Chembur, and Ghatkopar). The sampling strategy utilized stratified "
        "random sampling across residential welfare associations, senior citizen morning walking clubs, university student bodies, "
        "and local non-profit trusts.\n\n"
        "A structured 20-question digital and printed survey was administered. A total of N = 102 verified responses were collected, "
        "satisfying statistical validity requirements. Ethical consent and anonymization protocols were strictly enforced."
    )

    add_h1("3.2 Questionnaire and Interview Design")
    add_p(
        "The survey was partitioned into functional thematic sections to extract both quantitative validation and qualitative "
        "design feedback (Table 3.1)."
    )

    q_table = doc.add_table(rows=8, cols=4)
    q_table.rows[0].cells[0].text = "Q.No."
    q_table.rows[0].cells[1].text = "Section"
    q_table.rows[0].cells[2].text = "Sample Question"
    q_table.rows[0].cells[3].text = "Design Purpose & Engineering Justification"

    q_data = [
        ("Q1-Q2", "Respondent Profile", "Which category best describes you? (Student, Working Professional, Homemaker, Senior Citizen)", "Profiles potential user segments to inform UI contrast, font accessibility, and onboarding flows."),
        ("Q3-Q5", "Problem Validation", "Which community challenges have you or your society experienced? (Select all that apply)", "Validates whether the lack of trustworthy volunteers and unused space access are acute ground realities."),
        ("Q6-Q9", "Service Requirements", "Which services would you be most interested in using? (Medicine, Groceries, Tutoring, Space)", "Ranks community demand to prioritize core functional modules on the main selection dashboard."),
        ("Q10-Q12", "Participation & Supply", "Would you be willing to contribute your time or share unused community space?", "Gauges two-sided marketplace viability (supply of volunteers and spaces vs. demand)."),
        ("Q13-Q15", "Trust, Safety & Security", "Do you think Aadhaar KYC and doorstep PIN verification are sufficient for safety?", "Determines whether proposed security measures provide adequate peace of mind for seniors."),
        ("Q16-Q18", "Dual Platform Concept", "Would a platform combining community aid with space sharing benefit your locality?", "Tests user acceptance of the novel integrated architecture."),
        ("Q19-Q20", "Open Feedback & Adoption", "What features or improvements would make this platform most effective?", "Gathers qualitative requirements directly from community members.")
    ]
    for idx, (qno, sec, ques, purp) in enumerate(q_data):
        row = q_table.rows[idx+1].cells
        row[0].text = qno
        row[1].text = sec
        row[2].text = ques
        row[3].text = purp
    set_table_styling(q_table, [Inches(0.8), Inches(1.5), Inches(2.2), Inches(2.5)])

    add_h1("3.3 Survey and Interview Findings Analysis")
    add_p(
        "The survey data collected from N = 102 respondents was analyzed using statistical frequency distribution and cross-tabulation. "
        "The empirical findings are summarized below."
    )

    add_h2("Respondent Demographics")
    add_p("The demographic profile revealed substantial interest from youth volunteers and working professionals (Table 3.2, Figure 3.1).")

    demo_table = doc.add_table(rows=7, cols=3)
    demo_table.rows[0].cells[0].text = "Demographic Category"
    demo_table.rows[0].cells[1].text = "Number of Responses"
    demo_table.rows[0].cells[2].text = "Percentage Distribution (%)"

    demo_data = [
        ("Student (Youth Volunteers)", "49", "48.0%"),
        ("Working Professional", "26", "25.5%"),
        ("Teacher / Academician", "17", "16.7%"),
        ("Homemaker", "7", "6.9%"),
        ("Senior Citizen Resident", "2", "2.0%"),
        ("Other / Community Worker", "1", "1.0%")
    ]
    for idx, (cat, cnt, pct) in enumerate(demo_data):
        row = demo_table.rows[idx+1].cells
        row[0].text = cat
        row[1].text = cnt
        row[2].text = pct
    set_table_styling(demo_table, [Inches(3.2), Inches(1.8), Inches(2.0)])

    add_image_with_caption("extracted_images/charts/fig3_1_demographics.png", "Figure 3.1: Distribution of Survey Respondents by Category (N = 102)", width=Inches(5.5))

    add_h2("Ground-Level Community Challenges Identified")
    add_p(
        "When asked about challenges experienced in their locality (multi-select), 48.0% cited difficulty finding trustworthy volunteers, "
        "46.1% cited students lacking tutoring/guidance, 43.1% cited difficulty finding affordable community spaces, and 41.2% cited "
        "elderly residents needing accompaniment to medical visits (Figure 3.2). Only 11.8% reported facing none of these issues."
    )

    add_image_with_caption("extracted_images/charts/fig3_2_challenges.png", "Figure 3.2: Real-World Community Challenges Identified on the Ground (N = 102)", width=Inches(5.8))

    add_h2("High-Demand Community Services")
    add_p(
        "Medical and hospital appointment assistance emerged as the single highest priority (68.6%, 70 responses), followed by "
        "Tutoring and Mentoring (60.8%, 62 responses), Digital/Technical Literacy (48.0%, 49 responses), and Community Space Booking "
        "(19.6%, 20 responses) (Figure 3.3)."
    )

    add_image_with_caption("extracted_images/charts/fig3_3_services.png", "Figure 3.3: Priority Community Services Requested by Survey Respondents", width=Inches(5.8))

    add_h2("Willingness to Contribute & Platform Security Validation")
    add_p(
        "Crucially, 80.4% of respondents expressed a direct willingness to contribute to their locality—either by volunteering their "
        "time (49.0%), sharing an unused space (5.9%), or both (31.4%) (Figure 3.4). Furthermore, 73.5% confirmed that the proposed "
        "doorstep PIN verification and Aadhaar KYC badges made them completely comfortable using the platform, while 77.5% validated "
        "the combined mutual-aid and space-sharing architecture (Figure 3.5). Finally, 84.3% stated they would actively recommend "
        "the platform to their housing society or college."
    )

    add_image_with_caption("extracted_images/charts/fig3_4_willingness.png", "Figure 3.4: Respondent Willingness to Contribute Mutual Aid or Physical Space", width=Inches(5.5))
    add_image_with_caption("extracted_images/charts/fig3_5_validation.png", "Figure 3.5: Validation of System Safety & Core Dual-Platform Architecture", width=Inches(5.8))

    add_h1("3.4 Finalized Feature List Based on Empirical Findings")
    add_p(
        "Open-ended survey feedback was systematically translated into concrete engineering implementations via a "
        "Feedback-to-Improvement Matrix (Table 3.3)."
    )

    fim_table = doc.add_table(rows=9, cols=3)
    fim_table.rows[0].cells[0].text = "Empirical Feedback Received"
    fim_table.rows[0].cells[1].text = "Identified User Need"
    fim_table.rows[0].cells[2].text = "Final Engineered Implementation in ConnectSphere"

    fim_data = [
        ("Concerns regarding volunteer theft or fraud during home deliveries.", "Security & Identity Verification", "Engineered 4-digit Safety PIN handover verification and supervisor-audited Aadhaar KYC badges."),
        ("Senior citizens cannot read small font sizes on typical apps.", "Visual Accessibility (WCAG)", "Added instant accessibility font scaling controls (A-, A, A+) and high-contrast color styling."),
        ("Space booking in housing societies is opaque and gatekeepers reject visitors.", "Access Accountability", "Automated Space Owner portal with downloadable SVG QR Gate Entry Passes for security guards."),
        ("Volunteers drop out due to lack of recognition.", "Volunteer Motivation & Retention", "Created Volunteer Hub displaying total completed missions, senior citizen ratings, and community service hours."),
        ("Medical prescriptions require accurate notes and pharmacy directions.", "Clear Task Description", "Structured request form with pharmacy notes, address input, and urgency level selectors (Urgent, Today, Flexible)."),
        ("Users accidentally submit duplicate errand requests.", "Submission Safeguards", "Engineered a pre-submission Review Screen (review.html) displaying all errand details before final commit."),
        ("NGOs struggle to separately manage volunteers and event halls.", "Dual-Resource Integration", "Created the Organizer Desk (organize.html) allowing NGOs to pair hall bookings with volunteer teams."),
        ("Residents need immediate emergency escalation during medical crises.", "Crisis Management", "Integrated 24/7 National Emergency SOS (112) and Senior Citizen Helpline (1800-200-4567) top bar.")
    ]
    for idx, (fb, nd, imp) in enumerate(fim_data):
        row = fim_table.rows[idx+1].cells
        row[0].text = fb
        row[1].text = nd
        row[2].text = imp
    set_table_styling(fim_table, [Inches(2.0), Inches(1.8), Inches(3.2)])

    add_h2("Synthesized Dual-Resource Architecture Working Model")
    add_p(
        "Table 3.4 illustrates how the two core pillars of the platform interact synergistically to support complete community initiatives."
    )

    dual_table = doc.add_table(rows=4, cols=3)
    dual_table.rows[0].cells[0].text = "System Section"
    dual_table.rows[0].cells[1].text = "Primary Resource Utilized"
    dual_table.rows[0].cells[2].text = "Core Community Purpose"

    dual_data = [
        ("Community Micro-Volunteering", "Resident time, youth energy, and specialized skills", "Fulfills rapid, localized assistance for seniors (medicine pickup, groceries, tutoring)."),
        ("Community Empty Space Sharing", "Underutilized physical rooms, society halls, clubhouses", "Democratizes access to safe, affordable venues for neighborhood activities."),
        ("Integrated Platform Synergy", "People + Skills + Physical Spaces", "Enables complex initiatives (e.g., an NGO hosting an Eye Screening Camp at Shanti Niketan Clubhouse staffed by youth volunteers).")
    ]
    for idx, (sec, res, purp) in enumerate(dual_data):
        row = dual_table.rows[idx+1].cells
        row[0].text = sec
        row[1].text = res
        row[2].text = purp
    set_table_styling(dual_table, [Inches(2.0), Inches(2.0), Inches(3.0)])

    doc.add_page_break()

    # ==========================================
    # CHAPTER 4: SYSTEM DESIGN & CREATIVE IDEATION
    # ==========================================
    add_title("CHAPTER 4\nSYSTEM DESIGN AND CREATIVE IDEATION", size=16, space_before=12, space_after=14)
    
    add_h1("4.1 Proposed System Architecture and Solution Approach")
    add_p(
        "The architecture of the ConnectSphere platform is structured around a decoupled, 3-tier progressive web model optimized "
        "for high responsiveness, cross-tab reactive synchronization, and zero-dependency client deployment (Figure 4.1):\n"
        "1. Presentation Layer (UI/UX): Built with semantic HTML5, modern CSS3 variables, WCAG-compliant high-contrast themes, "
        "and client-side accessibility font scaling. Features five specialized portal views tailored to each role.\n"
        "2. State & Messaging Layer: Implements a synchronized client-side messaging architecture using the modern HTML5 "
        "BroadcastChannel API (`reach_sync`) paired with `window.onstorage` ping listeners. When a Space Owner approves a booking "
        "or a Volunteer accepts a task in Tab 2, a broadcast message triggers immediate re-rendering of the Resident's pass slip "
        "or live tracker in Tab 1 (<50 ms latency).\n"
        "3. Local Data Store & Persistence Layer (AppStore): A fault-tolerant, encapsulated local storage abstraction layer "
        "(`AppStore`) maintaining collections for tasks, spaces, bookings, activities, KYC verifications, and grievances, with "
        "automatic fallback seeding to guarantee that no view renders blank."
    )

    add_image_with_caption("charts/fig4_1_architecture.png", "Figure 4.1: Proposed Layered Architectural Model for the ConnectSphere Platform", width=Inches(5.8))

    add_h1("4.2 UML Modeling")
    add_p(
        "To rigorously formalize the platform's actors, functional boundaries, operational workflows, and state transitions, "
        "comprehensive UML models were constructed in Experiment 4."
    )

    add_h2("4.2.1 Use Case Diagram and Actor Descriptions")
    add_p(
        "Figure 4.2 illustrates the core use case interactions between the five primary system actors and the supporting security kernels:\n"
        "• Resident / User: Registers/logs in via OTP, browses community services, submits errand assistance requests, books community spaces, tracks requests and bookings, makes payments, and submits ratings and feedback.\n"
        "• Volunteer: Undergoes verification, logs in, views available neighborhood requests, accepts or rejects errand requests, tracks task and location, completes assignments, and views personal task history and ratings.\n"
        "• Space Owner: Registers physical spaces, manages venue specifications and amenities, defines availability schedules, reviews incoming booking requests, and approves or declines venue reservations.\n"
        "• NGO / Society Admin: Coordinates community welfare drives, creates public events, requests volunteer assistance teams, books community spaces, manages member lists, and audits operational summary reports.\n"
        "• System Admin: Verifies user and volunteer credentials, audits space owner listings, resolves grievances and complaints, monitors active tasks, curates platform content, generates analytical reports, and manages system settings.\n"
        "• Included Security & Core Subsystems: Shared use case kernels include Authentication (OTP Login), User Verification (ID Verification), Secure Chat, Emergency SOS escalation, Ratings & Reviews, and Admin Monitoring & Notifications."
    )

    add_image_with_caption("uml_diagrams/use_case_diagram.jpg", "Figure 4.2: UML Use Case Diagram Depicting 5 Primary System Actors and Security Kernels", width=Inches(6.0))

    add_h2("4.2.2 Activity Diagram and Process Flow")
    add_p(
        "The operational flows of the platform are modeled across two fundamental activity workflows:\n"
        "1. Micro-Volunteering Workflow (Figure 4.3): Traces the end-to-end journey from user authentication, role selection, service selection, and errand request submission. The system queries nearby available volunteers. If accepted, the resident receives immediate notification and live tracking begins until task completion and feedback submission. If declined, the user is notified and the request dynamically re-routes to the next nearby volunteer.\n"
        "2. Empty Space Booking Workflow (Figure 4.4): Models parallel execution paths between Space Owners (listing venues, defining amenities, setting time-slot availability, and submitting for review) and Community Users (searching, filtering by capacity/date, and sending booking requests). Both flows converge at the owner review decision gate: approval triggers confirmed status and booking notification; rejection notifies the user and prompts alternative venue discovery."
    )

    add_image_with_caption("uml_diagrams/activity_micro_volunteering.png", "Figure 4.3: UML Activity Diagram: Hyperlocal Micro-Volunteering Errand Workflow", width=Inches(3.3))
    add_image_with_caption("uml_diagrams/activity_space_booking.jpg", "Figure 4.4: UML Activity Diagram: Community Empty Space Discovery and Booking Workflow", width=Inches(3.8))

    add_h2("4.2.3 State Diagram and Transitions")
    add_p(
        "The dynamic state lifecycles of system entities are modeled using finite state machine diagrams:\n"
        "1. Micro-Volunteering Task Lifecycle (Figure 4.5): Beginning from the Initial State, the errand moves to Request Created and enters Waiting for Volunteer. From here, it can transition via Timeout/No Response to Request Cancelled, via User Cancellation to Final State, or upon volunteer acceptance to Volunteer Assigned. It subsequently progresses through Live Location Active, Volunteer Arrived, and Task in Progress. Upon completion, Location Tracking turns off and Rating/Feedback is recorded. If an issue arises during task execution, an Issue/Complaint state triggers Complaint Submission, Investigation, and Administrative Resolution (Warning/Suspension) before terminating at the Final State.\n"
        "2. Community Space Reservation Lifecycle (Figure 4.6): Initiating from User Login, the user browses and views space details before submitting a booking request, placing the booking in Booking Pending (awaiting owner review). If the owner rejects, the state transitions to Booking Rejected with user notification to re-browse. If approved, the state advances to Booking Confirmed, dynamically generating the QR entry code. On event day, the pass transitions to Check-in (QR scan), Space in Use, Checkout (QR scan), and Booking Completed, culminating in Rate and Provide Feedback."
    )

    add_image_with_caption("uml_diagrams/state_errand_lifecycle.png", "Figure 4.5: UML State Machine Diagram: Micro-Volunteering Errand Lifecycle", width=Inches(2.9))
    add_image_with_caption("uml_diagrams/state_space_booking.png", "Figure 4.6: UML State Machine Diagram: Community Space Pass Reservation & QR Lifecycle", width=Inches(2.4))

    add_h1("4.3 Project Timeline and Work Breakdown")
    add_p(
        "The project execution spanned July 2026 to November 2026 across structured developmental phases (Figure 4.7):\n"
        "• Phase 1 — Problem Ideation & Field Survey (July – Aug 2026): Topic finalization, design thinking empathy mapping, and community survey execution (N = 102).\n"
        "• Phase 2 — UML Modeling & System Architecture (Aug – Sept 2026): UML modeling (Use Case, Activity, State), architectural specification, and database schema formulation.\n"
        "• Phase 3 — Core UI/UX & Responsive Prototyping (Sept – Oct 2026): Development of responsive multi-page web application, BroadcastChannel cross-tab synchronization, SVG QR code generation, and PIN security logic.\n"
        "• Phase 4 — Testing, Usability Walkthrough & Deployment (Oct – Nov 2026): Usability evaluation (28/35 heuristic score on DBIT 35-point rubric), peer feedback iterations, GitHub Pages deployment, and documentation."
    )

    add_image_with_caption("charts/fig4_7_gantt_chart.png", "Figure 4.7: Project Timeline Gantt Chart and Work Breakdown Structure (July - November 2026)", width=Inches(6.0))

    doc.add_page_break()

    # ==========================================
    # CHAPTER 5: PROTOTYPE IMPLEMENTATION
    # ==========================================
    add_title("CHAPTER 5\nPROTOTYPE IMPLEMENTATION AND PROOF OF CONCEPT", size=16, space_before=12, space_after=14)
    
    add_h1("5.1 Development Environment and Software Tools Selected")
    add_p(
        "To deliver a robust, high-fidelity proof of concept (PoC), the team selected full-stack client-side web technologies "
        "(HTML5, CSS3, JavaScript ES6) rather than static mockup tools (Figma/Canva). This decision was justified by several technical factors:\n"
        "1. True Interactivity & State Persistence: Unlike click-through image frames, HTML/JS allows persistent storage of form data "
        "across pages, dynamic mathematical QR code rendering, and live state transitions.\n"
        "2. Real-Time Cross-Window Communication: Web APIs (BroadcastChannel, LocalStorage event listeners) enable live testing "
        "across two separate browser tabs (e.g., Space Owner on Tab 2 approving a request and instantly witnessing Tab 1 update).\n"
        "3. Zero-Deployment Friction: Pure client-side web technology deploys seamlessly to GitHub Pages, allowing any evaluator "
        "or senior citizen to access the live system immediately without installing bulky APKs or container runtimes."
    )

    add_h1("5.2 Screen-by-Screen Walkthrough and Visual Design")
    add_p(
        "The platform architecture guides users through an intuitive, forward-moving 5-screen primary journey without dead ends, "
        "complemented by specialized operational desks. The detailed walkthrough of each screen interface is presented below."
    )

    # Screens 1 to 5
    add_h2("Screen 1: Landing & Welcome Portal Gateway (index.html)")
    add_p(
        "• Purpose: Serves as the public entry gateway for all neighborhood stakeholders. Displays the 24/7 senior citizen toll-free helpline (1800-200-4567), emergency SOS panic trigger, font size adjusters (A-, A, A+), service comparison overview, and a role-based login gateway.\n"
        "• Visual Elements: Prominent helpline banner, neighborhood care branding, Aadhaar-verified login cards, quick demo-role selector.\n"
        "• Forward Interaction: User selects their role (e.g., 'Resident / Senior') and clicks 'Sign In' or 'Get Help' → Navigates directly to the Resident Hub (dashboard.html)."
    )
    add_image_with_caption("extracted_images/exp5/screen_1.png", "Figure 5.1: Landing & Entry Screen Interface (index.html)", width=Inches(5.6))

    add_h2("Screen 2: Core Feature & Problem Category Selection (dashboard.html)")
    add_p(
        "• Purpose: Presents the resident with an uncluttered directory of assistance categories and an active overview of pending requests.\n"
        "• Visual Elements: Aadhaar verification badge, large visual category cards (Medicine Pickup, Grocery Aid, Student Tutoring, Companion Walk), and active booking list.\n"
        "• Forward Interaction: Clicking on a service card (e.g., 'Medicine Pickup') or 'Request Errand Help' → Focuses the action form and navigates to Screen 3 (help.html)."
    )
    add_image_with_caption("extracted_images/exp5/screen_2.jpg", "Figure 5.2: Resident Core Service Selection Hub (dashboard.html)", width=Inches(5.6))

    add_h2("Screen 3: Input / Action / Form Screen (help.html)")
    add_p(
        "• Purpose: Captures structured errand requirements in a clean, senior-friendly format without cognitive overload.\n"
        "• Visual Elements: Errand category selector, prescription/item notes textarea, pickup/delivery address input, preferred execution time slot, urgency level pills (Urgent / Today / Flexible), and voice accessibility transcription.\n"
        "• Forward Interaction: User completes inputs and clicks 'Proceed to Review Request →' → Validates all fields, bundles data into session draft, and navigates to Screen 4 (review.html)."
    )
    add_image_with_caption("extracted_images/exp5/screen_3.png", "Figure 5.3: Structured Errand Request Form (help.html)", width=Inches(5.6))

    add_h2("Screen 4: Confirmation / Detail Review Screen (review.html)")
    add_p(
        "• Purpose: Critical verification checkpoint that aggregates all entered errand data to eliminate accidental submissions or typographical errors.\n"
        "• Visual Elements: Summary table displaying category, items, address, contact phone, delivery estimate, and safety guarantee badge.\n"
        "• Forward Interaction: User reviews details and clicks 'Confirm & Request Volunteer →' → Commits the task to the community pool, generates Tracking ID (TSK-101), issues Safety PIN (4821), and navigates to Screen 5 (confirmation.html)."
    )
    add_image_with_caption("extracted_images/exp5/screen_4.png", "Figure 5.4: Pre-Submission Summary Review Screen (review.html)", width=Inches(5.6))

    add_h2("Screen 5: Success & Live Operational Status Tracker (confirmation.html)")
    add_p(
        "• Purpose: Displays real-time operational status updates for the dispatched task, volunteer arrival details, and the essential safety PIN.\n"
        "• Visual Elements: Horizontal multi-step progress stepper, status banner ('Volunteer Assigned & En Route: Karan Verma'), assigned volunteer contact card, and a prominent 4-digit Handover PIN (#4821).\n"
        "• Forward Interaction: Once the volunteer arrives at the doorstep, the senior verbally provides the PIN to verify safe delivery. Clicking 'Return to Dashboard' returns to the user hub."
    )
    add_image_with_caption("extracted_images/exp5/screen_5.png", "Figure 5.5: Live Operational Status Tracker with 4-Digit Doorstep PIN (confirmation.html)", width=Inches(5.6))

    # Extended Desks: Screens 6 to 12
    add_h2("Screen 6: Volunteer Operations Hub & Field Desk (volunteer.html)")
    add_p(
        "• Purpose: Specialized field operations portal for background-verified volunteers to manage assignments.\n"
        "• Visual Elements: Online/Paused duty toggle, total completed missions counter, senior citizen rating display (4.9/5.0), and list of nearby broadcasted errands with distance indicators (e.g., '0.4 km away').\n"
        "• Forward Interaction: Volunteer clicks 'Accept Errand' to claim a task, initiates travel, and clicks 'Verify Safety PIN & Complete' to input the senior's PIN upon physical delivery."
    )
    add_image_with_caption("extracted_images/exp5/screen_6.png", "Figure 5.6: Volunteer Operations Hub & Field Desk Interface (volunteer.html)", width=Inches(5.6))

    add_h2("Screen 7: Community Empty Space Directory (spaces.html)")
    add_p(
        "• Purpose: Searchable civic catalog of underutilized neighborhood facilities (society clubhouses, parish halls, reading rooms).\n"
        "• Visual Elements: Search bar, capacity filters (1-50, 50-100, 100+), pricing tags (Free / Subsidized), amenity badges (Air Conditioning, Tables, Restroom), and space cards.\n"
        "• Forward Interaction: User clicks 'Book / Request Space' on a venue card (e.g., 'Shanti Niketan Clubhouse') → Opens the reservation modal and advances to the review process."
    )
    add_image_with_caption("extracted_images/exp5/screen_7.png", "Figure 5.7: Community Empty Space Directory (spaces.html)", width=Inches(5.6))

    add_h2("Screen 8: Space Digital Entry Pass & Verifiable QR Slip (pass.html)")
    add_p(
        "• Purpose: Official digital slip generated for community space reservations, dynamically reflecting owner approval or rejection.\n"
        "• Visual Elements: High-contrast header, reference ID (#BKG-2026-902), live status banner (Green for Confirmed, Red for Declined, Yellow for Pending), dynamically computed SVG QR code token, caretaker hotline, and a 'Download / Print Pass' button.\n"
        "• Forward Interaction: Attendees present this digital slip at the building security gate for instant visual or QR camera verification."
    )
    add_image_with_caption("extracted_images/exp5/screen_8.png", "Figure 5.8: Space Digital Gate Entry Pass with Real-Time SVG QR Code (pass.html)", width=Inches(5.6))

    add_h2("Screen 9: Space Provider Facility Management Portal (owner.html)")
    add_p(
        "• Purpose: Administrative desk for society secretaries and venue trustees to manage facilities and evaluate incoming requests.\n"
        "• Visual Elements: Pending requests counter, booking cards with requester details, and instant '✓ Approve (Generate QR)' and '✗ Reject Request' decision buttons.\n"
        "• Forward Interaction: Space Owner clicks 'Approve' or 'Reject' → Updates central store and broadcasts sync event over BroadcastChannel, instantly updating the member's pass slip."
    )
    add_image_with_caption("extracted_images/exp5/screen_9.png", "Figure 5.9: Space Provider Facility Management Portal (owner.html)", width=Inches(5.6))

    add_h2("Screen 10: Community Event Organizer Hub (organize.html)")
    add_p(
        "• Purpose: Enables NGOs and welfare organizers to schedule complex community drives by bundling venue reservations with volunteer recruitment.\n"
        "• Visual Elements: Multi-resource event creation form, required volunteer headcount input, space venue dropdown, and active dual-tracker view.\n"
        "• Forward Interaction: Organizer submits event details → Automatically posts volunteer openings to the Volunteer Hub and submits a booking request to the Space Owner."
    )
    add_image_with_caption("extracted_images/exp5/screen_10.png", "Figure 5.10: Community Event Organizer Desk (organize.html)", width=Inches(5.6))

    add_h2("Screen 11: Safety Grievance & Dispute Resolution Desk (complaints.html)")
    add_p(
        "• Purpose: Civic dispute desk ensuring complete accountability, providing residents and volunteers a transparent channel to report misconduct or facility damage.\n"
        "• Visual Elements: Structured grievance form capturing related booking ID, incident category, detailed statement, and evidence photo attachment.\n"
        "• Forward Interaction: User clicks 'Submit Grievance' → Generates a tracked ticket (#CMP-2026-104) and routes it to the administrative oversight queue."
    )
    add_image_with_caption("extracted_images/exp5/screen_11.png", "Figure 5.11: Safety Grievance & Dispute Resolution Desk (complaints.html)", width=Inches(5.6))

    add_h2("Screen 12: Platform Governance & Supervisor Admin Console (admin.html)")
    add_p(
        "• Purpose: Executive oversight portal for college project supervisors and community administrators to audit platform integrity.\n"
        "• Visual Elements: PIN-protected security gateway (PIN: admin2026), live statistics dashboard, volunteer Aadhaar KYC verification queue, space safety audit, and complaint investigation console.\n"
        "• Forward Interaction: Administrator reviews uploaded photo IDs and clicks 'Approve KYC & Grant Verified Badge' to activate new volunteer accounts."
    )
    add_image_with_caption("extracted_images/exp5/screen_12.png", "Figure 5.12: Platform Governance & Supervisor Admin Console (admin.html)", width=Inches(5.6))

    add_h2("Proof of Concept Deployment Details")
    add_bullet("Live Deployed URL: https://aanchalyadav-21.github.io/CMV-space/", bold_prefix="Public Web Application: ")
    add_bullet("GitHub Source Code Repository: https://github.com/aanchalyadav-21/CMV-space", bold_prefix="Version-Controlled Repository: ")
    add_bullet("Deployment Stack: Semantic HTML5, CSS3 Variables, Modern JavaScript ES6, GitHub Actions Pages Pipeline.", bold_prefix="Technology Architecture: ")

    doc.add_page_break()

    # ==========================================
    # CHAPTER 6: USER TESTING & EVALUATION
    # ==========================================
    add_title("CHAPTER 6\nUSER TESTING, PEER REVIEW, AND DESIGN EVALUATION", size=16, space_before=12, space_after=14)
    
    add_h1("6.1 Testing Methodology and Primary Task Scenario")
    add_p(
        "To rigorously evaluate the functional usability, visual clarity, navigation flow, and design consistency of the "
        "developed web prototype, structured peer walkthrough testing was conducted during Experiment 6 under the "
        "Community Engagement Project 1 curriculum (Course Code: 25CE3CEP01, AY 2026-27).\n\n"
        "• Evaluated Group: Group No. C-04 (Class: COMP C, Batch: C)\n"
        "• Student Investigators: Aanchal Yadav (Roll No. 54), Ansley Rayen (Roll No. 45), Simone Rodrigues (Roll No. 46), "
        "Kritika Singh (Roll No. 56), Disha Shetty (Roll No. 50).\n"
        "• Prototype Evaluated: Community Micro-Volunteering & Empty Space (ConnectSphere).\n"
        "• Prototyping Stack: HTML / CSS / JavaScript.\n"
        "• Reviewer Group: Group No. C-05 (Reviewer Group Lead Signature: Shreyash).\n"
        "• Faculty Evaluator: Prof. Snehal (Reviewed & Signed: 26/10/26).\n"
        "• Primary Task Scenario Given to Users: \"Smooth flow from login (role-based) to task completion\".\n\n"
        "Evaluators from Reviewer Group C-05 executed an end-to-end user journey simulating typical residential interactions: "
        "logging into the platform, selecting designated user roles, submitting an errand assistance request, reviewing task summary, "
        "monitoring live status with the 4-digit doorstep Safety PIN, booking a community space with owner approval, and verifying "
        "the final confirmation slip and SVG QR gate pass."
    )

    add_h1("6.2 Usability Walkthrough Evaluation (35-Point Rubric)")
    add_p(
        "The quantitative evaluation was formally administered using DBIT's standardized Part A: Usability & Visual Walkthrough "
        "Rubric. Reviewer Group C-05 assessed seven core HCI heuristic parameters on a 5-point Likert scale (1 = Strongly Disagree, "
        "2 = Disagree, 3 = Neutral, 4 = Agree, 5 = Strongly Agree), yielding a total possible score of 35 points. "
        "The exact scores and evaluative findings recorded during the laboratory session are presented in Table 6.1."
    )

    rubric_table = doc.add_table(rows=9, cols=4)
    rubric_table.rows[0].cells[0].text = "Sr. No."
    rubric_table.rows[0].cells[1].text = "Evaluation Parameter & Rubric Checklist Prompt"
    rubric_table.rows[0].cells[2].text = "Score (1–5)"
    rubric_table.rows[0].cells[3].text = "Evaluator Assessment & Observation"

    rubric_data = [
        ("1", "First Impression & Clarity: On the landing screen, is it instantly clear what community problem this product addresses?", "4", "Agree. The landing page clearly articulates the dual neighborhood mandate of hyperlocal errand assistance and civic venue sharing."),
        ("2", "Button Affordance: Are interactive buttons and clickable cards visually distinct from static elements and banners?", "3", "Neutral. Reviewers noted that certain profile cards contained multiple buttons performing duplicate tasks, creating visual ambiguity."),
        ("3", "Forward Navigation Flow: Does clicking primary CTA buttons advance you smoothly to the expected next screen without dead ends?", "4", "Agree. Forward progression from service selection to form input, review screen, and live status tracker operated smoothly without dead ends."),
        ("4", "Typography & Legibility: Are all headings, body text, and labels easy to read with good contrast against the background?", "4.5", "Strongly Agree / High Distinction. Clear typographic hierarchy, high-contrast headings, and accessible label sizing ensured excellent readability."),
        ("5", "Design System Consistency: Are visual components (fonts, colors, button styles, corner radii) uniform across all screens?", "3.5", "Satisfactory / Above Average. Card corner radii and typography were uniform, but the color palette chosen was noted as visually overwhelming on specific pages."),
        ("6", "Clarity of Language: Are labels, buttons, and instructions free from confusing technical jargon and easy for everyday users to grasp?", "4", "Agree. Action-oriented terms such as 'Senior Assistance', 'Medicine Pickup', and 'Book Space' were intuitive and free of developer jargon."),
        ("7", "Task Completion Feedback: On the final screen, is it clearly confirmed that the task or action was completed successfully?", "5", "Strongly Agree (Perfect Score). The live operational tracker with the 4-digit doorstep Safety PIN (#4829) and instant SVG QR pass provided unambiguous confirmation."),
        ("Total", "TOTAL USABILITY SCORE (Sum of Parameters 1 to 7)", "28 / 35", "Overall Usability Benchmark: 80.0% (Strong Performance across Core User Journeys).")
    ]
    for idx, (sr, param, score, obs) in enumerate(rubric_data):
        row = rubric_table.rows[idx+1].cells
        row[0].text = sr
        row[1].text = param
        row[2].text = score
        row[3].text = obs
    set_table_styling(rubric_table, [Inches(0.6), Inches(2.9), Inches(0.9), Inches(2.6)])

    p_tot = doc.add_paragraph("Quantitative Summary: The prototype achieved an overall score of 28.0 / 35.0 (80.0%). The system excelled particularly in Task Completion Feedback (5/5) and Typography & Legibility (4.5/5), while identifying button affordance (3/5) and color palette calibration (3.5/5) as key areas for targeted refinement.")
    p_tot.paragraph_format.space_before = Pt(6)
    p_tot.paragraph_format.space_after = Pt(12)
    for r in p_tot.runs:
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)

    add_h1("6.3 Peer Constructive Feedback Analysis")
    add_p(
        "Qualitative feedback was formally recorded in Part B: Peer Constructive Feedback by Reviewer Group C-05 (signed by Shreyash) "
        "and supplemented by Faculty Evaluation recommendations (dated 26/10/26). The observations are categorized into Specific Likes, "
        "Criticisms, Unclear Aspects, and Concrete Improvement Ideas, followed by the engineered rectifications applied in the final release."
    )

    add_h2("6.3.1 Qualitative Observations Collected from Peer Reviewers")
    add_p(
        "1. Likes (What worked well):\n"
        "• Activity Screen: Reviewers highlighted the live activity screen as a standout UI accomplishment, praising its real-time operational status updates, step progress visualization, and transparent errand tracking.\n"
        "• Dashboard: The centralized role-based dashboard was commended for clean structural layout, intuitive service cards, and seamless entry into micro-volunteering and space reservation workflows.\n\n"
        "2. Criticisms (Points of friction or confusion):\n"
        "• Duplicate Button Controls: 'The screen consists of multiple buttons doing the same task.' Reviewers observed redundant action buttons on user and profile cards that caused hesitation regarding which button to click.\n"
        "• Overwhelming Color Palette: 'The color palette chose looks overwhelming.' The initial color scheme featured multiple competing vibrant colors across adjacent elements, causing visual fatigue.\n\n"
        "3. Questions (Unclear aspects):\n"
        "• 'Nothing.' Reviewer Group C-05 confirmed that the interface left zero unanswered questions during interaction; the operational pathways, role separation, and functional steps were clear and self-contained.\n\n"
        "4. Ideas for Design Improvement (Peer Suggestions):\n"
        "• Text Density Reduction: 'Reduce the amount of text onto each screen.' Trimming descriptive body paragraphs to ensure quick scanning, especially for senior citizen usability.\n"
        "• Color & Layout Harmonization: 'Can use good colour combinations for layout & remove the extra buttons doing the same task.' Streamlining duplicate controls into a unified primary CTA and adopting a harmonious, restrained color palette."
    )

    add_h2("6.3.2 Faculty Feedback and Key Recommendations")
    add_p(
        "Faculty Reviewer (Prof. Snehal, Evaluated: 26/10/26) provided authoritative academic feedback:\n"
        "\"Redundant buttons on profiles. & interface is a bit bulky. Overall design is consistent. Title needs work. Overall, good work for integrating two solutions in one.\"\n\n"
        "The faculty commended the successful conceptual and technical integration of two complementary societal solutions—hyperlocal "
        "micro-volunteering mutual aid and community empty space sharing—into a single unified ecosystem. Concurrently, three specific "
        "directives were issued: (1) eliminate redundant profile buttons; (2) reduce interface bulkiness; and (3) formalize the project title."
    )

    add_h2("6.3.3 Feedback-Driven Design Rectifications Implemented")
    add_p(
        "To directly address all peer criticisms and faculty directives, the engineering team executed four concrete architectural "
        "and visual iterations in the final deployed version of ConnectSphere (Table 6.2)."
    )

    peer_fb_table = doc.add_table(rows=5, cols=4)
    peer_fb_table.rows[0].cells[0].text = "Source & Category"
    peer_fb_table.rows[0].cells[1].text = "Identified Observation / Friction"
    peer_fb_table.rows[0].cells[2].text = "Root Cause Analysis"
    peer_fb_table.rows[0].cells[3].text = "Engineered Rectification Applied in ConnectSphere"

    peer_fb_data = [
        ("Peer Criticism (C-05) & Faculty Note", "The screen consists of multiple buttons doing the same task; redundant buttons on profiles.", "Duplicate CTA buttons existed on profile views and card headers performing identical navigation actions.", "Pruned all redundant button triggers. Each card and profile view was refactored to feature a single, high-affordance primary action button with distinct visual hierarchy."),
        ("Peer Criticism (C-05)", "The color palette chose looks overwhelming.", "Uncoordinated high-saturation accent colors competed for visual attention across adjacent dashboard cards.", "Refactored the CSS design system using the 60-30-10 color rule: 60% neutral background (#f8fafc), 30% slate structural cards (#ffffff with #334155 text), and 10% focused accent colors (emerald #10b981 for confirmation, navy #0369a1 for navigation)."),
        ("Peer Suggestion & Faculty Note", "Reduce amount of text onto each screen; interface is a bit bulky.", "Lengthy instructional paragraphs increased cognitive load for elderly residents.", "Streamlined text density across all 12 screens. Replaced multi-line instructions with concise bullet summaries, modal help tooltips, and progressive disclosure toggles."),
        ("Faculty Recommendation", "Title needs work; overall good work for integrating two solutions in one.", "Preliminary working title 'CMV-Space' was an ambiguous developer acronym.", "Formalized the project branding across all screens, documentation, and repository to 'ConnectSphere: Community Micro-Volunteering & Empty Space Sharing'.")
    ]
    for idx, (cat, fb, fric, rect) in enumerate(peer_fb_data):
        row = peer_fb_table.rows[idx+1].cells
        row[0].text = cat
        row[1].text = fb
        row[2].text = fric
        row[3].text = rect
    set_table_styling(peer_fb_table, [Inches(1.4), Inches(1.8), Inches(1.8), Inches(2.0)])

    doc.add_page_break()

    # ==========================================
    # CHAPTER 7: CONCLUSION & FUTURE SCOPE
    # ==========================================
    add_title("CHAPTER 7\nCONCLUSION: SOCIETAL IMPACT AND FUTURE SCOPE", size=16, space_before=12, space_after=14)
    
    add_h1("7.1 Community Impact and Societal Value Created")
    add_p(
        "The ConnectSphere: Community Micro-Volunteering & Empty Space Sharing project successfully demonstrates that human-centered "
        "software engineering can directly alleviate urban social isolation and resource misallocation. By establishing an "
        "accessible digital bridge between vulnerable senior citizens, energetic student volunteers, housing society committees, "
        "and non-profit organizers, the platform achieves substantial societal impact:\n"
        "1. Restoring Senior Independence: Enables elderly residents to procure emergency medicines, attend clinic visits, and "
        "manage household errands with dignity, reducing anxiety and dependency on distant relatives.\n"
        "2. Fostering Intergenerational Empathy: Channels college youth energy into structured, rewarding civic micro-volunteering "
        "without demanding unsustainable long-term time commitments.\n"
        "3. Optimizing Underutilized Community Assets: Unlocks hundreds of square feet of idle community hall and clubhouse capacity, "
        "transforming locked rooms into bustling community learning centers, medical screening camps, and yoga circles.\n"
        "4. Enforcing Transparent Governance: Eliminates gatekeeper bias through automated reservation approvals, tamper-evident "
        "doorstep PIN verification, and formal grievance reporting."
    )
    add_p(
        "Prototype Constraints & Boundaries:\n"
        "As a Phase 1 implementation, the current system relies on client-side state machines and simulated databases. While "
        "highly performant for localized demonstration, it operates within single-device browser storage environments and lacks "
        "real-time multi-tenant cloud persistence and automated SMS cellular gateway triggers."
    )

    add_h1("7.2 Future Enhancements and Deployment Roadmap")
    add_p(
        "To transition the validated prototype into a production-grade municipal utility, a phased development roadmap is planned:\n"
        "• Phase 2 — Cloud Backend & Real-Time Geospatial Engine: Migrate local storage to a distributed cloud database (Node.js/Express "
        "with PostgreSQL and Redis caching). Integrate OpenStreetMap and Leaflet geospatial indexing to calculate exact walking distances "
        "and match tasks within precise 500-meter neighborhood clusters.\n"
        "• Phase 3 — Cellular SMS & Voice Accessibility Integration: Implement Twilio/Fast2SMS cellular APIs to dispatch SMS OTPs "
        "and doorstep PIN notifications directly to basic senior feature phones without requiring smartphone app installation. Incorporate "
        "Web Speech API for multilingual voice-based task submission in Marathi, Hindi, and English.\n"
        "• Phase 4 — Government & Municipal Corporation Collaboration: Partner with local municipal ward offices (BMC) and Senior "
        "Citizen Welfare Associations to integrate verified voter ID/Aadhaar DigiLocker verification, institutionalizing the platform "
        "as an official civic mutual-aid infrastructure."
    )
    add_p(
        "In synthesis, Community Engagement Project 1 has successfully traversed the complete trajectory from field-level empathy "
        "discovery and empirical survey validation to rigorous UML architectural modeling and a fully deployed, tested web application, "
        "fulfilling all academic objectives of Course Code 25CE3CEP01 with engineering excellence and social purpose."
    )

    doc.add_page_break()

    # ==========================================
    # REFERENCES
    # ==========================================
    add_title("REFERENCES", size=16, space_before=12, space_after=14)
    add_p("All references are cited in IEEE format in the order of appearance within the text:")

    refs = [
        "[1] R. S. N. Lindberg, B. Signer, and O. De Troyer, \"Towards design recommendations for social engagement platforms supporting volunteering targeting older people in local communities,\" in Proc. 16th Int. Conf. on PErvasive Technologies Related to Assistive Environments (PETRA '23), Corfu, Greece, 2023, pp. 245–254.",
        "[2] A. Belina, \"Digital volunteering through a volunteering crowdsourcing platform: lessons from TuDu.org.pl,\" European Journal of Service Management, vol. 41, no. 1, pp. 15–24, 2022.",
        "[3] G. Urrea and E. Yoo, \"The role of volunteer experience on performance on online volunteering platforms,\" Journal of Operations Management, vol. 69, no. 4, pp. 582–605, 2023.",
        "[4] M. Sun, R. Debnath, N. Lonsdale, C. Wilcox, and R. Bardhan, \"Future workspace needs flexibility and diversity: A machine learning-driven behavioural analysis of co-working space,\" Building and Environment, vol. 235, p. 110214, 2023.",
        "[5] L. Yue, H. Zhao, Y. D. Wei, P. Zhao, C. Miao, H. Zhang, and S. Wang, \"Spatial inequality and shared accessibility in the fifteen-minute community life circle,\" Applied Geography, vol. 162, p. 103164, 2026.",
        "[6] Be My Eyes, \"Bringing sight to blind and low-vision people,\" Official Platform Documentation, 2024. [Online]. Available: https://www.bemyeyes.com. [Accessed: Oct. 2026].",
        "[7] Catchafire, \"Skills-based volunteer matching for social good,\" Catchafire Knowledge Base, 2023. [Online]. Available: https://www.catchafire.org. [Accessed: Oct. 2026].",
        "[8] Idealist, \"Connecting people, organizations, and resources for good,\" Action Without Borders, 2024. [Online]. Available: https://www.idealist.org. [Accessed: Oct. 2026].",
        "[9] Peerspace, \"Unique spaces for meetings, events, and productions,\" Peerspace Platform Guide, 2024. [Online]. Available: https://www.peerspace.com. [Accessed: Oct. 2026].",
        "[10] VolunteerMatch, \"Where volunteering begins,\" VolunteerMatch Research Reports, 2024. [Online]. Available: https://www.volunteermatch.org. [Accessed: Oct. 2026].",
        "[11] World Health Organization, \"World report on ageing and health,\" WHO Guidelines Approved by the Guidelines Review Committee, Geneva, Switzerland, Tech. Rep., 2021.",
        "[12] W3C, \"Web Content Accessibility Guidelines (WCAG) 2.1,\" W3C Recommendation, Jun. 2018. [Online]. Available: https://www.w3.org/TR/WCAG21/.",
        "[13] MDN Web Docs, \"BroadcastChannel API: Synchronizing state across browsing contexts,\" Mozilla Developer Network, 2024. [Online]. Available: https://developer.mozilla.org/en-US/docs/Web/API/BroadcastChannel."
    ]
    for ref_str in refs:
        p_r = doc.add_paragraph()
        p_r.paragraph_format.space_after = Pt(6)
        p_r.paragraph_format.line_spacing = 1.15
        r = p_r.add_run(ref_str)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10.5)

    doc.add_page_break()

    # ==========================================
    # APPENDICES
    # ==========================================
    add_title("APPENDICES", size=16, space_before=12, space_after=14)
    
    add_h1("Appendix A - Stakeholder Interaction / Community Evidence")
    add_p(
        "As mandated by the Community Engagement Project guidelines, documentary evidence of field engagement, stakeholder "
        "interaction, and survey execution was compiled:\n"
        "1. Field Survey Administration: Digital questionnaire links and hardcopy feedback sheets administered across residential "
        "societies in Kurla and Chembur, securing N = 102 verified responses.\n"
        "2. Stakeholder Video/In-Person Consultations: Consultations conducted with elderly residents, resident welfare committee "
        "members (Shanti Niketan CHS), and student volunteer representatives.\n"
        "3. Live Platform Demonstration: Tested live with peer evaluators on GitHub Pages, verifying the real-time cross-tab space "
        "decision synchronization and doorstep PIN verification workflows."
    )

    add_h1("Appendix B - Course Outcomes, CO-PO-PSO Mapping and Evidence of CO Achievement")
    add_p(
        "Table B.1 maps the project artifacts and report sections against the Course Outcomes (CO1 to CO6) prescribed for "
        "Community Engagement Project 1 (25CE3CEP01)."
    )

    co_table = doc.add_table(rows=7, cols=3)
    co_table.rows[0].cells[0].text = "Course Outcome (CO)"
    co_table.rows[0].cells[1].text = "Project Evidence / Delivered Artefact"
    co_table.rows[0].cells[2].text = "Report Section"

    co_data = [
        ("CO1: Identify community needs, stakeholder requirements, and SDGs. (Remember - Factual Knowledge)",
         "• Completed 4-Quadrant Empathy Map (Says, Thinks, Does, Feels)\n• Detailed User Persona Profile (Mrs. Sharda, 68)",
         "Sections 1.1 and 1.2"),
        ("CO2: Explain social, environmental, technical, and ethical factors influencing solutions. (Understand - Conceptual)",
         "• Comparative literature matrix of 5 recent research papers\n• Benchmark analysis of 5 existing applications and identified research gaps",
         "Sections 2.1, 2.2, and 2.3"),
        ("CO3: Apply appropriate engineering tools, models, and methodologies. (Apply - Procedural Knowledge)",
         "• UML System Models: Use Case Diagram, Activity Diagrams (Volunteering & Space), State Machine Diagrams\n• Work Breakdown Gantt Chart",
         "Sections 4.2 and 4.3"),
        ("CO4: Analyse system performance, stakeholder feedback, and operational constraints. (Analyse - Conceptual & Procedural)",
         "• Structured field survey analysis report (charts and percentage distributions from N = 102 respondents)\n• Formulated 1-2 sentence validated Problem Statement and Feature Justification Matrix",
         "Sections 3.3, 3.4, and Appendix A"),
        ("CO5: Evaluate functionality, sustainability, and societal impact using technical criteria. (Evaluate - Metacognitive)",
         "• Completed 35-point Usability & Visual Walkthrough rubric across 7 heuristic parameters (Scored 28.0/35.0 on DBIT rubric)\n• Structured Peer Constructive Feedback report from Group C-05 and Faculty Review",
         "Sections 6.2 and 6.3"),
        ("CO6: Design and validate an innovative, sustainable, and socially relevant solution. (Create - Metacognitive Knowledge)",
         "• Interactive 5-screen primary user journey + 7 extended operational desks\n• Version-controlled GitHub repository and live public deployment on GitHub Pages (https://aanchalyadav-21.github.io/CMV-space/)",
         "Chapter 5 (Sections 5.1 and 5.2)")
    ]
    for idx, (co, ev, sec) in enumerate(co_data):
        row = co_table.rows[idx+1].cells
        row[0].text = co
        row[1].text = ev
        row[2].text = sec
    set_table_styling(co_table, [Inches(2.2), Inches(3.5), Inches(1.3)])

    add_h2("CO-PO-PSO Mapping Matrix")
    add_p("The project's contribution across Program Outcomes (PO1 to PO11) and Program Specific Outcomes (PSO1 to PSO3) is articulated below (1 = Low, 2 = Medium, 3 = High):")

    matrix_table = doc.add_table(rows=7, cols=15)
    m_headers = ["CO", "PO1", "PO2", "PO3", "PO4", "PO5", "PO6", "PO7", "PO8", "PO9", "PO10", "PO11", "PSO1", "PSO2", "PSO3"]
    for i, h in enumerate(m_headers):
        matrix_table.rows[0].cells[i].text = h

    m_data = [
        ["CO1", "2", "2", "2", "-", "1", "-", "-", "1", "2", "-", "-", "1", "1", "1"],
        ["CO2", "2", "2", "2", "-", "1", "1", "-", "1", "2", "-", "-", "1", "1", "1"],
        ["CO3", "2", "2", "3", "2", "2", "-", "-", "1", "2", "1", "1", "2", "2", "2"],
        ["CO4", "2", "3", "3", "2", "2", "-", "-", "1", "2", "1", "1", "2", "2", "2"],
        ["CO5", "2", "2", "3", "2", "3", "1", "1", "1", "2", "2", "1", "2", "2", "2"],
        ["CO6", "2", "2", "3", "2", "3", "1", "1", "1", "2", "2", "2", "3", "2", "2"]
    ]
    for idx, r_vals in enumerate(m_data):
        row = matrix_table.rows[idx+1].cells
        for col_idx, val in enumerate(r_vals):
            row[col_idx].text = val
    set_table_styling(matrix_table, [Inches(0.6)] + [Inches(0.42)]*14)

    add_h2("CO-PO-PSO Mapping Justification")
    add_p(
        "• CO1 maps to PO1-PO3, PO8, PO9, PSO1-PSO3: Applies foundational engineering knowledge, analytical thinking, teamwork, and ethics to understand elderly vulnerabilities through empathy maps.\n"
        "• CO2 maps to PO1-PO5, PO8, PO9, PSO1-PSO3: Requires literature analysis of peer-reviewed papers and benchmark platforms to translate findings into actionable engineering gaps.\n"
        "• CO3 maps to PO1-PO5, PO8-PO11, PSO1-PSO3: Applies creative modeling tools (UML Use Case, Activity, State diagrams) and project timeline management.\n"
        "• CO4 maps to PO1-PO5, PO8-PO11, PSO1-PSO3: Conducts rigorous empirical data analysis on N = 102 respondents to formulate the validated Problem Statement.\n"
        "• CO5 maps to PO1-PO11, PSO1-PSO3: Evaluates software usability against a 35-point heuristic rubric and addresses peer constructive feedback.\n"
        "• CO6 maps to PO1-PO11, PSO1-PSO3: Synthesizes design into a working, deployed, high-impact web application (ConnectSphere) serving real community needs."
    )

    target_files = [
        "ConnectSphere_Final_Submission_Report.docx",
        "Community_Engagement_Project_1_Report.docx"
    ]
    saved = []
    for f in target_files:
        try:
            doc.save(f)
            saved.append(f)
            print(f"Successfully saved: {f} ({os.path.getsize(f):,} bytes)")
        except PermissionError:
            print(f"File currently locked (open in Word): {f}")
    
    if not saved:
        fallback = f"ConnectSphere_Report_{int(time.time())}.docx"
        doc.save(fallback)
        saved.append(fallback)
        print(f"Saved to fallback file: {fallback}")

if __name__ == "__main__":
    create_full_report()
