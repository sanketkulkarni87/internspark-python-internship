from datetime import datetime
import pytz

class Timezone:
    def __init__(self, name):
        self.name = name
        self.timezone = pytz.timezone(name)

    def get_time(self):
        return datetime.now(self.timezone)

# You can add more timezone classes and methods as needed