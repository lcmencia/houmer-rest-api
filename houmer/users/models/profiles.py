"""Profile model."""

# Django
from django.db import models

# Utilities
from houmer.utils.models import HoumerModel


class Profile(HoumerModel):
    """Profile model.

    A profile holds a user's public data like biography, picture,
    and statistics.
    """

    users = models.OneToOneField('users.User', on_delete=models.CASCADE)

    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )
    biography = models.TextField(max_length=500, blank=True)

    # Stats
    properties_taken = models.PositiveIntegerField(default=0)
    properties_offered = models.PositiveIntegerField(default=0)
    reputation = models.FloatField(
        default=5.0,
        help_text="User's reputation based on the properties taken and offered."
    )

    def __str__(self):
        """Return user's str representation."""
        return str(self.user)
