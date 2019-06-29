from collections import OrderedDict

languages = {
    'en': 'English',
    'es': 'Español',
    'fr': 'Français',
}

test_basic_params = OrderedDict([
    ('en', 'Open Contracting Data Standard'),
    ('es', 'Estándar de Datos de Contrataciones Abiertas'),
    ('fr', 'Standard de Données sur la Commande Publique Ouverte'),
])

test_search_params = [
    ('en', r'found \d+ page\(s\) matching'),
    ('es', r'encontró \d+ página\(s\) acorde'),
    ('fr', r'\d+ page\(s\) trouvée\(s\) qui corresponde\(nt\)'),
]
