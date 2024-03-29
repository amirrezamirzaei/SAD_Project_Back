from django.urls import path
from content.views import ContentView, LibraryView, AddContentToLibraryView, GetLibraryFiles, DownloadView, \
    GrantPermission, GetSharedFiles, GrantPermissionLibrary, RemoveContentFromLibraryView, EditInfoContentView

urlpatterns = [
    path('content/', ContentView.as_view(), name="view content"),
    path('library/', LibraryView.as_view(), name="view library"),
    path('add-content-to-library/', AddContentToLibraryView.as_view(), name="add content to library"),
    path('remove-content-from-library/', RemoveContentFromLibraryView.as_view(), name="remove content from library"),
    path('edit-info-content/', EditInfoContentView.as_view(), name="edit info content"),
    path('get-library-files/', GetLibraryFiles.as_view(), name="get library files"),
    path('download/<str:file_path>', DownloadView.as_view(), name='download view'),
    path('grant-permission/', GrantPermission.as_view(), name='grant permission'),
    path('grant-permission-library/', GrantPermissionLibrary.as_view(), name='grant permission library'),
    path('get-shared-file/', GetSharedFiles.as_view(), name='get shared files'),
]
