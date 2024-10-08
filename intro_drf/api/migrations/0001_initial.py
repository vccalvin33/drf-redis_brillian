# Generated by Django 4.2.7 on 2024-08-21 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Institutions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("symbol", models.TextField(blank=True, null=True)),
                ("updated_on", models.TextField(blank=True, null=True)),
                ("net_transaction", models.IntegerField(blank=True, null=True)),
                ("top_sellers", models.JSONField(blank=True, null=True)),
                ("date", models.TextField(blank=True, null=True)),
                ("top_buyers", models.JSONField(blank=True, null=True)),
            ],
            options={"db_table": "institutions", "managed": False,},
        ),
        migrations.CreateModel(
            name="Metadata",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sector", models.TextField(blank=True, null=True)),
                ("sub_sector", models.TextField(blank=True, null=True)),
                ("slug", models.TextField(blank=True, null=True)),
                ("sub_sector_id", models.TextField(blank=True, null=True)),
            ],
            options={"db_table": "metadata", "managed": False,},
        ),
        migrations.CreateModel(
            name="Reports",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sub_sector", models.TextField(blank=True, null=True)),
                ("total_companies", models.TextField(blank=True, null=True)),
                ("total_market_cap", models.TextField(blank=True, null=True)),
                ("avg_market_cap", models.TextField(blank=True, null=True)),
                ("filtered_median_pe", models.TextField(blank=True, null=True)),
                ("filtered_weighted_avg_pe", models.TextField(blank=True, null=True)),
                ("min_company_pe", models.TextField(blank=True, null=True)),
                ("max_company_pe", models.TextField(blank=True, null=True)),
                ("avg_yoy_q_earnings_growth", models.TextField(blank=True, null=True)),
                ("avg_yoy_q_revenue_growth", models.TextField(blank=True, null=True)),
                ("weighted_max_drawdown", models.TextField(blank=True, null=True)),
                ("weighted_rsd_close", models.TextField(blank=True, null=True)),
                ("median_yield_ttm", models.TextField(blank=True, null=True)),
            ],
            options={"db_table": "reports", "managed": False,},
        ),
    ]
