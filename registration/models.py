import uuid

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
# from payments.models import Pass
from django.db.models.signals import post_save, pre_save
from django.utils.safestring import mark_safe

from .utils import generate_registration_code, send_ca_confirmation_mail


class User(AbstractUser):
    google_picture = models.TextField(default='', blank=True)
    is_google = models.BooleanField(default=False)
    profile_complete = models.BooleanField(default=False)


class PreRegistration(models.Model):
    # choices
    YEAR_CHOICES = (
        ('1', 'First Year'),
        ('2', 'Second Year'),
        ('3', 'Third Year'),
        ('4', 'Fourth Year'),
        ('5', 'Fifth Year'),
        ('6', 'Other')
    )
    STATE_CHOICES = (
        ('1', 'Andhra Pradesh'),
        ('2', 'Arunachal Pradesh'),
        ('3', 'Assam'),
        ('4', 'Bihar'),
        ('5', 'Chhattisgarh'),
        ('6', 'Goa'),
        ('7', 'Gujarat'),
        ('8', 'Haryana'),
        ('9', 'Himachal Pradesh'),
        ('10', 'Jammu & Kashmir'),
        ('11', 'Jharkhand'),
        ('12', 'Karnataka'),
        ('13', 'Kerala'),
        ('14', 'Madhya Pradesh'),
        ('15', 'Maharashtra'),
        ('16', 'Manipur'),
        ('17', 'Meghalaya'),
        ('18', 'Mizoram'),
        ('19', 'Nagaland'),
        ('20', 'Odisha'),
        ('21', 'Punjab'),
        ('22', 'Rajasthan'),
        ('23', 'Sikkim'),
        ('24', 'Tamil Nadu'),
        ('25', 'Telangana'),
        ('26', 'Tripura'),
        ('27', 'Uttarakhand'),
        ('28', 'Uttar Pradesh'),
        ('29', 'West Bengal'),
        ('30', 'Andaman & Nicobar Islands'),
        ('31', 'Delhi'),
        ('32', 'Chandigarh'),
        ('33', 'Dadra & Naagar Haveli'),
        ('34', 'Daman & Diu'),
        ('35', 'Lakshadweep'),
        ('36', 'Puducherry'),
    )
    # Validators
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # Model
    full_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    college = models.CharField(max_length=100)
    college_state = models.CharField(max_length=2, choices=STATE_CHOICES, default='22')
    current_year = models.CharField(max_length=1, choices=YEAR_CHOICES, default='1')
    por = models.CharField(max_length=500, blank=True, default='')
    por_holder_contact = models.CharField(max_length=1000, blank=True, default='')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Pre Registration'
        verbose_name_plural = 'Pre Registrations'


class PreCA(models.Model):
    YEAR_CHOICES = (
        ('1', 'First Year'),
        ('2', 'Second Year'),
        ('3', 'Third Year'),
        ('4', 'Fourth Year'),
        ('5', 'Fifth Year'),
        ('6', 'Other')
    )
    STATE_CHOICES = (
        ('1', 'Andhra Pradesh'),
        ('2', 'Arunachal Pradesh'),
        ('3', 'Assam'),
        ('4', 'Bihar'),
        ('5', 'Chhattisgarh'),
        ('6', 'Goa'),
        ('7', 'Gujarat'),
        ('8', 'Haryana'),
        ('9', 'Himachal Pradesh'),
        ('10', 'Jammu & Kashmir'),
        ('11', 'Jharkhand'),
        ('12', 'Karnataka'),
        ('13', 'Kerala'),
        ('14', 'Madhya Pradesh'),
        ('15', 'Maharashtra'),
        ('16', 'Manipur'),
        ('17', 'Meghalaya'),
        ('18', 'Mizoram'),
        ('19', 'Nagaland'),
        ('20', 'Odisha'),
        ('21', 'Punjab'),
        ('22', 'Rajasthan'),
        ('23', 'Sikkim'),
        ('24', 'Tamil Nadu'),
        ('25', 'Telangana'),
        ('26', 'Tripura'),
        ('27', 'Uttarakhand'),
        ('28', 'Uttar Pradesh'),
        ('29', 'West Bengal'),
        ('30', 'Andaman & Nicobar Islands'),
        ('31', 'Delhi'),
        ('32', 'Chandigarh'),
        ('33', 'Dadra & Naagar Haveli'),
        ('34', 'Daman & Diu'),
        ('35', 'Lakshadweep'),
        ('36', 'Puducherry'),
    )
    # Validators
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # Model
    full_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    city = models.CharField(max_length=50)
    college = models.CharField(max_length=100)
    college_state = models.CharField(max_length=2, choices=STATE_CHOICES, default='22')
    current_year = models.CharField(max_length=1, choices=YEAR_CHOICES, default='1')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'CA Pre Registration'
        verbose_name_plural = 'CA Pre Registrations'


def post_save_campus_ambassador_pre(sender, instance, created, **kwargs):
    if created:
        send_ca_confirmation_mail(instance=instance)


post_save.connect(post_save_campus_ambassador_pre, sender=PreCA)


class UserProfile(models.Model):
    # choices
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('T', 'Other'),
    )
    YEAR_CHOICES = (
        ('1', 'First Year'),
        ('2', 'Second Year'),
        ('3', 'Third Year'),
        ('4', 'Fourth Year'),
        ('5', 'Fifth Year'),
        ('6', 'Other')
    )
    STATE_CHOICES = (
        ('1', 'Andhra Pradesh'),
        ('2', 'Arunachal Pradesh'),
        ('3', 'Assam'),
        ('4', 'Bihar'),
        ('5', 'Chhattisgarh'),
        ('6', 'Goa'),
        ('7', 'Gujarat'),
        ('8', 'Haryana'),
        ('9', 'Himachal Pradesh'),
        ('10', 'Jammu & Kashmir'),
        ('11', 'Jharkhand'),
        ('12', 'Karnataka'),
        ('13', 'Kerala'),
        ('14', 'Madhya Pradesh'),
        ('15', 'Maharashtra'),
        ('16', 'Manipur'),
        ('17', 'Meghalaya'),
        ('18', 'Mizoram'),
        ('19', 'Nagaland'),
        ('20', 'Odisha'),
        ('21', 'Punjab'),
        ('22', 'Rajasthan'),
        ('23', 'Sikkim'),
        ('24', 'Tamil Nadu'),
        ('25', 'Telangana'),
        ('26', 'Tripura'),
        ('27', 'Uttarakhand'),
        ('28', 'Uttar Pradesh'),
        ('29', 'West Bengal'),
        ('30', 'Andaman & Nicobar Islands'),
        ('31', 'Delhi'),
        ('32', 'Chandigarh'),
        ('33', 'Dadra & Naagar Haveli'),
        ('34', 'Daman & Diu'),
        ('35', 'Lakshadweep'),
        ('36', 'Puducherry'),
    )
    # Validators
    contact = RegexValidator(r'^[0-9]{10}$', message='Not a valid number!')
    # Model
    referred_by = models.ForeignKey('CampusAmbassador', blank=True, null=True, on_delete=models.SET_NULL, related_name="referred_users", related_query_name="referred_user")
    # referred_by_igmun = models.ForeignKey("igmun.IGMUNCampusAmbassador", blank=True, null=True, on_delete=models.SET_NULL, related_name="referred_igmun_users", related_query_name="referred_igmun_user")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    phone = models.CharField(max_length=10, validators=[contact])
    # avatar = models.ImageField(upload_to="user-avatars/", null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    current_year = models.CharField(max_length=1, choices=YEAR_CHOICES, default='1')
    college = models.CharField(max_length=128)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    # _pass = models.ManyToManyField(Pass, verbose_name="Passes", related_name="users", related_query_name="user")
    uuid = models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, unique=True)
    registration_code = models.CharField(max_length=12, unique=True, editable=False, default="")
    timestamp = models.DateTimeField(auto_now_add=True)
    events_registered = models.ManyToManyField("events.Event", blank=True)
    # workshops_registered = models.ManyToManyField(Workshop, through='WorkshopRegistration',
    #                                             through_fields=('userprofile', 'workshop'), blank=True)
    # registration_code_igmun = models.CharField(max_length=15, editable=False, default="", blank=True)
    # timestamp = models.DateTimeField(auto_now_add=True)
    is_ca = models.BooleanField(default=False)
    # is_igmun_ca = models.BooleanField(default=False)
    amount_paid = models.BooleanField(default=False)
    pronites = models.BooleanField(default=False)
    igmun = models.BooleanField(default=False)
    accomodation = models.BooleanField(default=False)
    main_pronite = models.BooleanField(default=False)
    flagship = models.BooleanField(default=False)
    igmun_pref = models.CharField(max_length=1000, default='', blank=True)

    class Meta:
        ordering = ['user__first_name']

    def __str__(self):
        return self.user.get_full_name()

    # @property
    # def events(self):
    #     return '; '.join([e.name for e in self.events_registered.all()])

    # def passes(self):
    #     return ', '.join([p.name for p in self._pass.all()])

    def qr_code(self):
        base_url = "https://chart.apis.google.com/chart?chs=150x150&cht=qr"
        data = self.registration_code
        return mark_safe(
            f'<img src="{base_url}&chl={data}&choe=UTF-8" \
            style="width: 150px; height: 150px" />'
        )
    qr_code.short_description = 'QR Code'

    def pronites_qr(self):
        base_url = "https://chart.apis.google.com/chart?chs=150x150&cht=qr"
        data = self.uuid
        return mark_safe(
            f'<img src="{base_url}&chl={data}&choe=UTF-8" \
            style="width: 150px; height: 150px" />'
        )
    pronites_qr.short_description = 'Pronites QR'


def pre_save_user_profile(sender, instance, **kwargs):
    if instance._state.adding is True:
        name = ''.join(instance.user.get_full_name().split())
        count = instance.__class__.objects.count()

        if len(name) >= 3:
            code = generate_registration_code(name, count)
        else:
            code = generate_registration_code('X' * (3 - len(name)) + name, count)

        instance.registration_code = f"IG-{code}"

        # if instance.igmun is True:
        #     instance.registration_code_igmun = f"IGMUN-{code}"


pre_save.connect(pre_save_user_profile, sender=UserProfile)


class CampusAmbassador(models.Model):
    ca_user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    referral_code = models.CharField(max_length=12, editable=False, unique=True, primary_key=True)
    verified = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Campus Ambassadors"

    @property
    def number_referred(self):
        return self.referred_users.count()

    def __str__(self):
        return self.ca_user.user.get_full_name()


def pre_save_campus_ambassador(sender, instance, **kwargs):
    if instance._state.adding is True:
        instance.referral_code = instance.ca_user.registration_code


pre_save.connect(pre_save_campus_ambassador, sender=CampusAmbassador)
