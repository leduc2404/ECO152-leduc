with open("d:\\KTHP 2026\\ECO152-leduc\\congthuc.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# indices 614 to 879 are lines 615 to 880
new_lines = lines[:614] + lines[880:]

with open("d:\\KTHP 2026\\ECO152-leduc\\congthuc.html", "w", encoding="utf-8") as f:
    f.writelines(new_lines)
