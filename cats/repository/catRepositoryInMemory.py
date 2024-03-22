cats = list()


def addCat(cat):
    cats.append(cat)


def findCatByName(name):
    for cat in cats:
        if cat.name == name:
            return cat
