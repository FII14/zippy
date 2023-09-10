import zipfile
from tqdm import tqdm
import os

zip_file_name = input("Enter the ZIP file name: ")

if not os.path.exists(zip_file_name):
    print("ZIP file not found.")
    exit(1)
    
wordlist_name = input("Enter the custom wordlist file name: ")

if not os.path.exists(wordlist_name):
    print("Custom wordlist file not found.")
    exit(1)

try:
    with open(zip_file_name, "rb") as zip_file:
        zip_file = zipfile.ZipFile(zip_file)

    with open(wordlist_name, "r", encoding="utf-8", errors="ignore") as wordlist_file:
        passwords = wordlist_file.readlines()
except Exception as e:
    print("An error occurred while opening files:", e)
    exit(1)

for password in tqdm(passwords, desc="Progress", ncols=100, ascii=True):
    password = password.strip()
    try:
        zip_file.extractall(pwd=password.encode("utf-8"))
        print(f"Password found: {password}")
        break
    except Exception as e:
        pass
else:
    print("No matching password found.")
    
