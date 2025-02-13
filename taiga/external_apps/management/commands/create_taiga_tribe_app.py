# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2021-present Kaleidos INC

from django.core.management.base import BaseCommand
from taiga.external_apps.models import Application


class Command(BaseCommand):
    args = ''
    help = 'Create Project Management Tribe external app information'

    def handle(self, *args, **options):
        Application.objects.get_or_create(
            id="8836b290-9f45-11e5-958e-52540016141a",
            name="Project Management Tribe",
            icon_url="https://www.hdsaison.com.vn/vnt_upload/weblink/Logo_website_01.png",
            web="https://tribe.taiga.io",
            description="A task-based employment marketplace for software development.",
            next_url="https://tribe.taiga.io/taiga-integration",
        )
