import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
from datetime import datetime
import json
from PIL import Image, ImageTk

def load_module_commands():
    with open('modules.json') as file:
        return json.load(file)

module_commands = load_module_commands()

def generate_odd_content(selected_modules, date):
    odd_content = ""
    for module_name in selected_modules:
        module_info = module_commands.get(module_name, {})
        formatted_commands = {key: command.format(date=date) for key, command in module_info.items() if key != 'comment'}
        comment_template = module_info.get("comment", "No comment provided")
        comment = comment_template.format(**formatted_commands)
        odd_content += f"Modül: {module_name}\n{comment}\n\n"
    return odd_content

def generate_odd_file():
    environment = env_var.get()
    raw_date = date_entry.get()
    link = link_entry.get()
    selected_modules = [module for module, var in modules_vars.items() if var.get()]


    try:
        input_date = datetime.strptime(raw_date, '%d-%m-%Y')
        formatted_date = input_date.strftime('%d%m%Y')
    except ValueError:
        messagebox.showerror("Tarih Formatı Hatalı", "Lütfen tarihi 'gg-aa-yyyy' formatında girin.")
        return

    odd_content = f"Ortam: {environment}\nTarih: {raw_date}\nLink: {link}\n\n"
    odd_content += generate_odd_content(selected_modules, formatted_date)

    filename = f"ODD_{formatted_date}.txt"
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Documents", "*.txt")],
        initialdir="./",
        initialfile=filename,
        title="Operasyonel Kabul Dokümanı Kaydet"
    )

    if filepath:
        with open(filepath, 'w') as file:
            file.write(odd_content)
        messagebox.showinfo("Başarılı", f"ODD kaydedildi: {filepath}")

ctk.set_appearance_mode("Light")  # "Light" da kullanılabilir

# Arayüz elemanları
root = ctk.CTk()  # customtkinter kullanımı
root.title("ODD Otomatizasyon Arayüzü")

# Pencere boyutlarını belirle ve ekranın ortasına yerleştir
root_width = 800
root_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (root_width / 2))
y_coordinate = int((screen_height / 2) - (root_height / 2))
root.geometry(f"{root_width}x{root_height}+{x_coordinate}+{y_coordinate}")

# Arka plan resmini yükle ve yerleştir
background_image = Image.open('images.png')  # Resmin yolu
background_photo = ImageTk.PhotoImage(background_image.resize((root_width, root_height)))
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Tarih ve link girişi, beyaz arka plan ile
date_entry = ctk.CTkEntry(root, placeholder_text="GG-AA-YYYY", width=250, fg_color="white",border_color='black')
date_entry.pack(pady=30, padx=10, anchor='center')

link_entry = ctk.CTkEntry(root, placeholder_text="Linki buraya giriniz", width=250, fg_color="white",border_color='black')
link_entry.pack(pady=30, padx=10, anchor='center')

# Ortam seçimi için radio butonları, beyaz arka plan ile
env_var = tk.StringVar(value='TEST')
radio_frame = ctk.CTkFrame(root, fg_color="white")
radio_frame.pack(pady=20, anchor='center')
ctk.CTkRadioButton(radio_frame, text='TEST', variable=env_var, value='TEST', fg_color="blue").pack(side=tk.LEFT, padx=15)
ctk.CTkRadioButton(radio_frame, text='PROD', variable=env_var, value='PROD', fg_color="blue").pack(side=tk.RIGHT, padx=15)

# Modüller için onay kutuları, beyaz arka plan ile
modules_frame = ctk.CTkFrame(root, fg_color="white", border_width=2, border_color='black', width=200, height=300)
modules_frame.pack(pady=20, padx=20)

modules = ["HOOK", "GUI-PANEL", "UNICA-INTEGRATOR", "APP", "NTM", "WEBSDK2"]
modules_vars = {}
for module in modules:
    var = tk.BooleanVar()
    modules_vars[module] = var
    checkbox = ctk.CTkCheckBox(modules_frame, text=module, variable=var, fg_color="blue")
    checkbox.pack(side='top', pady=2, padx=10, anchor='w')


# ODD oluştur butonu, beyaz arka plan ile
generate_odd_button = ctk.CTkButton(root, text="ODD Oluştur", command=generate_odd_file, fg_color="blue")
generate_odd_button.pack(pady=15, anchor='center')

root.mainloop()