languages = {
    "en": "English",
    "es": "Español",
    "fr": "Français",
}

test_basic_params = {
    "en": "Open Contracting Data Standard",
    "es": "Estándar de Datos para las Contrataciones Abiertas",
    "fr": "Standard de Données sur la Commande Publique Ouverte",
}

test_search_params = [
    ("en", r"Found \d+ pages matching"),
    ("es", r"encontraron \d+ páginas que coinciden"),
    ("fr", r"\d+ pages correspondant"),  # codespell:ignore
]
