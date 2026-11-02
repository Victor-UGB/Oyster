from django.contrib import admin
from .models import Post, UserProfile, User, Tag, Folder, Pearl, PearlSourceType, PearlStatus
# from .models import Family
# Register your models here.


admin.site.register(Post)
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Tag)
admin.site.register(Folder)
admin.site.register(Pearl)

# admin.site.register(PearlSourceType)
# admin.site.register(PearlStatus)
