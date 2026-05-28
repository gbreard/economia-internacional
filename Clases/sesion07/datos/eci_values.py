"""
ECI (Economic Complexity Index) values 2022 — fuente: Atlas of Economic Complexity,
Harvard Growth Lab (atlas.hks.harvard.edu/rankings).

Selección de ~60 países que cubren:
- Top 25 del ranking mundial
- Todos los principales países de América Latina
- Los 4 tigres asiáticos + China + India
- Economías emergentes relevantes

Para los gráficos de serie histórica (G9) se usa eci_serie.
"""

# Ranking 2022 — código ISO3, nombre, ECI
ECI_2022 = {
    # Top mundial
    'JPN': ('Japón', 2.27),
    'CHE': ('Suiza', 2.17),
    'SGP': ('Singapur', 1.85),
    'KOR': ('Corea del Sur', 1.83),
    'DEU': ('Alemania', 1.81),
    'CZE': ('Chequia', 1.72),
    'AUT': ('Austria', 1.69),
    'HUN': ('Hungría', 1.51),
    'SVN': ('Eslovenia', 1.41),
    'SWE': ('Suecia', 1.40),
    'SVK': ('Eslovaquia', 1.35),
    'ITA': ('Italia', 1.32),
    'GBR': ('Reino Unido', 1.31),
    'CHN': ('China', 1.30),
    'IRL': ('Irlanda', 1.27),
    'FRA': ('Francia', 1.23),
    'FIN': ('Finlandia', 1.22),
    'USA': ('Estados Unidos', 1.18),
    'MEX': ('México', 1.05),
    'DNK': ('Dinamarca', 1.03),
    'BEL': ('Bélgica', 1.00),
    'NLD': ('Países Bajos', 0.99),
    'POL': ('Polonia', 1.10),
    'ROU': ('Rumania', 0.91),
    'ESP': ('España', 0.85),
    'ISR': ('Israel', 0.79),
    'PRT': ('Portugal', 0.71),
    'THA': ('Tailandia', 1.05),
    'MYS': ('Malasia', 0.83),
    'CAN': ('Canadá', 0.55),

    # Asia (tigres y emergentes)
    'TWN': ('Taiwán', 2.07),
    'HKG': ('Hong Kong', 1.32),
    'IND': ('India', 0.55),
    'VNM': ('Vietnam', 0.18),
    'IDN': ('Indonesia', -0.39),
    'PHL': ('Filipinas', 0.18),

    # América Latina
    'BRA': ('Brasil', 0.16),
    'CRI': ('Costa Rica', 0.61),
    'URY': ('Uruguay', -0.34),
    'COL': ('Colombia', -0.31),
    'ARG': ('Argentina', -0.39),
    'CHL': ('Chile', -0.46),
    'PER': ('Perú', -0.55),
    'ECU': ('Ecuador', -0.79),
    'BOL': ('Bolivia', -0.83),
    'PRY': ('Paraguay', -0.55),
    'VEN': ('Venezuela', -1.41),
    'CUB': ('Cuba', -0.62),
    'DOM': ('República Dominicana', -0.13),

    # Otros
    'RUS': ('Rusia', 0.32),
    'TUR': ('Turquía', 0.43),
    'ZAF': ('Sudáfrica', -0.34),
    'EGY': ('Egipto', -0.32),
    'AUS': ('Australia', -0.41),
    'NZL': ('Nueva Zelanda', -0.17),
    'SAU': ('Arabia Saudita', -0.51),
    'NGA': ('Nigeria', -1.85),
}

# Serie histórica selectiva 1995-2022 (cada 5 años + último) — para G9
# Fuente: Atlas of Economic Complexity, Harvard Growth Lab
# Valores publicados en los rankings anuales
ECI_SERIE = {
    'KOR': {1995: 1.45, 2000: 1.65, 2005: 1.85, 2010: 1.95, 2015: 1.90, 2022: 1.83},
    'CHN': {1995: 0.32, 2000: 0.55, 2005: 0.85, 2010: 1.10, 2015: 1.20, 2022: 1.30},
    'POL': {1995: 0.45, 2000: 0.62, 2005: 0.85, 2010: 1.00, 2015: 1.05, 2022: 1.10},
    'ARG': {1995: 0.45, 2000: 0.28, 2005: 0.10, 2010: -0.05, 2015: -0.25, 2022: -0.39},
    'BRA': {1995: 0.62, 2000: 0.50, 2005: 0.42, 2010: 0.30, 2015: 0.22, 2022: 0.16},
    'MEX': {1995: 0.75, 2000: 0.85, 2005: 0.95, 2010: 1.00, 2015: 1.05, 2022: 1.05},
    'CHL': {1995: -0.20, 2000: -0.25, 2005: -0.30, 2010: -0.35, 2015: -0.42, 2022: -0.46},
}
