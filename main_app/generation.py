import random
from datetime import datetime
from dateutil.relativedelta import relativedelta
from .models import Card, Series


class GenerationCards:
    """generating a random number of cards"""

    def __init__(self, request):
        self.card = Card.objects.create
        self.series = Series.objects.get(pk=request.POST['series'])
        self.value = request.POST['value']
        self.year = request.POST['year']
        self.month = request.POST['month']

    def set_up(self):
        for _ in range(0, int(self.value)):
            self.creating_card()

    def creating_card(self):
        self.card(
            series=self.series,
            number=self.random_number(),
            end_date=self.end_date(),
            cvv=self.random_cvv(),
            status='not activated'
        )

    def end_date(self):
        """Calculation of the expiration date of the card, taking into account the months 28/29/30/31"""
        end_date = datetime.today() + relativedelta(years=+int(self.year), months=+int(self.month))
        return end_date

    @staticmethod
    def random_cvv():
        """Create random cvv"""
        return str(random.randint(0, 999)).zfill(3)

    @staticmethod
    def random_number():
        """Create random number"""
        return str(random.randint(0, 9999999999999999)).zfill(9)
