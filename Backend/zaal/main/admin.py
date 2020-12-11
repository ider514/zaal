from django.contrib import admin
from .models import Court, CourtPaymentInfo, Calendar, CourtLocation, Amenities, CourtFiles, Manager, Reservations, Payment, Review, UserLocation, UserPaymentInfo

# Register your models here.
myModels = [Court, CourtPaymentInfo, Calendar, CourtLocation, Amenities,
CourtFiles, Manager, Reservations, Payment, Review, UserLocation, UserPaymentInfo]  # iterable list
admin.site.register(myModels)
