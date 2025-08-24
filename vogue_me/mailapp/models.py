import re
import secrets
from datetime import timedelta

from cryptography.fernet import Fernet
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class LoginAuth(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    auth_code   = models.CharField(max_length=10)
    cipher_key  = models.CharField(max_length=44, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    expires_at  = models.DateTimeField()
    authed_at   = models.DateTimeField(null=True)

    def __init__(self):
        super().__init__()

        token = secrets.token_urlsafe(16)
        token = re.sub(r"[^a-zA-Z\d]", "", token)[:8].upper()
        self.auth_code = token

        # 키 생성 (안전하게 보관해야 함)
        self.cipher_key = Fernet.generate_key()

    def get_encrypted_code(self):
        f = Fernet(self.cipher_key)

        # 데이터 암호화
        data_to_encrypt = self.auth_code.encode("utf-8")
        return f.encrypt(data_to_encrypt)

    def verify_code(self, encrypted_code):
        f = Fernet(self.cipher_key)

        # 데이터 복호화
        decrypted_data = f.decrypt(encrypted_code)
        return decrypted_data == self.auth_code


    def save(self, *args, **kwargs):
        # if not self.auth_code:
        #     token = secrets.token_urlsafe(16)
        #     token = re.sub(r"[^a-zA-Z\d]", "", token)[:8].upper()

        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(minutes=10)
        super().save(*args, **kwargs)