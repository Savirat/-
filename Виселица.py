_sonfather = {"Дмитрий":"Олегович","Олег":"Владимирович","Эдуард":"Анатольевич"}
_inpSon = ""
while _inpSon != "":
    _inpSon = input ("Введите имя. Для удаления нажмите 0")
    if _inpSon in _sonfather:
        print (_sonfather[_inpSon])
    elif _inpSon == 0:
        inpDel 
    else:
        print ("Такого имени нет. Добавить отца? Ввод для выхода")
        _father = input ()
        if _father != "":
            _sonfather [_inpSon] = _father
        continue



































# программа перераспределения навыков у персонажа
#import random
#x=0
#_skills = 30
#_inpskills = None
#_chars = {"Ловкость":0,"Сила":0,"Здоровье":0,"Мудрость":0}
#_char = ""
#_inpChar = None

#while _inpChar != 0:
#    print ("Характеристика:")
#    x=0
#    for key in _chars:
#        x+=1
#        print (str(x)+f": {key}: {_chars[key]}")
#    print (f"У вас еть {_skills} очков на распределение.", end= " ")
#    print ("Наберите номер характеристики, которую хотите изменить.")
#    print ("0 для выхода.")
#    _inpChar = int(input())
#    print ()

#    if _inpChar==1:
#        _char="Ловкость"

#    elif _inpChar==2:
#        _char="Сила"

#    elif _inpChar==3:
#        _char="Здоровье"

#    elif _inpChar==4:
#        _char="Мудрость"

#    else: 
#        print ("Неверный ввод")
#        continue

#    print ("У вас отсталось очков:", str(_skills))
#    _intCountSkill = int(input ("Сколько очков хотите потратить на этот навык? "))
#    _skills += _chars[_char]
#    _chars[_char] = 0
#    if _intCountSkill <= _skills:
#        _chars[_char] = _intCountSkill
#        _skills -= _intCountSkill
#    else:
#        print ("Неверный ввод")
#    continue
        