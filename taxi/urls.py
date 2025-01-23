from django.urls import path

from .views import index, ManufacturerListView, CarListView, CarDetailView, DriverListView, DriverDetailView

urlpatterns = [
    path("", index, name="index"),
    path("manufacturer/", ManufacturerListView, name="manufacturer-list"),
    path("cars/", CarListView, name="car-list"),
    path("cars/pk/", CarDetailView, name="car-detail"),
    path("drivers/", DriverListView, name="driver-list"),
    path("drivers/pk/", DriverDetailView, name="driver-detail")
]

app_name = "taxi"
