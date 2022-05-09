from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_quill.fields import QuillField


class SiteProperties:
    site = models.OneToOneField(
        Site, verbose_name=_("details"), on_delete=models.CASCADE
    )


class Image(models.Model):
    site = models.ForeignKey(
        Site,
        verbose_name=_("Page site"),
        on_delete=models.CASCADE,
        related_name="images",
    )
    name = models.CharField(_("Image name"), max_length=50)
    image = models.ImageField(
        _("Image file"),
        upload_to="content/",
        height_field=None,
        width_field=None,
        max_length=None,
    )

    def __str__(self) -> str:
        return self.name


class Document(models.Model):
    site = models.ForeignKey(
        Site,
        verbose_name=_("Page site"),
        on_delete=models.CASCADE,
        related_name="documents",
    )
    name = models.CharField(_("Document name"), max_length=50)
    file = models.FileField(_("Document file"), upload_to=None, max_length=100)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    site = models.ForeignKey(
        Site, verbose_name=_("Category site"), on_delete=models.CASCADE
    )
    title = models.CharField(_("Category title"), max_length=50)
    slug = models.SlugField(_("Category Slug"))
    in_navbar = models.BooleanField(_("Category appears in navbar"))

    def __str__(self) -> str:
        return self.title


class Page(models.Model):
    TYPES = [("1", "standard"), ("2", "galary")]

    category = models.ForeignKey(
        Category,
        verbose_name=_("Site category"),
        on_delete=models.CASCADE,
        related_name="pages",
        blank=True,
        null=True,
    )
    title = models.CharField(_("Page title"), max_length=50)
    slug = models.SlugField(_("Page Slug"))
    content = QuillField(_("Quill's Richt Text"))  # Quill
    in_navbar = models.BooleanField(_("Site appears in navbar"))
    type = models.CharField(_("Page Types"), max_length=50, choices=TYPES)
    images = models.ManyToManyField(
        Image,
        verbose_name=_("Pages images"),
        related_name="pages",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        _("Page created at"), auto_now=True, auto_now_add=False
    )
    updated_at = models.DateTimeField(
        _("Page updated at"), auto_now=True, auto_now_add=False
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="pages",
        verbose_name=_("Page author"),
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return self.title
