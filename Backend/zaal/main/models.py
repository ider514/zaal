import datetime
from django.db import models
from django.conf import settings

MOBILE = 'MO'
CASH = 'CS'
CARD = 'CA'
METHOD_CHOICES = [
    (MOBILE, 'Mobile'),
    (CASH, 'Cash'),
    (CARD, 'Card'),
]

# Create your models here.
class Court(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return "%s court" % self.name
    description = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(editable=True)
    modified_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = datetime.datetime.now()
        self.modified = datetime.datetime.now()
        return super(Court, self).save(*args, **kwargs)
    EXCLUSIVE = 'EX'
    STANDART = 'ST'
    NIGHT = 'NI'
    NONE = 'NO'
    CATEGORY_CHOICES = [
        (EXCLUSIVE, 'Exclusive'),
        (STANDART, 'Standart'),
        (NIGHT, 'Night'),
        (NONE, 'None'),
    ]
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=NONE,
    )
    rating = models.IntegerField()
class CourtPaymentInfo(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE,)
    method = models.CharField(
        max_length=2,
        choices=METHOD_CHOICES,
        default=MOBILE,
    )
    info = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = "CourtPaymentInfo"

class Calendar(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    timeline = models.IntegerField()

class CourtLocation(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE,)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)

class Amenities(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    amenitites = models.CharField(max_length=20)
    class Meta:
        verbose_name_plural = "Amenities"

class CourtFiles(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE,)
    image = models.ImageField(upload_to='images/')
    class Meta:
        verbose_name_plural = "CourtFiles"

class Manager(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 254) 
    phone_number = models.CharField(max_length=8)
    def __str__(self):
        return "%s manager of %s" % (self.name, self.court)
    password = models.CharField(max_length=50)

class Reservations(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    start_date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=200, blank=True)
    FULL = 'FU'
    HALF = 'HA'
    CATEGORY_CHOICES = [
        (FULL, 'Full'),
        (HALF, 'Half'),
    ]
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=FULL,
    )
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    cancellation_fee = models.DecimalField(max_digits=8, decimal_places=2)
    cancelled_at = models.DateTimeField()
    PAID = 'PA'
    UNPAID = 'UN'
    CANCELLED = 'CA'
    STATUS_CHOICES = [
        (PAID, 'Paid'),
        (UNPAID, 'Unpaid'),
        (CANCELLED, 'Cancelled'),
    ]
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=UNPAID,
    )
    payment_date_time = models.DateTimeField()
    cancellation_date_time = models.DateTimeField()
    class Meta:
        verbose_name_plural = "Reservations"

class Payment(models.Model):
    reservation = models.ForeignKey(Reservations, on_delete=models.CASCADE)
    method = models.CharField(
        max_length=2,
        choices = METHOD_CHOICES,
        default = MOBILE,
    )
    date_time = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)

class Review(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    review = models.CharField(max_length=200)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

# class USER(models.Model):
#     username=models.CharField(max_length=100)
#     password=models.CharField(max_length=100)
#     email=models.CharField(max_length=50)
#     profile_pic=models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None,blank=True)
#     phone_no=models.CharField(max_length=50)
#     address=models.TextField()
#     state=models.CharField(max_length=30,blank=True)
#     pin_code=models.IntegerField(blank=True)
#     def __str__(self):
#         return "Customer: "+self.username

class UserLocation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)

class UserPaymentInfo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    method = models.CharField(
        max_length=2,
        choices = METHOD_CHOICES,
        default = MOBILE,
    )
    info = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = "UserPaymentInfo"
