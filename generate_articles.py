import os

BASE_DIR = "articles"
os.makedirs(BASE_DIR, exist_ok=True)

def detect_folder(title):

    t = title.lower()

    if "oracle" in t:
        return "oracle"
    elif "postgres" in t:
        return "postgresql"
    elif "redis" in t:
        return "redis"
    elif "mongodb" in t:
        return "mongodb"
    elif "cassandra" in t:
        return "cassandra"
    else:
        return "others"


with open("titles.txt") as f:
    titles = f.readlines()


for title in titles:

    title = title.strip()

    if not title:
        continue

    folder = detect_folder(title)

    folder_path = os.path.join(BASE_DIR, folder)
    os.makedirs(folder_path, exist_ok=True)

    id_part = title.split(" ")[0]

    filename = id_part + ".md"
    filepath = os.path.join(folder_path, filename)

    content = f"""# {title}

Status: Draft

---

## Overview
Content coming soon.

---

## Steps

1.
2.
3.

---

## Commands

Example command here

---

## Troubleshooting

---

## Notes

"""

    with open(filepath, "w") as f:
        f.write(content)

print("All articles generated successfully.")
