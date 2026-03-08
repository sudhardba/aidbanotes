import os

BASE_DIR = "docs"

folders = {
    "oracle": "oracle",
    "postgresql": "postgresql",
    "redis": "redis",
    "mongodb": "mongodb",
    "cassandra": "cassandra",
    "database": "database"
}

# create main folders
for f in folders.values():
    os.makedirs(os.path.join(BASE_DIR, f), exist_ok=True)


def detect_folder(title):

    t = title.lower()

    if "oracle" in t:
        return "oracle"

    if "postgres" in t:
        return "postgresql"

    if "redis" in t:
        return "redis"

    if "mongodb" in t:
        return "mongodb"

    if "cassandra" in t:
        return "cassandra"

    return "database"


with open("titles.txt") as f:
    titles = f.readlines()


for i, title in enumerate(titles):

    title = title.strip()

    if not title:
        continue

    folder = detect_folder(title)

    id_part = title.split(" ")[0]

    filename = id_part + ".md"

    filepath = os.path.join(BASE_DIR, folder, filename)

    content = f"""---
title: {title}
nav_order: {i+1}
---

# {title}

Status: Draft

---

## Overview

Content coming soon.

---

## Commands

---

## Troubleshooting

---

## Notes

"""

    with open(filepath, "w") as f:
        f.write(content)

print("All articles generated.")
