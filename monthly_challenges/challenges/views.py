from django.shortcuts import render
from django.http import Http404,HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


monthly_challenges = {
    "january": "Challenge 1",
    "february": "Challenge 2",
    "march": "Challenge 3",
    "april": "Challenge 4",
    "may": "Challenge 5",
    "june": "Challenge 6",
    "july": "Challenge 7",
    "august": "Challenge 8",
    "september": "Challenge 9",
    "october": "Challenge 10",
    "november": "Challenge 11",
    "december": None,
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    redirecet_path = reverse("month-challenge", args=[redirect_month]) 
    return HttpResponseRedirect(redirecet_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month,
        })
    except:
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        raise Http404()
    




