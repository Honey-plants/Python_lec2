import json
import pandas as pd

obj = """
{"name":"Wes",
 "place_lived":["United States", "Spain", "Germany"],
 "siblings":[{"name":"scott", "age":25, "pet":"zuko"},
             {"name":"kim", "age":30, "pet":"kitty"}]
}
"""

data = json.loads(obj)
print(data)
print(type(data))
print()
print(data['siblings'])
print()
frame = pd.DataFrame(data['siblings'])
print(frame)