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
    banner = gradient_text("=== Runtime Sans Error Menu ===", "#0000FF", "#00FFFF")

    table = Table(
        box=box.HEAVY,
        title=gradient_text("Chọn chế độ OBF", "#FF1493", "#00FFFF"),
        show_header=True,
        header_style="bold cyan",
        border_style="#C0FF3E"
    )

    table.add_column("STT", justify="center")
    table.add_column("Obfuscate", justify="center")
    table.add_column("Author", justify="center")
    table.add_column("Status", justify="center")
    table.add_column("Note", justify="center")

    # ✅ mỗi hàng chỉ có 5 cột
    table.add_row(
        "[bold yellow]1",
        gradient_text("Emoji", "#00FFFF", "#008CF0"),
        gradient_text("Zu", "#C0FF3E", "#FFB90F"),
        gradient_text("Online ✔", "#7CFC00", "#32CD32"),
        gradient_text("Ổn định", "#FFFF00", "#C0FF3E")
    )
    table.add_row(
        "[bold yellow]2",
        gradient_text("Sala", "#FF0000", "#FFA500"),
        gradient_text("NTD", "#C0FF3E", "#FFB90F"),
        gradient_text("Online ✔", "#7CFC00", "#32CD32"),
        gradient_text("Có thể dùng", "#FFFF00", "#C0FF3E")
    )
    table.add_row(
        "[bold yellow]3",
        gradient_text("Chine", "#8A2BE2", "#00FFFF"),
        gradient_text("NTD", "#C0FF3E", "#FFB90F"),
        gradient_text("Online ✔", "#7CFC00", "#32CD32"),
        gradient_text("Ổn định", "#FFFF00", "#C0FF3E")
    )
    table.add_row(
        "[bold yellow]4",
        gradient_text("Japan", "#00FF00", "#FFFF00"),
        gradient_text("NTD", "#C0FF3E", "#FFB90F"),
        gradient_text("Online ✔", "#7CFC00", "#32CD32"),
        gradient_text("Ổn định", "#FFFF00", "#C0FF3E")
    )
    table.add_row(
        "[bold yellow]5",
        gradient_text("Hangul", "#FF1493", "#FF4500"),
        gradient_text("NTD", "#C0FF3E", "#FFB90F"),
        gradient_text("Offline ✘", "#FF4040", "#FF0000"),
        gradient_text("Đang bảo trì", "#FF4040", "#FF0000")
    )
    table.add_row(
        "[bold yellow]6",
        gradient_text("Shadow", "#FF69B4", "33CCFF"),  # bỏ dấu cách thừa
        gradient_text("WhiteNN", "#C0FF3E", "#FFB90F"),
        gradient_text("Offline ✘", "#FF4040", "#FF0000"),
        gradient_text("Đang bảo trì", "#FF4040", "#FF0000")
    )
    table.add_row(
        "[bold yellow]7",
        gradient_text("Layer", "#00CED1", "#1E90FF"),
        gradient_text("JunidoKai", "#C0FF3E", "#FFB90F"),
        gradient_text("Offline ✘", "#FF4040", "#FF0000"),
        gradient_text("Đang bảo trì", "#FF4040", "#FF0000")
    )

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