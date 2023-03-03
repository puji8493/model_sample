import os
import django

# Django設定モジュールの設定
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from authors.models import Authors, Countries, Sects, Works, Comments
from django.contrib.auth import get_user_model
from django.conf import settings


# from accounts.models import User

def get_user_comment():
    # 現在アプリケーションで使用しているUserモデルを取得
    User = get_user_model()

    # モデルマネージャーを使用して、指定されたemailアドレスに関連するUserオブジェクトを取得
    user = User.objects.get(email='arupa@gmail.com')
    print(f'id:{user.id},e-mail: {user.email}')

    user_1 = get_user_model().objects.first()
    print(f'users.objecs_firstのid:{user_1.id},e-mail: {user_1.email}')

    user_2 = get_user_model().objects.last()
    print(f'users.objecs_firstのid:{user_2.id},e-mail: {user_2.email}')

    # #ちなみにgetメソッドは値が取得できないとエラーを返す
    print(f'users.objects.get(id=3):{User.objects.get(id=3)}')
    print(f'users.objects.get(pk=2):{User.objects.get(pk=2)}')

    # allメソッドはクエリセットオブジェクトを返す
    # リストのような使い方ができる
    print('User.objects.all()でQueryDictを取得')
    print(type(User.objects.all()))
    print(User.objects.all())

    for user in User.objects.all():
        print(f'user.id:{user.id},email:{user.email},active:{user.active},staff:{user.staff},admin:{user.admin}')

    """CommentモデルとUserモデルを紐付ける"""
    # Comment オブジェクトをcreateメソッドで作る
    # objects.create() は、インスタンスを作成して保存する
    comment1 = Comments.objects.create(user=user_1, work=Works.objects.get(title="笛を吹く少年"),
                                       body='コメント1　力強い印象だった')

    print("comment1(id): ", comment1.id)  # 数値
    print("comment1(user):", comment1.user)  # ユーザーインスタンス
    print("comment1(work): ", comment1.work)  # 作品インスタンス
    print("comment1(body):", comment1.body)  # コメント本文

    # Comment オブジェクト クラスのinstanceを初期化
    # その後saveメソッドで保存する
    comment2 = Comments(user=user_2, work=Works.objects.get(title="踊り子"), body='コメント2　ドガ先輩…ヤバイ')
    comment2.save()
    print("comment2(id):", comment2.id)  # 数値
    print("comment2(user):", comment2.user)  # ユーザーインスタンス
    print("comment2(work):", comment2.work)  # 作品インスタンス
    print("comment2(body):", comment2.body)  # コメント本文

    # Comment オブジェクトを1つ更新する
    comment1.body = 'オランピアもいつかみたい。ゴーギャンやピカソも影響うけた絵書いてる'
    comment1.save()
    print("comment1(id): ", comment1.id)  # 数値
    print("comment1(user):", comment1.user)  # ユーザーインスタンス
    print("comment1(work): ", comment1.work)  # 作品インスタンス
    print("comment1(body):", comment1.body)  # コメント本文

    # Comment1オブジェクトに関連付けられた works オブジェクトを変更する
    # 笛を吹く少年 から、Workクラスのtitleが睡蓮のオブジェクトを取得して、comment1.worksに代入する
    work4 = Works.objects.get(title="睡蓮")
    comment1.work = work4
    comment1.save()
    print(comment1.id, comment1.user, comment1.work.title, comment1.body)  # 数値, ユーザーインスタンス, エントリインスタンス, コメント本文


def select_authors():
    authors = Authors.objects.all()
    for author in authors:
        print(f'作者:{author.name},享年:{author.age},国:{author.countries},ヤバイ度:{author.fly_level}')


def select_works():
    works = Works.objects.all()
    for work in works:
        print(f'作品:{work.title},カテゴリ:{work.sect.name},作者:{work.authors.name}')


def get_type():
    """AUTH_USER_MODELはStringクラス"""
    print(settings.AUTH_USER_MODEL)
    print(type(settings.AUTH_USER_MODEL))

    """get_user_model()はUserクラス自体を返す"""
    user = get_user_model()
    print(user)
    print(type(user))


def create_author():
    """Authorモデルを作成する"""

    sect_obj = Sects.objects.get(name='impressionism')
    # author = Authors.objects.get_or_create(name='マネ', age=51, country=Countries.objects.get(name='france'),
    #                                        fly_level=3, )
    author = Authors.objects.get(name='マネ')
    author.sect.add(sect_obj)

    print(Sects.objects.all())
    # sect_obj = Sects.objects.filter(name__in=['fauvism', 'cubism'])
    # print(sect_obj)
    # # name__inはリストを渡す
    # author = Authors.objects.create(name='ジュルジュ・ブラック', age=81, country=Countries.objects.get(name='france'), fly_level=3)
    # # sect_objの戻り値　*可変長引数
    # author.sect.set(sect_obj)
    # print(author.sect.all())

    # author = Authors.objects.get_or_create(name='ジョアン・ミロ', age=90, countries=Countries.objects.get(name='spain'), fly_level=3)
    # author.sects.add(Sects.objects.get(name='surrealism',name='realism'))
    # print(author.sect)


def create_sect():
    sect = Sects.objects.create(name='fauvism')


def create_works():
    # 初期化
    # Authors.objects.get(name='ジョアン・ミロ').delete()
    # Authors.objects.get(name='ジュルジュ・ブラック').delete()

    # sectのオブジェクトを取得
    sect_obj1 = Sects.objects.get(name='realism')
    sect_obj2 = Sects.objects.get(name='surrealism')

    # set()メソッドの引数はリスト等の iterable
    # 予めfilter__inでリストで絞り込み格納
    sect_obj3 = Sects.objects.filter(name__in=['fauvism', 'cubisme'])

    # add() メソッドは、すでに設定されているタグに、新しいタグを追加する
    # ただし、すでに設定されているのと同じタグを指定しても無視される
    # entry2.tags.add(tag4, tag5, )
    # ManyToManyField の追加は、本体がデータベースに保存されるまではできない

    auth1, created = Authors.objects.get_or_create(name='ジョアン・ミロ', age=90, country=Countries.objects.get(name='spain'),
                                                   fly_level=3)
    auth1.sect.add(sect_obj1, sect_obj2)

    auth2 = Authors.objects.create(name='ジュルジュ・ブラック', age=81, country=Countries.objects.get(name='france'), fly_level=3)
    auth2.sect.set(sect_obj3)


    Works.objects.get_or_create(title='農園', sect=Sects.objects.get(name='realism'),
                                author=Authors.objects.get(name='ジョアン・ミロ'), )
    Works.objects.get_or_create(title='カタルーニャの風景', sect=Sects.objects.get(name='surrealism'),
                                author=Authors.objects.get(name='ジョアン・ミロ'), )

    Works.objects.get_or_create(title='木のうしろの家', sect=Sects.objects.get(name='fauvism'),
                                author=Authors.objects.get(name='ジュルジュ・ブラック'), )
    Works.objects.get_or_create(title='ギターをもつ女', sect=Sects.objects.get(name='cubisme'),
                                author=Authors.objects.get(name='ジュルジュ・ブラック'), )

    # 故に、以下はNG
    # entry3 = Entry(user=user, title='タイトル1', body='本文1', tags=[tag1, tag2])
    # auth1 = Authors.objects.create(name='ジョアン・ミロ', age=90, country=Countries.objects.get(name='spain'), fly_level=3,sect=sect_obj1)

    # 以下はOK(auth2 が保存されたあとだから)
    auth2 = Authors(name='ジュルジュ・ブラック', age=81, country=Countries.objects.get(name='france'), fly_level=3)
    auth2.save()
    auth2.sect.set(sect_obj3)
    print(auth2.name, auth2.sect.all(), sep=":")


def create_manytomany_sect():
    """
    ManytoManyFieldの設定のモデルを作成

    ManyToMany フィールドのメソッドは、以下の4つ
    add, set, remove, clear
    いずれも、実行直後に即座にデータベースは更新される。なので、 save() は不要。

    add() メソッドは、すでに設定されているタグに、新しいタグを追加する
    ただし、すでに設定されているのと同じタグを指定しても無視される
    以下では、tag3, tag4 が設定されていたところに、さらに、tag4, tag5 を追加しようとする
    ただし、tag4 はすでに設定されているので、 tag3, tag4, tag5 となる
    """

    sects = Sects.objects.all()
    for sect in sects:
        records = sect.authors_set.all()
        print(f'{sect.name}に紐づいた作者は{records}')

    # １対多い
    for sect in sects:
        records = sect.works_set.all()
        print(f'{sect.name}に紐づいた作品は{records}')

    auth = Authors.objects.all()
    for au in auth:
        # １対多
        records = au.works_set.all()
        # 多から１
        sect = au.sect.all()
        print(f'{au.name}は{records}の作品をもつ')
        print(f'{au.name}は{sect}の作風をもつ')


    # 多対多を紐づけて取得する場合は、setを使う

    # sects = Sects.objects.all()
    #
    # for sect in sects:
    #     # 各派閥に対して、authors_set という空のセットを作成
    #     authors_set = set()
    #     print(authors_set,'oi')
    #     # その派閥に所属する作者を取得
    #     authors = sect.authors_set.all()
    #     print(authors)
    #     for author in authors:
    #         authors_set.add(author.name)
    #     print(f'{sect.name}: {authors_set}')


if __name__ == '__main__':
    # select_authors()
    # select_works()
    # get_type()
    # create_author()
    # create_works()
    # get_user_comment()
    # create_sect()
    create_manytomany_sect()
