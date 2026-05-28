student = {
    "101": {"name": "rajest", "age": 28, "city": "nagpur"},
    "102": {"name": "utkarsh", "age": 24, "city": "INdore"},
    "103": {"name": "ritesh", "age": 18, "city": "BLR"},
    "104": {"name": "parth", "age": 35, "city": "HYD"},
}

for k, v in student.items():
    print(f"Roll no = {k}, name = {v['name']} , age = {v['age']}, city = {v['city']}")
