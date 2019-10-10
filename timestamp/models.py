import time
from datetime import datetime, date
from django.core.exceptions import ValidationError
from django.db import models


class Timestamp(models.Model):
    unix_ts = models.IntegerField()
    date_ts = models.DateTimeField()

    @classmethod
    def create(cls, ts):
        """This is not very nice.
        The best practice is to enforce a date format for the endpoint."""
        try:
            date_ = date.fromtimestamp(int(ts))
        except ValueError:
            try:
                date_ = datetime.strptime(ts, "%B %d, %Y")
            except ValueError:
                raise ValidationError('Incorrect timestamp')
            else:
                unix_ts = time.mktime(date_.timetuple())
                date_ts = ts
        else:
            unix_ts = ts
            date_ts = date_.strftime("%B %d, %Y")

        return cls(unix_ts=unix_ts, date_ts=date_ts)
