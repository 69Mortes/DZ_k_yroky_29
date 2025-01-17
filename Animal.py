class Animals:                          # Создаем класс на тему животных
        def __init__(self,name,poroda,ves):        # Создаем конструктор, указав в скобках атрибуты
                self.name = name                # Динамический атрибут name
                self.poroda = poroda                  # Динамический атрибут poroda
                self.ves = ves

        # Создаем методы класса
        def hello(self):
                print(f"Животное {self.name}  принадлежит к Семейству {self.poroda}. Обитают в Африке и могут достигать в весе до {self.ves} кг.")

        def pro(self):
                print("____________________________________________________\n"
                        f"тут должен быть текст, но {self.name} его съел!\n"
                        "--_-____________ -- --- _____________ -----------\n")

        def slon(self):
                print(f"Встречаются африканские {self.name}ы на территории всего континента,\n"
                        "как в тропических лесах Западной и Центральной Африки,\n"
                        "так и на юге Сахары. Животные приспосабливаются к любой среде обитания,\n"
                        "лишь бы в ней было легко найти пищу и воду.\n"
                         f"{self.name} являются самыми крупными на земле млекопитающими.\n")

        def zhiraf(self):
                print(f"{self.name} является самым высоким на планете парнокопытным млекопитающем.\n"
                      f"Их высота составляет 5,5 – 6,1 м, причем одну треть занимает стройная шея.\n"
                      f"Самки обычно немного ниже и легче. Ареал обитания жирафов ближе к югу и юго-востоку от Сахары.\n")

        def zebra(self):
                print("Полосатые животные делятся на виды: саванная, пустынная, горная. Обитают обычно в степях.\n"
                        "Длина тела зебры приблизительно 2 м. Животные – травоядные. Чтобы удовлетворить организм\n"
                        f"достаточным количеством калорий, {self.name} употребляет за сутки 5-7 кг пищи.\n")

        def lev(self):
                print(f"{self.name} - это животное млекопитающее и является хищником. Наиболее крупными особями являются самцы.\n"
                      f"Их вес и размер тела зависят от подвида животного.\n"
                      f"В длина туловища – от 2,5 м без учета хвоста, высота холки – 120-125 см.\n"
                      f"Африканские львы обитают к югу от Сахары. Излюбленные места проживания хищников – саванны.\n")

        def nosorog(self):
                print(f"{self.name} является вторым по размеру животным континента. Его длина – 2-5 м, высота – 1-3 м.\n"
                      "Толстокожие млекопитающие питаются растительностью, съедая за сутки около 72 кг травы и листьев.\n"
                      "Отличительная особенность животного – это рог, который состоит из белка каротина и может достигать до 158 см.\n"
                      "в Африке проживает два вида носорогов: черные и белые.\n")