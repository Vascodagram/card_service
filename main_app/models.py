from datetime import datetime
from django.db import models
from django.utils import timezone

STATUS_CHOICES = (
    ('not activated', 'Неактивована'),
    ('activated', 'Активована'),
    ('overdue', 'Прострочена')
)


class Card(models.Model):
    series = models.ForeignKey('Series', on_delete=models.CASCADE)
    number = models.CharField(max_length=16, unique=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=True, null=True)
    cvv = models.CharField(max_length=3)
    balance = models.FloatField(default=0)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='not activated')

    def __str__(self):
        return f'{self.series.name, self.number, self.balance}'

    @classmethod
    def from_db(cls, db, field_names, values):
        """ Card expiration date """
        instance = super().from_db(db, field_names, values)
        if instance.end_date < timezone.now():
            instance.save()
        return instance

    def save(self, *args, **kwargs):
        if self.end_date < datetime.now(self.end_date.tzinfo):
            self.status = 'overdue'
        super(Card, self).save(*args, **kwargs)


class Balance(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, blank=True, null=True, related_name='parent_card')
    name = models.CharField(max_length=15, default='Платіж', blank=True, null=True)
    transaction = models.FloatField(default=0)

    def __str__(self):
        return f'Name: {self.name}, Trans: {self.transaction}, Number: {self.card.number}'

    def save(self, *args, **kwargs):
        if self.transaction:
            balance = self.card.balance + self.transaction
            Card.objects.filter(pk=self.card.id).update(balance=balance)
        super(Balance, self).save(*args, **kwargs)


class Series(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name}'



