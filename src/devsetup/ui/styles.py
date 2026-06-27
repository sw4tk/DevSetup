from rich.theme import Theme
from rich import box

# 5-Tier Semantic Color System
APP_THEME = Theme(
    {
        "success": "bold green",
        "warning": "bold yellow",
        "error": "bold red",
        "info": "bold cyan",
        "secondary": "dim",
        "panel_border": "dim",
        "header": "bold white",
    }
)


class Icons:
    SUCCESS = "[success]✓[/success]"
    WARNING = "[warning]⚠[/warning]"
    ERROR = "[error]✗[/error]"
    INFO = "[info]ℹ[/info]"
    BULLET = "[secondary]•[/secondary]"
    LOCK = "[warning]🔒[/warning]"
    PLUS = "[success]+[/success]"
    MINUS = "[secondary]-[/secondary]"


# Minimalist table style (Whitespace is UI)
# Removes heavy vertical/horizontal grid lines for scannability
MINIMAL_TABLE = box.SIMPLE
