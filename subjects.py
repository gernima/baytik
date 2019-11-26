import telebot
from gtts import gTTS
import enchant
import wikipedia
import re
import sqlite3
from yandex_translate import YandexTranslate
import os, dotenv

data = """862 г. – «Призвание варягов» на Русь.
862–879 гг. – Княжение Рюрика в Новгороде.
879–912 гг. – Княжение Олега в Киеве.
882 г. – Объединение Новгорода и Киева в единое государство при князе Олеге.
907, 911 гг. – Походы Олега на Царьград. Договоры с греками.
912–945 гг. – Княжение Игоря в Киеве.
945 г. – Восстание древлян.
945–962 гг. – Правление княгини Ольги в малолетстве ее сына князя Святослава.
957 г. – Крещение княгини Ольги в Константинополе.
962–972 гг. – Княжение Святослава Игоревича.
964–972 гг. – Военные походы князя Святослава.
980–1015 гг. – Княжение Владимира I Святославича Святого.
988 г. – Принятие христианства на Руси.
1019–1054 гг. – Княжение Ярослава Мудрого.
1037 г. – Начало строительства храма Св. Софии в Киеве.
1045 г. – Начало строительства храма Св. Софии в Новгороде Великом.
1072 г. – Окончательное оформление «Русской Правды» («Правда Ярославичей»).
1097 г. – Съезд князей в Любече. Закрепление раздробленности Древнерусского государства.
1113–1125 гг. – Великое княжение Владимира Мономаха.
1125–1157 г. – Княжение Юрия Владимировича Долгорукого во Владимире.
1136 г. – Установление республики в Новгороде.
1147 г. – Первое упоминание о Москве в летописи.
1157–1174 гг. – Княжение Андрея Юрьевича Боголюбского.
1165 г. – Постройка храма Покрова на Нерли.
1185 г. – Поход князя Игоря Новгород Северского на половцев. «Слово о полку Игореве».
1199 г. – Объединение Волынского и Галицкого княжеств.
1202 г. – Образование Ордена меченосцев.
1223 г., 31 мая. – Битва на реке Калке.
1237–1240 гг. – Нашествие монголо татар во главе с ханом Батыем на Русь.
1237 г. – Объединение Тевтонского ордена с Орденом меченосцев. Образование Ливонского ордена.
1238 г., 4 марта. – Битва на реке Сити.
1240 г., 15 июля. – Невская битва. Разгром князем Александром Ярославичем шведских рыцарей на реке Неве. Прозван Невским.
1240 г. – Разгром монголо-татарами Киева.
1242 г., 5 апреля. – Ледовое побоище. Разгром князем Александром Ярославичем Невским крестоносцев на Чудском озере.
1243 г. – Образование государства Золотая Орда.
1252–1263 гг. – Княжение Александра Невского на великокняжеском владимирском престоле.
1264 г. – Распад Галицко Волынского княжества под ударами Орды.
1276 г. – Образование самостоятельного Московского княжества.
1325–1340 гг. – Правление князя Ивана Калиты в Москве.
1326 г. – Перенесение резиденции главы Русской православной церкви – митрополита – из Владимира в Москву, превращение Москвы в общерусский религиозный центр.
1327 г. – Восстание в Твери против золотоордынцев.
1359–1389 гг. – Правление князя (с 1362 г. – великого князя) Дмитрия Ивановича (после 1380 г. – Донского) в Москве.
1360–1430 гг. – Жизнь и деятельность Андрея Рублева.
1378 г. – Битва на реке Воже.
1380 г., 8 сентября – Куликовская битва.
1382 г. – Разгром Москвы Тохтамышем.
1389–1425 гг. – Княжение Василия I Дмитриевича.
1410 г., 15 июля – Грюнвальдская битва. Разгром Тевтонского ордена.
1425–1453 гг. – Династическая война между сыновьями и внуками Дмитрия Донского.
1439 г. – Флорентийская церковная уния об объединении католической и православной церквей под главенством Папы Римского. Акт об унии подписан русским митрополитом Исидором, за что он был низложен.
1448 г. – Избрание епископа Рязанского Ионы митрополитом Русской православной церкви и вся Руси. Установление автокефалии (самостоятельности) Русской православной церкви от Византии.
1453 г. – Падение Византийской империи.
1462–1505 гг. – Княжение Ивана III.
1463 г. – Присоединение к Москве Ярославля.
1469–1472 гг. – Путешествие Афанасия Никитина в Индию.
1471 г. – Сражение на реке Шелони московских и новгородских войск.
1478 г. – Присоединение Новгорода Великого к Москве.
1480 г. – «Стояние на реке Угре». Ликвидация ордынского ига.
1484–1508 гг. – Строительство нынешнего Московского Кремля. Сооружение соборов и Грановитой палаты, кирпичных стен.
1485 г. – Присоединение Твери к Москве.
1497 г. – Составление «Судебника» Ивана III. Установление единых норм уголовной ответственности и судебно процессуальных норм для всей страны, ограничение права крестьянского перехода от одного феодала к другому – неделя до и неделя после 26 ноября (Юрьева дня осеннего).
Конец XV – начало XVI в. – Завершение процесса складывания Российского централизованного государства.
1503 г. – Полемика между Нилом Сорским (лидером нестяжателей, проповедовавших отказ церкви от всякого имущества) и игуменом Иосифом Волоцким (лидером стяжателей, сторонника сохранения церковного землевладения). Осуждение взглядов нестяжателей на церковном Cоборе.
1503 г. – Присоединение к Москве Юго Западных русских земель.
1505–1533 гг. – Правление Василия III.
1510 г. – Присоединение Пскова к Москве.
1514 г. – Присоединение Смоленска к Москве.
1521 г. – Присоединение Рязани к Москве.
1533–1584 гг. – Правление великого князя Ивана IV Грозного.
1547 г. – Венчание Ивана IV Грозного на царство.
1549 г. – Начало созыва Земских соборов.
1550 г. – Принятие «Судебника» Ивана IV Грозного.
1551 г. – «Стоглавый собор» Русской православной церкви.
1552 г. – Присоединение Казани к Москве.
1555–1560 гг. – Строительство Покровского собора в Москве (храма Василия Блаженного).
1556 г. – Присоединение Астрахани к Москве.
1556 г. – Принятие «Уложения о службе».
1558–1583 гг. – Ливонская война.
1561 г. – Разгром Ливонского ордена.
1564 г. – Начало книгопечатания на Руси. Издание Иваном Федоровым «Апостола» – первой печатной книги, имеющей установленную дату.
1565–1572 гг. – Опричнина Ивана IV Грозного.
1569 г. – Заключение Люблинской унии об объединении Польши с Великим княжеством Литовским в одно государство – Речь Посполитую.
1581 г. – Первое упоминание о «заповедных летах».
1581 г. – Поход Ермака в Сибирь.
1582 г. – Подписание Ям Запольского перемирия России с Речью Посполитой.
1583 г. – Заключение Плюсского перемирия со Швецией.
1584–1598 гг. – Царствование Федора Иоанновича.
1589 г. – Учреждение патриаршества на Руси. Патриарх Иов.
1597 г. – Указ об «урочных летах» (пятилетнем сроке сыска беглых крестьян).
1598–1605 гг. – Правление Бориса Годунова.
1603 г. – Восстание крестьян и холопов под предводительством Хлопка.
1605–1606 гг. – Правление Лжедмитрия I.
1606–1607 гг. – Восстание крестьян под предводительством Ивана Болотникова.
1606–1610 гг. – Правление царя Василия Шуйского.
1607–1610 гг. – Попытка Лжедмитрия II захватить власть в России. Существование «Тушинского лагеря».
1609–1611 гг. – Оборона Смоленска.
1610–1613 гг. – «Семибоярщина».
1611 г., март – июнь. – Первое ополчение против польских войск во главе с П. Ляпуновым.
1612 г. – Второе ополчение под руководством Д. Пожарского и К. Минина.
1612 г., 26 октября. – Освобождение Москвы от польских интервентов Вторым ополчением.
1613 г. – Избрание Земским собором Михаила Романова на царство. Начало династии Романовых. 1613–1645 гг. – Царствование Михаила Федоровича Романова.
1617 г. – Заключение Столбовского «вечного мира» со Швецией.
1618 г. – Деулинское перемирие с Польшей.
1632–1634 гг. – Смоленская война между Россией и Речью Посполитой.
1645–1676 гг. – Правление царя Алексея Михайловича.
1648 г. – Экспедиция Семена Дежнева по реке Колыме и Ледовитому океану.
1648 г. – Начало восстания Богдана Хмельницкого на Украине.
1648 г. – «Соляной бунт» в Москве.
1648–1650 гг. – Восстания в различных городах России.
1649 г. – Принятие Земским собором нового свода законов – «Соборного уложения» царя Алексея Михайловича. Окончательное закрепощение крестьян.
ок. 1653–1656 гг. – Реформа патриарха Никона. Начало церковного раскола.
1654 г., 8 января. – Переяславская рада. Воссоединение Украины с Россией.
1654–1667 гг. – Война России с Речью Посполитой за Украину.
1662 г. – «Медный бунт» в Москве.
1667 г. – Заключение Андрусовского перемирия между Россией и Речью Посполитной.
1667 г. – Введение Новоторгового устава.
1667–1671 гг. – Крестьянская война под предводительством Степана Разина.
1672 г., 30 мая. – Рождение Петра I.
1676–1682 гг. – Правление Федора Алексеевича.
1682 г. – Отмена местничества.
1682, 1698 гг. – Стрелецкие восстания в Москве.
1682–1725 гг. – Царствование Петра I (1682–1689 гг. – при регентстве Софьи, до 1696 г. – совместно с Иваном V).
1686 г. – «Вечный мир» с Польшей.
1687 г. – Открытие Славяно греко латинской академии.
1695, 1696 гг. – Походы Петра I на Азов.
1697–1698 гг. – «Великое посольство».
1700–1721 гг. – Северная война.
1703 г., 16 мая. – Основание Санкт Петербурга.
1707–1708 гг. – Крестьянское восстание под предводительством К. Булавина.
1708, 28 сентября. – Битва при деревне Лесной.
1709 г., 27 июня. – Полтавская битва.
1710–1711 гг. – Прутский поход.
1711 г. – Учреждение Сената.
1711–1765 гг. – Жизнь и деятельность М.В. Ломоносова.
1714 г. – Указ о единонаследии (отменен в 1731 г.).
1714, 27 июля. – Сражение при мысе Гангут.
1718–1721 гг. – Учреждение коллегий.
1720 г. – Сражение у острова Гренгам.
1721 г. – Ништадтский мир со Швецией.
1721 г. – Провозглашение Петра I императором. Россия стала империей.
1722 г. – Принятие «Табели о рангах».
1722 г. – Подписание указа о наследии престола.
1722–1723 гг. – Каспийский поход.
1725 г. – Открытие Академии наук в Санкт Петербурге.
1725–1727 гг. – Правление Екатерины I.
1727–1730 гг. – Правление Петра II.
1730–1740 гг. – Правление Анны Иоанновны. «Бироновщина».
1741–1761 гг. – Правление Елизаветы Петровны.
1755 г., 25 января. – Открытие Московского университета.
1756–1763 гг. – Семилетняя война.
1757 г. – Основание в Санкт Петербурге Академии художеств.
1761–1762 гг. – Правление Петра III.
1762 г. – «Манифест о вольности дворянской».
1762–1796 гг. – Правление Екатерины II.
1768–1774 гг. – Русско турецкая война.
1770 г. – Победа русского флота над турецким в битве при Чесме и русских сухопутных сил над турецкой армией в сражениях у рек Ларга и Кагул.
1774 г. – Заключение Кючук Кайнарджийского мира по итогам русско турецкой войны. Крымское ханство переходило под протекторат России. Россия получала территорию Причерноморья между Днепром и Южным Бугом, крепости Азов, Керчь, Кинбурн, право свободного прохода российских торговых кораблей через черноморские проливы.
1772, 1793, 1795 гг. – Разделы Польши между Пруссией, Австрией и Россией. К России отошли территории Правобережной Украины, Белоруссии, часть Прибалтики и Польши.
1772–1839 гг. – Жизнь и деятельность М.М. Сперанского.
1773–1775 гг. – Крестьянская война под предводительством Емельяна Пугачева.
1775 г. – Проведение губернской реформы в Российской империи.
1782 г. – Открытие памятника Петру I «Медный всадник» (Э. Фальконе).
1783 г. – Вхождение Крыма в состав Российской империи. Георгиевский трактат. Переход Восточной Грузии под протекторат России.
1785 г. – Издание жалованных грамот дворянству и городам.
1787–1791 г. – Русско турецкая война.
1789 г. – Победы русских войск под командованием А.В. Суворова при Фокшанах и Рымнике.
1790 г. – Победа русского флота над турецким в сражении при мысе Калиакрия.
1790 г. – Выход в свет книги А.Н. Радищева «Путешествие из Петербурга в Москву».
1790 г. – Взятие русскими войсками под командованием А.В. Суворова турецкой крепости Измаил на Дунае.
1791 г. – Заключение Ясского мира по итогам русско турецкой войны. Подтверждалось присоединение к России Крыма и Кубани, территории Причерноморья между Южным Бугом и Днестром.
1794 г. – Восстание в Польше под предводительством Тадеуша Костюшко.
1796–1801 гг. – Правление Павла I.
1797 г. – Отмена установленного Петром I порядка престолонаследия. Восстановление порядка наследования престола по праву первородства по мужской линии.
1797 г. – Издание Павлом I манифеста о трехдневной барщине.
1799 г. – Итальянский и Швейцарский походы А. В. Суворова.
1801–1825 г. – Правление Александра I.
1802 г. – Учреждение министерств вместо коллегий.
1803 г. – Указ о «вольных хлебопашцах».
1803 г. – Принятие устава, вводившего автономию университетов.
1803–1804 гг. – Первая русская кругосветная экспедиция под руководством И.Ф. Крузенштерна и Ю. Ф. Лисянского.
1804–1813 гг. – Русско иранская война. Окончилась Гюлистанским миром.
1805–1807 гг. – Участие России в III и IV антинаполеоновских коалициях.
1805 г., декабрь. – Поражение русских и австрийских войск в сражении при Аустерлице.
1806–1812 г. – Русско турецкая война.
1807 г. – Поражение русской армии под Фридландом.
1807 г. – Заключение Тильзитского мира между Александром I и Наполеоном Бонапартом (присоединение России к континентальной блокаде Англии, согласие России на создание вассального Франции Герцогства Варшавского).
1808–1809 гг. – Русско шведская война. Присоединение Финляндии к Российской империи.
1810 г. – Создание Государственного совета по инициативе М.М. Сперанского.
1812 г., июнь – декабрь. – Отечественная война с Наполеоном.
1812 г. – Заключение Бухарестского мира по итогам русско турецкой войны.
1812 г., 26 августа – Бородинская битва.
1813–1814 гг. – Заграничные походы русской армии.
1813 г. – «Битва народов» при Лейпциге.
1813 г. – Заключение Гюлистанского мира по итогам русско иранской войны.
1814–1815 гг. – Венский конгресс европейских государств. Решение вопросов устройства Европы после Наполеоновских войн. Присоединение к России Герцогства Варшавского (Царства Польского).
1815 г. – Создание «Священного союза».
1815 г. – Дарование Александром I Царству Польскому Конституции.
1816 г. – Начало массового создания военных поселений по инициативе А.А. Аракчеева.
1816–1817 гг. – Деятельность «Союза спасения».
1817–1864 гг. – Кавказская война.
1818–1821 гг. – Деятельность «Союза благоденствия».
1820 г. – Открытие Антарктиды российскими мореплавателями под командованием Ф.Ф. Беллинсгаузена и М.П. Лазарева. 1821–1822 гг. – Образование Северного и Южного обществ декабристов.
1821–1881 гг. – Жизнь и деятельность Ф.М. Достоевского.
1825 г., 14 декабря. – Восстание декабристов на Сенатской площади в Петербурге.
1825 г., 29 декабря – 1826 г., 3 января. – Восстание Черниговского полка.
1825–1855 гг. – Правление Николая I.
1826–1828 гг. – Русско иранская война.
1828 г. – Заключение Туркманчайского мира по итогам русско иранской войны. Гибель А.С. Грибоедова.
1828–1829 гг. – Русско турецкая война.
1829 г. – Заключение Адрианопольского мира по итогам русско турецкой войны.
1831–1839 гг. – Деятельность кружка Н.В. Станкевича.
1837 г. – Открытие первой железной дороги Петербург – Царское Село.
1837–1841 гг. – Проведение П.Д. Киселевым реформы управления государственными крестьянами.
1840–1850-е гг. – Споры между славянофилами и западниками.
1839–1843 гг. – Денежная реформа Е.Ф. Канкрина.
1840–1893 гг. – Жизнь и деятельность П.И. Чайковского.
1844–1849 гг. – Деятельность кружка М.В. Буташевича– Петрашевского.
1851 г. – Открытие железной дороги Москва – Санкт-Петербург.
1853–1856 гг. – Крымская война.
1853 г., ноябрь. – Сражение при Синопе.
1855–1881 гг. – Правление Александра II.
1856 г. – Парижский конгресс.
1856 г. – Основание П.М. Третьяковым коллекции русского искусства в Москве.
1858, 1860 гг. – Айгунский и Пекинский договоры с Китаем.
1861 г., 19 февраля. – Отмена крепостного права в России.
1861–1864 гг. – Деятельность организации «Земля и воля».
1862 г. – Образование «Могучей кучки» – объединения композиторов (М.А. Балакирев, Ц.А. Кюи, М.П. Мусоргский, Н.А. Римский Корсаков, А.П. Бородин).
1864 г. – Земская, судебная и школьная реформы.
1864–1885 гг. – Присоединение Средней Азии к Российской империи.
1867 г. – Продажа Аляски США.
1869 г. – Открытие Д. И. Менделеевым Периодического закона химических элементов.
1870 г. – Реформа городского самоуправления.
1870–1923 гг. – Деятельность «Товарищества передвижных художественных выставок».
1873 г. – Создание «Союза трех императоров».
1874 г. – Проведение военной реформы – введение всеобщей воинской обязанности.
1874, 1876 гг. – Осуществление народниками «хождений в народ».
1876–1879 гг. – Деятельность новой организации «Земля и воля».
1877–1878 гг. – Русско турецкая война.
1878 г. – Сан-Стефанский мирный договор.
1878 г. – Берлинский конгресс.
1879 г. – Раскол организации «Земля и воля». Возникновение организаций «Народная воля» и «Черный передел».
1879–1881 гг. – Деятельность организации «Народная воля».
1879–1882 гг. – Оформление Тройственного союза.
1881 г., 1 марта. – Убийство народовольцами Александра II.
1881–1894 гг. – Правление Александра III.
1882 г. – Отмена временнообязанного положения крестьян. Перевод крестьян на обязательный выкуп.
1883–1903 гг. – Деятельность группы «Освобождение труда».
1885 г. – Стачка на Никольской мануфактуре Т.С. Морозова в Орехово Зуеве (Морозовская стачка).
1887 г. – Принятие циркуляра «о кухаркиных детях».
1889 г. – Принятие «Положения о земских начальниках».
1891–1893 гг. – Оформление франко русского союза.
1891–1905 гг. – Строительство Транссибирской железнодорожной магистрали.
1892 г. – Передача П.М. Третьяковым своей коллекции русского искусства в дар городу Москве.
1894–1917 гг. – Правление Николая II.
1895 г. – Изобретение А.С. Поповым радиосвязи.
1895 г. – Создание «Союза борьбы за освобождение рабочего класса».
1897 г. – Первая всеобщая перепись населения России.
1897 г. – Денежная реформа С.Ю. Витте.
1898 г. – I съезд РСДРП.
1899 г. – Гаагская мирная конференция 26 держав по проблемам разоружения, созванная по инициативе России.
1901–1902 гг. – Создание партии социалистов-революционеров (эсеров) в результате объединения неонароднических кружков.
1903 г. – II съезд РСДРП. Создание партии.
1903 г. – Создание «Союза земцев конституционалистов».
1904–1905 гг. – Русско японская война.
1904 г., август – Сражение под городом Ляоян.
1904 г., сентябрь – Сражение на реке Шахэ.
1905 г., 9 января – «Кровавое воскресенье». Начало первой российской революции.
1905–1907 гг. – Первая российская революция.
1905 г., февраль – Поражение русской армии под городом Мукденом.
1905 г., май – Гибель русского флота возле острова Цусима.
1905 г., июнь – Восстание на броненосце «Князь Потемкин-Таврический».
1905 г., август – Заключение Портсмутского мирного договора по итогам русско японской войны. Россия уступала Японии южную часть Сахалина, арендные права на Ляодунский полуостров и Южно Маньчжурскую железную дорогу.
1905 г., 17 октября – Издание Манифеста «Об усовершенствовании государственного порядка».
1905 г., ноябрь – Создание «Союза русского народа».
1905 г., декабрь – Вооруженное восстание в Москве и ряде других городов.
1906 г., апрель – июль – Деятельность I Государственной думы.
1906 г., 9 ноября – Указ о выходе крестьян из общины. Начало проведения столыпинской аграрной реформы.
1907 г., февраль – июнь – Деятельность II Государственной думы.
1907 г., 3 июня – Роспуск II Государственной думы. Принятие нового избирательного закона (третьеиюньский переворот).
1907–1912 гг. – Деятельность III Государственной думы.
1907 г., август – Русско английское соглашение о разграничении зон влияния в Иране, Афганистане и Тибете. Окончательное оформление союза «Антанта».
1912 г. – Ленский расстрел.
1912–1917 гг. – Деятельность IV Государственной думы.
1914 г., 1 августа – 1918 г., 9 ноября – Первая мировая война.
1915 г., август. – Создание Прогрессивного блока.
1916 г., май – «Брусиловский прорыв».
1917 г., февраль – Февральская буржуазно демократическая революция в России.
1917 г., 2 марта – Отречение Николая II от престола. Образование Временного правительства.
1917 г., май – Образование 1-го коалиционного Временного правительства.
1917 г., июнь – Деятельность I Всероссийского съезда Советов рабочих и солдатских депутатов.
1917 г., июль – Образование 2-го коалиционного Временного правительства.
1917 г., август – Корниловский мятеж.
1917 г., 1 сентября – Провозглашение России республикой.
1917 г., 24–26 октября – Вооруженное восстание в Петрограде. Свержение Временного правительства. II Всероссийский съезд Советов (Провозглашение России Республикой Советов.). Принятие декретов о мире и земле. 1918 г., январь. – Созыв и роспуск Учредительного собрания.
1918 г., 3 марта. – Заключение Брестского мира между Советской Россией и Германией. Россия потеряла Польшу, Литву, часть Латвии, Финляндию, Украину, часть Белоруссии, Карс, Ардаган и Батум. Договор аннулирован в ноябре 1918 г. после революции в Германии.
1918–1920 гг. – Гражданская война в России.
1918 г. – Принятие Конституции РСФСР.
1918–1921 г., март – Проведение советским правительством политики «военного коммунизма».
1918 г., июль – Расстрел царской семьи в Екатеринбурге.
1920–1921 гг. – Антибольшевистские восстания крестьян в Тамбовской и Воронежской областях («антоновщина»), Украине, Поволжье, Западной Сибири.
1921 г., март – Заключение Рижского мирного договора РСФСР с Польшей. К Польше отходили территории Западной Украины и Западной Белоруссии.
1921 г., февраль – март – Восстание матросов и солдат в Кронштадте против политики «военного коммунизма».
1921 г., март. – X съезд РКП(б). Переход к нэпу.
1922 г. – Генуэзская конференция.
1922 г., 30 декабря – Образование СССР.
1924 г. – Принятие Конституции СССР.
1925 г., декабрь – XIV съезд ВКП(б). Провозглашение курса на индустриализацию страны. Разгром «троцкистско зиновьевской оппозиции».
1927 г., декабрь – XV съезд ВКП(б). Провозглашение курса на коллективизацию сельского хозяйства.
1928–1932 гг. – Первый пятилетний план развития народного хозяйства СССР.
1929 г. – Начало сплошной коллективизации.
1930 г. – Завершение строительства Турксиба.
1933–1937 гг. – Второй пятилетний план развития народного хозяйства СССР.
1934 г. – Принятие СССР в Лигу Наций.
1934 г., 1 декабря – Убийство С. М. Кирова. Начало массовых репрессий.
1936 г. – Принятие Конституции СССР («победившего социализма»).
1939 г., 23 августа – Подписание пакта о ненападении с Германией.
1939 г, 1 сентября – 1945 г., 2 сентября – Вторая мировая война.
1939 г, ноябрь – 1940 г., март – Советско финляндская война.
1941 г., 22 июня – 1945 г., 9 мая – Великая Отечественная война.
1941 г., июль – сентябрь – Смоленское сражение.
1941 г, 5–6 декабря – Контрнаступление Красной армии под Москвой.
1942 г., 19 ноября – 1943 г, 2 февраля – Контрнаступление Красной армии под Сталинградом. Начало коренного перелома в ходе Великой Отечественной войны.
1943 г., июль – август – Курская битва.
1943 г., сентябрь – декабрь – Битва за Днепр. Освобождение Киева. Завершение коренного перелома в ходе Великой Отечественной войны.
1943 г., 28 ноября – 1 декабря – Тегеранская конференция глав правительств СССР, США и Великобритании.
1944 г., январь – Окончательная ликвидация блокады Ленинграда.
1944 г., январь – февраль – Корсунь Шевченковская операция.
1944 г., июнь – август – Операция по освобождению Белоруссии («Багратион»).
1944 г., июль – август – Львовско Сандомирская операция.
1944 г., август – Ясско Кишиневская операция.
1945 г., январь – февраль – Висло Одерская операция.
1945 г., 4–11 февраля – Крымская (Ялтинская) конференция глав правительств СССР, США и Великобритании.
1945 г., апрель – май – Берлинская операция.
1945 г., 25 апреля – Встреча на р. Эльбе у Торгау передовых советских и американских войск.
1945 г., 8 мая – Капитуляция Германии.
1945 г., 17 июля – 2 августа – Берлинская (Потсдамская) конференция глав правительств СССР, США и Великобритании.
1945 г, август – сентябрь – Разгром Японии. Подписание акта о безоговорочной капитуляции японских вооруженных сил. Окончание Второй мировой войны.
1946 г. – Начало «холодной войны».
1948 г. – Разрыв дипломатических отношений с Югославией.
1949 гг. – Начало компании по борьбе с «космополитизмом».
1949 г. – Создание Совета экономической взаимопомощи (СЭВ).
1949 г. – Создание в СССР ядерного оружия.
1953 г., 5 марта – Смерть И. С. Сталина.
1953 г., август – Сообщение об испытании в СССР водородной бомбы.
1953 г., сентябрь – 1964 г., октябрь – Избрание Н. С. Хрущева первым секретарем ЦК КПСС. Смещен с постов в октябре 1964 г.
1954 г. – Введена в действие Обнинская АЭС.
1955 г. – Образование Организации Варшавского договора (ОВД).
1956 г., февраль – ХХ съезд КПСС. Доклад Н. С. Хрущева «О культе личности и его последствиях».
1956 г., октябрь – ноябрь – Восстание в Венгрии; подавлено советскими войсками.
1957 г., 4 октября – Запуск в СССР первого в мире искусственного спутника Земли.
1961 г., 12 апреля – Полет Ю. А. Гагарина в космос.
1961 г., октябрь – XXII съезд КПСС. Принятие новой Программы партии – программы строительства коммунизма. 1962 г. – Карибский кризис.
1962г., июнь – Забастовка на Новочеркасском электровозостроительном заводе; расстрел демонстрации рабочих.
1963г., август – Подписание в Москве договора между СССР, США и Англией о запрещении испытаний ядерного оружия в атмосфере, под водой и космическом пространстве.
1965 г. – Начало проведения экономической реформы А.Н Косыгина.
1968 г. – Ввод войск стран-участниц Варшавского договора в Чехословакию.
1972 г., май – Подписание договора об ограничении стратегических наступательных вооружений (ОСВ 1) между СССР и США.
1975 г. – Совещание по безопасности и сотрудничеству в Европе (Хельсинки).
1979 г. – Подписание договора об ограничении стратегических наступательных вооружений (ОСВ 2) между СССР и США.
1979–1989 гг. – «Необъявленная война» в Афганистане.
1980 г., июль – август – Олимпийские игры в Москве.
1985 г., март – Избрание М.С. Горбачева генеральным секретарем ЦК КПСС.
1986 г., 26 апреля – Авария на Чернобыльской АЭС.
1987 г. – Заключение между СССР И США договора о ликвидации ракет средней и меньшей дальности.
1988 г. – ХIX партийная конференция. Провозглашение курса на реформу политической системы.
1989 г., май – июнь. – Первый съезд народных депутатов СССР.
1990 г., март – Избрание на Третьем съезде народных депутатов СССР М.С. Горбачева Президентом СССР. Исключение из Конституции 6-й статьи.
1990 г., 12 июня – Принята Декларация о государственном суверенитете РСФСР.
1991 г. 12 июня – Избрание Б.Н. Ельцина Президентом РСФСР.
1991 г., июль – Подписание договора между СССР и США о сокращении и ограничении стратегических наступательных вооружений (ОСНВ 1).
1991 г., 19–21 августа – Попытка государственного переворота (ГКЧП).
1991 г., 8 декабря – Беловежские соглашение о роспуске СССР и создание СНГ.
1991 г., 25 декабря – Сложение М.С. Горбачевым полномочий Президента СССР.
1992 г. – Начало проведения радикальной экономической реформы Е.Т. Гайдара.
1993 г., январь – Подписание договора между Россией и США о сокращении стратегических наступательных вооружений (СНВ 2).
1993 г., 3–4 октября – Вооруженные столкновения сторонников Верховного Совета с правительственными войсками в Москве.
1993 г., 12 декабря – Выборы в Федеральное собрание – Государственную Думу и Совет Федерации и референдум по проекту Конституции РФ.
1994 г. – Присоединение РФ к программе НАТО «Партнерство во имя мира».
1994 г., декабрь – Начало широкомасштабных действий против чеченских сепаратистов.
1996 г. – Вступление России в Совет Европы.
1996 г., июль – Избрание Б.Н. Ельцина Президентом РФ (на второй срок).
1997 г. – Создание по инициативе Д.С. Лихачева государственного телеканала «Культура».
1998 г., август – Финансовый кризис в России (дефолт).
1999 г., сентябрь – Начало антитеррористической операции в Чечне.
2000 г., март – Избрание В.В. Путина Президентом РФ.
2000 г. – Присуждение Нобелевской премии по физике Ж.И. Алферову за фундаментальные исследования в сфере информационных и телекоммуникационных технологий.
2002 г. – Договор между Россией и США о взаимном сокращении ядерных боеголовок.
2003 г. – Присуждение Нобелевской премии по физике А.А. Абрикосову и В.Л. Гинзбургу за работы в области квантовой физики, в частности за исследования сверхпроводимости и сверхтекучести.
2004 г., март – Избрание В.В. Путина Президентом РФ (на второй срок).
2005 г. – Создание Общественной палаты.
2006 г. – Начало осуществления программы национальных проектов в области сельского хозяйства, жилищного строительства, здравоохранения и образования.
2008 г., март – Избрание Д.А. Медведева Президентом РФ.
2008 г., август – Вторжение грузинских войск в Южную Осетию. Проведение российской армией операции по принуждению Грузии к миру. Признание Россией независимости Абхазии и Южной Осетии.
2008 г., ноябрь – Принятие закона об увеличении срока полномочий Госдумы и Президента РФ (5 и 6 лет соответственно).
"""
datas = data.split("\n")
dotenv.load_dotenv()
token_yan = os.environ['token_yan']
en_alph = 'abcdefghijklmnopqrstuvwxyz'
ru_alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def get_date(inp):
    res = []
    if len(inp) == 3:
        for i in datas:
            if i[:3] == inp:
                res.append(i)
    elif len(inp) == 4:
        for i in datas:
            if i[:4] == inp:
                res.append(i)
    if len(res) != 0:
        return '\n'.join(res)
    return 'У нас нет такой даты'


def create_audio(message):
    if message.text.strip().lower()[0] in en_alph:
        lang = 'en'
    else:
        lang = 'ru'
    tts = gTTS(message.text, lang)
    tts.save('says.mp3')
    file = open('says.mp3', 'rb')
    return file


translate = YandexTranslate(token_yan)


def translating(text):
    try:
        if text.strip()[0].lower() in en_alph:
            a = 'en-ru'
        else:
            a = 'ru-en'
        return translate.translate(text, a)['text'][0]
    except:
        return 'Ошибка проверьте предыдущее сообщение'


def check_orphographic(text, lang="ru_RU"):
    try:
        d = enchant.Dict(lang)  # создание словаря для US English (англ язык)
        words = text.split(' ')
        if d.check(text) or (' ' in text and len([x for x in text.split(' ') if not d.check(x)]) == 0):
            return 'Все правильно'  # проверка орфографии (верно)
        res = []
        for word in words:
            if d.check(word):
                res.append(word)
            else:
                res.append(word.upper())
        return ' '.join(res)
    except:
        pass
    return 'Ошибка, проверьте предыдущее сообщение'


def lit_bio_search(what, small=False):
    try:
        some = wikipedia.set_lang("ru")
        some = wikipedia.page(what)
        res = []
        if small:
            search = wikipedia.summary(sentences=10, title=what)  # sentenses - кол-во предложений
            res.append(search)
        else:
            res.append(some.content)
        res.append("\nИсточник: " + some.url)
        return ' '.join(res)
    except:
        return 'Ошибка'


def get_composition(message, bot, keyboard):
    try:
        s = message.text
        con = sqlite3.connect('compositions.db')
        cur = con.cursor()
        s = s.lower()
        s.replace('Сочинение', '')
        s = re.sub(r'\s', '', s)
        s = re.sub(r'[^\w\s]', '', s)
        s = '%' + s + '%'
        res = cur.execute("SELECT content FROM compositions WHERE Name LIKE '{}'".format('%' + s + '%')).fetchone()[0]
        con.close()
        if len(res) != 0:
            a = res.split('\n')
            a = [x for x in a if len(x) != 0]
            q = '\n'.join(a)
            if len(q) > 4000:
                bot.send_message(message.chat.id, q[:4000], reply_markup=keyboard)
                bot.send_message(message.chat.id, q[4000:8000], reply_markup=keyboard)
                try:
                    bot.send_message(message.chat.id, q[8000:12000], reply_markup=keyboard)
                except:
                    pass
                try:
                    bot.send_message(message.chat.id, q[12000:16000], reply_markup=keyboard)
                except:
                    pass
            else:
                bot.send_message(message.chat.id, q, reply_markup=keyboard)
    except:
        bot.send_message(message.chat.id, 'Сочинение не найдено', reply_markup=keyboard)


def convert_base(num, to_base=10, from_base=2):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]

