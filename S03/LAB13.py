# Funkcja exec()

files_to_process = [
    r"LAB13_sourcefiles/math_sin_square.py",
    r"LAB13_sourcefiles/math_square_root.py"
    ]

for file in files_to_process:
    with open(file, 'r') as f:
        print(f"File {file}")
        source = f.read()
        exec(source)
