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

category_map = {
    "backup": "Backup",
    "restore": "Recovery",
    "flashback": "Recovery",
    "replication": "Replication",
    "replica": "Replication",
    "performance": "Performance",
    "tuning": "Performance",
    "monitor": "Monitoring",
    "metrics": "Monitoring",
    "security": "Security",
    "encryption": "Security",
    "cluster": "Architecture",
    "architecture": "Architecture",
    "setup": "Setup",
    "installation": "Setup",
    "troubleshooting": "Troubleshooting"
}

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = text.replace(" ", "-")
    return text

def detect_category(title):
    for key in category_map:
        if key in title.lower():
            return category_map[key]
    return "General"

with open(INPUT_FILE) as f:
    titles = f.readlines()

for title in titles:

    title = title.strip()
    if not title:
        continue

    slug = slugify(title)

    folder = "_others"
    tech_name = "others"

    for tech in tech_map:
        if tech in title.lower():
            folder = tech_map[tech]
            tech_name = tech
            break

    os.makedirs(folder, exist_ok=True)

    category = detect_category(title)

    filename = f"{folder}/{slug}.md"

    content = f"""---
title: {title}
layout: default
category: {category}
permalink: /{tech_name}/{slug}/
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

print("All 500 articles created successfully.")
