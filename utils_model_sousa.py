import os
import django

# Django設定モジュールの設定
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from authors.models import Authors, Countries, Sects, Works,Comment
from django.contrib.auth import get_user_model
#from accounts.models import User

def get_user():

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

    #allメソッドはクエリセットオブジェクトを返す
    #リストのような使い方ができる
    print('User.objects.all()でQueryDictを取得')
    print(type(User.objects.all()))
    print(User.objects.all())

    for user in User.objects.all():
        print(f'user.id:{user.id},email:{user.email},active:{user.active},staff:{user.staff},admin:{user.admin}')

    """CommentモデルとUserモデルを紐付ける"""
    # Comment オブジェクトをcreateメソッドで作る
    comment1 = Comment.objects.create(user=user_1, works=Works.objects.get(title="笛を吹く少年"), body='コメント1　力強い印象だった')
    print("comment1(id): ",comment1.id)  #　数値
    print("comment1(user):", comment1.user)# ユーザーインスタンス
    print("comment1(works): ", comment1.works)# 作品インスタンス
    print("comment1(body):", comment1.body) # コメント本文

    # Comment オブジェクトをinstanceを生成してsaveメソッドで作る
    comment2 = Comment(user=user_2, works=Works.objects.get(title="踊り子"), body='コメント2　ドガ先輩…ヤバイ')
    comment2.save()
    print("comment2(id):",comment2.id)  # 数値
    print("comment2(user):", comment2.user)# ユーザーインスタンス
    print("comment2(works):", comment2.works)# 作品インスタンス
    print("comment2(body):", comment2.body) # コメント本文

    # Comment オブジェクトを1つ更新する
    comment1.body = 'オランピアもいつかみたい。ゴーギャンやピカソも影響うけた絵書いてる'
    comment1.save()
    print("comment1(id): ",comment1.id)  #　数値
    print("comment1(user):", comment1.user)# ユーザーインスタンス
    print("comment1(works): ", comment1.works)# 作品インスタンス
    print("comment1(body):", comment1.body) # コメント本文


    # Comment1オブジェクトに関連付けられた works オブジェクトを変更する
    # 笛を吹く少年 から、Workクラスのtitleが睡蓮のオブジェクトを取得して、comment1.worksに代入する
    works4 = Works.objects.get(title="睡蓮")
    comment1.works = works4
    comment1.save()
    print(comment1.id, comment1.user, comment1.works.title, comment1.body)  # 数値, ユーザーインスタンス, エントリインスタンス, コメント本文

def select_authors():
    authors = Authors.objects.all()
    for author in authors:
        print(f'作者:{author.name},享年:{author.age},国:{author.countries},ヤバイ度:{author.fly_level}')


def select_works():
    works = Works.objects.all()
    for work in works:
        print(f'作品:{work.title},カテゴリ:{work.sect.name},作者:{work.authors.name}')



if __name__ == '__main__':
    # select_authors()
    # select_works()
    get_user()