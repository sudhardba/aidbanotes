import os
import re

INPUT_FILE = "titles.txt"

tech_map = {
    "oracle": "_oracle",
    "postgresql": "_postgresql",
    "redis": "_redis",
    "mongodb": "_mongodb",
    "cassandra": "_cassandra"
}

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = text.replace(" ", "-")
    return text

with open(INPUT_FILE) as f:
    titles = f.readlines()

for title in titles:

    title = title.strip()
    if not title:
        continue

    slug = slugify(title)

    folder = "_others"

    for tech in tech_map:
        if tech in title.lower():
            folder = tech_map[tech]
            break

    os.makedirs(folder, exist_ok=True)

    filename = f"{folder}/{slug}.md"

    permalink_folder = folder.replace("_","")

    content = f"""---
title: {title}
layout: default
permalink: /{permalink_folder}/{slug}/
---

# {title}

Content coming soon.

## Overview

## Commands

## Troubleshooting

## Notes
"""

    with open(filename, "w") as f:
        f.write(content)

    print("Created:", filename)

print("All posts generated successfully.")
