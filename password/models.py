import string
import random
from django.db import models
('~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/', 'A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
('~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/', 'A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')


# Create your models here.
def create_random_password():
    length = random.randint(8,30)
    special_characters = ('~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<',
                          '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/')
    upper_case=tuple(string.ascii_uppercase)
    lower_case=tuple(string.ascii_lowercase)
    letters=tuple(special_characters+upper_case+lower_case)
    password=''
    for _ in range(length):
        password+=random.choice(letters)
    return password


class Password(models.Model):
    website = models.CharField(max_length=90, null=True)
    username = models.CharField(max_length=90)
    password = models.CharField(max_length=90, default=create_random_password)
    note = models.TextField(null=True)
    url=models.URLField(null=True)
