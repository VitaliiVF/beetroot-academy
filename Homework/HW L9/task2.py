from sys import path
from pprint import pprint

pprint(f"Кількість шляхів пошуку модулів: {len(path)}: {path}")

path.append("/Users/vitalijfedun/Desktop/Python beetroot/Homework")

print()

pprint(f"Кількість шляхів пошуку модулів: {len(path)}: {path}")