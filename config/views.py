from django.shortcuts import render
from burgers.models import Burger, Drink


def main(request):
    return render(request, "main.html")


def burger_list(request):
    burgers = Burger.objects.all()
    print("전체 햄버거 목록:", burgers)

    context = {
        "burgers": burgers,
    }
    return render(request, "burger_list.html", context)


def burger_search(request):
    keyword = request.GET.get("keyword")
    # 키 값이 있을 때, 검색된 QuerySet으로 할당
    if keyword is not None:
        burgers = Burger.objects.filter(name__contains=keyword)
    # 키 값이 없을 때, 빈 QuerySet으로 할당
    else:
        burgers = Burger.objects.none()

    context = {
        "burgers": burgers,
    }
    return render(request, "burger_search.html", context)


def drink_list(request):
    drinks = Drink.objects.all()

    context = {
        "drinks": drinks,
    }
    return render(request, "drink_list.html", context)
