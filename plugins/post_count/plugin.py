import os
import re
import glob
from mkdocs.plugins import BasePlugin


class PostCountPlugin(BasePlugin):
    """
    MkDocs plugin that:
    1. Auto-generates index.md in each database folder at build time
    2. Injects {{ db_counts }} with post counts on the homepage
    """

    def _scan_folders(self, docs_dir):
        """Scan docs_dir for database folders and their .md files."""
        folders = {}
        for entry in sorted(os.listdir(docs_dir)):
            entry_path = os.path.join(docs_dir, entry)
            if not os.path.isdir(entry_path):
                continue
            if entry.startswith(".") or entry == "assets":
                continue
            md_files = glob.glob(os.path.join(entry_path, "*.md"))
            md_files = [f for f in md_files if os.path.basename(f).lower() != "index.md"]
            folders[entry] = sorted(md_files)
        return folders

    def _extract_title(self, filepath):
        """Extract title from front matter or derive from filename."""
        with open(filepath) as f:
            content = f.read()
        m = re.search(r"^title:\s*(.+)$", content, re.MULTILINE)
        if m:
            return m.group(1).strip()
        return os.path.basename(filepath).replace(".md", "").replace("-", " ").title()

    def on_pre_build(self, config, **kwargs):
        """Auto-generate index.md in each database folder."""
        docs_dir = config["docs_dir"]
        folders = self._scan_folders(docs_dir)

        for folder, md_files in folders.items():
            display = folder.replace("-", " ").title()
            lines = [f"---", f"title: {display}", f"---", "", f"# {display}", ""]

            if md_files:
                lines.append(f"**{len(md_files)}** articles available.")
                lines.append("")
                for mf in md_files:
                    basename = os.path.basename(mf)
                    title = self._extract_title(mf)
                    lines.append(f"- [{title}]({basename})")
            else:
                lines.append("No articles yet. Add `.md` files to this folder to get started.")

            lines.append("")
            idx_path = os.path.join(docs_dir, folder, "index.md")
            with open(idx_path, "w") as f:
                f.write("\n".join(lines))

    def on_page_markdown(self, markdown, page, config, files, **kwargs):
        if "{{ db_counts }}" not in markdown:
            return markdown

        docs_dir = config["docs_dir"]
        folders = self._scan_folders(docs_dir)

        lines = []
        lines.append("| Database | Posts |")
        lines.append("|----------|-------|")
        for folder, md_files in folders.items():
            display_name = folder.replace("-", " ").title()
            count = len(md_files)
            link = f"[{display_name}]({folder}/index.md)"
            lines.append(f"| {link} | {count} |")

        return markdown.replace("{{ db_counts }}", "\n".join(lines))
