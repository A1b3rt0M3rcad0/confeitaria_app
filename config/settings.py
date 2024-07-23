
class Config:
 
    # SQlAlchemy Connection, Apeneas sqlite
    database_path = "database/confeitaria.db"
    database = {
        "url": f"sqlite:///{database_path}",
        "echo": True
    }

    # Logger
    logger = {
        'name': 'app.log' 
    }

    # Colors
    colors = {
        'base': '#FCE4EC',      # Rosa Suave
        'main': '#F48FB1',      # Rosa Médio
        'emphasis': '#C2185B',  # Rosa Escuro
        'hover': '#EC407A'      # Rosa Intenso
    }

    # App Fonts and Font_Sizes
    font = 'Courier'

    font_sizes = {
        'title': 28,         # For main titles and headers
        'subtitle': 22,      # For secondary headers and subtitles
        'body': 16,          # For main text and descriptions
        'button': 14,        # For text inside buttons
        'entry': 14,         # For text in input fields
        'message': 14,       # For warning messages and quick tips
        'footer': 10         # For footers and small details
    }

    # Paddings widgets
    paddings = {
        'title': (30, 20),        # Padding horizontal e vertical para títulos principais (Label)
        'subtitle': (30, 15),     # Padding horizontal e vertical para subtítulos (Label)
        'body': (30, 15),         # Padding horizontal e vertical para texto principal e descrições (Label)
        'button': (15, 10),       # Padding horizontal e vertical para botões (Button)
        'entry': (15, 10),        # Padding horizontal e vertical para campos de entrada (Entry)
        'message': (30, 10),      # Padding horizontal e vertical para mensagens e dicas (Label)
        'footer': (30, 10),       # Padding horizontal e vertical para rodapés (Label)
        'checkbox': (10, 5),      # Padding horizontal e vertical para caixas de seleção (Checkbutton)
        'radiobutton': (10, 5),   # Padding horizontal e vertical para botões de rádio (Radiobutton)
        'listbox': (10, 5),       # Padding horizontal e vertical para caixas de lista (Listbox)
        'scrollbar': (10, 5),     # Padding horizontal e vertical para barras de rolagem (Scrollbar)
        'scale': (10, 5),         # Padding horizontal e vertical para escalas (Scale)
        'menu': (10, 5),          # Padding horizontal e vertical para menus (Menu)
        'canvas': (10, 10),       # Padding horizontal e vertical para canvas (Canvas)
        'text': (10, 10)          # Padding horizontal e vertical para widget de texto (Text)
    }

    # Widgets Sizes
    size_label = (100, 25)
    size_label_unit = (50, 25)
    size_label_text = (300, 25)
    size_entry = (200, 30)
    size_option_menu = (150, 30)
    size_button = (100, 30)
