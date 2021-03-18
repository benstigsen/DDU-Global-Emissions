# Convert three letter codes -> two letter codes
# (Denmark) DNK -> DK
import json

codes = None

with open("iso3.json", "r") as file:
  codes = json.load(file)

with open("data.json", "r") as file:
  data = file.read()
  
  for key in codes:
    data = data.replace(f"\"{codes[key]}", f"\"{key}")
  
  data = json.loads(data)
  
  output = ""
  for i in data:
    code = i["Code"]
    value = str(i["Annual CO2 emissions"])
    
    if len(code) == 2 and not "E" in value:
      output += f'{code}: {{emission: {value}}},\n'
  
  with open("test.txt", "w") as out:
    out.write(output)
    
  print(output)

