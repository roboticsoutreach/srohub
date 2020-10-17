from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import ListView
from inventory.models import Asset


class SearchView(LoginRequiredMixin, ListView):

    model = Asset
    template_name = "inventory/search.html"
    paginate_by = 15

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=object_list, **kwargs)
        if "query" in self.request.GET:
            data["query"] = self.request.GET["query"]
        return data

    def get_queryset(self):
        if "query" in self.request.GET and self.request.GET["query"] != "":
            return Asset.get_search_queryset(self.request.GET["query"])
        else:
            return Asset.objects.order_by("-updated_at").all()
