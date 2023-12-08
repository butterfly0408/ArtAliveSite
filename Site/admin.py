from django.contrib import admin


from .models import Class, Artist, Teacher, Artwork, MailList


class ClassAdmin(admin.ModelAdmin):
    list_display = ('group', 'day', 'time',)


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'phone', 'email', 'prefix',)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('artist',)
    filter_horizontal = ('classes',)


class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'artist', 'image', 'title', 'medium', 'size', 'price', 'status',)
    list_filter = ('artist',)


class MailListAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "events", "newsletter",)


# Register your models here.

admin.site.register(Class, ClassAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Artwork, ArtworkAdmin)
admin.site.register(MailList, MailListAdmin)
