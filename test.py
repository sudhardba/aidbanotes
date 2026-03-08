import os
import re

INPUT_FILE = "titles.txt"

tech_map = {
    "Oracle": "_oracle",
    "PostgreSQL": "_postgresql",
    "Redis": "_redis",
    "MongoDB": "_mongodb",
    "Cassandra": "_cassandra"
}

# create only first 10 per tech
limit_per_tech = 10
count = {k: 0 for k in tech_map}

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

    for tech in tech_map:
        if tech.lower() in title.lower():

            if count[tech] >= limit_per_tech:
                break

            folder = tech_map[tech]
            os.makedirs(folder, exist_ok=True)

            slug = slugify(title)
            filename = f"{folder}/{slug}.md"

            content = f"""---
title: {title}
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

            count[tech] += 1
            break

print("All posts generated successfully.")
