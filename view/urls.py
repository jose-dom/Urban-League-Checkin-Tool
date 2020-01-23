from django.urls import path
from view import views as main
from view.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, VisitorListView

urlpatterns = [
    path('', PostListView.as_view(), name='view-home'),#Home Page/Visitor CheckIn
    path('post/', PostListView.as_view(), name='view-post'),#Annoucements
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),#Annoucement Detail View
    path('post/new/', PostCreateView.as_view(), name='post-create'),#Annoucement Create View
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),#Annoucement Update View
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),#Annoucement Delete View
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('analytics/', VisitorListView.as_view(), name='analytics'),
    path('reports/', main.reports, name='reports'),
]