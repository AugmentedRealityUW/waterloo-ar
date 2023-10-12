

with open("hemoglobin_model_adjust.pdb", "r") as f:
    x = f.readlines()

newlines = []
for line in x:

    if "HETATM 1069" in line:
        newlines.append("HETATM 1069  O2A HEM A 142       4.033  29.488  60.454  1.00 41.90           O\n")

    elif "HETATM 1066" in line:
        newlines.append("HETATM 1066  O1A HEM A 142       3.894  27.609  61.398  1.00 50.71           O\n")

    elif "HETATM 1064" in line:
        newlines.append("HETATM 1064  CGA HEM A 142       3.820  28.215  60.389  1.00 32.49           C\n")

    else:
        newlines.append(line)

print(newlines)

with open("hemoglobin_fix_CG.pdb", "w") as f:
    f.writelines(newlines)