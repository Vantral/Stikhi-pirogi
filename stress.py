from russtress import Accent
accent = Accent()
text = """а любишь ролевые игры
тебе кого изобразить
изобрази мне человека
который только что ушел

любимый взял меня за локоть
подвёл к окну и показал
всё то чего я не увижу
вовеки если не заткнусь
"""
accented_text = accent.put_stress(text)
print(accented_text)