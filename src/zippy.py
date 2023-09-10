import zipfile
from tqdm import tqdm
import os

file_zip = input("Masukkan nama file zip $ ")
file_wordlist = "wordlist/rockyou txt"

with open(file_zip, "rb") as fz:
    fz = zipfile.ZipFile(file_zip)

with open(file_wordlist, "r", encoding="latin-1", errors="ignore") as fw:
    daftar_kata_sandi = fw.readlines()

for kata_sandi in tqdm(daftar_kata_sandi, desc="Progress", ncols=100, ascii=True):
    kata_sandi = kata_sandi.strip()
    try:
        zip_file.extractall(pwd=kata_sandi.encode("latin-1"))
        print(f"[+] Kata Sandi ditemukan: {kata_sandi}")
        break
    except Exception:
        pass
else:
    print("Kata sandi tidak ditemukan di dalam file wordlist.")
