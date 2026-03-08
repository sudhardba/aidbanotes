---
layout: page
title: Oracle
---

# Oracle Articles

<ul>
{% for post in site.oracle %}
<li><a href="{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}
</ul>