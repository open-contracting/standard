languages = {
    'en': 'English',
    'es': 'Español',
    'fr': 'Français',
}

test_basic_params = {
    'en': 'Open Contracting Data Standard',
    'es': 'Estándar de Datos para las Contrataciones Abiertas',
    'fr': 'Standard de Données sur la Commande Publique Ouverte',
}

test_search_params = [
    ('en', r'found \d+ page\(s\) matching'),
    # See https://github.com/sphinx-doc/sphinx/issues/11008
    # ('es', r'encontraron \d+ páginas que coinciden'),
    # ('fr', r'\d+ page\(s\) correspondant'),
]
