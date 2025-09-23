from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich import box
from pystyle import *
import requests

def zmhex(hex_color: str) -> str:
    hex_color = hex_color.lstrip("#")
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return f"{r};{g};{b}"


gradient = Colors.DynamicMIX((
    zmhex("#0000FF"),
    zmhex("#0000CD"),
    zmhex("#00F5FF"),
    zmhex("#7FFFD4"),
    zmhex("#54FF9F"),
    zmhex("#00FF7F"),
    zmhex("#00FF00"),
    zmhex("#7CFC00"),
    zmhex("#ADFF2F"),
    zmhex("#32CD32"),
    zmhex("#00FA9A"),
    zmhex("#7FFF00"),
    zmhex("#C0FF3E"),
    zmhex("#FF1493"),
    zmhex("#FF34B3"),
    zmhex("# FF3E96")
))

text = '''
╔════════════════════════════════════════════════════════════════╗
║ ██████╗ ██████╗ ███████╗    ████████╗ ██████╗  ██████╗ ██╗     ║
║██╔═══██╗██╔══██╗██╔════╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ║
║██║   ██║██████╔╝█████╗         ██║   ██║   ██║██║   ██║██║     ║
║██║   ██║██╔══██╗██╔══╝         ██║   ██║   ██║██║   ██║██║     ║
║╚██████╔╝██████╔╝██║            ██║   ╚██████╔╝╚██████╔╝███████╗║
║ ╚═════╝ ╚═════╝ ╚═╝            ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝║
╚════════════════════════════════════════════════════════════════╝

            Cảnh báo không sử dụng để che giấu mã độc
               Nếu cố tình thì tự chịu trách nhiệm 
               
                   ENTER để vào tool
'''

Anime.Fade(Center.Center(text),gradient,Colorate.Vertical,interval=0.05,enter=True)
console = Console()

def zmhec(hex_color: str) -> str:
    hex_color = hex_color.lstrip("#")
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return f"{r};{g};{b}"

def zmh(text: str, *hex_colors: str) -> str:
    rgb_list = [zmhec(c) for c in hex_colors]
    gradient = Colors.DynamicMIX(rgb_list)
    return Colorate.Horizontal(gradient, text, 1)

def zurgb(hex_color: str):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def zuht(content: str, c1: str, c2: str):
    rgb1 = zurgb(c1)
    rgb2 = zurgb(c2)
    length = max(1, len(content))

    text = Text()
    for i, ch in enumerate(content):
        r = int(rgb1[0] + (rgb2[0]-rgb1[0]) * i/length)
        g = int(rgb1[1] + (rgb2[1]-rgb1[1]) * i/length)
        b = int(rgb1[2] + (rgb2[2]-rgb1[2]) * i/length)
        text.append(ch, style=f"rgb({r},{g},{b}) bold")
    return text
    
def textt(content: str, c1: str, c2: str, c3: str):
    rgb1, rgb2, rgb3 = zurgb(c1), zurgb(c2), zurgb(c3)
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
        title=zuht("Chọn chế độ OBF", "#FF1493", "#00FFFF"),
        show_header=True,
        header_style="bold cyan",
        border_style="#FFFFFF"
    )

    table.add_column("STT", justify="center")
    table.add_column("Obfuscate", justify="center")
    table.add_column("Author", justify="center")
    table.add_column("Status", justify="center")
    table.add_column("Note", justify="center")

    table.add_row("[bold yellow]1",zuht("Emoji", "#00FFFF", "#008CF0"),zuht("Zu", "#C0FF3E", "#FFB90F"),zuht("Online ✔", "#7CFC00", "#32CD32"),zuht("Ổn định", "#FFFF00", "#C0FF3E"))
    table.add_row("[bold yellow]2",zuht("Sala", "#FF0000", "#FFA500"),zuht("Shin", "#C0FF3E", "#FFB90F"),zuht("Online ✔", "#7CFC00", "#32CD32"),zuht("Ổn định", "#FFFF00", "#C0FF3E"))
    table.add_row("[bold yellow]3",zuht("Chine", "#8A2BE2", "#00FFFF"),zuht("NTD", "#C0FF3E", "#FFB90F"),zuht("Online ✔", "#7CFC00", "#32CD32"),zuht("Ổn định", "#FFFF00", "#C0FF3E"))
    table.add_row("[bold yellow]4",zuht("Japan", "#00FF00", "#FFFF00"),zuht("NTD", "#C0FF3E", "#FFB90F"),zuht("Online ✔", "#7CFC00", "#32CD32"),zuht("Ổn định", "#FFFF00", "#C0FF3E"))
    table.add_row("[bold yellow]5",zuht("Hangul", "#FF1493", "#FF4500"),zuht("NTD", "#C0FF3E", "#FFB90F"),zuht("Offline ✘", "#FF4040", "#FF0000"),zuht("Đang vá bảo mật", "#FF4040", "#FF0000"))
    table.add_row("[bold yellow]6",zuht("Shadow", "#FF69B4", "#33CCFF"),zuht("WhiteNN", "#C0FF3E", "#FFB90F"),zuht("Online ✔", "#7CFC00", "#32CD32"),zuht("Có thể dùng", "#FFFF00", "#C0FF3E"))
    table.add_row("[bold yellow]7",zuht("Layer", "#00CED1", "#1E90FF"),zuht("JunidoKai", "#C0FF3E", "#FFB90F"),zuht("Online ✔", "#7CFC00", "#32CD32"),zuht("Có thể dùng", "#FFFF00", "#C0FF3E"))

    panel = Panel(
        Align.center(table),
        title=banner,
        border_style="bold #00FFFF",
        padding=(1, 2)
    )

    console.clear()
    console.print(panel)

if __name__ == "__main__":
    menu_banner()

wnn = zmh("┏━━━━≯ Nhập lựa chọn ≮━━━━≯「OBF TOOL」\n┗━⊁﷼: ","#0000FF","#00FFFF","#FFFFFF","#00FFFF","#0000FF")
chon = input(wnn).strip()

if chon == '1':
    exec(requests.get('https://raw.githubusercontent.com/serverbywhite/Server/main/server99.py').text)

if chon == '2':
    exec(requests.get('https://raw.githubusercontent.com/serverbywhite/Server/main/server103.py').text)

if chon == '3':
    exec(requests.get('https://raw.githubusercontent.com/serverbywhite/Server/main/server100.py').text)

if chon == '4':
    exec(requests.get('https://raw.githubusercontent.com/serverbywhite/Server/main/server104.py').text)

if chon == '5':
    exec(requests.get('https://raw.githubusercontent.com/serverbywhite/Server/main/server404.py').text)

if chon == '6':
    exec(requests.get('https://raw.githubusercontent.com/serverbywhite/Server/main/server101.py').text)

if chon == '7':
    exec(requests.get('https://raw.githubusercontent.com/serverbywhite/Server/main/server102.py').text)
