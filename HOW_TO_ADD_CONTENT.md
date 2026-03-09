# How To Add Content

This guide explains how to:

- Add a new post to an existing technology (Oracle, Cassandra, etc.)
- Add a new section/category inside an existing technology
- Add a brand-new technology (for example: Yugabyte, Neo4j)

## 1. Add A New Post (Existing Technology)

Example target technologies:

- `_oracle/`
- `_cassandra/`
- `_postgresql/`
- `_mongodb/`
- `_redis/`
- `_others/`

### Step-by-step

1. Create a markdown file in the correct collection folder.
2. Use a kebab-case file name.
3. Add front matter using the template below.
4. Write the runbook content.
5. Commit and push.

### Post front matter template

```yaml
---
title: <Readable Title>
parent: <Section Name>
layout: default
category: <Section Name>
permalink: /<technology>/<slug>/
---
```

Example for Oracle:

```yaml
---
title: Oracle Undo Monitoring Guide
parent: Operations
layout: default
category: Operations
permalink: /oracle/oracle-undo-monitoring-guide/
---
```

### Recommended section names (`parent`)

- `Operations`
- `Backup`
- `Recovery`
- `Performance`
- `Setup`
- `Troubleshooting`
- `Architecture`
- `Monitoring`
- `Security`
- `Replication`

Use the section names already present on that technology landing page.

## 2. Add A New Section Inside Existing Technology

If you want a new section like `Compliance` under Oracle:

1. Set post front matter to `parent: Compliance` and `category: Compliance`.
2. Update the landing page (for example `oracle.md`) to include a block for that section.

Landing-page section block template:

```liquid
{% assign compliance = site.oracle | where_exp: "item", "item.parent == 'Compliance'" %}
## Compliance ({{ compliance | size }})
{% for doc in compliance %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}
```

Without this step, posts still exist but may not show under a visible section heading.

## 3. Add A Brand-New Technology (Yugabyte, Neo4j, etc.)

Example below uses `yugabyte`.

### Step 1: Create collection folder

Create folder:

```text
_yugabyte/
```

### Step 2: Register collection in `_config.yml`

```yaml
collections:
  yugabyte:
    output: true
```

### Step 3: Create landing page `yugabyte.md`

Template:

```yaml
---
title: Yugabyte
nav_order: 7
---
```

```markdown
# Yugabyte Articles

{% assign ops = site.yugabyte | where_exp: "item", "item.parent == 'Operations'" %}
## Operations ({{ ops | size }})
{% for doc in ops %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign backup = site.yugabyte | where_exp: "item", "item.parent == 'Backup'" %}
## Backup ({{ backup | size }})
{% for doc in backup %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}
```

Add more section blocks as needed.

### Step 4: Add to sidebar `_navigation.yml`

```yaml
  - title: Yugabyte
    url: /yugabyte
```

### Step 5: Create first post in `_yugabyte/`

```yaml
---
title: Yugabyte Backup Strategy
parent: Backup
layout: default
category: Backup
permalink: /yugabyte/yugabyte-backup-strategy/
---
```

## 4. URL and Naming Rules

- Folder name and collection key should match: `_yugabyte` -> `site.yugabyte`
- Permalink should start with technology name: `/yugabyte/.../`
- Keep file names lowercase and kebab-case

## 5. Quick Validation Checklist

Before push, verify:

1. Front matter exists and uses `---` correctly.
2. `parent` value exactly matches a section heading on landing page.
3. New technology is registered in `_config.yml`.
4. New technology is added in `_navigation.yml`.
5. Landing page uses correct collection handle (`site.<technology>`).

## 6. Common Mistakes

- New folder created but collection missing in `_config.yml`
- Typo in collection handle (`site.yugabtye` instead of `site.yugabyte`)
- `parent` value mismatch (for example `Operation` vs `Operations`)
- Permalink not aligned with technology path

Following this guide ensures your new posts and technologies automatically map into the site navigation and section pages.