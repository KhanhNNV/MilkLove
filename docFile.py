with open("kw_ht.inp","r") as file:
    key=file.read()

with open("doc.inp", "r") as file2:
    dem=0
    for line in file2:
        content = ""
        dem+=1
        content += f"{dem}. "+ line.strip() + "\n"+ "\n" + key + "\n"
        print(content)
        content = ""

