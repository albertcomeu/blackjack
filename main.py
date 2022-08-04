#импортируем библиотеки
#tkinter - для создания gui,PIL - для работы с JPG,random - для перемешивания карт
import time
import tkinter as tk
from tkinter.ttk import Combobox
import tkinter.messagebox
from PIL import Image, ImageTk
import random


class Card():
    #каждый экземпляр класса будет иметь значение и масть(value,suit)
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    #каждой карте в игре соответствует числовое значение данный метод позволяет его получить
    def get_card_value(self):
        if self.value in 'JQK':
            return 10

        elif self.value == 'A':
            return 11

        else:
            return '23456789'.index(self.value)+2

    #функция для вывода значения и масти
    def __str__(self):
        return (self.value + self.suit)

class Hand():
    #класс Hand состоит из экземпляров класса Card которые он хранит в списке cards
    def __init__(self):
        self.cards = []

    #функция добавляет в список новую карту
    def add_card(self,card):
        self.cards.append(card)

    #функция позволяет получить суммарное числовое значение всех карт и их количество
    def get_value(self):
        res = 0

        for card in self.cards:
            if(card.get_card_value() == 'A' and res <= 21):
                res += card.get_card_value()

            elif(card.get_card_value() == 'A' and res > 21):
                res += 1

            else:
                res += card.get_card_value()


        return res

    #функция для вывод информации о картах
    def __str__(self):
        res = ""

        for card in self.cards:
            res += str(card) + " "
        res += str(self.get_value())
        return res

#класс Deck создаёет колоду карт и перемешивает её с помощью метода shuffle
class Deck():
    def __init__(self):
        values = '23456789JQKA'
        suits = 'SCDH'

        self.cards = [Card(v,s) for v in values for s in suits]

        random.shuffle(self.cards)

    #функция позволяет получить карту и удаить её из колоды или проще говоря сдать карту
    def deal_card(self):
        return self.cards.pop()


#основной класс программы
class Game:
    root = tk.Tk()#создаём рабочую область


    def __init__(self):
        self.root = Game.root
        self.root.geometry('640x480')#задаём размеры окна

        self.root.resizable(False, False)

        #открываем изображение и с помощью метода resize библиотеки Image растягиваем изображение меню по размеру окна
        img = Image.open('images/menubackground.jpg')
        imag = img.resize((640, 480), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(imag)#этот метод позволяет использовать изображение tkinter
        panel = tk.Label(self.root, image=image)
        panel.pack(side="top", fill="both", expand="no")#pack размещает изобржаение в качестве фона

        #создаёем две кнопки первая при нажатии очищает все виджеты и переносит в меню выбора кол-во игроков,вторая закрывает окно
        self.b1 = tk.Button(self.root, text='начать игру', command=lambda: [self.b1.place_forget(),self.b2.place_forget(),Game.players_num(self)],bg="black", fg="orange")
        self.b2 = tk.Button(self.root, text='выйти', command=self.root.quit, bg="black", fg="orange")

        #функции для размещения кнопок
        self.b1.place(x=250, y=220)
        self.b2.place(x=250, y=260)

        tk.messagebox.showwarning("", "Азартные игры - плохо, будьте осторожны!")

        #запускает окно и выполняет вышеописаные действия
        self.root.mainloop()

    @staticmethod
    def players_num(self):
        #нажатие в предыдущей функции кнопки "начать игру" запускает эту функцию
        #с помощью combobox пользователь выбирает количество игроков
        combo = Combobox()
        combo['values'] = (1, 2, 3)
        combo.current(1)
        combo.place(x=250, y=240)
        #после выбора количества игроков пользователь нажимает кнопку "начать игру и запускается основаная функция игры board"
        lbl = tk.Label(text="выберете кол-во игроков",font = ("Arial Bold",10),bg="black", fg="orange")
        b3 = tk.Button(text='начать игру', command=lambda:[b3.place_forget(), combo.place_forget(), lbl.place_forget(),Game.board(combo.get())], bg="black", fg="orange")
        lbl.place(x=250, y=220)
        b3.place(x=250, y=260)


    @classmethod
    def cropp(self,card):
        #функция которая получая данные карты(значение и масть) открывает файл со всеми картами и ищет нужную
        img = Image.open('images/cards.jpg')

        if('S' in card):
            x1, x2, x3, x4 = 15, 40, 820, 144

        elif ('H' in card):
            x1, x2, x3, x4 = 15, 125, 820, 228

        elif('C' in card):
            x1, x2, x3, x4 = 15, 213, 820, 315

        elif ('D' in card):
                x1, x2, x3, x4 = 15, 300, 820, 400

        if '2' in card:
            cropped = img.crop((x1+67, x2, x3-685, x4-22))

        elif '3' in card:
            cropped = img.crop((x1+129, x2, x3-622, x4-22))

        elif '4' in card:
            cropped = img.crop((x1+193, x2, x3-560, x4-22))

        elif '5' in card:
            cropped = img.crop((x1+254, x2, x3-499, x4-22))

        elif '6' in card:
            cropped = img.crop((x1+316, x2, x3-436, x4-22))

        elif '7' in card:
            cropped = img.crop((x1+378, x2, x3-373, x4-22))

        elif '8' in card:
            cropped = img.crop((x1+439, x2, x3-312, x4-22))

        elif '9' in card:
            cropped = img.crop((x1+500, x2, x3-251, x4-22))

        elif '10' in card:
            cropped = img.crop((x1+563, x2, x3-188, x4-22))

        elif 'J' in card:
            cropped = img.crop((x1+624, x2, x3-126, x4-22))

        elif 'Q' in card:
            cropped = img.crop((x1+687, x2, x3-64, x4-22))

        elif 'K' in card:
            cropped = img.crop((x1+747, x2, x3-3, x4-22))

        elif 'A' in card:
            cropped = img.crop((x1+6, x2, x3-745, x4-22))

        self.cropped = cropped
        return self.cropped

    @classmethod
    def drawpic(self,card,x,y):
        #функция поолучая информацию о карте(значаение и масть) с помощью функции cropp отрисовывает изображение карты на игровом поле
        self.image = ImageTk.PhotoImage(Game.cropp(card).resize((60, 90), Image.ANTIALIAS))
        panel1 = tk.Label(self.root, image=self.image)
        self.pics.append(self.image)
        panel1.place(x=x, y=y)

    @classmethod
    def choice(self,psum,dsum):
        #функция которая в зависимости от значений карт на руках и дилера определяет брать боту карту или нет
        if(psum == 12 and (dsum in (5,6))):
            return 'no'

        elif(psum in (13,14) and dsum in (3,4,5,6)):
            return 'no'

        elif(psum in (15,16) and dsum in (2,3,4,6)):
            return 'no'

        elif(psum >= 17):
            return 'no'

        else:
            return 'yes'

    @classmethod
    def board(self,pn):
        #основная функция игры
        #этот цикл удалет все предыдущие виджеты
        for widget in self.root.winfo_children():
            widget.destroy()

        #открываем изобржаение игрового поля и ставим его на фон
        img = Image.open('images/boardbg.jpg')

        imag = img.resize((640, 480), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(imag)
        panel = tk.Label(self.root,image=image)
        panel.pack(side="top", fill="both", expand="no")

        #создание колоды
        d = Deck()

        #список для сохранения ссылок на использованные изображения карт
        #(если его не использоваться будет ортрисовываться только последняя)
        self.pics = []

        #создание списка для хранения экземпляров класса Hand() длякаждого игрока
        players_hand = []

        #создание экземпляров класса Hand()
        for i in range(int(pn)):
            players_hand.append(Hand())

        #создание экземпляра класса Hand() для дилера
        dealer_hand = Hand()

        for i in range(1,len(players_hand)):
            #в зависимости от номера игрока даёт ему две карты,располагает их на нужных позициях и отрисовывает
            if (i == 1): x, y = 85, 205

            if (i == 2): x, y = 500, 205

            players_hand[i].add_card(d.deal_card())
            players_hand[i].add_card(d.deal_card())

            #список карт для текущего игрока(нужен для правильной передачи информации для отрисовки)
            cardlist = players_hand[i].__str__().split(sep=' ')

            for j in range(len(cardlist) - 1):
                self.count = 0
                Game.drawpic(cardlist[j], x, y)
                x += 20

        #раздаёт пользователю две карты
        players_hand[0].add_card(d.deal_card())
        players_hand[0].add_card(d.deal_card())

        #раздаёт дилеру две карты
        dealer_hand.add_card(d.deal_card())

        #список карт пользователя(нужен для правильной передачи информации для отрисовки)
        cardlist = players_hand[0].__str__().split(sep=' ')

        self.x,self.y = 296,270#задаёт координаты для отрисовки карт пользователя

        #отрисовка карт пользователя
        for i in range(len(cardlist)-1):
            Game.drawpic(cardlist[i],self.x,self.y)
            self.x += 20

        #задаёт координаты для отрисовки карт дилера
        self.x,self.y = 296,50

        #отрисовка карт дилера
        Game.drawpic(dealer_hand.__str__()[:2],self.x,self.y)

        #понадобится позднее для проверки условий
        in_game = True

        self.x,self.y = 316,270#задаёт координаты для отрисовки карт пользователя

        #цикл игры

        while (players_hand[0].get_value() < 21):
            #пока сумма очков карт < 21 пользователю предлагается выбор взять карту или нет
            q = tk.messagebox.askquestion('', 'взять карту(д/н)?')
            if (q == 'yes'):
                #если пользователь выбирает взять,то алгоритм выдает её ему и отрисовывает на игровом поле
                self.x += 20
                players_hand[0].add_card(d.deal_card())
                cardlist = players_hand[0].__str__().split(sep=' ')
                Game.drawpic(cardlist[len(cardlist)-2],self.x,self.y)

                if (players_hand[0].get_value() > 21):
                    #выполняется в случае если сумма очков больше 21
                    tk.messagebox.showinfo('', 'вы проиграли!')
                    if(int(pn) > 1): break #если игроков > 1 то ход переходит к ним

                    else: in_game = False #иначе если игорк 1(т.е только пользователь и дилер то игра заканчивается)

            else:
                #в случае если пользователь отказался брать карту то ход переходит к другим
                tk.messagebox.showinfo('', 'вы не взяли карту')
                break

        for i in range(1,len(players_hand)):#цикл для хода ботов(игроков которыми пользователь не управляет)
            #в зависимости от того какой именно бот задаются координаты для отрисовки
            if (i == 1):
                x, y = 125, 205

            if (i == 2):
                x, y = 540, 205

            while (players_hand[i].get_value() < 21):
                q = Game.choice(players_hand[i].get_value(),dealer_hand.get_value())#вызов функции choice
                #для выбор брать или не брать карту

                if (q == 'yes'):
                    tk.messagebox.showinfo('', 'игорк ' + str((i+1)) + ' взял карту')
                    players_hand[i].add_card(d.deal_card())
                    cardlist = players_hand[i].__str__().split(sep=' ')
                    Game.drawpic(cardlist[len(cardlist)-2],x,y)
                    x+= 20

                    if (players_hand[i].get_value() > 21):
                        tk.messagebox.showinfo('', 'игорк ' + str((i+1)) + ' проиграл!')
                        break

                else:
                    tk.messagebox.showinfo('', 'игорк '+str((i+1)) +' не взял карту')
                    break

        if (in_game):
            #если игра идёт и не выбыли все игорки то дилер набирает карты пока сумма их очков < 17
            self.x, self.y = 316, 50

            while (dealer_hand.get_value() < 17):
                dealer_hand.add_card(d.deal_card())
                dealerlist = list(dealer_hand.__str__().split(sep=' '))

                Game.drawpic(dealerlist[len(dealerlist)-2],self.x,self.y)#отрисовка взятой карты
                self.x += 20

                if (dealer_hand.get_value() > 21):
                    #если сумма очков дилера > 21 игра заканчивается его поражением
                    tk.messagebox.showinfo('', 'дилер проиграл!')
                    in_game = False

        if (in_game):
            #если остался дилер и не все игроки выбыли то создаём словарь элемент которого состоит из номера игрока и суммы его очков
            slist = {}
            for i in range(len(players_hand)):
                if players_hand[i].get_value() <= 21: slist['игорк ' + str(i+1)] = players_hand[i].get_value()#если сумма очков > 21то
                #значение в словарь не добавляется

            slist['dealer'] = dealer_hand.get_value()
            # находит максимальное значение в словаре
            maxs = max(slist.values())

            winner = 0

            for k, v in slist.items():
                if v == maxs:
                    winner = k

            tk.messagebox.showinfo('', winner + ' победил набрав больше всего очков (' + str(maxs) + ')')
            #и выводит номер победителя с сообщением о победе

        q1 = tk.messagebox.askquestion('', 'сыграть ещё(д/н)?')#выбор сыграть ещё или нет

        if(q1 == 'yes'):
            #если выбрано сыграть то удаляются все виджеты с окана и вызывается класс Game
            for widget in self.root.winfo_children():
                widget.destroy()
            Game()

        else:
            #в случае нет то окно игры закрывается
            exit(0)

        self.root.mainloop()#для работы и отображения виджетов tkinter


if __name__ == "__main__":
    g1 = Game()#первый вызов класса Game
    time.sleep(5)