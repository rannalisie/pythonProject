import json

dicionario = {
  "LISA": ["LISA do 27", "27/03/1997", "RECEP_01"],
  "JEN": ["JEN do 16", "16/01/1996", "RAIOX_02"],
  "SOO": ["SOO do 03", "03/01/1995", "RECEP_03"],
  "CHAE": ["CHAE do 11", "11/02/1997", "RAIOX_01"]
}

with open("bd1.json", "w") as json_file:
    json.dump(dicionario,json_file)