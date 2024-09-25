from django.db import models
from datetime import datetime

class VisaInfo(models.Model):
    serial_id = models.IntegerField(unique=True, null=True, blank=True)
    visa_qnt = models.IntegerField(null=True, blank=True)
    visa_no = models.CharField(max_length=50, null=True, blank=True)
    visa_iss_dt = models.CharField(max_length=50, null=True, blank=True, default='')
    submitted_date = models.CharField(max_length=50, null=True, blank=True, default='')
    # submitted_date = models.DateField(default=datetime.now, null=True, blank=True)
    destination = models.CharField(max_length=50, null=True, blank=True, default='')
    visa_person_name = models.CharField(max_length=50, null=True, blank=True, default='')
    village = models.CharField(max_length=50, null=True, blank=True, default='')
    thana = models.CharField(max_length=50, null=True, blank=True, default='')
    phone_no = models.CharField(max_length=20, null=True, blank=True, default='')
    post_office = models.CharField(max_length=50, null=True, blank=True, default='')
    district = models.CharField(max_length=50, null=True, blank=True, default='')
    mobile = models.CharField(max_length=20, null=True, blank=True, default='')
    sponser_id = models.CharField(max_length=50, null=True, blank=True, default='')
    sponser_name_english = models.CharField(max_length=200, null=True, blank=True, default='')
    sponser_name_arabic = models.CharField(max_length=200, null=True, blank=True, default='')
    sponser_phone = models.CharField(max_length=20, null=True, blank=True, default='')
    sponser_address = models.CharField(max_length=100, null=True, blank=True, default='')
    sender_name = models.CharField(max_length=100, null=True, blank=True, default='')
    sender_phone = models.CharField(max_length=20, null=True, blank=True, default='')
    sender_address = models.CharField(max_length=50, null=True, blank=True, default='')

    def __str__(self):
        return f"{self.serial_id} - {self.visa_no}"

class VisaApplication(models.Model):
    visa_info = models.ForeignKey(VisaInfo, on_delete=models.CASCADE, null=True, blank=True)
    serial_no = models.CharField(max_length=50, null=True, blank=True)
    # id_number = models.CharField(max_length=50, null=True, blank=True, default='')
    # name_employer = models.CharField(max_length=50, null=True, blank=True, default='')
    SEX_CHOICES = [('----', '----'), ('Male', 'Male'), ('Female', 'Female')]
    POT_CHOICES = [('----', '----'), ('WORK', 'WORK'), ('TRANSIT', 'TRANSIT'), ('VISIT', 'VISIT'), ('UMRAH', 'UMRAH'), ('RESIDENCE', 'RESIDENCE'), 
                   ('HAJJ', 'HAJJ'), ('DIPLOMACY', 'DIPLOMACY')]
    
    # visa_date = models.CharField(max_length=50, null=True, blank=True)

    f_name = models.CharField(max_length=50, null=True, blank=True, default='')
    father_name = models.CharField(max_length=50, null=True, blank=True, default='')

    # dob = models.DateField(default=datetime.now, null=True, blank=True)
    dob = models.CharField(max_length=50, null=True, blank=True, default='')

    prv_nationality = models.CharField(max_length=50, null=True, blank=True, default='BANGLADESHI')
    prs_nationality = models.CharField(max_length=50, null=True, blank=True, default='BANGLADESHI')
    sex = models.CharField(max_length=6, choices=SEX_CHOICES, default='----', null=True, blank=True)
    marital_s = models.CharField(max_length=50, null=True, blank=True, default='MARRIED')
    sect = models.CharField(max_length=50, null=True, blank=True, default='')
    religion = models.CharField(max_length=50, null=True, blank=True, default='ISLAM')
    poi_1 = models.CharField(max_length=50, null=True, blank=True, default='DHAKA')
    qualification = models.CharField(max_length=50, null=True, blank=True, default='CLASS EIGHT')
    profession = models.CharField(max_length=50, null=True, blank=True, default='WORKER')
    home_add_and_tel_no = models.CharField(max_length=50, null=True, blank=True, default='')

    pot = models.CharField(max_length=10, choices=POT_CHOICES, default='----', null=True, blank=True)

    # date_passport_issued = models.DateField(default=datetime.now, null=True, blank=True)
    date_passport_issued = models.CharField(max_length=50, null=True, blank=True, default='')

    passport_no = models.CharField(max_length=50, null=True, blank=True, default='')

    dosK = models.CharField(max_length=50, null=True, blank=True, default='')
    doa = models.CharField(max_length=50, null=True, blank=True, default='')
    dod = models.CharField(max_length=50, null=True, blank=True, default='')
    
    # doa = models.DateField(default=datetime.now, null=True, blank=True)
    # dod = models.DateField(default=datetime.now, null=True, blank=True)
   
    relationship = models.CharField(max_length=50, null=True, blank=True, default='')

    # auth = models.CharField(max_length=50, null=True, blank=True, default='')
    # office_employer = models.CharField(max_length=50, null=True, blank=True, default='')
    # office_id = models.CharField(max_length=50, null=True, blank=True, default='')

    office_date = models.CharField(max_length=50, null=True, blank=True, default='')
    office_fee = models.CharField(max_length=50, null=True, blank=True, default='')
    office_type = models.CharField(max_length=50, null=True, blank=True, default='')
    office_duration = models.CharField(max_length=50, null=True, blank=True, default='')
    mofa_no = models.CharField(max_length=50, null=True, blank=True, default='')

    def __str__(self):
        return self.serial_no or "No description"
