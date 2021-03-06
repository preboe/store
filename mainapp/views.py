from django.shortcuts import render
from django.views.generic import DeleteView
from .models import Soap, Cosmetics, Perfume

from .forms import LoginForm





def test_view(request):
    return render(request, 'base.html', {})

def password(request):
    return render(request, 'password.html',)


class ProductDetailView(DeleteView):

    CT_MODEL_MODEL_CLASS = {
        'soap': Soap,
        'cosmetics': Cosmetics,
        'perfume': Perfume,
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    # model = Model
    # queryset = Model.objects.all()
    context_object_name = 'prodect'
    template_name = 'product_detail.html'
    slug_url_kwarg = 'slug'


