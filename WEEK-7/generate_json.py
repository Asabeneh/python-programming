import json

def generate_json(lst, filename):
    with open(f'./{filename}', 'w', encoding='utf-8') as f:
        json.dump(lst, f, indent=4)