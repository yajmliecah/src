from __future__ import unicode_literals

from django.db import models


class Country(models.Model):
    ASIA = (
            ('PHILIPPINES', 'Philippines'),
            ('JAPAN', 'Japan'),
            ('CHINA', 'China'),
        )
    name = models.CharField(max_length=20, choices=ASIA)