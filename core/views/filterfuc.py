def search_view(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        countries = Country.objects.search(**form.cleaned_data)
    else:
        countries = Country.objects.all()
    return render(request, "country/search.html",
            {"form": form, "country_list": countries})