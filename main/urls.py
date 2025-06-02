from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import (
    home,
    bookevent,
    addevent,
    Single_event,
    delete_event,
    view_parti,
    all_event,
    event_search,
    confirm,
    prompt,
    create_travel_buddy,
    search_users,
    user_profile_detail,
)

# For serving media files in development
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Home / Index
    path('', home, name='index'),

    # Event booking / unbooking
    path('book_unbook/<int:id>/', bookevent, name='book_unbook'),

    # Add, view single, and delete events
    path('add_event/', addevent, name='add_event'),
    path('viewe_event/<int:id>/', Single_event, name='viewe_event'),
    path('remove_event/<int:event_id>/', delete_event, name='remove_event'),

    # AJAX: view participants
    path('viewe_parti/', view_parti, name='viewe_parti'),

    # Event list + search (GET ?q=...)
    path('viewe_all_event/', all_event, name='viewe_all_event'),

    # Legacy POST-based search (if you still use it)
    path('event/search/', event_search, name='event_search'),

    # Confirmation & prompt (unused for search)
    path('confirm/<str:name>/<str:location>/<str:date>/', confirm, name='confirm'),
    path('prompt/<int:id>/', prompt, name='prompt'),

    # Authentication
    path('logout/', LogoutView.as_view(), name='logout'),

    # Travel Buddy
    path('create_travel_buddy/', create_travel_buddy, name='create_travel_buddy'),
    path('search_travel_buddy/', search_users, name='search_travel_buddy'),
    path('profile/<int:user_id>/', user_profile_detail, name='user_profile_detail'),
]

# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
