# Generated by Django 3.0.4 on 2020-03-05 14:34

import django.db.models.deletion
import inventory.asset_code
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AssetManufacturer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("notes", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="AssetModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                (
                    "is_container",
                    models.BooleanField(
                        default=False, verbose_name="Can contain assets"
                    ),
                ),
                ("notes", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "asset_manufacturer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="inventory.AssetManufacturer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Asset",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "asset_code",
                    models.CharField(
                        default=inventory.asset_code.generate_asset_code,
                        max_length=11,
                        unique=True,
                        validators=[inventory.asset_code.validate_asset_code],
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=30, null=True)),
                (
                    "condition",
                    models.CharField(
                        choices=[
                            ("U", "Unknown"),
                            ("B", "Broken"),
                            ("A", "Needs Assembly"),
                            ("R", "Needs Repair"),
                            ("W", "Working"),
                        ],
                        default="U",
                        max_length=2,
                    ),
                ),
                ("notes", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "asset_model",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="inventory.AssetModel",
                    ),
                ),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="inventory.Asset",
                    ),
                ),
            ],
        ),
    ]
