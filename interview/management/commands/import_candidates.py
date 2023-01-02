import csv

from interview.models import Candidate
from django.core.management import BaseCommand

# python manage.py import_candidates --path file.csv


class Command(BaseCommand):
    help = 'Import the candidate information into the system from a csv file'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **options):
        path = options['path']
        with open(path, 'rt') as file:
            reader = csv.reader(file, dialect='excel', delimiter=',')
            for row in reader:
                Candidate.objects.create(
                    username=row[0],
                    city=row[1],
                    phone=row[2],
                    major=row[3],
                    degree=row[4],
                    email=row[5],
                    doctor_school=row[6],
                    master_school=row[7],
                    bachelor_school=row[8]
                )
