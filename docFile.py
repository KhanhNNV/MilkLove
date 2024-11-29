#read key and hastag
with open("kw_ht.inp","r") as file:
    key=file.read()
#read content
with open("doc.inp", "r") as file2:
    count=0
    for line in file2:
        content = ""
        count+=1
        content += f"{count}. "+ line.strip() + "\n" + "\n" + key + "\n"
        print(content)

