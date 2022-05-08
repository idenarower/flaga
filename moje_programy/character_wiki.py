import wikipedia as wiki
wiki.set_lang("pl")

def character( name):
    content = wiki.summary(name, sentences=6)
    return content