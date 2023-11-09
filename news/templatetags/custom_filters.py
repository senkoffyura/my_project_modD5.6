from django import template


register = template.Library()

unacceptable_words = ["текст",
                      "проверка",
]

@register.filter()
def censor(value):
    text = str(value)
    for i in unacceptable_words:
        iCaps = i.capitalize()
        replCaps = (i.capitalize()[0]).ljust(len(i),"*")
        repl = (i[0].ljust(len(i), "*"))
        text = text.replace(i,repl)
        text = text.replace(iCaps, replCaps)

    return text