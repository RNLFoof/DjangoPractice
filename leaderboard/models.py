from datetime import timedelta

from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
from django.forms import ModelForm, SelectDateWidget

from leaderboard.widgets import DurationSelectorWidget


class Score(models.Model):
    user = models.CharField(max_length=32)
    title = models.CharField(max_length=2000)
    start_time = models.DateField()
    duration = models.DurationField(validators=[MinValueValidator(timedelta())])
    emoji = models.ImageField(upload_to="leaderboard/static/leaderboard/emojis/")

    @classmethod
    def create(cls, user, title, start_time, duration, emoji):
        score = cls(user=user, title=title, start_time=start_time, duration=duration, emoji=emoji)
        return score

    def __str__(self):
        return self.user

    def tier(self):
        if self.duration.days >= 1:
            return "tier4"
        elif self.duration.seconds >= 60*60*8:
            return "tier3"
        elif self.duration.seconds >= 60*60*2:
            return "tier2"
            return "tier1"
        return "tier0"

    def tierpath(self):
        return f"leaderboard/images/{self.tier()}.png"

    def emojipath(self):
        return f"leaderboard/emojis/{self.emoji.name.split('/')[-1]}"
    
class ScoreForm(ModelForm):
    class Meta:
        model = Score
        fields = ["user", "title", "start_time", "duration", "emoji"]
        widgets = {
            "duration": DurationSelectorWidget(),
            "start_time": SelectDateWidget()
        }