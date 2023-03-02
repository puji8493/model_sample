from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

"""
ユーザーモデルクラスの属するappを作成し、設定する
モデルクラスを作成する
モデルクラスを操作するモデルマネジャークラスを作成する
モデルクラスとモデルマネジャーを紐付ける
データベースへ作成したモデルを書き込む
Djangoのユーザー認証で使用することを宣言する
"""

class UserManager(BaseUserManager):
    """ユーザーモデルをemailで管理するためのモデルマネジャークラス"""

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Eメールアドレス',
        max_length=255,
        unique=True,
    )
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    """モデルクラスとモデルマネジャーを紐付ける"""
    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.admin

    def has_module_perms(self, app_label):
        return self.admin

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

