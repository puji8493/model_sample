import django
import os

# Django設定モジュールの設定
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from authors.models import Authors, Countries, Sects, Works


def delete_countries():
    """
    最初の実行時に、 Countriesモデルのレコードをすべて削除。
    それから、 Countiesクラスのインスタンスを追加し、更新していく。
    """
    Countries.objects.all().delete()

def insert_countries():
    """
    レコードの挿入
    instanceを生成して保存
    既存の要素が登録されている場合はエラーを発生させる
    """
    country_1 = Countries(name='japan')
    country_1.save()

    country_2 = Countries.objects.create(name='austria')

    """
    get_or_createメソッドを使用して保存
    既存の要素が登録されている場合は保存せず、新規のみ登録する
    Countriesに”janan”が登録されている状態get_or_createを実行すると、エラーを起こさない
    """

    countries_list = ['japan', 'netherlands', 'france', 'england', 'spain']

    for i in countries_list:
        # createdにはデータがあった場合は、”True”が入る
        country, created = Countries.objects.get_or_create(name=i)
        print(f'name:{country.name}, get_or_createの結果:{created}')

    countries = Countries.objects.all()
    print(f'Countriesクラスのレコード数:{countries.count()}')

    for i,country in enumerate(countries,start=1):
        print(f'no:{i}, name:{country.name}')

if __name__ == '__main__':
    delete_countries()  # 最初の実行時に、 Countriesのレコードをすべて削除
    insert_countries()  # レコードの挿入
