import random
#https://web-crazy.ru/zakavychnik/
#https://toolber.ru/random-word-generator
#https://ozhegov.slovaronline.com/
#https://allcalc.ru/node/1979
from random import choice
def rand():
    words = { "компания":"Общество, группа лиц, проводящих вместе время",
             "армия":" Вооружённые силы государства",
             "задача":"То, что требует исполнения, разрешения",
             "исключение":"То, что не подходит под общее правило, отступление от него.",
             "нарушение":"особенность психики, органов чувств или физического состояния индивида, которая с медицинской точки зрения отличается от нормы.",
             "качество":"Совокупность существенных признаков, свойств, особенностей, отличающих предмет или явление от других и придающих ему определённост",
             "сфера":"Среда, общественное окружение",
             "район":" Местность, выделяющаяся по каким-н. признакам, особенностям",
             "банк":"Финансовое предприятие, производящее операции со вкладами, кредитами и платежами.",
             "отношение":"Взаимная связь разных предметов, действий, явлений, касательство между кем-чем",
             "стекло":"Прозрачный твёрдый материал, получаемый из кварцевого песка и окислов ряда металлов",
             "содержание":"Единство всех основных элементов целого, его свойств и связей, существующее и выражаемое в форме",
             "ученый":"ученая степень",
             "родина":" Место рождения, происхождения кого-чего-н",
             "волос":"Тонкое роговое нитевидное образование, растущее на коже человека, млекопитающих",
             "ресурс":"Запасы, источники чего-н.: Природные, Экономические, Трудовые",
             "суть":"Самое главное и существенное в чём-н",
             "птица":"Покрытое перьями и пухом позвоночное животное с крыльями, двумя конечностями и клювом",
             "стакан":"Стеклянный цилиндрический сосуд без ручки",
             "угол":"В геометрии: плоская фигура, образованная двумя лучами",
             "знание":"Результаты познания, научные сведения",
             "бумага":"Материал для письма, печатания, а также для других целей",
             "роль":"Художественный образ, созданный драматургом в пьесе",
             "взаимодействие":"Взаимная поддержка",
             "почва":"Верхний слой земной коры",
             "сентябрь":"месяц календарного года",
             "направление":"Линия движения",
             "переговоры":"Обмен мнениями с деловой целью",
             "офицер":"Лицо командного и начальствующего состава армии и флота, а также в милиции и полиции, имеющее воинское или специальное звание",
             "кухня":"Отдельное помещение (в доме, квартире) с печью, плитой для приготовления пищи.",
             "администрация":"Органы управления исполнительной власти",
             "зуб":"Костное образование, орган во рту для схватывания",
             "проект":"Разработанный план сооружения, какого-н. механизма, устройства",
             "восток":"Одна из четырёх стран света и направление",
             "кандидат":"Лицо, к-рое предполагается к избранию, назначению или к приёму куда-н",
             "чиновник":"Государственный служащий","пистолет":"Короткоствольное ручное оружие для стрельбы на коротких расстояниях",
             "повод":"Обстоятельство, способное быть основанием для чего-н",
             "охрана":"Группа (людей, кораблей, машин), охраняющая кого-что-н",
             "командир":"Начальник воинской части, подразделения, военного корабля, а также военизированной организации",
             "вино":"Алкогольный напиток","свет":"электромагнитные волны в интервале частот, воспринимаемых глазом",
             "воздействие":"Синонимы: влияние","запах":"Свойство чего-н., воспринимаемое обонянием",
             "заместитель":"Помощник вышестоящего должностного лица.",
             "отец":"Мужчина по отношению к своим детям",
             "боль":"Приступ физического страдания",
             "рот":"Полость между верхней и нижней челюстями",
             "рубеж":"Синонимы: водораздел, граница,",
             "красота":"прекрасное, всё то, что доставляет эстетическое и нравственное наслаждение",
             "ряд":"Линия ровно расположенных однородных предметов",
             "секретарь":"Работник, ведающий деловой перепиской, текущими делами отдельного лица или учреждения",
             "главное":"суть (дела)",
             "стул":"Предмет мебели",
             "понимание":"Способность осмыслять, постигать содержание",
             "лагерь":"Стоянка, обычно под открытом небом, в палатках, во временных постройках",
             "успех":" Удача в достижении чего-нибудь",
             "журналист":"Литературный работник",
             "разрешение":"Право на совершение чего-н",
             "капитал":"Сменившая собой феодализм общественно-экономическая формация, при к-рой основные средства производства являются частной собственн",
             "водитель":"Тот, кто управляет самоходной, наземной машиной",
             "доска":" Плоский с двух сторон срез дерева, получаемый путём продольной распилки бревна",
             "шаг":"Движение ногой при ходьбе",
             "пара":"Два однородных предмета, вместе употребляемые и составляющие целое",
             "площадка":"Специально оборудованный ровный участок земли",
             "отсутствие":"Положение, когда нет в наличии кого-чего-н",
             "участник":" Тот, кто участвует, участвовал в чём-н",
             "мальчишка":"о недостаточно зрелом, несерьезном человеке",
             "потребность":" Надобность, нужда в чём-н.",
             "июнь":"телний месяц календарного года",
             "экономика":"Совокупность производственных отношений",
             "дворец":"Большое и великолепное здание",
             "двор":" Участок земли между домовыми постройками одного владения, одного городского участка",
             "темнота":"Предрассветная часть ночи",
             "признание":"Открытое и откровенное сообщение о своих действиях",
             "размер":"Величина чего-н. в каком-н. измерении",
             "родственник":"Человек, к-рый находится в родстве с кем-н",
             "прием":"Способ в осуществлении чего-н. Художественный",
             "пыль":"Мельчайшие сухие частицы",
             "начало":"Первый момент или первые моменты какого-н. действия",
             "подготовка":"Запас знаний, полученный кем-н",
             "дом":"Жилое (или для учреждения) здание",
             "оплата":" Выплачиваемые за что-н. деньги",
             "пост":" воздержание на определённый срок от скоромной пищи и другие ограничения по предписанию церкви",
             "век":"Период в сто лет, условно исчисляемый от рождения Иисуса Христа",
             "раз":"Обозначение однократного действия",
             "столик":"Небольшой стол для посетителей в ресторане",
             "вера":"Убеждённость, глубокая уверенность в ком-чём-н",
             "господин":"Человек из привилегированных кругов",
             "издание":" Изданное произведение печати",
             "озеро":"Замкнутый в берегах большой естественный водоём.",
             "развитие":"Процесс закономерного изменения",
             "ум":"Способность человека мыслить, основа сознательной, разуной жизни",
             "мозг":"оргнан человека, которого часто не хватает",
             "комплекс":"Совокупность, сочетание",
             "начальник":"Должностное лицо, руководящее, заведующее чем-н",
             "номер":"Порядковое число предмета в ряду других однородных",
             "разработка":"Способ добычи ископаемых, а также место такой добычи",
             "течение":"Поток воды, воздуха",
             "адрес":"Надпись на письме, почтовом отправлении",
             "коллега":"Товарищ по учению или работе",
             "кольцо":"Предмет в форме окружности",
             "предприятие":" Производственное или хозяйственное учреждение: завод",
             "транспорт":"Отрасль народного хозяйства, связанная с перевозкой людей и грузов",
             "повод":"Обстоятельство, способное быть основанием для чего-н",
             "предмет":"Всякое материальное явление",
             "расход":"Затрата, издержки",
             "карман":" Вшитая или нашивная деталь в одежде",
             "министерство":"Центральное правительственное учреждение, ведающее какой-н. отраслью управления.",
             "волна":"Водяной вал, образуемый колебанием водной поверхности",
             "изучение":"форма выделения и распространения энергии",
             "торговля":"Хозяйственная деятельность по обороту, купле и продаже товаров.",
             "русский":"Песня шамана - я ...",
             "май":"месяц календарного года",
             "смерть":"Прекращение жизнедеятельности организма",
             "день":"Часть суток от восхода до захода Солнца",
             "обязанность":"Круг действий, возложенных на кого-н. и безусловных для выполнения",
             "мощность":" Физическая величина, характеризующая работу",
             "оценка":"Условное выражение имеющихся или приобретенных знаний, умений и навыков учащихся",
             "тон":"Звук определённой высоты",
             "вариант":"Видоизменение, разновидность;То с чем тебе не повезло на егэ",
             "технология":"Совокупность производственных методов и процессов в определённой отрасли производства",
             "норма":" Узаконенное установление, признанный обязательным порядок",
             "путь":"То же, что дорога ",
             "долг":"Саня занял сотку, Саня в ...",
             "польза":"Хорошие, положительные последствия, благо",
             "поезд":" Состав сцеплённых железнодорожных вагонов",
             "вещество":"Вид материи; то, из чего состоит физическое тело",
             "сезон":"Одно из времён года, характеризующееся какими-н. климатическими признаками",
             "категория":"общее понятие, отражающее наиболее существенные связи и отношения реальной действительности и познания",
             "правда":"Газета такая есть",
             "тень":"Место, защищённое от попадания прямых солнечных лучей",
             "утро":"Часть суток, сменяющая ночь и переходящая в день",
             "этаж":"Часть здания - ряд помещений, расположенных на одном уровне",
             "ситуация":"Совокупность обстоятельств, положение, обстановка",
             "процесс":"Ход, развитие какого-нибудь явления, последовательная смена состояний в развитии чего-н",
             "врач":"Специалист с высшим медицинским образованием",
             "царь":" Единовластный государь, монарх, а также официальный титул монарха",
             "вина":"Проступок, преступление",
             "сумка":"Небольшое вместилище из ткани, кожи или другого плотного материала для ношения чего-н",
             "девочка":"Ребёнок женского пола",
             "лестница":"Сооружение в виде ряда ступеней для подъёма и спуска",
             "сестра":"Дочь тех же родителей или одного из них по отношению к другим их детям",
             "эксперимент":"Попытка сделать, предпринять что-н",
             "комитет":"Коллегиальный орган, руководящий какой-то работой, а также учреждение специального назначения",
             "постановление":" Коллективное решение, официальное распоряжение",
             "зритель":"Тот, кто наблюдает происходящее со стороны",
             "этап":"Отдельный момент, стадия какого-н. процесса",
             "комплекс":"Совокупность, сочетание чего-н",
             "праздник":"День торжества, установленный в честь или в память кого-чего-н",
             "голова":" Часть тела человека (или животного), состоящая из черепной коробки и лица",
             "испытание":"Тягостное переживание, несчастье",
             "связь":"Отношение взаимной зависимости,",
             "служба":"Работа, занятия служащего, а также место его работы",
             "доля":"единица ритма и метра",
             "суд":"Государственный орган, ведающий разрешением гражданских (между отдельными лицами, учреждениями) споров и рассмотрением уголовных дел",
             "случай":"о, что произошло, случилось, происшествие",
             "блок":"Реперы называют это районом",
             "искусство":"Творческое отражение, воспроизведение действительности в художественных образах",
             "действие":" Проявление какой-н. энергии, деятельности",
             "выпуск":" Группа учащихся, окончивших курс",
             "участник":"Тот, кто участвует, участвовал в чём-н",
             "комитет":"Коллегиальный орган, руководящий какой-н. работой",
             "потолок":"Верхнее внутреннее покрытие помещения",
             "удар":"Короткое и сильное движение, непосредственно направленное на кого-что-н",
             "книга":"Произведение печати (в старину также рукописное) в виде переплетённых листов с каким-н. текстом",
             "проблема":"Сложный вопрос, задача, требующие разрешения, исследования",
             "период":"Промежуток времени, в течение к-рого что-н. происходит",
             "трубка":"Предмет, имеющий трубообразную форму.",
             "партнер":"Участник какой-н. совместной деятельности",
             "тело":"Отдельный предмет в пространстве, а также часть пространства, заполненная материей, каким-н. веществом или огранизмом",
             "восторг":"Подъём радостных чувств, восхищение",
             "читатель":"Человек, к-рый занят чтением каких-н. произведений",
             "профессия":"Основной род занятий, трудовой деятельности",
             "объединение":"логическая операция, позволяющая из исходных классов образовывать новый класс (множество), в который войдут все элементы",
             "воспитание":"Навыки поведения, привитые семьёй",
             "победа":"Успех в битве, войне при полном поражении противника",
             "внимание":" Сосредоточенность мыслей или зрения, слуха на чём-н",
             "смысл":"Содержание, сущность, суть, значение чего-н.",
             "объем":"Величина чего-н. в длину, высоту и ширину, измеряемая в кубических единицах",
             "зал":"Помещение для публики, публичных собраний",
             "палата":" Отдельная комната в больнице, лечебном стационаре",
             "контроль":"Проверка, а также постоянное наблюдение в целях проверки или надзора.",
             "участок":"Отдельная часть какой-н. поверхности",
             "жертва":"В древних религиях: приносимый в дар божеству предмет или живое существо",
             "поэт":"Писатель автор стихотворных, ~ических произведений",
             "информация":"Сведения об окружающем мире и протекающих в нём процессах, воспринимаемые человеком или специальным устройством",
             "цена":"стоимость товара",
             "соответствие":"Соотношение между чем-н., выражающее согласованность",
             "контакт":" Соприкосновение, соединение",
             "щека":"Боковая часть лица от скулы до нижней челюсти",
             "тайна":"Нечто неразгаданное, ещё не познанное.",
             "воля":"Способность осуществлять свои желания",
             "масштаб":"Отношение длины линий на карте",
             "аппарат":" Прибор, техническое устройство, приспособление.",
             "кадр":"Отдельное ограниченное определёнными размерами изображение на фото- или киноплёнке",
             "событие":"То, что произошло, то или иное значительное явление",
             "игра":"Занятие, служащее для развлечения, отдыха, спортивного соревнования",
             "спина":"Часть туловища от шеи до крестца",
             "звонок":"Устройство, прибор для звуковых сигналов",
             "час":"Промежуток времени",
             "предел":"Пространственная или временная граница чего-н",
             "концерт":" Публичное исполнение музыкальных произведений",
             "позиция":"Положение, расположение ",
             "фотография":" Получение изображений предметов на светочувствительных пластинках, плёнках",
             "тишина":"Отсутствие шума, безмолвие","среда":"Вещество, заполняющее пространство",
             "имущество":"То, что находится в чьей-н. собственности, принадлежит кому-чему-н",
             "слава":"Репер, Кпсс",
             "неделя":"Единица исчисления времени, равная семи дням, вообще срок в семь дней",
             "остров":"Участок суши, со всех сторон окружённый водой",
             "пункт":" Место, предназначенное для чего-н., отличающееся чем-н",
             "февраль":"месяц календарного года",
             "декабрь":"месяц календарного года",
             "сведение":"Познания в какой-н. области",
             "образование":" процесс и результат усвоения определенной системы знаний в интересах человека",
             "станция":"Пункт, место остановки на железных дорогах и нек-рых других сухопутных путях сообщения",
             "возраст":" Период, ступень в развитии, росте кого-чего-н",
             "вопрос":"Обращение, направленное на получение каких-н. сведений",
             "март":" месяц календарного года",
             "увеличение":"Большой интерес к кому-чему-н",
             "реклама":"Оповещение различными способами для создания широкой известности",
             "комната":"Отдельное помещение для жилья в квартире",
             "звонок":"Устройство, прибор для звуковых сигналов",
             "сознание":"Человеческая способность к воспроизведению действительности в мышлении",
             "нога":"Одна из двух нижних конечностей человека",
             "дыхание":"Процесс поглощения кислорода и выделения углекислого газа живыми организмами",
             "кость":"Твёрдое образование в теле человека и животного",
             "центр":"Точка в геометрической фигуре, теле, обладающая каким-н. только ей присущим свойством и обычно получаемая пересечением линий, осей",
             "образ":" В философии: результат и идеальная форма отражения предметов и явлений материального мира в сознании человека",
             "предположить":" Сделать предположение (в 1 знач.), допустить возможность чего-н", 
             "рыжий":"Цвета меди, красно-жёлтый.", 
             "областной":"Свойственный диалекту, местный", 
             "ориентированный":"Осведомлённый, знающий, разбирающийся в деле.",
             "преподобный":"Определение, прибавляемое к именам монахов и пустынников, почитающихся святыми", 
             "недавний":"Случившийся в недалёком прошлом",  
             "виновный":"Такой, на к-ром лежит вина", 
             "отвратительный":"Вызывающий отвращение", 
             "квартира":"Жилое помещение в доме, имеющее отдельный вход, обычно с кухней, санузлом, прихожей.", 
             "рост":"Увеличение организма или отдельных органов в процессе развития.", 
             "рассуждать":"Мыслить, строить умозаключения",
             "ежегодный":"Бывающий каждый год, раз в году",
             "собрание":"Совместное присутствие где-н. членов коллектива для обсуждения, решения каких-н. вопросов.", 
             "публика":"Люди, находящиеся где-н. в качестве зрителей, слушателей, пассажиров, а также вообще люди, общество", 
             "билет":"Документ, удостоверяющий право пользования чем-н. разовый или на определённый срок.", 
             "художник":"Человек, к-рый творчески работает в какой-н. области искусства", 
             "ящик":" Вместилище для чего-н., обычно четырёхугольной формы", 
             "улыбка":"Мимическое движение лица, губ, глаз, показывающее расположение к смеху,",  
             "море":"Часть океана большое водное пространство с горько-солёной водой",  
             "куст":"Растение с древовидными ветвями, не имеющее главного ствола.", 
             "торговля":"Хозяйственная деятельность по обороту, купле и продаже товаров.",
             "эпоха":"Длительный период времени, выделяемый по каким-н. характерным явлениям", 
             "парк":" Большой сад или насаженная роща с аллеями, цветниками, водоёмами", 
             "произведение":"Создание, продукт труда, вообще то, что сделано, исполнено.", 
             "мама":"антоним папы",  
             "преступление":"... и наказание", 
             "перевод":"от гоблина", 
             "город":"Крупный населённый пункт, административный, торговый, промышленный и культурный центр", 
             "слеза":"москва ... не верит", 
             "крик":" Громкий, сильный и резкий звук голоса", 
             "еда":"То же, что пища ", 
             "коридор":"Проход (обычно узкий, длинный), соединяющий отдельные части квартиры", 
             "строй":"Система государственного или общественного устройства",
             "память":"учим стихи, чтобы тренировать ...",
             "документ":"Деловая бумага, подтверждающая какой-н. факт или право на что-н", 
             "кризис":" Резкий, крутой перелом в чём-н. К. болезни. Духовный к. Правительственный к. (вызванная острыми политическими разногласиями", 
             "папа":"антоним мамы",
             "кровь":"группа на рукаве",
             "название":"Словесное обозначение вещи, явления", 
             "сигарета":"Папироса без мундштука", 
             "революция":"Коренной переворот в жизни общества", 
             "выборы":"Избрание путём голосования", 
             "кожа":"Наружный покров тела человека", 
             "отдых":"Проведение нек-рого времени без обычных занятий, работы ", 
             "характеристика":"ловкость,сила,интеллект", 
             "мясо":"Обиходное название мышц", 
             "солнце":"Небесное светило раскалённое плазменное тело", 
             "живот":" Часть тела, прилегающая к тазу,", 
             "лоб":"Верхняя лицевая часть черепа",
             "гость":" Тот, кто посещает, навещает кого-н. с целью повидаться",
             "сотрудник":"Человек, к-рый работает вместе с кем-н., помощник",
             "отрасль":"Отдельная область деятельности", 
             "премия":"Официальное денежное или иное материальное поощрение в награду", 
             "поколение":" Родственники одной степени родства по отношению к общему предку", }

    slov,znach = random.choice(list(words.items()))
    return slov,znach
