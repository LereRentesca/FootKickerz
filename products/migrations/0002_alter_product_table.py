# Generated by Django 4.2.3 on 2023-08-01 01:41

from django.db import migrations

def populate_sport(apps, schemaeditor):
    entries = {
        "Running":"The action of rapidly propelling yourself forward on foot.",
        "Training":"Is teaching, or developing in oneself or others, any skills and knowledge or fitness that relate to specific useful competencies.",
        "Lifestyle":"The way in which a person or group lives.",
        "Basketball":"It is a team sport that involves two teams of five active players each trying to score points against one another by throwing a ball.",
        "Trail":"Is an unpaved lane or a small paved road not intended for usage by motorized vehicles, usually passing through a natural area.",
        "Workout & Gym":"A session of vigorous physical exercise or training.",
        "Sandals & Slides":"A light shoe with either an openwork upper or straps attaching the sole to the foot.",
        "Soccer":"It is a team sport, involving 11 players on each side who use their legs, head and torso to pass a ball and score goals.",
    }
    Sport = apps.get_model("products","Sport")
    for key, value in entries.items():
        sport = Sport(name=key, description=value)
        sport.save()

def populate_brand(apps, schemaeditor):
    entries = {
        "Jordan":"Air Jordan is a line of basketball shoes produced by Nike, Inc. Related apparel and accessories are marketed under Jordan Brand.",
        "Nike":"The world's largest athletic apparel company, Nike is best known for its footwear, apparel, and equipment. Founded in 1964 as Blue Ribbon Sports, the company became Nike in 1971 after the Greek goddess of victory.",
        "Adidas":"Is German manufacturer of athletic shoes and apparel and sporting goods. In the early 21st century it was the largest sportswear manufacturer in Europe and the second largest (after Nike) in the world.",
        "Puma":"Is a German multinational corporation that designs and manufactures athletic and casual footwear, apparel and accessories, headquartered in Herzogenaurach, Bavaria, Germany.",
        "Under Armour":"Is a developer, marketer, and distributor of apparel, footwear, and related accessories. The company's product portfolio comprises sweat shirts, socks, football gloves, shoes, sandals, performance bags, baseball batting gloves, and other related products.",
    }
    Brand = apps.get_model("products","Brand")
    for key, value in entries.items():
        brand = Brand(name=key, description=value)
        brand.save()


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='product',
            table='sneakersapp.product',
        ),
        migrations.RunPython(populate_sport),
        migrations.RunPython(populate_brand)
    ]
