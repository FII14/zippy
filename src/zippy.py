import zipfile
from tqdm import tqdm

zip_file = input("Enter the ZIP file name: ")
wordlist_file = input("Enter the wordlist file name: ")

with open(wordlist_file, 'r', encoding="utf-8", errors="ignore") as wordlist:
    password_list = wordlist.readlines()

with tqdm(total=len(password_list)) as pbar:
    for line in password_list:
        password = line.strip()
        try:
            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                zip_ref.extractall(pwd=password.encode())
            print(f"Password found: {password}")
            break
        except Exception as e:
            pbar.update(1)
    else:
        print("No matching password found in the wordlist.")
