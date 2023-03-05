import csv
import os
import django
import pathlib

# Django設定モジュールの設定
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from authors.models import Authors, Countries, Sects, Works, Comments
from django.contrib.auth import get_user_model
from django.conf import settings

CSV_PATH = pathlib.Path(__file__).resolve().parent / 'utlis_comment.csv'
CSV_EXPORT_PATH = pathlib.Path(__file__).resolve().parent / 'utlis_import.csv'

def update_comment():

    with CSV_PATH.open(mode='r', encoding='utf-8', newline='') as f:
        readr = csv.DictReader(f)
        for row in readr:
            Comments.objects.create(
                user=get_user_model().objects.get(id=row['user_id']),
                work=Works.objects.get(title=row['work']),
                body=row['body']
            )
    print(Comments.objects.all())


def export_csv():

    with CSV_EXPORT_PATH.open(mode='w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        # ヘッダー行を書き込み
        writer.writerow(['id', 'user', 'work', 'body'])

        # Commentsの全インスタンスを取得して、1行ずつCSVに書き込み
        for comment in Comments.objects.all():
            writer.writerow([comment.id, comment.user, comment.work, comment.body])


if __name__ == '__main__':
    # update_comment()
    export_csv()