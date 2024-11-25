with open("doc.inp", "r") as file:
    #read the first 2 lines and store it in 2 variables ht and kw
    kw = file.readline().strip()
    ht = file.readline().strip()

    content = ""
    for line in file:
        content += line.strip() + "\n" + kw + "\n" + ht + "\n"

print(content)