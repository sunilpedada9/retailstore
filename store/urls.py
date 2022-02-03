from django.conf.urls import url
from store import views

#
urlpatterns=[
    url(r"^create_category/$",views.CategoryCreate.as_view()),
    url(r"^category_list/",views.CategoryListAndRemove.as_view()),
    url(r"^remove_category/$",views.CategoryListAndRemove.as_view()),
    url(r"^create_product$",views.CreateItem.as_view()),
    url(r"^product_list/",views.ListUpdateRemoveItem.as_view()),
    url(r"^update_product$",views.ListUpdateRemoveItem.as_view()),
    url(r"^remove_product$",views.ListUpdateRemoveItem.as_view()),
    url(r"^create_rack$",views.CRUDRack.as_view()),
    url(r"^update_rack$",views.CRUDRack.as_view()),
    url(r"^rack_list$",views.CRUDRack.as_view()),
    url(r"^remove_rack$",views.CRUDRack.as_view())
]