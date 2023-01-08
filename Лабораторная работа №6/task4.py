import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(filename, delimiter = ",", new_line = "\n") -> list[dict]:
    def create_element(list_):
        return {headers[i]: list_[i] for i in range(len(headers))}

    with open(filename, 'r') as f:
        str_file = f.read()
    rows = []
    for j in str_file.split(new_line):
        rows.append(j.split(delimiter))
    headers = rows[0]
    return [create_element(rows[j]) for j in range(1, len(rows))]


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
