{% extends 'base.html' %}
{% block content %}


<h1>Delete Stock</h1>

{% if ticker %}
	{% for item in ticker %}
		{{ item }} - <a href="{% url 'delete' item.id %}">delete</a><br/>
	{% endfor %}
{% else %}
	You dont' have any tickers
{% endif %}



{% endblock %}