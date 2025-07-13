from django.urls import path

from . import views

urlpatterns = [
    # ex: /pediatrics/
    path("", views.index, name="index"),
    # ex: /pediatrics/5/
    # path("<int:question_id>/", views.detail, name="detail"),
    # # ex: /pediatrics/5/results/
    # path("<int:question_id>/results/", views.results, name="results"),
    # # ex: /pediatrics/5/vote/
    # path("<int:question_id>/vote/", views.vote, name="vote"),
]