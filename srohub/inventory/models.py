from django.db import models
from django.conf import settings

from simple_history.models import HistoricalRecords

from .asset_code import validate_asset_code, generate_asset_code


class AssetManufacturer(models.Model):
    """The manufacturer of an asset."""

    name = models.CharField(max_length=30)
    notes = models.TextField(blank=True)
    history = HistoricalRecords()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class AssetModel(models.Model):
    """The model of an asset."""

    name = models.CharField(max_length=30)
    is_container = models.BooleanField(default=False, verbose_name="Can contain assets")
    asset_manufacturer = models.ForeignKey(AssetManufacturer, on_delete=models.PROTECT)
    history = HistoricalRecords()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def display_name(self) -> str:
        if self.asset_manufacturer.name == settings.INVENTORY_ORG:
            return self.name
        return f"{self.asset_manufacturer.name} {self.name}"

    def __str__(self) -> str:
        return self.display_name


class Asset(models.Model):
    """An individual instance of a assetmodel."""

    class Condition(models.TextChoices):
        """The condition of an item."""
        UNKNOWN = 'U'
        BROKEN = 'B'
        NEEDS_ASSEMBLY = 'A'
        NEEDS_REPAIR = 'R'
        WORKING = 'W'

    asset_code = models.CharField(
        max_length=11,
        unique=True,
        validators=[validate_asset_code],
        default=generate_asset_code,
    )
    name = models.CharField(max_length=30, null=True, blank=True)
    location = models.ForeignKey('Asset', on_delete=models.PROTECT)
    asset_model = models.ForeignKey(AssetModel, on_delete=models.PROTECT)
    condition = models.CharField(
        max_length=2,
        choices=Condition.choices,
        default=Condition.UNKNOWN,
    )
    history = HistoricalRecords()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def display_name(self) -> str:
        if self.name is None or len(self.name) == 0:
            return self.asset_model.display_name
        else:
            return self.name

    def __str__(self) -> str:
        return f"{self.display_name} ({self.asset_code})"
