from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.views.generic import ListView
from blog.models import *
from django.core.paginator import Paginator

def asosiy(request):
    jurnal = Jurnallar.objects.all()
    turi = Fayl_turi.objects.all()
    context = {
        "jurnal": jurnal,
        "fayl_turi": turi
    }
    return render(request, "index.html", context=context)


def jurnal_detel(request, id):
    detel = get_object_or_404(Jurnallar, id=id)
    context = {
        "jurnal_detel": detel
    }
    return render(request, "jurnal_detail.html", context=context)


def yangilik_detel(request, id):
    detel = get_object_or_404(Yangiliklar, id=id)
    context = {
        "yangilik_detel": detel
    }
    return render(request, "yangilik_detel.html", context=context)


class SearchResultList(ListView):
    model = Jurnallar
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fayl_turi"] = Fayl_turi.objects.all()
        context["jurnal"] = self.get_queryset()

        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        return self.model.objects.filter(
            Q(nomi__icontains=query) | Q(Text__icontains=query)
        )


def sinov_detel(request, id=id):
    turi = Fayl_turi.objects.all()
    if (id != 0):
        n = Jurnallar.objects.filter(kategory=id)
    else:
        n = Jurnallar.objects.all()
    context = {
        "jurnal": n,
        "fayl_turi": turi
    }
    return render(request, "index.html", context=context)


def jurnallar(request):
    contact_list = Jurnallar.objects.all()
    paginator = Paginator(contact_list, 8)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "jurnallar.html", {"page_obj": page_obj})


def yangiliklar(request):
    contact_list = Yangiliklar.objects.all()
    paginator = Paginator(contact_list, 4)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    mainNew = Yangiliklar.objects.get(mainNew=True)

    context = {
        "page_obj": page_obj,
        "mainNew": mainNew
    }

    return render(request, "yangiliklar.html", context)


def talablarList(request):
    talablar = Talablar.objects.all()

    return render(request, 'talablar.html', context={"talablar": talablar })

def taxririyatList(request):
    taxririyat = Tahririyat.objects.all()

    return render(request, 'taxririyat.html', context={"taxririyats": taxririyat})