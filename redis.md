---
title: Redis
nav_order: 4
---

# Redis Articles

{% assign ops = site.redis | where_exp: "item", "item.parent == 'Operations'" %}
## Operations ({{ ops | size }})
{% for doc in ops %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign backup = site.redis | where_exp: "item", "item.parent == 'Backup'" %}
## Backup ({{ backup | size }})
{% for doc in backup %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign repl = site.redis | where_exp: "item", "item.parent == 'Replication'" %}
## Replication ({{ repl | size }})
{% for doc in repl %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign mon = site.redis | where_exp: "item", "item.parent == 'Monitoring'" %}
## Monitoring ({{ mon | size }})
{% for doc in mon %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign setup = site.redis | where_exp: "item", "item.parent == 'Setup'" %}
## Setup ({{ setup | size }})
{% for doc in setup %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign sec = site.redis | where_exp: "item", "item.parent == 'Security'" %}
## Security ({{ sec | size }})
{% for doc in sec %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign ts = site.redis | where_exp: "item", "item.parent == 'Troubleshooting'" %}
## Troubleshooting ({{ ts | size }})
{% for doc in ts %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign arch = site.redis | where_exp: "item", "item.parent == 'Architecture'" %}
## Architecture ({{ arch | size }})
{% for doc in arch %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}
