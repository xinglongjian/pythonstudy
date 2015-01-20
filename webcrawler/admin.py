from django.contrib import admin
from webcrawler.models import Province,City,Weather,Crawlerdb,District,BussZone,Community,House,HousePrice
# Register your models here.

admin.site.register(Province)
admin.site.register(City)
admin.site.register(Weather)
admin.site.register(Crawlerdb)
admin.site.register(District)
admin.site.register(BussZone)
admin.site.register(Community)
admin.site.register(House)
admin.site.register(HousePrice)