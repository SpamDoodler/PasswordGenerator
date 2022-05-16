from src import generator

generator = generator.generator()
generator.secLevel.manuelSecurity(12, 14, True)
generator.create_password()
print(generator.length)
generator.save()



