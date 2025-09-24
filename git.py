#==≠==≠==≠==≠==≠====≠==≠==≠==≠==≠==≠==#
#Copyright by JunidoKai
#Version : 24.0202.0706.11
#Python 3.12 
#09/22/2025 00:20:27 GMT+07:00
#Nếu decode vui lòng để lại comment này
#==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==#
#==≠==Thư Viện==≠==#
import requests, base64, os, sys, socket
from time import sleep
#==≠==≠=Màu=≠==≠==#
xam = "\033[1;38;5;8m"
xla = "\033[1;38;5;10m"
vang = "\033[1;38;5;11m"
xduong = "\033[1;38;5;14m"
trang = "\033[1;38;5;15m"
xdam = "\033[1;38;5;21m"
xlv1 = "\033[1;38;5;42m"
xv1 = "\033[1;38;5;44m"
xlv2 = "\033[1;38;5;49m"
dv1 = "\033[1;38;5;50m"
la = "\033[1;38;5;79m"
vchuoi = "\033[1;38;5;154m"
do = "\033[1;38;5;196m"
mv1 = "\033[1;38;5;199m"
tim = "\033[1;38;5;201m"
cam = "\033[1;38;5;202m"
hdam = "\033[1;38;5;204m"
hong = "\033[1;38;5;211m"
vlightc = "\033[1;38;5;214m"
clightv = "\033[1;38;5;220m"
#==≠==≠=Thông Báo=≠==≠==#
done = xla + "[" + xlv2 + "✔" + xla +"]"
kt = xla + "[⊀" + trang + "/" + xla + "⊁]"  + trang + "=" + xv1 + ">"
error = vlightc + "[" + clightv + "!" + vlightc + "]"
#==≠==≠=Admin=≠==≠==#
wnn = xdam+"W"+xla+"h"+vang+"i"+do+"t"+cam+"e"+vchuoi+" NN"+xam
ma = hdam+"M"+hong+"i"+hdam+"n"+hong+"h"+hdam+"A"+hong+"n"+hdam+"h"+hong+"s🐰"+xam
jndk = xdam+"J"+xv1+"u"+xduong+"n"+xlv2+"i"+xlv1+"d"+xla+"o" +clightv+" K"+vlightc+ "a"+cam+"i"+xam
ht = wnn+trang+" & "+ma+trang+" & "+ jndk
#==≠==≠=IP=≠==≠==#
def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url)
#==≠==Banner==≠==#
def minhanhs():
 os.system("cls" if os.name == "nt" else "clear")
 macuti = f"""               {ht}\n
⠀⠀⠀⠀⠀⣠⣶⣦⠀⠀⠀⣀⣤⣴⣶⣶ ⠀⠀⠀⠀⣀⣴⣦⠀     {dv1}Copyright{trang} : {ma}
⠀⠀⠀ ⣾⣿⣿⣿⣠⣴⣿⣿⣿⣿⣿⣿⠀⣀⣤⣶⣿⣿⣿⡟⠀     {dv1}Admin{trang}     : {wnn}
⣀⣀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀     {dv1}Admin{trang}     : {jndk}
⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣤⣤⣤
⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿     {xla}Name Tool{trang} :{xam}
⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁        {xlv2}         Banner{xam}
⠀⠀⣿⣿⡟⠀⠀⠀⠀{xla} ⡴⠖⠦{xam}⠼⢿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀
⠀⠀⣿⣿⠀⠀⠀⠀⠀{xla}⣼⣇⣋⡗{xam}⠀⠀⢿⣿⢻⣿⡟⢿⣿⣿⣷⠀     {dv1}Github   {trang} : {do}@404ERROR{xam}
⠀⣀⣿⣿⣤⣤⣤⣤⣤⣬⣭⣥⣤⣤⣤⣤⣤⣼⣿⣇⡀⠙⣿⡿⠀                 {xlv1}@whitenn{xam}
⠀⣿⣿⣿⠛⠻⣿⡟⠛⠛⠛⠛⠛⠛⣿⡿⠛⠻⣿⣿⡇⠀⠀⠀⠀                 {xlv1}@junidokai{xam}
⠀⣿⣿⣿⠀⠀⠀⣠⣾⣿⣿⣿⣿⣦⣀⠀{do}⣿{xam}⠀⣿⣿⡇⠀⠀⠀⠀
⠀⠙⢿⣿⣶⣾⣿⣿⣿⣿⠿⠿⣿⣿⣿⣿⣶⣾⣿⠟⠁⠀⠀⠀⠀     {xduong}IP của bạn : {xlv2}{ip}{xam}
⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣦⣴⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{do}                         Hoàng Xa - Trường Xa{trang} là của {vang}Việt Nam 🇻🇳

"""
 for X in macuti:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00010)
minhanhs()
#==≠==Soucre==≠==#
print(f"{xla}Link lấy Token {trang}: {vang}https://github.com/settings/tokens\n") 
def github_login():
    token = input(f"{xduong}Nhập Token : ").strip()
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json"
    }
    minhanhs()
    user = requests.get("https://api.github.com/user", headers=headers).json()
    print(" ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print(f"  {xduong}{kt}   Tài khoản {trang}╗\n                      ╚≻ {mv1}{user['login']} {done}")
    print(" ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    return headers, user['login']

def choose_or_create_repo(headers, username):
    repos = requests.get(f"https://api.github.com/user/repos", headers=headers).json()
    print(f"\n{kt} Repo hiện có :")
    for idx, repo in enumerate(repos):
        print(f"  {kt}{xla} Repo {idx+1}{trang}: {vang}{repo['name']}")
    choice = input(f"\nNhập số để chọn repo hoặc gõ [n] để tạo repo mới: ").strip()
    os.system('clear')
    minhanhs()

    if choice.lower() == 'n':
        repo_name = input(f"\n{kt} Nhập tên repo mới {trang}:{clightv} ").strip()
        data = {
            "name": repo_name,
            "auto_init": True,
            "private": False
        }
        minhanhs()
        r = requests.post("https://api.github.com/user/repos", headers=headers, json=data)
        if r.status_code == 201:
            print(f"{kt}Repo '{repo_name}' đã được tạo.")
            return repo_name
        else:
            print(f"{error}Không tạo được repo \nKiểm tra lại token hoặc quyền.")
            exit()
    else:
        repo_name = repos[int(choice)-1]['name']
        return repo_name

def create_or_upload_file(headers, username, repo):
    file_choice = input(f"\nChọn [1] Tải file từ máy lên\nChọn [2] Tạo file mới|\nNhập lựa chọn: ").strip()
    if file_choice == '1':
        file_path = input(f"Nhập đường dẫn file: ").strip()
        file_name = os.path.basename(file_path)
        with open(file_path, "rb") as f:
            content = base64.b64encode(f.read()).decode()
    else:
        file_name = input(f"Nhập tên file mới (ví dụ: hello.txt): ").strip()
        text = input(f"Nhập nội dung file: ").strip()
        content = base64.b64encode(text.encode()).decode()

    # Tạo README.md nếu chưa có
    readme_url = f"https://api.github.com/repos/{username}/{repo}/contents/README.md"
    r = requests.get(readme_url, headers=headers)
    if r.status_code == 404:
        print("Tạo README.md...")
        data = {
            "message": "Add README.md",
            "content": base64.b64encode("# README".encode()).decode()
        }
        requests.put(readme_url, headers=headers, json=data)

    # Upload file
    file_url = f"https://api.github.com/repos/{username}/{repo}/contents/{file_name}"
    data = {
        "message": f"Add {file_name}",
        "content": content
    }
    r = requests.put(file_url, headers=headers, json=data)
    if r.status_code in [200, 201]:
        print(f"Đã upload file {file_name} thành công.")
        raw_link = f"https://raw.githubusercontent.com/{username}/{repo}/main/{file_name}"
        print(f"Link raw: {raw_link}")
    else:
        print("Lỗi upload file:", r.json())

def delete_file(headers, username, repo):
    url = f"https://api.github.com/repos/{username}/{repo}/contents/"
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        items = [item for item in r.json() if item['type'] == 'file']
        if not items:
            print("Repo không có file nào để xoá.")
            return

        print("\n📂 Danh sách file:")
        for idx, item in enumerate(items):
            print(f"{idx+1}. {item['name']}")

        choice = input("Nhập số thứ tự file muốn xoá: ").strip()
        try:
            idx = int(choice) - 1
            file_info = items[idx]
            file_name = file_info['name']
            sha = file_info['sha']

            confirm = input(f"Bạn có chắc muốn xoá {file_name}? (y/n): ").strip().lower()
            if confirm == 'y':
                file_url = f"https://api.github.com/repos/{username}/{repo}/contents/{file_name}"
                data = {
                    "message": f"Delete {file_name}",
                    "sha": sha
                }
                r = requests.delete(file_url, headers=headers, json=data)
                if r.status_code == 200:
                    print(f"Đã xoá file {file_name} thành công.")
                else:
                    print("Lỗi khi xoá file:", r.json())
            else:
                print("Đã huỷ xoá file.")
        except (IndexError, ValueError):
            print("Lựa chọn không hợp lệ.")
    else:
        print("Không thể lấy danh sách file:", r.json())

def main():
    headers, username = github_login()
    repo = choose_or_create_repo(headers, username)

    while True:
        print("\n=== MENU ===")
        print("1. Upload/Tạo file mới")
        print("2. Đổi repo")
        print("3. Xoá file")
        print("4. Thoát")

        choice = input("Chọn (1/2/3/4): ").strip()

        if choice == '1':
            create_or_upload_file(headers, username, repo)
        elif choice == '2':
            repo = choose_or_create_repo(headers, username)
        elif choice == '3':
            delete_file(headers, username, repo)
        elif choice == '4':
            print("Tạm biệt")
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()