class TimeZone:
    def __init__(self, name_zone, hour, minute):
        self.name = name_zone
        self.offset_hours = hour
        self.offset_minutes = minute

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name_zone):
        if isinstance(name_zone, str) and len(' '.join(name_zone.split())) > 0:
            self._name = ' '.join(name_zone.split())
        else:
            raise ValueError(f'Timezone bad name - {name_zone}')

    @property
    def offset_hours(self):
        return self._hour

    @offset_hours.setter
    def offset_hours(self, hour):
        if isinstance(hour, int):
            if -12 <= hour <= 14:
                self._hour = hour
            else:
                raise ValueError('Offset must be between -12:00 and +14:00.')
        else:
            raise ValueError('Hour offset must be an integer.')

    @property
    def offset_minutes(self):
        return self._minute

    @offset_minutes.setter
    def offset_minutes(self, minute):
        if isinstance(minute, int):
            if -59 <= minute <= 59:
                self._minute = minute
            else:
                raise ValueError('Minutes offset must between -59 and 59.')
        else:
            raise ValueError('Minutes offset must be an integer.')