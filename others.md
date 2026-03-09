---
title: Others
nav_order: 6
---

# Other Database Articles

{% assign ops = site.others | where_exp: "item", "item.parent == 'Operations'" %}
## Operations ({{ ops | size }})
{% for doc in ops %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign backup = site.others | where_exp: "item", "item.parent == 'Backup'" %}
## Backup ({{ backup | size }})
{% for doc in backup %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign mon = site.others | where_exp: "item", "item.parent == 'Monitoring'" %}
## Monitoring ({{ mon | size }})
{% for doc in mon %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign sec = site.others | where_exp: "item", "item.parent == 'Security'" %}
## Security ({{ sec | size }})
{% for doc in sec %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign ts = site.others | where_exp: "item", "item.parent == 'Troubleshooting'" %}
## Troubleshooting ({{ ts | size }})
{% for doc in ts %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign arch = site.others | where_exp: "item", "item.parent == 'Architecture'" %}
## Architecture ({{ arch | size }})
{% for doc in arch %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign perf = site.others | where_exp: "item", "item.parent == 'Performance'" %}
## Performance ({{ perf | size }})
{% for doc in perf %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}

{% assign rec = site.others | where_exp: "item", "item.parent == 'Recovery'" %}
## Recovery ({{ rec | size }})
{% for doc in rec %}
- [{{ doc.title }}]({{ doc.url }})
{% endfor %}