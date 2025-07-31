records = [
{'name':"rice","price":120,"category":"grocery"},
{'name':"sugar","price":220,"category":"grocery"},
{'name':"wheat","price":320,"category":"grocery"},
{'name':"cereal","price":420,"category":"grocery"},
]
with open("Records.txt", "w") as f:
    f.write("ID\tNAME\tPRICE\tCATEGORY\n")  
    for i in range(len(records)):
        f.write(f"{i+1}\t{records[i]['name']}\t{records[i]['price']}\t{records[i]['category']}\n")
    f.close()

with open("Records.txt", "r") as f:
  
    print(f.read())
    f.close()


