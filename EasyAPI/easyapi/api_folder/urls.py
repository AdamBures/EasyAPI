from django.urls import path
from . import views

urlpatterns = [
	path("", views.main),
	path("detail/", views.get_data),
	path("detail/<str:model>", views.get_model),
	path("detail/<str:model>/<int:model_id>", views.get_model_by_id),
	path("import/", views.add_item)
]