# -*- coding: utf-8 -*-
"""Genere le PDF de hand-off du projet DC Rodez (rendu markdown-lite -> Platypus)."""
import re
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether)

INK      = colors.HexColor('#1a1a1a')
MUTED    = colors.HexColor('#5f6b7a')
ACCENT   = colors.HexColor('#0b6b5f')
ALERT    = colors.HexColor('#a3341f')
RULE     = colors.HexColor('#d5dbe2')
BAND     = colors.HexColor('#eef3f4')
CALLOUT  = colors.HexColor('#f6f8f9')

ss = getSampleStyleSheet()
S = {}
S['h1'] = ParagraphStyle('h1', parent=ss['Normal'], fontName='Helvetica-Bold', fontSize=19,
                         leading=23, textColor=INK, spaceBefore=0, spaceAfter=2)
S['sub'] = ParagraphStyle('sub', parent=ss['Normal'], fontName='Helvetica', fontSize=9.5,
                          leading=13, textColor=MUTED, spaceAfter=10)
S['h2'] = ParagraphStyle('h2', parent=ss['Normal'], fontName='Helvetica-Bold', fontSize=13,
                         leading=16, textColor=ACCENT, spaceBefore=15, spaceAfter=5)
S['h3'] = ParagraphStyle('h3', parent=ss['Normal'], fontName='Helvetica-Bold', fontSize=10.5,
                         leading=13.5, textColor=INK, spaceBefore=9, spaceAfter=3)
S['p'] = ParagraphStyle('p', parent=ss['Normal'], fontName='Helvetica', fontSize=9.3,
                        leading=13.2, textColor=INK, alignment=TA_JUSTIFY, spaceAfter=5)
S['li'] = ParagraphStyle('li', parent=S['p'], leftIndent=11, bulletIndent=2, spaceAfter=2.5,
                         alignment=0)
S['note'] = ParagraphStyle('note', parent=S['p'], fontSize=9.1, leading=12.8,
                           leftIndent=7, rightIndent=6, alignment=0, spaceAfter=0,
                           spaceBefore=0)
S['cell'] = ParagraphStyle('cell', parent=ss['Normal'], fontName='Helvetica', fontSize=8.3,
                           leading=11, textColor=INK)
S['cellb'] = ParagraphStyle('cellb', parent=S['cell'], fontName='Helvetica-Bold')

def inline(t):
    t = (t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    t = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<i>\1</i>', t)
    t = re.sub(r'`(.+?)`', r'<font name="Courier" size="8.4">\1</font>', t)
    return t

def build_table(rows, width):
    ncol = len(rows[0])
    if ncol == 2:
        w = [width * 0.34, width * 0.66]
    elif ncol == 3:
        w = [width * 0.26, width * 0.37, width * 0.37]
    else:
        w = [width / ncol] * ncol
    header = rows[0]
    has_header = any(c.strip() for c in header)
    data = []
    for i, r in enumerate(rows):
        sty = S['cellb'] if (i == 0 and has_header) else S['cell']
        data.append([Paragraph(inline(c), sty) for c in r])
    t = Table(data, colWidths=w, repeatRows=1 if has_header else 0)
    cmds = [
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LINEBELOW', (0, 0), (-1, -2), 0.4, RULE),
        ('BOX', (0, 0), (-1, -1), 0.6, RULE),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]
    if has_header:
        cmds += [('BACKGROUND', (0, 0), (-1, 0), BAND),
                 ('LINEBELOW', (0, 0), (-1, 0), 0.9, ACCENT)]
    t.setStyle(TableStyle(cmds))
    return t

def callout(lines, width):
    inner = [Paragraph(inline(l), S['note']) for l in lines]
    t = Table([[inner]], colWidths=[width])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), CALLOUT),
        ('LINEBEFORE', (0, 0), (0, -1), 2.2, ACCENT),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 7),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    return t

def render(md, width):
    story, i = [], 0
    lines = md.split('\n')
    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if not s:
            i += 1; continue
        if s == '---':
            story.append(Spacer(1, 4))
            t = Table([['']], colWidths=[width], rowHeights=[0.6])
            t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), RULE)]))
            story.append(t); story.append(Spacer(1, 6)); i += 1; continue
        if s.startswith('### '):
            story.append(Paragraph(inline(s[4:]), S['h3'])); i += 1; continue
        if s.startswith('## '):
            story.append(Paragraph(inline(s[3:]), S['h2'])); i += 1; continue
        if s.startswith('# '):
            story.append(Paragraph(inline(s[2:]), S['h1'])); i += 1; continue
        if s.startswith('@@'):
            story.append(Paragraph(inline(s[2:].strip()), S['sub'])); i += 1; continue
        if s.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                raw = lines[i].strip().strip('|')
                if not re.fullmatch(r'[\s|:-]+', lines[i].strip()):
                    rows.append([c.strip() for c in raw.split('|')])
                i += 1
            story.append(Spacer(1, 3))
            story.append(build_table(rows, width))
            story.append(Spacer(1, 7)); continue
        if s.startswith('> '):
            block = []
            while i < len(lines) and lines[i].strip().startswith('> '):
                block.append(lines[i].strip()[2:]); i += 1
            story.append(Spacer(1, 3))
            story.append(callout(block, width))
            story.append(Spacer(1, 7)); continue
        if s.startswith('- '):
            items = []
            while i < len(lines) and lines[i].strip().startswith('- '):
                items.append(Paragraph(inline(lines[i].strip()[2:]), S['li'], bulletText='•'))
                i += 1
            story.extend(items); story.append(Spacer(1, 4)); continue
        if re.match(r'^\d+\. ', s):
            items = []
            while i < len(lines) and re.match(r'^\d+\. ', lines[i].strip()):
                m = re.match(r'^(\d+)\. (.*)', lines[i].strip())
                items.append(Paragraph(inline(m.group(2)), S['li'], bulletText=m.group(1) + '.'))
                i += 1
            story.extend(items); story.append(Spacer(1, 4)); continue
        para = [s]; i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r'^(#|\||>|- |\d+\. |---|@@)', lines[i].strip()):
            para.append(lines[i].strip()); i += 1
        story.append(Paragraph(inline(' '.join(para)), S['p']))
    return story

def make_pdf(md, path, title):
    doc = BaseDocTemplate(path, pagesize=A4, title=title, author='Charles Delbes',
                          leftMargin=17 * mm, rightMargin=17 * mm,
                          topMargin=16 * mm, bottomMargin=16 * mm)
    fw = doc.width
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='n',
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)

    def deco(canvas, docu):
        canvas.saveState()
        canvas.setFont('Helvetica', 7.4)
        canvas.setFillColor(MUTED)
        canvas.drawString(doc.leftMargin, 10 * mm,
                          'Hand-off - Data center Rodez (ZA Bel-Air, Aveyron) - 27 aout 2026')
        canvas.drawRightString(A4[0] - doc.rightMargin, 10 * mm, 'p. %d' % docu.page)
        canvas.setStrokeColor(RULE); canvas.setLineWidth(0.4)
        canvas.line(doc.leftMargin, 12.5 * mm, A4[0] - doc.rightMargin, 12.5 * mm)
        canvas.restoreState()

    doc.addPageTemplates([PageTemplate(id='all', frames=[frame], onPage=deco)])
    doc.build(render(md, fw))
    return path
