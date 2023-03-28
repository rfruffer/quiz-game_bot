from telegram import Bot
from telegram import Update
from telegram import ParseMode
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import CallbackQueryHandler
from telegram.utils.request import Request
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
import csv, io, datetime
import sys
import io

sys.stdout = io.open(sys.stdout.fileno(), 'w', encoding='utf8')

import table
print ("Begining work...")

table.createTables()

channel_chat_id = 111 #main

consts = {
    "expectedDate":"25/12/2021 23:59"

}

BUTTON_INLINE_START = "button_inline_start"
BUTTON_INLINE_QUESTION1_1 = "button_inline_question1_1"
BUTTON_INLINE_QUESTION1_2 = "button_inline_question1_2"
BUTTON_INLINE_QUESTION1_3 = "button_inline_question1_3"
BUTTON_INLINE_QUESTION1_4 = "button_inline_question1_4"

BUTTON_INLINE_QUESTION2_1 = "button_inline_question2_1"
BUTTON_INLINE_QUESTION2_2 = "button_inline_question2_2"
BUTTON_INLINE_QUESTION2_3 = "button_inline_question2_3"
BUTTON_INLINE_QUESTION2_4 = "button_inline_question2_3"

BUTTON_INLINE_QUESTION3_1 = "button_inline_question3_1"
BUTTON_INLINE_QUESTION3_2 = "button_inline_question3_2"
BUTTON_INLINE_QUESTION3_3 = "button_inline_question3_3"
BUTTON_INLINE_QUESTION3_4 = "button_inline_question3_4"

BUTTON_INLINE_QUESTION4_1 = "button_inline_question4_1"
BUTTON_INLINE_QUESTION4_2 = "button_inline_question4_2"
BUTTON_INLINE_QUESTION4_3 = "button_inline_question4_3"
BUTTON_INLINE_QUESTION4_4 = "button_inline_question4_4"

BUTTON_INLINE_QUESTION5_1 = "button_inline_question5_1"
BUTTON_INLINE_QUESTION5_2 = "button_inline_question5_2"
BUTTON_INLINE_QUESTION5_3 = "button_inline_question5_3"
BUTTON_INLINE_QUESTION5_4 = "button_inline_question5_4"

BUTTON_INLINE_QUESTION6_1 = "button_inline_question6_1"
BUTTON_INLINE_QUESTION6_2 = "button_inline_question6_2"
BUTTON_INLINE_QUESTION6_3 = "button_inline_question6_3"
BUTTON_INLINE_QUESTION6_4 = "button_inline_question6_4"

BUTTON_INLINE_QUESTION7_1 = "button_inline_question7_1"
BUTTON_INLINE_QUESTION7_2 = "button_inline_question7_2"
BUTTON_INLINE_QUESTION7_3 = "button_inline_question7_3"
BUTTON_INLINE_QUESTION7_4 = "button_inline_question7_4"

BUTTON_INLINE_QUESTION8_1 = "button_inline_question8_1"
BUTTON_INLINE_QUESTION8_2 = "button_inline_question8_2"
BUTTON_INLINE_QUESTION8_3 = "button_inline_question8_3"
BUTTON_INLINE_QUESTION8_4 = "button_inline_question8_4"

BUTTON_INLINE_QUESTION9_1 = "button_inline_question9_1"
BUTTON_INLINE_QUESTION9_2 = "button_inline_question9_2"
BUTTON_INLINE_QUESTION9_3 = "button_inline_question9_3"
BUTTON_INLINE_QUESTION9_4 = "button_inline_question9_4"

BUTTON_INLINE_QUESTION10_1 = "button_inline_question10_1"
BUTTON_INLINE_QUESTION10_2 = "button_inline_question10_2"
BUTTON_INLINE_QUESTION10_3 = "button_inline_question10_3"
BUTTON_INLINE_QUESTION10_4 = "button_inline_question10_4"

#Кнопки под сообщением#
def get_base_inline_keyboard_start():
    keyboard = [
        [
            InlineKeyboardButton("Начинаем! 🎓", callback_data=BUTTON_INLINE_START),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

def get_base_inline_keyboard_question1():
    keyboard = [
        [
            InlineKeyboardButton("Ответ 1", callback_data=BUTTON_INLINE_QUESTION1_1),
            InlineKeyboardButton("Ответ 2", callback_data=BUTTON_INLINE_QUESTION1_2),
        ],
        [
            InlineKeyboardButton("Ответ 3", callback_data=BUTTON_INLINE_QUESTION1_3),
            InlineKeyboardButton("Ответ 4", callback_data=BUTTON_INLINE_QUESTION1_4),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

def get_base_inline_keyboard_question2():
    keyboard = [
        [
            InlineKeyboardButton("Ответ 1", callback_data=BUTTON_INLINE_QUESTION2_1),
            InlineKeyboardButton("Ответ 2", callback_data=BUTTON_INLINE_QUESTION2_2),
        ],
        [
            InlineKeyboardButton("Ответ 3", callback_data=BUTTON_INLINE_QUESTION2_3),
            InlineKeyboardButton("Ответ 4", callback_data=BUTTON_INLINE_QUESTION2_4),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

def get_base_inline_keyboard_question3():
    keyboard = [
        [
            InlineKeyboardButton("Ответ 1", callback_data=BUTTON_INLINE_QUESTION3_1),
            InlineKeyboardButton("Ответ 2", callback_data=BUTTON_INLINE_QUESTION3_2),
        ],
        [
            InlineKeyboardButton("Ответ 3", callback_data=BUTTON_INLINE_QUESTION3_3),
            InlineKeyboardButton("Ответ 4", callback_data=BUTTON_INLINE_QUESTION3_4),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

def get_base_inline_keyboard_question4():
    keyboard = [
        [
            InlineKeyboardButton("Ответ 1", callback_data=BUTTON_INLINE_QUESTION4_1),
            InlineKeyboardButton("Ответ 2", callback_data=BUTTON_INLINE_QUESTION4_2),
        ],
        [
            InlineKeyboardButton("Ответ 3", callback_data=BUTTON_INLINE_QUESTION4_3),
            InlineKeyboardButton("Ответ 4", callback_data=BUTTON_INLINE_QUESTION4_4),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

def get_base_inline_keyboard_question5():
    keyboard = [
        [
            InlineKeyboardButton("Ответ 1", callback_data=BUTTON_INLINE_QUESTION5_1),
            InlineKeyboardButton("Ответ 2", callback_data=BUTTON_INLINE_QUESTION5_2),
        ],
        [
            InlineKeyboardButton("Ответ 3", callback_data=BUTTON_INLINE_QUESTION5_3),
            InlineKeyboardButton("Ответ 4", callback_data=BUTTON_INLINE_QUESTION5_4),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

def get_base_inline_keyboard_question6():
    keyboard = [
        [
            InlineKeyboardButton("Ответ 1", callback_data=BUTTON_INLINE_QUESTION6_1),
            InlineKeyboardButton("Ответ 2", callback_data=BUTTON_INLINE_QUESTION6_2),
        ],
        [
            InlineKeyboardButton("Ответ 3", callback_data=BUTTON_INLINE_QUESTION6_3),
            InlineKeyboardButton("Ответ 4", callback_data=BUTTON_INLINE_QUESTION6_4),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

def get_base_inline_keyboard_question7():
    keyboard = [
        [
            InlineKeyboardButton("Ответ 1", callback_data=BUTTON_INLINE_QUESTION7_1),
            InlineKeyboardButton("Ответ 2", callback_data=BUTTON_INLINE_QUESTION7_2),
        ],
        [
            InlineKeyboardButton("Ответ 3", callback_data=BUTTON_INLINE_QUESTION7_3),
            InlineKeyboardButton("Ответ 4", callback_data=BUTTON_INLINE_QUESTION7_4),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

def get_base_inline_keyboard_question8():
    keyboard = [
        [
            InlineKeyboardButton("Ответ 1", callback_data=BUTTON_INLINE_QUESTION8_1),
            InlineKeyboardButton("Ответ 2", callback_data=BUTTON_INLINE_QUESTION8_2),
        ],
        [
            InlineKeyboardButton("Ответ 3", callback_data=BUTTON_INLINE_QUESTION8_3),
            InlineKeyboardButton("Ответ 4", callback_data=BUTTON_INLINE_QUESTION8_4),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

def get_base_inline_keyboard_question9():
    keyboard = [
        [
            InlineKeyboardButton("Ответ 1", callback_data=BUTTON_INLINE_QUESTION9_1),
            InlineKeyboardButton("Ответ 2", callback_data=BUTTON_INLINE_QUESTION9_2),
        ],
        [
            InlineKeyboardButton("Ответ 3", callback_data=BUTTON_INLINE_QUESTION9_3),
            InlineKeyboardButton("Ответ 4", callback_data=BUTTON_INLINE_QUESTION9_4),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

def get_base_inline_keyboard_question10():
    keyboard = [
        [
            InlineKeyboardButton("Ответ 1", callback_data=BUTTON_INLINE_QUESTION10_1),
            InlineKeyboardButton("Ответ 2", callback_data=BUTTON_INLINE_QUESTION10_2),
        ],
        [
            InlineKeyboardButton("Ответ 3", callback_data=BUTTON_INLINE_QUESTION10_3),
            InlineKeyboardButton("Ответ 4", callback_data=BUTTON_INLINE_QUESTION10_4),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

#Нижние кнопки#
def get_base_reply_keyboard():
    keyboard = [
        [
            KeyboardButton("База данных")
        ],
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
    )

#Обработчик ВСЕХ кнопок со ВСЕХ клавиатур#
def keyboard_callback_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data
    chat_id = update.effective_message.chat_id

    try :
        isDone = table.getStatus(chat_id) == "Successful"
    except:
        isDone = False

    if (expectedDate()):
        context.bot.send_message(
            chat_id = chat_id,
            text="Конкурс завершен",
            parse_mode=ParseMode.HTML
        )
        return

    if isDone:
        ball = table.getTotal(chat_id)
        context.bot.send_message(
            chat_id = chat_id,
            text=winMessage(ball),
            parse_mode=ParseMode.HTML
        )

    elif data == BUTTON_INLINE_START: #Начинаем! 🎓
        context.bot.edit_message_text(
            chat_id=chat_id,
            text=query.message.text,
            parse_mode=ParseMode.MARKDOWN,
            message_id=query.message.message_id
        )
        text = ['<b>Вопрос 1</b>',
                'Отгадайте популярный новогодний фильм <b>(1 балл)</b>\n',
                '🏢✈️🏢🛁👩‍❤️‍👨\n',
                'Варианты ответов:',
                '1. Отпуск по обмену',
                '2. Ирония судьбы, или С лёгким паром',
                '3. Один дома',
                '4. Улетели, прилетели, помылись, влюбились',]
        context.bot.send_message(
            chat_id=chat_id,
            text='\n'.join(text),
            parse_mode=ParseMode.HTML,
            reply_markup=get_base_inline_keyboard_question1()
        )

    elif data in [BUTTON_INLINE_QUESTION1_1, BUTTON_INLINE_QUESTION1_2,BUTTON_INLINE_QUESTION1_3,BUTTON_INLINE_QUESTION1_4]: #вопрос 2
        context.bot.edit_message_text(
            chat_id=chat_id,
            text="%s\n\n<b>Правильный ответ:</b>\n<i>Ирония судьбы, или С лёгким паром</i>"%(query.message.text),
            parse_mode=ParseMode.HTML,
            message_id=query.message.message_id
        )
        text = ['<b>Вопрос 2</b>',
                'Отгадайте новогоднюю песню <b>(1 балл)</b>\n',
                '❌❄️🏢🏢🏢🏘❌😃👍🏻\n',
                'Варианты ответов:',
                '1. Потолок ледяной, дверь скрипучая',
                '2. Заметает зима',
                '3. Кабы не было зимы в городах и сёлах',
                '4. Зимой в Норильске хорошо, ну а в Сочи л-у-у-чше',]
        if data == BUTTON_INLINE_QUESTION1_2:
            context.bot.answer_callback_query(callback_query_id=query.id, text="Вы правильно ответили 🥳", show_alert=True)
            table.setQuestion(chat_id, "1", 1)
        if data != BUTTON_INLINE_QUESTION1_2:
            context.bot.answer_callback_query(callback_query_id=query.id, text="Вы неверно ответили 😥", show_alert=True)
        context.bot.send_message(
            chat_id=chat_id,
            text='\n'.join(text),
            parse_mode=ParseMode.HTML,
            reply_markup=get_base_inline_keyboard_question2()
        )

    elif data in [BUTTON_INLINE_QUESTION2_1,BUTTON_INLINE_QUESTION2_2,BUTTON_INLINE_QUESTION2_3,BUTTON_INLINE_QUESTION2_4]: #вопрос 3
        context.bot.edit_message_text(
            chat_id=chat_id,
            text="%s\n\n<b>Правильный ответ:</b>\n<i>Кабы не было зимы в городах и селах</i>"%(query.message.text),
            parse_mode=ParseMode.HTML,
            message_id=query.message.message_id
        )
        text = ['<b>Вопрос 3</b>',
                'Отгадайте пословицу <b>(1 балл)</b>\n',
                '🐶♥️🏠🐯\n',
                'Варианты ответов:',
                '1. Тигр бережёт свою шкуру, а человек – имя',
                '2. На своей улице, и собака – тигр',
                '3. Люби свой дом, как тигра с собакой',
                '4. Собака в доме, как тигр на воле',]
        if data == BUTTON_INLINE_QUESTION2_3:
            context.bot.answer_callback_query(callback_query_id=query.id, text="Вы правильно ответили 🥳", show_alert=True)
            table.setQuestion(chat_id, "2", 1)
        if data != BUTTON_INLINE_QUESTION2_3:
            context.bot.answer_callback_query(callback_query_id=query.id, text="Вы неверно ответили 😥", show_alert=True)
        context.bot.send_message(
            chat_id=chat_id,
            text='\n'.join(text),
            parse_mode=ParseMode.HTML,
            reply_markup=get_base_inline_keyboard_question3()
        )

    elif data in [BUTTON_INLINE_QUESTION3_1,BUTTON_INLINE_QUESTION3_2,BUTTON_INLINE_QUESTION3_3,BUTTON_INLINE_QUESTION3_4]: #вопрос 4
        context.bot.edit_message_text(
            chat_id=chat_id,
            text="%s\n\n<b>Правильный ответ:</b>\n<i>На своей улице, и собака – тигр</i>"%(query.message.text),
            parse_mode=ParseMode.HTML,
            message_id=query.message.message_id
        )
        text = ['<b>Вопрос 4</b>',
                'Отгадайте мультфильм <b>(3 балла)</b>\n',
                '👦🏻🎄🚋💨🌌 \n',
                'Варианты ответов:',
                '1. Полярный экспресс',
                '2. Поезд в Рождество',
                '3. Новогодний экспресс',
                '4. Погоня за Новым годом',]
        if data == BUTTON_INLINE_QUESTION3_2:
            context.bot.answer_callback_query(callback_query_id=query.id, text="Вы правильно ответили 🥳", show_alert=True)
            table.setQuestion(chat_id, "3", 1)
        if data != BUTTON_INLINE_QUESTION3_2:
            context.bot.answer_callback_query(callback_query_id=query.id, text="Вы неверно ответили 😥", show_alert=True)
        context.bot.send_message(
            chat_id=chat_id,
            text='\n'.join(text),
            parse_mode=ParseMode.HTML,
            reply_markup=get_base_inline_keyboard_question4()
        )

    elif data in [BUTTON_INLINE_QUESTION4_1,BUTTON_INLINE_QUESTION4_2,BUTTON_INLINE_QUESTION4_3,BUTTON_INLINE_QUESTION4_4]: #вопрос 5
        context.bot.edit_message_text(
            chat_id=chat_id,
            text="%s\n\n<b>Правильный ответ:</b>\n<i>Полярный экспресс</i>"%(query.message.text),
            parse_mode=ParseMode.HTML,
            message_id=query.message.message_id
        )
        text = ['<b>Вопрос 5</b>',
                'Отгадайте фильм <b>(3 балла)</b>\n',
                '🏫👺👩‍❤️‍👨🕰🔮👄️\n',
                'Варианты ответов:',
                '1. Гринч - похититель Рождества',
                '2. Чародеи',
                '3. Новогодняя магия',
                '4. Неудержимые 3',]
        if data == BUTTON_INLINE_QUESTION4_1:
            context.bot.answer_callback_query(callback_query_id=query.id, text="Вы правильно ответили 🥳", show_alert=True)
            table.setQuestion(chat_id, "4", 3)
        if data != BUTTON_INLINE_QUESTION4_1:
            context.bot.answer_callback_query(callback_query_id=query.id, text="Вы неверно ответили 😥", show_alert=True)
        context.bot.send_message(
            chat_id=chat_id,
            text='\n'.join(text),
            parse_mode=ParseMode.HTML,
            reply_markup=get_base_inline_keyboard_question5()
        )

    elif data in [BUTTON_INLINE_QUESTION5_1,BUTTON_INLINE_QUESTION5_2,BUTTON_INLINE_QUESTION5_3,BUTTON_INLINE_QUESTION5_4]: #вопрос 6
        context.bot.edit_message_text(
            chat_id=chat_id,
            text="%s\n\n<b>Правильный ответ:</b>\n<i>Чародеи</i>"%(query.message.text),
            parse_mode=ParseMode.HTML,
            message_id=query.message.message_id
        )
        text = ['<b>Вопрос 6</b>',
                'Отгадайте сказку <b>(3 балла)</b>\n',
                '🐻👸🏼🤡❄️🌲🎅🏻\n',
                'Варианты ответов:',
                '1. Когда зажигаются ёлки',
                '2. Снегурочка',
                '3. Морозко',
                '4. Принцесса в цирке',]
        if data == BUTTON_INLINE_QUESTION5_2:
            context.bot.answer_callback_query(callback_query_id=query.id, text="Вы правильно ответили 🥳", show_alert=True)
            table.setQuestion(chat_id, "5", 3)
        if data != BUTTON_INLINE_QUESTION5_2:
            context.bot.answer_callback_query(callback_query_id=query.id, text="Вы неверно ответили 😥", show_alert=True)
        context.bot.send_message(
            chat_id=chat_id,
            text='\n'.join(text),
            parse_mode=ParseMode.HTML,
            reply_markup=get_base_inline_keyboard_question6()
        )

    elif data in [BUTTON_INLINE_QUESTION6_1,BUTTON_INLINE_QUESTION6_2,BUTTON_INLINE_QUESTION6_3,BUTTON_INLINE_QUESTION6_4]: #вопрос 7
        context.bot.edit_message_text(
            chat_id=chat_id,
            text="%s\n\n<b>Правильный ответ:</b>\n<i>Морозко</i>"%(query.message.text),
            parse_mode=ParseMode.HTML,
            message_id=query.message.message_id
        )
        text = ['<b>Вопрос 7</b>',
                'Отгадайте фильм <b>(5 баллов)</b>\n',
                '👧🏼✉️🤹‍♂️👨‍🚀👨🏻‍🍳🎅🏻\n',
                'Варианты ответов:',
                '1. Бедная Саша',
                '2. Сирота казанская',
                '3. Королева льда',
                '4. Интерстеллар',]
        if data == BUTTON_INLINE_QUESTION6_3:
            context.bot.answer_callback_query(callback_query_id=query.id, text="Вы правильно ответили 🥳", show_alert=True)
            table.setQuestion(chat_id, "6", 3)
        if data != BUTTON_INLINE_QUESTION6_3:
            context.bot.answer_callback_query(callback_query_id=query.id, text="Вы неверно ответили 😥", show_alert=True)
        context.bot.send_message(
            chat_id=chat_id,
            text='\n'.join(text),
            parse_mode=ParseMode.HTML,
            reply_markup=get_base_inline_keyboard_question7()
        )

    elif data in [BUTTON_INLINE_QUESTION7_1,BUTTON_INLINE_QUESTION7_2,BUTTON_INLINE_QUESTION7_3,BUTTON_INLINE_QUESTION7_4]: #вопрос 8
        context.bot.edit_message_text(
            chat_id=chat_id,
            text="%s\n\n<b>Правильный ответ:</b>\n<i>Сирота казанская</i>"%(query.message.text),
            parse_mode=ParseMode.HTML,
            message_id=query.message.message_id
        )
        text = ['<b>Вопрос 8</b>',
                'Отгадайте книгу <b>(5 баллов)</b>\n',
                '👹 ✨🌌🌙👩🏻❤️👠👨🏻\n',
                'Варианты ответов:',
                '1. Дьявол носит Prada',
                '2. Золушка',
                '3. Ночь перед Рождеством',
                '4. Чертовская ночь',]
        if data == BUTTON_INLINE_QUESTION7_2:
            context.bot.answer_callback_query(callback_query_id=query.id, text="Вы правильно ответили 🥳", show_alert=True)
            table.setQuestion(chat_id, "7", 5)
        if data != BUTTON_INLINE_QUESTION7_2:
            context.bot.answer_callback_query(callback_query_id=query.id, text="Вы неверно ответили 😥", show_alert=True)
        context.bot.send_message(
            chat_id=chat_id,
            text='\n'.join(text),
            parse_mode=ParseMode.HTML,
            reply_markup=get_base_inline_keyboard_question8()
        )

    elif data in [BUTTON_INLINE_QUESTION8_1,BUTTON_INLINE_QUESTION8_2,BUTTON_INLINE_QUESTION8_3,BUTTON_INLINE_QUESTION8_4]: #Вопрос 9
        context.bot.edit_message_text(
            chat_id=chat_id,
            text="%s\n\n<b>Правильный ответ:</b>\n<i>Ночь перед Рождеством</i>"%(query.message.text),
            parse_mode=ParseMode.HTML,
            message_id=query.message.message_id
        )
        text = ['<b>Вопрос 9</b>',
                'Отгадайте фильм <b>(5 баллов)</b>\n',
                '🎅🏻🍷🚬🚓👦🏻🙏🏻\n',
                'Варианты ответов:',
                '1. Один дома 2',
                '2. Кровавый Санта',
                '3. Плохой Санта',
                '4. Просто ужасный Санта',]
        if data == BUTTON_INLINE_QUESTION8_3:
            context.bot.answer_callback_query(callback_query_id=query.id, text="Вы правильно ответили 🥳", show_alert=True)
            table.setQuestion(chat_id, "8", 5)
        if data != BUTTON_INLINE_QUESTION8_3:
            context.bot.answer_callback_query(callback_query_id=query.id, text="Вы неверно ответили 😥", show_alert=True)
        context.bot.send_message(
            chat_id=chat_id,
            text='\n'.join(text),
            parse_mode=ParseMode.HTML,
            reply_markup=get_base_inline_keyboard_question9()
        )

    elif data in [BUTTON_INLINE_QUESTION9_1,BUTTON_INLINE_QUESTION9_2,BUTTON_INLINE_QUESTION9_3,BUTTON_INLINE_QUESTION9_4]: #Вопрос 10
        context.bot.edit_message_text(
            chat_id=chat_id,
            text="%s\n\n<b>Правильный ответ:</b>\n<i>Плохой Санта</i>"%(query.message.text),
            parse_mode=ParseMode.HTML,
            message_id=query.message.message_id
        )
        text = ['<b>Вопрос 10</b>',
                'Отгадайте фильм <b>(5 баллов)</b>\n',
                '👩🏻🎄🧤💖\n',
                'Варианты ответов:',
                '1. Интуиция',
                '2. Рождественская ярмарка',
                '3. Встреча',
                '4. Рождество на двоих',]
        if data == BUTTON_INLINE_QUESTION9_3:
            context.bot.answer_callback_query(callback_query_id=query.id, text="Вы правильно ответили 🥳", show_alert=True)
            table.setQuestion(chat_id, "9", 5)
        if data != BUTTON_INLINE_QUESTION9_3:
            context.bot.answer_callback_query(callback_query_id=query.id, text="Вы неверно ответили 😥", show_alert=True)
        context.bot.send_message(
            chat_id=chat_id,
            text='\n'.join(text),
            parse_mode=ParseMode.HTML,
            reply_markup=get_base_inline_keyboard_question10()
        )

    elif data in [BUTTON_INLINE_QUESTION10_1,BUTTON_INLINE_QUESTION10_2,BUTTON_INLINE_QUESTION10_3,BUTTON_INLINE_QUESTION10_4]: #ФИНАЛ
        context.bot.edit_message_text(
            chat_id=chat_id,
            text="%s\n\n<b>Правильный ответ:</b>\n<i>Интуиция</i>"%(query.message.text),
            parse_mode=ParseMode.HTML,
            message_id=query.message.message_id
        )

        if data == BUTTON_INLINE_QUESTION10_1:
            context.bot.answer_callback_query(callback_query_id=query.id, text="Вы правильно ответили 🥳", show_alert=True)
            table.setQuestion(chat_id, "10", 5)
        if data != BUTTON_INLINE_QUESTION10_1:
            context.bot.answer_callback_query(callback_query_id=query.id, text="Вы неверно ответили 😥", show_alert=True)

        sum = int(table.getSum(chat_id))
        table.setTotal(chat_id, sum)
        ball = table.getTotal(chat_id)
        text = winMessage(ball)
        table.setStatus(chat_id)

        context.bot.send_message(
            chat_id=chat_id,
            text=text,
            parse_mode=ParseMode.HTML
        )

        userInfo = "Участник Id: %d\nЛогин: %s\nИмя: %s %s\nВсего набрано очков: %d\n"%(chat_id, str(update.effective_user.username),str(update.effective_user.first_name), str(update.effective_user.last_name), table.getTotal(chat_id))
        context.bot.send_message(
            chat_id = channel_chat_id,
            text=userInfo,
            parse_mode=ParseMode.HTML
        )

def do_start(update: Update, context: CallbackContext):
    chat_id = update.effective_message.chat_id
    try :
        isAwaiting = table.getStatus(chat_id) == "Awaiting"
        isDone = table.getStatus(chat_id) == "Successful"
    except:
        isAwaiting = False
        isDone = False

    table.setParticipant(chat_id)
    if (expectedDate()):
        context.bot.send_message(
            chat_id = chat_id,
            text="Розыгрыш состоялся! Результаты смотрите в нашем телеграм-канале",
            parse_mode=ParseMode.HTML
        )
        return

    if isDone:
        ball = table.getTotal(chat_id)
        context.bot.send_message(
            chat_id = chat_id,
            text=winMessage(ball),
            parse_mode=ParseMode.HTML
        )
        return

    if isAwaiting:
        context.bot.send_message(
            chat_id = chat_id,
            text="Невозможно перезапустить бота после начала викторины",
            parse_mode=ParseMode.HTML
        )
        return

    text = [
        '<a href="https://thumb.cloud.mail.ru/weblink/thumb/xw1/XUpR/Z5qJFUXDK">&#8205;</a>',
        'Отвечайте на вопросы, получайте баллы за каждый ответ и выигрывайте подарки от партнёров «Мультибонуса».\n',
        '🔹 суперпризы, если набрали более 20-ти баллов;\n',
        '🔹 стандартные призы, если набрали до 20 баллов;\n',
        '🔹 поощрительные призы, если набрали до 10 баллов.\n',
        'Удачи!'

    ]
    # info = [
    #     '🔹 более 20-ти баллов — участвуете в розыгрыше суперпризов от партнёров программы;\n',
    #     '🔹 до 20 баллов — участвуете в розыгрыше призов от партнеров программы;\n',
    #     '🔹 до 10 баллов — участвуете в розыгрыше промокодов от партнёров программы.\n'
    # ]
    # update.message.reply_text(
    #     text='\n'.join(text),
    #     parse_mode=ParseMode.HTML,
    #     disable_web_page_preview=False
    # )
    # context.bot.send_message(
    #     chat_id = update.message.chat_id,
    #     text='\n'.join(info),
    #     parse_mode=ParseMode.HTML,
    #     reply_markup=get_base_inline_keyboard_start(),
    # )
    update.message.reply_text(
        chat_id = update.message.chat_id,
        text='\n'.join(text),
        parse_mode=ParseMode.HTML,
        reply_markup=get_base_inline_keyboard_start(),
    )

def do_echo(update: Update, context: CallbackContext):
    text = update.message.text
    creator = update.message.chat.id
    try :
        isDone = table.getStatus(creator) == "Successful"
    except:
        isDone = False

    if creator == channel_chat_id:

        resultMassage = list(text.split("\n"))
        #print(resultMassage)
        notifySend = "SendWiners:"

        if resultMassage[0].find(notifySend) != -1:
            notify(text, context, notifySend, creator)
        if text == "Admin menu":
            context.bot.send_message(
                chat_id = creator,
                text='<b>Админское меню добавлено</b>',
                parse_mode=ParseMode.HTML,
                reply_markup=get_base_reply_keyboard()
            )
        if text == "База данных":
            try:
                # col_name = ['Id','Reporter', 'Status', 'Total', 'Question 1', 'Question 2', 'Question 3', 'Question 4', 'Question 5', 'Question 6', 'Question 7', 'Question 8', 'Question 9', 'Question 10']
                # requestParticipants.extend(table.getAllData())
                requestParticipants = table.getAllData()

                s = io.StringIO()
                csv.writer(s).writerows(requestParticipants)
                s.seek(0)

                buf = io.BytesIO()

                buf.write(s.getvalue().encode())
                buf.seek(0)

                buf.name = 'report_from_database.csv'

                context.bot.send_document(
                    chat_id=creator,
                    document=buf
                )

            except:
                context.bot.send_message(
                    chat_id = creator,
                    text="Еще нет участников",
                    parse_mode=ParseMode.HTML
                )
        return

    if isDone:
        ball = table.getTotal(creator)
        context.bot.send_message(
            chat_id = creator,
            text=winMessage(ball),
            parse_mode=ParseMode.HTML
        )

def winMessage(ball):
    # print (type(ball))
    if ball < 1:
        return ("К сожалению, вы не ответили правильно ни на один из вопросов")
    if ball > 0 and  ball <= 10:
        return ("Поздравляем! Вы набрали %d баллов. Вы получаете подарок от партнёра —  cкидка до 40%% на сервисный сбор по промокоду ."%(ball))
    if ball > 10 and  ball <= 20:
        return ("Поздравляем! Вы набрали %d баллов. Вы получаете подарок от партнёра  —  подписку на 45 дней по промокоду ."%(ball))
    if ball > 20:
        return ("Поздравляем! Вы набрали %d баллов. Вам подарок от партнёра  – бесплатная подписка на сервис на 90 дней для новых клиентов по промокоду ."%(ball))

def notify(massage, context, secret, creator):

    listUsers = massage.replace(secret, '')
    rows = list(listUsers.split("\n"))
    for row in rows:
        try:
            if row == "":
                continue
            context.bot.send_message(
                chat_id = row,
                text="Поздравляем! Вы выиграли супер-приз! Подробнее об этом в нашем телеграм-канале ",
                parse_mode=ParseMode.HTML,
            )
            context.bot.send_message(
                chat_id = creator,
                text="%s - Success"%(row),
                parse_mode=ParseMode.HTML
            )
        except:
            context.bot.send_message(
                chat_id = creator,
                text="%s - Failed"%(row),
                parse_mode=ParseMode.HTML
            )

def expectedDate():
    CurrentDate = datetime.datetime.now()

    ExpectedDate = consts["expectedDate"]
    ExpectedDate = datetime.datetime.strptime(ExpectedDate, "%d/%m/%Y %H:%M")

    if CurrentDate > ExpectedDate:
        return True
    else:
        return False

def main():

    req = Request(
        connect_timeout=0.5,
        read_timeout=1.0,
    )
    bot = Bot(
        token='',
        request=req,
    )
    updater = Updater(
        bot=bot,
        use_context=True,
    )


    # Навесить обработчики команд
    start_handler = CommandHandler("start", do_start)
    message_handler = MessageHandler(Filters.text, do_echo)
    buttons_handler = CallbackQueryHandler(callback=keyboard_callback_handler)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(message_handler)
    updater.dispatcher.add_handler(buttons_handler)

    # Начать бесконечную обработку входящих сообщений
    updater.start_polling()
    updater.idle()

    print ("Finished work...")

if __name__ == '__main__':
    main()
