"""
Genera Plan_de_clases.pdf desde Clases del programa.docx usando docx2pdf.
Si docx2pdf no está disponible, intenta con LibreOffice.
"""
import sys, io, subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from pathlib import Path

programa_dir = Path(r"C:\Users\gbrea\OneDrive\Documentos\UMET\Economia Intenacional\programa")
docx_path = programa_dir / "Clases del programa.docx"
pdf_path = programa_dir / "Plan_de_clases.pdf"

try:
    from docx2pdf import convert
    convert(str(docx_path), str(pdf_path))
    print(f"✓ PDF generado con docx2pdf: {pdf_path}")
except ImportError:
    print("docx2pdf no disponible, intentando con LibreOffice...")
    try:
        result = subprocess.run([
            "soffice", "--headless", "--convert-to", "pdf",
            "--outdir", str(programa_dir),
            str(docx_path)
        ], capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            # LibreOffice genera el PDF con el nombre del docx
            generated = programa_dir / "Clases del programa.pdf"
            if generated.exists():
                generated.rename(pdf_path)
            print(f"✓ PDF generado con LibreOffice: {pdf_path}")
        else:
            print(f"✗ Error LibreOffice: {result.stderr}")
    except FileNotFoundError:
        print("✗ Ni docx2pdf ni LibreOffice disponibles.")
        print("  Para generar el PDF:")
        print("  - Abrir 'Clases del programa.docx' en Word")
        print("  - Guardar como PDF → 'Plan_de_clases.pdf'")
