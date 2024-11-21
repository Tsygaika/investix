import matplotlib.pyplot as plt
from tkinter import *


def clicked():
    plt.close('all')    #if windows was opened, we will close it and open new again

    years = years_.get()
    inflation = inflation_.get()    #getting string data from it
    monthly = monthly_.get()
    profitability = profitability_.get()


    #antidemin
    if any((not x.isdigit()) for x in [years,inflation,monthly,profitability]):     #if one of the variables is not
        from tkinter import messagebox                                  #integer, we will display an error message
        messagebox.showinfo('Негодяй', 'Я знал, что ты это сделаешь. Не делай так больше!')
        return

    years = int(years)  #converting to integer format
    inflation = int(inflation)  / 100 + 1
    monthly = int(monthly)
    profitability = int(profitability) / 100 + 1


    #alghoritm
    amount = []     #the list of years amounts
    without_invest = []
    years_list = []     #the list of years
    general_amount = 0      #amount at the end of the year
    general_amount_2 = 0    #amount for "without_invest" list
    for i in range(1, years + 1):
        general_amount += 12 * monthly
        general_amount = general_amount * profitability / inflation
        general_amount_2 = (general_amount_2 + 12 * monthly) / inflation

        amount.append(general_amount)
        without_invest.append(general_amount_2)
        years_list.append(str(i))

    #showing plots
    plt.plot(years_list, amount, label=f'Если откладывать под {format(profitability*100-100,'.1f')}% годовых')
    plt.plot(years_list, without_invest, label='Если просто откладывать')
    plt.legend()    #show legend
    plt.title("График накоплений")
    plt.xlabel("Года\nСумма в рублях указана относительно сегодняшнего дня. Чтобы узнать \nсумму в конце накопления, в поле 'Уровень роста цен' впишите 0.")
    plt.ylabel("Рубли")
    plt.ylabel("Рубли")
    #plt.text(0, 0, "",fontsize=7)
    plt.subplots_adjust(bottom=0.2)    #setting bottom padding
    plt.show()


top_padding = 20    #some constants
left_padding = 60
back_color = 'white'
font = 'Calibri 11'
no_hover = '#D4D4D4'    #color for entry cell when cursor is not on it
hover = 'black'         #color for entry cell when cursor is on it
bg_cell = '#FAFAFA'     #background color for entry cell

#default settings
entry_seetings = {"width":7, "relief":"flat", "highlightbackground":no_hover, "highlightcolor":hover, "bg":bg_cell,
           "highlightthickness":1}
text_settings = {"bg":back_color, "font":font}

window = Tk()
window.title("График накоплений")
window.geometry('400x200')
window.configure(bg=back_color)
window.resizable(False, False)  #disabling the ability of changing window size


#the first row
text_1 = Label(window, text_settings, text="Срок инвестирования: ")
text_1.grid(column=0, row=0, sticky=W, padx=(left_padding, 0), pady=(top_padding, 0))  #also adding top and left padding

years_ = Entry(window, entry_seetings)
years_.grid(column=1, row=0, pady=(top_padding, 0)) #adding top padding
years_.focus()      #focus on the top cell

text_2 = Label(window, text_settings, text=" лет")
text_2.grid(column=2, row=0, pady=(top_padding, 0))    #also adding top padding


#the second row
text_1 = Label(window, text_settings, text="Уровень роста цен: ")
text_1.grid(column=0, row=1, sticky=W, padx=(left_padding, 0))  #also adding left padding

inflation_ = Entry(window, entry_seetings)
inflation_.grid(column=1, row=1)

text_2 = Label(window, text_settings, text=" %")
text_2.grid(column=2, row=1, sticky=W)


#the third row
text_1 = Label(window, text_settings, text="Ежемесячные инвестиции: ")
text_1.grid(column=0, row=2, sticky=W, padx=(left_padding, 0))  #also adding left padding

monthly_ = Entry(window, entry_seetings)
monthly_.grid(column=1, row=2)

text_2 = Label(window, text_settings, text=" руб.")
text_2.grid(column=2, row=2, sticky=W)


#the fourth row
text_1 = Label(window, text_settings, text="Годовая доходность: ")
text_1.grid(column=0, row=3, sticky=W, padx=(left_padding, 0))  #also adding left padding

profitability_ = Entry(window, entry_seetings)
profitability_.grid(column=1, row=3)

text_2 = Label(window, text_settings, text=" %")
text_2.grid(column=2, row=3, sticky=W)


#the button
def on_enter(e):    #the button when hover
    btn['background'] = '#EBEBEB'
    btn['highlightcolor'] = 'gray'

def on_leave(e):    #the button when cursor leave it
    btn['background'] = 'white'
    btn['highlightcolor'] = 'black'

lbl = Label(window, text=" ", bg=back_color, font="Calibri 15")   #space
lbl.grid(column=0, row=5)
btn = Button(window, text_settings, text="Показать график", command=clicked, highlightcolor="black",
           highlightthickness=1, default='active', relief=FLAT, bd=0)
btn.grid(row=6, column=0, sticky=E, columnspan=3, padx=(0, 75)) #setting personal shift for button
btn.bind("<Enter>", on_enter)   #linking the hover button state with the same name function
btn.bind("<Leave>", on_leave)   #linking the button state when cursor leave it with the same name function

window.mainloop()