import json

# 1️⃣ JSON файлын ашу
with open(r"C:\Users\Эльмира\OneDrive\Рабочий стол\lab4\json.py\sample-data.json") as f:
    data = json.load(f)


# 2️⃣ Тақырыпты шығару
print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<8}".format("DN", "Description", "Speed", "MTU"))
print("-" * 50, "-" * 20, "------", "------")

# 3️⃣ Мәліметтерді шығару
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes.get("dn", "")
    descr = attributes.get("descr", "")
    speed = attributes.get("speed", "")
    mtu = attributes.get("mtu", "")
    print("{:<50} {:<20} {:<8} {:<8}".format(dn, descr, speed, mtu))
