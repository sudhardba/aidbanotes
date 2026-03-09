---
title: PostgreSQL
nav_order: 2
---

# PostgreSQL Articles

{% assign ops = site.postgresql | where_exp: "item", "item.parent == 'Operations'" %}
## Operations ({{ ops | size }})
{% for doc in ops %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign backup = site.postgresql | where_exp: "item", "item.parent == 'Backup'" %}
## Backup ({{ backup | size }})
{% for doc in backup %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign repl = site.postgresql | where_exp: "item", "item.parent == 'Replication'" %}
## Replication ({{ repl | size }})
{% for doc in repl %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign mon = site.postgresql | where_exp: "item", "item.parent == 'Monitoring'" %}
## Monitoring ({{ mon | size }})
{% for doc in mon %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign perf = site.postgresql | where_exp: "item", "item.parent == 'Performance'" %}
## Performance ({{ perf | size }})
{% for doc in perf %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign setup = site.postgresql | where_exp: "item", "item.parent == 'Setup'" %}
## Setup ({{ setup | size }})
{% for doc in setup %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign ts = site.postgresql | where_exp: "item", "item.parent == 'Troubleshooting'" %}
## Troubleshooting ({{ ts | size }})
{% for doc in ts %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign arch = site.postgresql | where_exp: "item", "item.parent == 'Architecture'" %}
## Architecture ({{ arch | size }})
{% for doc in arch %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign rec = site.postgresql | where_exp: "item", "item.parent == 'Recovery'" %}
## Recovery ({{ rec | size }})
{% for doc in rec %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}
