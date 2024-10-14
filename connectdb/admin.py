from django.contrib import admin
from .models import Sector, RFIDTag, Personnel, Visitors, LogType, Logs

# Register Sector Model
@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ('sector_id', 'sector_name', 'location')
    search_fields = ('sector_name', 'location')

# Register RFID Tag Model
@admin.register(RFIDTag)
class RFIDTagAdmin(admin.ModelAdmin):
    list_display = ('rfidTag_id', 'tag_type', 'issue_date', 'expiry_time', 'sector')
    list_filter = ('tag_type', 'sector')
    search_fields = ('rfidTag_id', 'tag_type')

# Register Personnel Model
@admin.register(Personnel)
class PersonnelAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'contact_number', 'rfid_tag')
    search_fields = ('first_name', 'last_name', 'email')

# Register Visitors Model
@admin.register(Visitors)
class VisitorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'address', 'contact_number', 'sector', 'rfid_tags')
    search_fields = ('fist_name', 'last_name', 'address')
    list_filter = ('sector',)

# Register LogType Model
@admin.register(LogType)
class LogTypeAdmin(admin.ModelAdmin):
    list_display = ('log_id', 'rfid_tag', 'log_type')
    search_fields = ('log_type',)

# Register Logs Model
@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('logs_id', 'time_in', 'time_out', 'log_type')
    list_filter = ('time_in', 'time_out', 'log_type')
    search_fields = ('logs_id',)
