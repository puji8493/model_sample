import os
import django
from django.conf import settings

# Django設定モジュールの設定
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from authors.models import Authors, Countries, Sects, Works

# ここからDjangoのORMを使用した処理を記述する
country_1 = Countries.objects.create(name='Netherlands')
country_2 = Countries.objects.create(name='France')
country_3 = Countries.objects.create(name='England')
country_4 = Countries.objects.create(name='spain')

sect_1 = Sects.objects.create(name='impressionism')
sect_2 = Sects.objects.create(name='neoclassicism')
sect_3 = Sects.objects.create(name='cubisme')
sect_4 = Sects.objects.create(name='naturalistic')

author_1 = Authors.objects.create(name='ピカソ', age=91, fly_level=5,countries=country_4)
author_1.sects.add(sect_3)

author_2 = Authors.objects.create(name='ドガ', age=83, fly_level=5,countries=country_2)
author_2.sects.add(Sects.objects.get(name='naturalistic'))

author_3 = Authors.objects.create(name='モネ', age=83, fly_level=3,countries=country_2)
author_2.sects.add(Sects.objects.get(name='naturalistic'))

works_1 = Works.objects.create(
    title='ゲルニカ',
    sect=Sects.objects.get(name="cubisme"),
    authors=Authors.objects.get(name="ピカソ")
)

works_2 = Works.objects.create(
    title='海辺を走る二人',
    sect=Sects.objects.get(name="neoclassicism"),
    authors=Authors.objects.get(name="ピカソ")
)

works_3 = Works.objects.create(
    title='踊り子',
    sect=Sects.objects.get(name="impressionism"),
    authors=Authors.objects.get(name="ドガ")
)

try:
    sect = Sects.objects.get(name="impressionism")
except Sects.DoesNotExist:
    sect = None

if sect:
    works_4 = Works.objects.create(
        title='睡蓮',
        sect=sect,
        authors=Authors.objects.get(name="モネ")
    )
else:
    print("Sects.DoesNotExist")


# 処理が完了したら終了
django.db.connections.close_all()
