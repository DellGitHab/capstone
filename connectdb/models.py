from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User model
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('personnel', 'Personnel'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='personnel')

# Sector Model
class Sector(models.Model):
    sector_id = models.AutoField(primary_key=True)
    sector_name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.sector_name

# RFID Tag Model
class RFIDTag(models.Model):
    rfidTag_id = models.AutoField(primary_key=True)
    tag_type = models.CharField(max_length=50)
    issue_date = models.DateTimeField()
    expiry_time = models.DateTimeField()
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)

    def __str__(self):
        return f"RFID Tag {self.rfidTag_id} ({self.tag_type})"

# Personnel Model
class Personnel(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)  # Direct reference to CustomUser
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    rfid_tag = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Visitors Model
class Visitors(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    rfid_tags = models.ForeignKey(RFIDTag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Log Type Model
class LogType(models.Model):
    log_id = models.AutoField(primary_key=True)
    rfid_tag = models.ForeignKey(RFIDTag, on_delete=models.CASCADE)
    log_type = models.CharField(max_length=50)

    def __str__(self):
        return f"Log Type {self.log_id}: {self.log_type}"

# Logs Model
class Logs(models.Model):
    logs_id = models.AutoField(primary_key=True)
    time_in = models.DateTimeField()
    time_out = models.DateTimeField(null=True, blank=True)  # Allow time_out to be optional
    log_type = models.ForeignKey(LogType, on_delete=models.CASCADE)

    def __str__(self):
        return f"Log {self.logs_id}: {self.time_in} to {self.time_out if self.time_out else 'Still logged in'}"

# Log Entry Model
class LogEntry(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='log_entries')  # Direct reference to CustomUser
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)  # Optional field for IP address
    status = models.CharField(max_length=10)  # e.g., 'success' or 'failure'
    user_agent = models.TextField(null=True, blank=True)  # Optional field for the user's browser info

    def __str__(self):
        return f"LogEntry {self.id}: {self.user} on {self.timestamp} - {self.status}"
