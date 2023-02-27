import os
import django

# Django設定モジュールの設定
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from authors.models import Authors, Countries, Sects, Works


def select_authors():
    authors = Authors.objects.all()
    for author in authors:
        print(f'作者:{author.name},享年:{author.age},国:{author.countries},ヤバイ度:{author.fly_level}')

def select_works():
    works = Works.objects.all()
    for work in works:
        print(f'作品:{work.title},カテゴリ:{work.sect.name},作者:{work.authors.name}')

if __name__ == '__main__':
    select_authors()
    select_works()
