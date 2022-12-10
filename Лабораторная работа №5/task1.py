from pprint import pprint

new_dict = []

for i in range(0,16):
    new_dict.append({'bin': bin(i), 'dec': i, 'oct': oct(i), 'hex': hex(i)})


pprint(new_dict)
