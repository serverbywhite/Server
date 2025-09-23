from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich import box
from pystyle import *

def hex_to_rgb_str(hex_color: str) -> str:
    hex_color = hex_color.lstrip("#")
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return f"{r};{g};{b}"


gradient = Colors.DynamicMIX((
    hex_to_rgb_str("#0000FF"),  # cam
    hex_to_rgb_str("#0000CD"),  # hồng
    hex_to_rgb_str("#00F5FF"),   # tím
    hex_to_rgb_str("#7FFFD4"),
    hex_to_rgb_str("#54FF9F"),
    hex_to_rgb_str("#00FF7F"),
    hex_to_rgb_str("#00FF00"),
    hex_to_rgb_str("#7CFC00"),
    hex_to_rgb_str("#ADFF2F"),
    hex_to_rgb_str("#32CD32"),
    hex_to_rgb_str("#00FA9A"),
    hex_to_rgb_str("#7FFF00"),
    hex_to_rgb_str("#C0FF3E"),
    hex_to_rgb_str("#FF1493"),
    hex_to_rgb_str("#FF34B3"),
    hex_to_rgb_str("# FF3E96")
))

text = '''
Cảnh báo không sử dụng để che giấu mã độc
   Nếu cố tình thì tự chịu trách nhiệm 
╔════════════════════════════════════════════════════════════════╗
║ ██████╗ ██████╗ ███████╗    ████████╗ ██████╗  ██████╗ ██╗     ║
║██╔═══██╗██╔══██╗██╔════╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ║
║██║   ██║██████╔╝█████╗         ██║   ██║   ██║██║   ██║██║     ║
║██║   ██║██╔══██╗██╔══╝         ██║   ██║   ██║██║   ██║██║     ║
║╚██████╔╝██████╔╝██║            ██║   ╚██████╔╝╚██████╔╝███████╗║
║ ╚═════╝ ╚═════╝ ╚═╝            ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝║
╚════════════════════════════════════════════════════════════════╝
'''

Anime.Fade(
    Center.Center(text),
    gradient,
    #Colors.DynamicMIX((Colors.blue, Colors.green)),
    Colorate.Vertical,
    interval=0.05,
    enter=True
)

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
    
def textt(content: str, c1: str, c2: str, c3: str):
    rgb1, rgb2, rgb3 = hex_to_rgb(c1), hex_to_rgb(c2), hex_to_rgb(c3)
    length = max(1, len(content))

    text = Text()
    for i, ch in enumerate(content):
        ratio = i / (length - 1) if length > 1 else 0
        if ratio < 0.5:
            r = int(rgb1[0] + (rgb2[0] - rgb1[0]) * (ratio / 0.5))
            g = int(rgb1[1] + (rgb2[1] - rgb1[1]) * (ratio / 0.5))
            b = int(rgb1[2] + (rgb2[2] - rgb1[2]) * (ratio / 0.5))
        else:
            r = int(rgb2[0] + (rgb3[0] - rgb2[0]) * ((ratio - 0.5) / 0.5))
            g = int(rgb2[1] + (rgb3[1] - rgb2[1]) * ((ratio - 0.5) / 0.5))
            b = int(rgb2[2] + (rgb3[2] - rgb2[2]) * ((ratio - 0.5) / 0.5))
        text.append(ch, style=f"rgb({r},{g},{b}) bold")
    return text

def menu_banner():
    banner = textt("MinhAnhs ᕁ JunidoKai ᕁ WhiteNN ᕁ Zu", "#0000FF", "#00FFFF", "#00FF00")

    table = Table(
        box=box.HEAVY,
        title=gradient_text("Chọn chế độ OBF", "#FF1493", "#00FFFF"),
        show_header=True,
        header_style="bold cyan",
        border_style="#FFFFFF"
    )

    table.add_column("STT", justify="center")
    table.add_column("Obfuscate", justify="center")
    table.add_column("Author", justify="center")
    table.add_column("Status", justify="center")
    table.add_column("Note", justify="center")

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
        gradient_text("Shin", "#C0FF3E", "#FFB90F"),
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
        gradient_text("Shadow", "#FF69B4", "#33CCFF"),
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
        border_style="#00FFFF",
        padding=(1, 2)
    )

    console.clear()
    console.print(panel)

if __name__ == "__main__":
    menu_banner()

chon = input(f"Nhập lựa chọn : ").strip()

if chon == '1':
    exec(requests.get('https://raw.githubusercontent.com/serverbywhite/Server/main/server99.py').text)

if chon == '2':
    exec(requests.get('https://raw.githubusercontent.com/serverbywhite/Server/main/server100.py').text)

if chon == '3':
    exec(requests.get('https://raw.githubusercontent.com/serverbywhite/Server/main/server101.py').text)

if chon == '4':
    exec(requests.get('https://raw.githubusercontent.com/serverbywhite/Server/main/server102.py').text)

if chon == '5':
    exec(requests.get('https://raw.githubusercontent.com/serverbywhite/Server/main/server404.py').text)

if chon == '6':
    exec(requests.get('https://raw.githubusercontent.com/serverbywhite/Server/main/server404.py').text)

if chon == '7':
    exec(requests.get('https://raw.githubusercontent.com/serverbywhite/Server/main/server404.py').text)
