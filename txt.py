from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich import box

console = Console()

def hex_to_rgb(hex_color: str):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def gradient_text(content: str, c1: str, c2: str):
    """Tạo text gradient (tương thích rich cũ)"""
    rgb1 = hex_to_rgb(c1)
    rgb2 = hex_to_rgb(c2)
    length = max(1, len(content))

    text = Text()
    for i, ch in enumerate(content):
        r = int(rgb1[0] + (rgb2[0]-rgb1[0]) * i/length)
        g = int(rgb1[1] + (rgb2[1]-rgb1[1]) * i/length)
        b = int(rgb1[2] + (rgb2[2]-rgb1[2]) * i/length)
        text.append(ch, style=f"rgb({r},{g},{b}) bold")
    return text

def menu_banner():
    banner = gradient_text("=== Runtime Sans Error Menu ===", "#0000FF", "#00FF00")

    table = Table(
        box=box.HEAVY,
        title=gradient_text("Chọn chế độ OBF", "#FFA500", "#00FF00"),
        show_header=True,
        header_style="bold cyan",
        border_style="#C0FF3E",
        row_styles=["none", "dim"]
    )

    table.add_column("STT", justify="center")
    table.add_column("Obfuscate", justify="center")
    table.add_column("Author", justify="center")
    table.add_column("Status", justify="center")
    table.add_column("Note", justify="center")

    table.add_row("[bold yellow]1", gradient_text("Emoji", "#00FFFF", "#008CF0"), gradient_text("Zu", "#C0FF3E", "#FFB90F"), gradient_text("Online ✔", "#00FA9A", "#32CD32"), "Ổn định")
    table.add_row("2", gradient_text("Chine", "#FF0000", "#FFA500"), "NTD", "Online✔", "Có thể dùng")
    table.add_row("3", gradient_text("Shadow", "#8A2BE2", "#00FFFF"), "WhiteNN", "Online✔", "Ổn định")
    table.add_row("4", gradient_text("Layer", "#00FF00", "#FFFF00"), "JunidoKai", "Online✔", "Ổn định")
    table.add_row("5", gradient_text("Japan", "#FF1493", "#FF4500"), "NTD", "Offline✘", "Đang bảo trì")
    table.add_row("6", gradient_text("Hangul", "#FF69B4", "# 7CFC00"), "NTD", "Offline✘", "Đang bảo trì")
    table.add_row("7", gradient_text("Sala", "#00CED1", "#1E90FF"), "NTD", "Offline✘", "Đang bảo trì")

    panel = Panel(
        Align.center(table),
        title=banner,
        border_style="#ADFF2F",
        padding=(1, 2)
    )

    console.clear()
    console.print(panel)

if __name__ == "__main__":
    menu_banner()
    choice = console.input("\n[bold yellow]Nhập số để chọn chế độ: [/]")
    console.print(f"\nBạn đã chọn: [bold green]{choice}[/] ✅")