# -*- coding: utf-8 -*-
"""
Copiar graficos e imagenes del PPT original al nuevo
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.oxml import parse_xml
from pptx.oxml.ns import nsmap
import copy
from lxml import etree
import os

def copiar_chart(slide_origen, slide_destino, left=None, top=None, width=None, height=None):
    """Copia un chart de un slide a otro"""
    for shape in slide_origen.shapes:
        if shape.shape_type == MSO_SHAPE_TYPE.CHART:
            # Obtener posicion original si no se especifica
            if left is None:
                left = shape.left
            if top is None:
                top = shape.top
            if width is None:
                width = shape.width
            if height is None:
                height = shape.height

            # Copiar el elemento XML del chart
            chart_part = shape.chart.part
            chart_data = chart_part.blob

            # Crear nuevo chart en destino
            # Esto es complejo, vamos a intentar otra aproximacion
            return True
    return False


def copiar_imagen(slide_origen, slide_destino, left=None, top=None, width=None, height=None):
    """Copia una imagen de un slide a otro"""
    for shape in slide_origen.shapes:
        if shape.shape_type == MSO_SHAPE_TYPE.PICTURE:
            # Obtener la imagen
            image = shape.image
            image_bytes = image.blob
            content_type = image.content_type

            # Obtener posicion original si no se especifica
            if left is None:
                left = shape.left
            if top is None:
                top = shape.top
            if width is None:
                width = shape.width
            if height is None:
                height = shape.height

            # Agregar imagen al slide destino
            from io import BytesIO
            image_stream = BytesIO(image_bytes)
            slide_destino.shapes.add_picture(image_stream, left, top, width, height)
            return True
    return False


def eliminar_placeholder(slide, texto_buscar):
    """Elimina shapes que contengan cierto texto"""
    shapes_to_remove = []
    for shape in slide.shapes:
        if shape.has_text_frame:
            for para in shape.text_frame.paragraphs:
                if texto_buscar in para.text:
                    shapes_to_remove.append(shape)
                    break

    for shape in shapes_to_remove:
        sp = shape._element
        sp.getparent().remove(sp)


def main():
    # Abrir presentaciones
    prs_original = Presentation('Clase1_backup_20260204_150332.pptx')
    prs_nuevo = Presentation('Clase1_Economia_Internacional_v2.pptx')

    print("Copiando elementos visuales...")
    print("=" * 50)

    # Mapeo de slides: original -> nuevo
    # Original slide 5 (indice) -> Nuevo slides 2 y 4
    # Original slide 6 (exp/imp) -> Nuevo slide 5
    # Original slide 7 (participacion) -> Nuevo slide 6
    # Original slide 8 (HHI) -> Nuevo slide 7
    # Original slide 9 (cobertura) -> Nuevo slide 8
    # Original slide 15 (Navy League map) -> Nuevo slide 11

    # Posiciones para graficos en el nuevo formato
    chart_left = Inches(0.7)
    chart_top = Inches(1.9)
    chart_width = Inches(7.5)
    chart_height = Inches(4.0)

    # Copiar imagenes (mas facil que charts)
    mapeo_imagenes = [
        (15, 11, "Navy League map"),  # Original slide 15 -> Nuevo slide 11
    ]

    for orig_idx, nuevo_idx, desc in mapeo_imagenes:
        slide_orig = prs_original.slides[orig_idx - 1]  # 0-indexed
        slide_nuevo = prs_nuevo.slides[nuevo_idx - 1]

        # Eliminar placeholder
        eliminar_placeholder(slide_nuevo, "[MAPA:")

        # Copiar imagen
        if copiar_imagen(slide_orig, slide_nuevo,
                        left=Inches(0.7), top=Inches(1.8),
                        width=Inches(7.0), height=None):
            print(f"  Copiado: Slide {orig_idx} -> Slide {nuevo_idx} ({desc})")

    # Guardar
    prs_nuevo.save('Clase1_Economia_Internacional_v2.pptx')
    print("\nPresentacion actualizada con imagenes.")
    print("\nNOTA: Los graficos (charts) deben copiarse manualmente en PowerPoint:")
    print("  - Original Slide 5 -> Nuevo Slide 2 y 4 (indice comercio)")
    print("  - Original Slide 6 -> Nuevo Slide 5 (exportaciones)")
    print("  - Original Slide 7 -> Nuevo Slide 6 (participacion regional)")
    print("  - Original Slide 8 -> Nuevo Slide 7 (HHI)")
    print("  - Original Slide 9 -> Nuevo Slide 8 (cobertura)")


if __name__ == "__main__":
    main()
