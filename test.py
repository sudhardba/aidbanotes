import os
import re

# input file with titles
INPUT_FILE = "titles.txt"

# mapping folders
folders = {
    "Oracle": "oracle",
    "PostgreSQL": "postgresql",
    "Redis": "redis",
    "MongoDB": "mongodb",
    "Cassandra": "cassandra"
}

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = text.replace(" ", "-")
    return text

with open(INPUT_FILE) as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    if not line:
        continue

    for tech in folders:
        if tech.lower() in line.lower():
            folder = folders[tech]
            break
    else:
        continue

    filename = slugify(line) + ".md"
    path = os.path.join(folder, filename)

    os.makedirs(folder, exist_ok=True)

    with open(path, "w") as f:
        f.write(f"# {line}\n\nContent coming soon.\n")

print("Posts generated successfully")
