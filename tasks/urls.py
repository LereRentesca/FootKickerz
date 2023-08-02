from django.urls import path

from tasks.views import home, signup, signin, signout, tasks, create_tasks

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('tasks/', tasks, name='tasks'),
    path('tasks/create/', create_tasks, name='create'),
    path('logout/', signout, name='logout'),
    path('login/', signin, name='login'),
]