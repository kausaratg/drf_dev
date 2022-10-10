from django.urls import path
from products import views

urlpatterns = [
    path('', views.ProductCreateListAPIView.as_view()),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.ProductDeleteAPIView.as_view()),
    path('<int:pk>/', views.ProductDetailAPIView.as_view()),
    # path("list", views.ProductListAPIView.as_view())
]
