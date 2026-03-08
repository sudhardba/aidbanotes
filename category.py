import os

folder = "_oracle"

category_map = {
    "backup": "Backup",
    "restore": "Recovery",
    "flashback": "Recovery",
    "recovery": "Recovery",
    "performance": "Performance",
    "tuning": "Performance",
    "awr": "Performance",
    "monitor": "Monitoring",
    "metrics": "Monitoring",
    "security": "Security",
    "encryption": "Security",
    "cluster": "Architecture",
    "rac": "Architecture",
    "architecture": "Architecture",
    "install": "Setup",
    "setup": "Setup",
    "configuration": "Setup",
    "troubleshoot": "Troubleshooting"
}

def detect_category(title):
    title = title.lower()

    for key in category_map:
        if key in title:
            return category_map[key]

    return "General"


for file in os.listdir(folder):

    if file.endswith(".md"):

        path = os.path.join(folder, file)

        with open(path) as f:
            lines = f.readlines()

        title = ""

        for line in lines:
            if line.startswith("title:"):
                title = line.replace("title:", "").strip()

        category = detect_category(title)

        new_header = [
            "---\n",
            f"title: {title}\n",
            f"parent: {category}\n",
            "nav_order: 1\n",
            "---\n\n"
        ]

        content_start = 0
        for i,line in enumerate(lines):
            if line.strip() == "---":
                content_start = i+1
                break

        content = "".join(lines[content_start:])

        with open(path,"w") as f:
            f.writelines(new_header)
            f.write(content)

        print("Updated:",file)

print("All articles categorized.")
