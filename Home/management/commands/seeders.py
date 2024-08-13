from django_seeding import seeders
from django_seeding.seeder_registry import SeederRegistry

from Home.models import Marca

#
# @SeederRegistry.register
# class MarcaSeeder(seeders.Seeder):
#     id = 'CustomSeeder'
#     priopity = 8
#
#     def seed(self):
#         print(self.id)
#         post1 = Marca.objects.create(marca='post 1')
#         post2 = Marca.objects.create(marca='post 2')
#
#         # comment1 = Comment.objects.create(post=post1, content='comment1')
#         # comment2 = Comment.objects.create(post=post1, content='comment2')
#         # comment3 = Comment.objects.create(post=post2, content='comment3')
#         # comment4 = Comment.objects.create(post=post2, content='comment4')
#

print("entro")

@SeederRegistry.register
class MarcaSeeder(seeders.JSONFileModelSeeder):
    id = 'MarcaSeeder'
    priopity = 1
    model = Marca
    json_file_path = 'RestFullAPISIAC/fixtures/data.json'
