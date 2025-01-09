from django.shortcuts import render

# Create your views here.
from langchain_agent.views import process_query

def chatbot_view(request):
    response = ""
    if request.method == "POST":
        user_query = request.POST.get("query")
        response = process_query(user_query)
    return render(request, "chatbot.html", {"response": response})
