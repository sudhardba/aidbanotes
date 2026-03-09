---
title: Oracle
nav_order: 1
---

# Oracle Articles

{% assign ops = site.oracle | where_exp: "item", "item.parent == 'Operations'" %}
## Operations ({{ ops | size }})
{% for doc in ops %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign backup = site.oracle | where_exp: "item", "item.parent == 'Backup'" %}
## Backup ({{ backup | size }})
{% for doc in backup %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign recovery = site.oracle | where_exp: "item", "item.parent == 'Recovery'" %}
## Recovery ({{ recovery | size }})
{% for doc in recovery %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign perf = site.oracle | where_exp: "item", "item.parent == 'Performance'" %}
## Performance ({{ perf | size }})
{% for doc in perf %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign setup = site.oracle | where_exp: "item", "item.parent == 'Setup'" %}
## Setup ({{ setup | size }})
{% for doc in setup %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign ts = site.oracle | where_exp: "item", "item.parent == 'Troubleshooting'" %}
## Troubleshooting ({{ ts | size }})
{% for doc in ts %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign arch = site.oracle | where_exp: "item", "item.parent == 'Architecture'" %}
## Architecture ({{ arch | size }})
{% for doc in arch %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}
