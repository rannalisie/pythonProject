usuarios = {}
print(usuarios)

usuarios = {
    "lisa": ["lisa do 26", "27/12/2023", "Recep_01"],
    "jennie": ["jennie do 23", "05/01/2024", "Raiox_03"],
    "jisoo": ["jisoo do 14", "15/01/2024", "Triagem_03"],
    "rose": ["rose do 15", "27/01/2024", "Medicac_03"],
}
print(usuarios)

usuarios["taeyeon"] = ["Golden Voice", "22/02/2024", "Raiox_01"]
print(usuarios)

print("####----####")
print(usuarios.get("lisa"))
