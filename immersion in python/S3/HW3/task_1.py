"""
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.
"""

text = """Переезд в Гамбург. Предположительно второй дом Шопенгауэров в Гамбурге В начале 1793 года между Российской 
империей и Пруссией был подписан договор, вошедший в историю как Второй раздел Речи Посполитой. Согласно этому 
договору, Данциг должен был перейти во владение Пруссии. Шопенгауэр, как и другие крупные данцигские либеральные 
торговцы, был категорическим противником установления прусского контроля над его родным городом. Это были не эмоции, 
а трезвый расчёт — Шопенгауэр считал, что в условиях жёсткой иерархии военизированного прусского государства 
останется меньше возможностей для прибыльной торговли. За несколько часов до вступления в город прусских войск Генрих 
Флорис с семьёй покинул Данциг, переночевал в своём загородном доме, а на следующий день отправился в Гамбург . 
Переезд в Гамбург стоил Генриху Флорису примерно десятую долю его состояния, которое ему пришлось выплатить в виде 
налогов. В Гамбурге, который был во многом похож на Данциг с точки зрения законов, но в несколько раз крупнее, 
Шопенгауэры сперва поселились в промышленном квартале по адресу Альтштедтер-Нойенвег, 76. Дела у Генриха Флориса на 
новом месте пошли хорошо, и уже через 3 года, в 1796 году, семья переселилась в куда более просторное здание в более 
престижном районе — их новый адрес был Нойер-Вандрам, 97. Именно в этом доме 12 июля 1797 года у Шопенгауэров 
родилась дочь Аделе. После рождения дочери мать практически полностью устранилась от воспитания сына, которым теперь 
занимался практически исключительно Генрих Флорис — уже через четыре недели после рождения дочери он уехал с Артуром 
в путешествие по Франции. Шопенгауэр-старший оставил сына в Гавре на обучение у своего делового партнёра Грегуара де 
Блезимера, а сам отправился в Англию, после чего вернулся в Гамбург. Артур провёл в Гавре 2 года, а затем вернулся к 
отцу и матери в Гамбург. По возвращении он был помещён в дорогую частную школу доктора Иоганна Генриха Кристиана 
Рунге. Почти сразу обнаружилась страсть мальчика к наукам об окружающем мире и к философии, что чрезвычайно радовало 
доктора Рунге, но раздосадовало отца — он видел Артура своим преемником в бизнесе, а не учёным. Последний год жизни 
Стремясь отвлечь сына от «вредных мыслей», Генрих Флорис предложил своему сыну выбор: остаться в Гамбурге, 
чтобы готовиться к поступлению в университет, или отправиться в новое большое турне по Европе. Артур выбрал второе, 
и 3 мая 1803 года Генрих Флорис вместе с Иоганной и Артуром выехали из Гамбурга, оставив дома маленькую Аделе. Их 
путь лежал через Амстердам и Гаагу до Кале. Там они пересели на судно, пересекли Ла-Манш, после чего из Дувра 
отправились в Лондон, где задержались на несколько месяцев. 5 ноября путешественники покинули Англию и отправились в 
Париж, где также провели несколько месяцев. В надежде, что средиземноморский климат благотворно скажется на состоянии 
главы семейства, 4 марта 1804 года семья отправилась в Марсель. В этом городе Шопенгауэры пробыли до марта, 
после чего отправились в Швейцарию, а оттуда через южную Германию, Вену, Богемию и Саксонию — в Берлин, 
куда добрались 25 августа 1804 года. Из Берлина Генрих Флорис был срочно вызван в Гамбург по делам, в то время как 
Иоганна и Артур отправились в Данциг. В родном городе Генриха Флориса Артур должен был начать обучение торговому делу 
— уступка, на которую сын согласился, чтобы не расстраивать своего отца. В декабре семья получила известие, 
что здоровье отца резко ухудшилось — глубокая депрессия чередовалась с бурными приступами вспыльчивости и манией 
преследования. Они срочно выехали из Данцига в Гамбург. Утром 20 апреля 1805 года тело Генриха Флориса было найдено в 
канале за их домом — он выпал с верхнего этажа дома. Жена и сын считали, что это было самоубийством, но истинная 
причина смерти до сих пор не установлена"""

text = (text.lower()
        .replace(",", "")
        .replace(".", "")
        .replace(":", "")
        .replace(";", "")
        .replace("-", "")
        .replace("+", "")
        .replace("=", "")
        .replace("(", "")
        .replace(")", "")
        .replace("!", "")
        .replace("?", "")
        .replace("—", "")
        .replace("", "")
        .replace("\n", "")
        .split(" "))

word_dic = {}

for word in text:
    if word not in word_dic and word != '':
        word_dic[word] = 1
    elif word != '':
        word_dic[word] += 1

word_list = sorted(word_dic.items(), key=lambda item: item[1], reverse=True)
for i in range(10):
    print(word_list[i])


