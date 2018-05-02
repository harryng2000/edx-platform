# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-11 19:15
from __future__ import unicode_literals

from itertools import chain
from django.db import migrations


def populate_id_verification_aggregate(apps, schema_editor):
    """
    The code from this migration was removed because it caused a spike in database errors
    when it was run in the edX production environment. More details can be found here:
    https://openedx.atlassian.net/browse/ENT-969
    """
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('verify_student', '0007_idverificationaggregate'),
    ]

    operations = [
        migrations.RunPython(populate_id_verification_aggregate, reverse_code=migrations.RunPython.noop),
    ]
