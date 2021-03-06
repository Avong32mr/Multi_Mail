import datetime


default_names = ["Ephraim", "John", "Edward", "Charlie", "Ronald", "Sandra", "Chigozie", "Micheal","Fidel","Jotham","Chris","Benjamin","Aliyu","Kennedy","Moses","Isreal","Shalom","Abel","Babangida","Sheriff","Ango","Kenway","Adamu","Gandu","Jack","Sparrow"]
default_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99, 232.3,150,392.8,882,62,72.5,488,28.34,64,419,338,432,350,530,620,58,63.895,10.985]

unf_message = """Hi {name}! 
Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}.
Have a great one!
Team Uplift
"""


def make_messages(names, amounts):
    messages = []
    if len(names) == len(amounts):
        i = 0
        today = datetime.date.today()
        text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        for name in names:
            new_amount = "%.2f" %(amounts[i])
            new_msg = unf_message.format(
                    name=name,
                    date=text,
                    total=new_amount
                )
            i += 1
            print(new_msg)



make_messages(default_names, default_amounts)
