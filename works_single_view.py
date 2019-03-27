# -*- coding: utf-8 -*-
from core.infrastructure.api.drf.works_single_view.works_single_view.repositories import DjangoWorkRepository
from core.infrastructure.cli.get_works import GetWorks
from core.infrastructure.cli.load_works_from_csv import LoadWorksFromCSV
import click
import os
import django
from core.infrastructure.api.drf.works_single_view import settings
#  you have to set the correct path to you settings module

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "core.infrastructure.api.drf.works_single_view.settings")

settings.INSTALLED_APPS.remove('works_single_view.works_single_view')
settings.INSTALLED_APPS += ('core',)

django.setup()


@click.command()
@click.option('--cmd', help='The command to be executed')
@click.option('--csv', help='The csv path containing works')
def launcher(cmd: str, csv: str):
    workRepository = DjangoWorkRepository()

    if cmd == 'load_works_from_csv':
        print('Loading works from csv...')

        command = LoadWorksFromCSV(csv, workRepository)
        command.execute()

        print(str(len(workRepository.all())) + ' work(s) loaded!')

    if cmd == 'get_works':
        print('Getting works...')
        query = GetWorks(workRepository)
        works = query.execute()

        for work in works:
            print('-------------------')
            print('-------------------')
            print('Id: ' + work.id().value())
            print('Iswc: ' + work.iswc().value())
            print('Title: ' + work.title().value())
            print('Source: ' + work.source().value())

            contributors = []
            for contributor in work.contributors():
                contributors.append(contributor.name())

            print('Contributors: ' + "|".join(contributors))
            print('')


if __name__ == '__main__':
    launcher()
