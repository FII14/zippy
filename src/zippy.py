import zipfile

zip_file_name = input("Enter the zip file name: ")
wordlist_name = "wordlists/rockyou.txt"

with open(zip_file_name, "rb") as zip_file:
    zip_file = zipfile.ZipFile(zip_file_name)

with open(wordlist_name, "r", encoding="utf-8", errors="ignore") as wordlist_file:
    passwords = wordlist_file.readlines()

for password in passwords:
    password = password.strip()
    try:
        zip_file.extractall(pwd=password.encode("utf-8"))
        print(f"Password found: {password}")
        break
    except Exception:
        pass
else:
    print("No matching password found.")
