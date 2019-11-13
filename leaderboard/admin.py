from django.contrib import admin

# Register your models here.
from leaderboard.models import Score

class ScoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'emoji', "duration")

admin.site.register(Score, ScoreAdmin)