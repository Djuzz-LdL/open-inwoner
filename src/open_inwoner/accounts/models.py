from datetime import date
from uuid import uuid4

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.translation import ugettext_lazy as _

from localflavor.nl.models import NLBSNField, NLZipCodeField
from privates.storages import PrivateMediaFileSystemStorage

from open_inwoner.utils.validators import validate_phone_number

from .choices import ContactTypeChoices, LoginTypeChoices, StatusChoices
from .managers import DigidManager, UserManager, eHerkenningManager
from .query import MessageQuerySet


class User(AbstractBaseUser, PermissionsMixin):
    """
    Use the built-in user model.
    """

    first_name = models.CharField(
        _("first name"), max_length=255, blank=True, default=""
    )
    last_name = models.CharField(_("last name"), max_length=255, blank=True, default="")
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    rsin = models.CharField(max_length=9, null=True, blank=True)
    bsn = NLBSNField(null=True, blank=True)
    login_type = models.CharField(
        choices=LoginTypeChoices.choices,
        default=LoginTypeChoices.default,
        max_length=250,
    )
    birthday = models.DateField(null=True, blank=True)
    street = models.CharField(default="", blank=True, max_length=250)
    housenumber = models.CharField(default="", blank=True, max_length=250)
    postcode = NLZipCodeField(null=True, blank=True, max_length=250)
    city = models.CharField(default="", blank=True, max_length=250)
    deactivated_on = models.DateField(
        verbose_name=_("Deactivated on"),
        null=True,
        blank=True,
        help_text=_("This is the date the user decided to deactivate their account."),
    )
    is_prepopulated = models.BooleanField(
        _("prepopulated"),
        default=False,
        help_text=_("Indicates if fields have been prepopulated by Haal Central API."),
    )
    selected_themes = models.ManyToManyField(
        "pdc.Category",
        related_name="selected_by",
        blank=True,
    )

    objects = UserManager()
    digid_objects = DigidManager()
    eherkenning_objects = eHerkenningManager()

    USERNAME_FIELD = "email"
    _old_bsn = None

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._old_bsn = self.bsn

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def get_age(self):
        if self.birthday:
            today = date.today()
            age = (
                today.year
                - self.birthday.year
                - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
            )

            return age
        return None

    def get_address(self):
        if self.street:
            return f"{self.street} {self.housenumber}, {self.city}"
        return ""

    def deactivate(self):
        self.is_active = False
        self.deactivated_on = date.today()
        self.save()

    def get_active_contacts(self):
        return self.contacts.filter(contact_user__is_active=True)


class Contact(models.Model):
    uuid = models.UUIDField(
        verbose_name=_("UUID"),
        unique=True,
        default=uuid4,
        help_text=_("Used as a reference in the contacts api."),
    )
    first_name = models.CharField(
        verbose_name=_("First name"),
        max_length=250,
        help_text=_("The first name of the contact person."),
    )
    last_name = models.CharField(
        verbose_name=_("Last name"),
        max_length=250,
        help_text=_("The last name of the contact person"),
    )
    email = models.EmailField(
        verbose_name=_("Email address"),
        null=True,
        blank=True,
        help_text=_(
            "The email address of the contact person. This field can be left empty."
        ),
    )
    phonenumber = models.CharField(
        verbose_name=_("Phonenumber"),
        blank=True,
        default="",
        max_length=250,
        validators=[validate_phone_number],
        help_text=_(
            "The phonenumber of the contact person. This field can be left empty."
        ),
    )
    type = models.CharField(
        verbose_name=_("Type"),
        default=ContactTypeChoices.contact,
        max_length=200,
        choices=ContactTypeChoices.choices,
        help_text=_("The type of contact"),
    )
    created_on = models.DateTimeField(
        verbose_name=_("Created on"),
        auto_now_add=True,
        help_text=_(
            "This is the date the contact was created. This field is automatically set."
        ),
    )
    updated_on = models.DateTimeField(
        verbose_name=_("Updated on"),
        auto_now=True,
        help_text=_(
            "This is the date when the contact was last changed. This field is automatically set."
        ),
    )
    created_by = models.ForeignKey(
        "accounts.User",
        verbose_name=_("Created by"),
        on_delete=models.CASCADE,
        related_name="contacts",
        help_text=_("This is the person that entered the contact person."),
    )
    contact_user = models.ForeignKey(
        "accounts.User",
        verbose_name=_("Contact user"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="assigned_contacts",
        help_text=_(
            "The user from the contact, who was added based on the contact email."
        ),
    )

    class Meta:
        ordering = ("-updated_on", "-created_on")

    def __str__(self):
        return self.get_name()

    def get_name(self):
        return f"{self.first_name} {self.last_name}"


class Document(models.Model):
    uuid = models.UUIDField(
        verbose_name=_("UUID"),
        unique=True,
        default=uuid4,
        help_text=_("Used as a reference in the documents api."),
    )
    name = models.CharField(
        verbose_name=_("Name"),
        default="",
        max_length=250,
        help_text=_("The name of the document"),
    )
    file = models.FileField(
        verbose_name=_("File"),
        storage=PrivateMediaFileSystemStorage(),
        help_text="This will be the actual document.",
    )
    created_on = models.DateTimeField(
        verbose_name=_("Created on"),
        auto_now_add=True,
        help_text=_("This is the date the document was created"),
    )
    updated_on = models.DateTimeField(
        verbose_name=_("Updated on"),
        auto_now=True,
        help_text=_("This is the date when the document was last changed"),
    )
    owner = models.ForeignKey(
        "accounts.User",
        verbose_name=_("Owner"),
        on_delete=models.CASCADE,
        related_name="documents",
        help_text="This is the user that created the document.",
    )

    def __str__(self):
        return self.name


class Appointment(models.Model):
    uuid = models.UUIDField(
        verbose_name=_("UUID"),
        unique=True,
        default=uuid4,
        help_text=_("Used as a reference in the appointments api."),
    )
    name = models.CharField(
        verbose_name=_("Name"),
        default="",
        max_length=250,
        help_text=_("The name of the appointment."),
    )
    datetime = models.DateTimeField(
        verbose_name=_("Appointment time"),
        help_text=_("This is the time that the appointment is at."),
    )
    created_on = models.DateTimeField(
        verbose_name=_("Created on"),
        auto_now_add=True,
        help_text=_("This is the date the appointment was created"),
    )
    updated_on = models.DateTimeField(
        verbose_name=_("Updated on"),
        auto_now=True,
        help_text=_("This is the date when the appointment was last changed"),
    )
    created_by = models.ForeignKey(
        "accounts.User",
        verbose_name=_("Created by"),
        on_delete=models.CASCADE,
        related_name="appointments",
        help_text="The person that created the appointment.",
    )

    def __str__(self):
        return self.name


class Action(models.Model):
    uuid = models.UUIDField(
        verbose_name=_("UUID"),
        unique=True,
        default=uuid4,
        help_text=_("Used as a reference in the actions api."),
    )
    name = models.CharField(
        verbose_name=_("Name"),
        default="",
        max_length=250,
        help_text=_("The name of the action"),
    )
    status = models.CharField(
        verbose_name=_("Status"),
        default=StatusChoices.open,
        max_length=200,
        choices=StatusChoices.choices,
        help_text=_("The current status of the action"),
    )
    end_date = models.DateField(
        verbose_name=_("Action end date"),
        help_text=_("This is the date that the action should be done."),
        null=True,
    )
    created_on = models.DateTimeField(
        verbose_name=_("Created on"),
        auto_now_add=True,
        help_text=_("This is the date the action was created"),
    )
    updated_on = models.DateTimeField(
        verbose_name=_("Updated on"),
        auto_now=True,
        help_text=_("This is the date when the action was last changed"),
    )
    created_by = models.ForeignKey(
        "accounts.User",
        verbose_name=_("Created by"),
        on_delete=models.CASCADE,
        related_name="actions",
        help_text="The person that created the action.",
    )

    class Meta:
        ordering = ("end_date", "-created_on")

    def __str__(self):
        return self.name


class Message(models.Model):
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sent_messages",
        help_text=_("THe sender of the message"),
    )
    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="received_messages",
        help_text=_("The receiver of the message"),
    )
    created_on = models.DateTimeField(
        _("Created on"),
        auto_now_add=True,
        help_text=_("This is the date the message was created"),
    )
    content = models.TextField(_("Content"), help_text=_("Text content of the message"))
    seen = models.BooleanField(
        _("Seen"),
        default=False,
        help_text=_("Boolean shows if the message was seem by the receiver"),
    )

    objects = MessageQuerySet.as_manager()

    def __str__(self):
        return f"From: {self.sender}, To: {self.receiver} ({self.created_on.date()})"


class Invite(models.Model):
    inviter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sent_invites",
        help_text=_("User who created the invite"),
    )
    invitee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="received_invites",
        help_text=_("User who received the invite"),
    )
    contact = models.ForeignKey(
        Contact,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="invites",
        help_text=_("THe contact the creation of which triggered sending the invite"),
    )
    accepted = models.BooleanField(verbose_name=_("accepted"), default=False)
    key = models.CharField(verbose_name=_("key"), max_length=64, unique=True)
    created_on = models.DateTimeField(
        _("Created on"),
        auto_now_add=True,
        help_text=_("This is the date the message was created"),
    )

    def __str__(self):
        return f"For: {self.invitee} ({self.created_on.date()})"

    def save(self, **kwargs):
        if not self.pk:
            self.key = self.generate_key()

        return super().save(**kwargs)

    @staticmethod
    def generate_key():
        return get_random_string(64).lower()
