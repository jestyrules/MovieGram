from django.urls import path

from backend import views

urlpatterns = [
    path("indexpage/", views.indexpage, name="indexpage"),
    path("addcategory/", views.addcategory, name="addcategory"),
    path("categorysave/", views.categorysave, name="categorysave"),
    path("addlanguage/", views.addlanguage, name="addlanguage"),
    path("languagesave/", views.languagesave, name="languagesave"),
    path("addproduct/", views.addproduct, name="addproduct"),
    path("productsave/", views.productsave, name="productsave"),
    path("displayproduct/", views.displayproduct, name="displayproduct"),
    path("editproduct/<int:dataid>/", views.editproduct, name="editproduct"),
    path("updatemov/<int:dataid>/", views.updatemov, name="updatemov"),
    path("deleteproduct/<int:dataid>/", views.deleteproduct, name="deleteproduct"),
    path("adminlogin/", views.adminlogin, name="adminlogin"),
    path("adminsave/", views.adminsave, name="adminsave"),
    path("adminlogout/", views.adminlogout, name="adminlogout"),
]
