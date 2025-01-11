import os
import time

# Definisikan warna menggunakan ANSI escape sequences
colors = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
    "\033[97m"   # White
]

# Gambar ASCII tengkorak besar
skull = """
      _______
     /       \\
    |  O   O  |
    |    ^    |
    |   '-'   |
     \\_______/
        | |
       /   \\
      /_____\\
"""

def print_colored_skull():
    # Tampilkan gambar tengkorak dengan warna-warni
    for i, line in enumerate(skull.splitlines()):
        print(f"{colors[i % len(colors)]}{line}")
        time.sleep(0.2)  # Delay sedikit agar efek warna lebih terasa

# Bersihkan layar Termux
os.system("clear")

# Panggil fungsi untuk menampilkan tengkorak berwarna
print_colored_skull()

# Reset warna setelah tampilan selesai
print("\033[0m")