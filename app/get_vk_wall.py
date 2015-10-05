import vk
from app.models import Recipe, db
session = vk.Session()
api = vk.API(session)
posts = api.wall.get(domain="yummy_yummyboxx", count=5)

i = 1
for post in posts:
    title = str(posts[i]['text']).partition('<br>')[0]
    body = posts[i]['text']
    recipe = Recipe(title=title,body=body)
    registered_recipes = Recipe.query.filter_by(title = title,body=body).first()
    if recipe != registered_recipes:
        db.session.add(recipe)
        db.session.commit()
    i += 1
