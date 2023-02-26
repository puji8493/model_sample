import os
import django
from django.conf import settings

# Django設定モジュールの設定
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

# ここからDjangoのORMを使用した処理を記述する
from authors.models import Authors, Countries, Sects,Works

country_1 = Countries.objects.get_or_create(name='Netherlands')
country_2 = Countries.objects.get_or_create(name='France')
country_3 = Countries.objects.get_or_create(name='England')
country_4 = Countries.objects.get_or_create(name='spain')

sect_1 = Sects.objects.get_or_create(name='Impressionism')
sect_2 = Sects.objects.get_or_create(name='naturalistic')
sect_3 = Sects.objects.get_or_create(name='cubisme')

author_1 = Authors.objects.create(name='ピカソ', age=91, fly_level=5)
author_1.countries.set([country_4[0]])
author_1.sects.set([sect_3[0]])

author_2 = Authors.objects.create(name='ドガ', age=83, fly_level=5)
author_2.countries.set([country_2[0]])
author_2.sects.set([sect_1[0]])

author_3 = Authors.objects.create(name='モネ', age=86, fly_level=3)
author_3.countries.set([country_2[0]])
author_3.sects.set([sect_1[0]])


works_1 = Works.objects.get_or_create(title='ゲルニカ')
works_1[0].authors.add(author_1)

works_2 = Works.objects.get_or_create(title='踊り子')
works_2[0].authors.add(author_2)

# 処理が完了したら終了
django.db.connections.close_all()


# django.core.exceptions.FieldError: Cannot resolve keyword 'author' into field. Choices are: authors, id, title
# works_1 = Works.objects.get_or_create(title='ゲルニカ', author=author_1)
# works_2 = Works.objects.get_or_create(title='踊り子', author=author_2)


# TypeError: Direct assignment to the forward side of a many-to-many set is prohibited. Use countries.set() instead.
# author_1 = Authors.objects.create(name='ピカソ', age=91, countries=country_4, sects=sect_3,fly_level=5)
# author_2 = Authors.objects.create(name='ドガ', age=83, countries=country_2, sects=sect_1,fly_level=5)
# author_3 = Authors.objects.create(name='モネ', age=86, countries=country_2, sects=sect_1,fly_level=3)
