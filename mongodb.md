---
title: MongoDB
nav_order: 3
---

# MongoDB Articles

{% assign ops = site.mongodb | where_exp: "item", "item.parent == 'Operations'" %}
## Operations ({{ ops | size }})
{% for doc in ops %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign backup = site.mongodb | where_exp: "item", "item.parent == 'Backup'" %}
## Backup ({{ backup | size }})
{% for doc in backup %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign repl = site.mongodb | where_exp: "item", "item.parent == 'Replication'" %}
## Replication ({{ repl | size }})
{% for doc in repl %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign mon = site.mongodb | where_exp: "item", "item.parent == 'Monitoring'" %}
## Monitoring ({{ mon | size }})
{% for doc in mon %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign perf = site.mongodb | where_exp: "item", "item.parent == 'Performance'" %}
## Performance ({{ perf | size }})
{% for doc in perf %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign setup = site.mongodb | where_exp: "item", "item.parent == 'Setup'" %}
## Setup ({{ setup | size }})
{% for doc in setup %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign sec = site.mongodb | where_exp: "item", "item.parent == 'Security'" %}
## Security ({{ sec | size }})
{% for doc in sec %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign arch = site.mongodb | where_exp: "item", "item.parent == 'Architecture'" %}
## Architecture ({{ arch | size }})
{% for doc in arch %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign rec = site.mongodb | where_exp: "item", "item.parent == 'Recovery'" %}
## Recovery ({{ rec | size }})
{% for doc in rec %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}
