from django.urls import path

from new_app import views

urlpatterns = [
path("login",views.Log,name="login"),
path("seller",views.sellerR,name="seller"),
    path("coustmer",views.coustmerR,name="coustmer"),
    path("",views.land,name="land"),
    path("dash",views.dash,name="dash"),
    path("login_view",views.login_view,name="login_view"),
    path("blog_posting",views.blog_posting,name="blog_posting"),
    path("view",views.view,name="view"),
    path("delete/<int:id>",views.remove,name="delete"),
    path("update/<int:id>",views.update,name="update")
]