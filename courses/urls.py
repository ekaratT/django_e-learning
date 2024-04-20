from django.urls import path
from . import views


urlpatterns = [
    path('mine', views.ManageCourseListView.as_view(), name='manage_course_list'),
    path('create', views.CourseCreateView.as_view(), name='course_create'),
    path('<pk>/edit', views.CourseUpdateView.as_view(), name='course_edit'),
    path('<pk>/delete', views.CourseDeleteView.as_view(), name='course_delete'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout'),
    path('<pk>/module', views.CourseModuleUpdateView.as_view(), name='course_module_update'),
]