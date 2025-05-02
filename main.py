import random as rng
str = ""

for i in range(6):
    str += f"INSERT INTO hidden_layer_1 values({i+1}"
    for j in range(100):
        str += f", {rng.uniform(-1, 1)}"
    str += ");"
    print(str)
    str = ""

str = ""
for i in range(3):
    str += f"INSERT INTO hidden_layer_2 values({i+1}"
    for j in range(6):
        str += f", {rng.uniform(-1, 1)}"
    str += ");"
    print(f"{str}")
    str = ""

str = f"INSERT INTO output_layer values(1, {rng.uniform(-1, 1)}, {rng.uniform(-1, 1)}, {rng.uniform(-1, 1)});"
print(str)