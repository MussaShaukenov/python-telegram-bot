import telebot
from telebot import types

TOKEN = '1441130644:AAEQTzIFc5Yi1c09zvhVjWAcJHd3gpN_KAY'

bot = telebot.TeleBot(TOKEN)


# bot replies to start and help commands
@bot.message_handler(commands=['start'])
def greeting(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Music')
    item2 = types.KeyboardButton('Tech')
    item3 = types.KeyboardButton('Travel')
    item4 = types.KeyboardButton('Learning')
    item5 = types.KeyboardButton('Sports')
    item6 = types.KeyboardButton('Animation')
    markup.add(item1, item2, item3, item4, item5, item6)
    bot.send_message(message.chat.id, 'Hello! I will help you to find different kind of ' +
                     'YouTube channels for different kind of information.',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def reply_message(message):
    if message.chat.type == 'private':
        if message.text == 'Music':
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton('The Sound You Need', callback_data='the_sound_you_need')
            item2 = types.InlineKeyboardButton('Electro Posé', callback_data='electro_pose')
            item3 = types.InlineKeyboardButton('Majestic Casual', callback_data='majestic_casual')
            item4 = types.InlineKeyboardButton('Stay See', callback_data='stay_see')
            item5 = types.InlineKeyboardButton('Chill Masters', callback_data='chill_masters')
            item6 = types.InlineKeyboardButton('Future House Music', callback_data='future_house_music')
            item7 = types.InlineKeyboardButton('MrDeepSense', callback_data='mr_deep_sense')
            item8 = types.InlineKeyboardButton('Mr_Revillz', callback_data='mr_revillz')
            item9 = types.InlineKeyboardButton('Chilled Cow', callback_data='chilled_cow')
            item10 = types.InlineKeyboardButton('MrSuicideSheep', callback_data='mr_suicide_sheep')
            item11 = types.InlineKeyboardButton('Show All', callback_data='show_all_music')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)
            bot.send_message(message.chat.id, 'Choose YouTube Channel', reply_markup=markup)

        elif message.text == 'Tech':
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton('Marques Brownlee', callback_data='brown_lee')
            item2 = types.InlineKeyboardButton('UrAvgConsumer', callback_data='ur_avg_consumer')
            item3 = types.InlineKeyboardButton('LinusTechTips', callback_data='linus_tech_lips')
            item4 = types.InlineKeyboardButton('Unbox Therapy', callback_data='unbox_therapy')
            item5 = types.InlineKeyboardButton('Austin Evans', callback_data='austin_evans')
            item6 = types.InlineKeyboardButton('Jonathan Morrison', callback_data='j_morrison')
            item7 = types.InlineKeyboardButton('Jonathan Rettinger', callback_data='j_rettinger')
            item8 = types.InlineKeyboardButton('MrWhoseTheBoss', callback_data='mr_whose_the_boss')
            item9 = types.InlineKeyboardButton('Android Authority', callback_data='android_authority')
            item10 = types.InlineKeyboardButton('iJustine', callback_data='i_justine')
            item11 = types.InlineKeyboardButton('Show All', callback_data='show_all_tech')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)
            bot.send_message(message.chat.id, 'Choose YouTube Channel', reply_markup=markup)

        elif message.text == 'Travel':
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton('Bald & Bankrupt', callback_data='bald_and_bankrupt')
            item2 = types.InlineKeyboardButton('Indigo Traveller', callback_data='indigo_traveller')
            item3 = types.InlineKeyboardButton('Kara & Nate', callback_data='kara_and_nate')
            item4 = types.InlineKeyboardButton('The Endless Adventure', callback_data='endless_adventure')
            item5 = types.InlineKeyboardButton('FunForLouis', callback_data='fun_for_louis')
            item6 = types.InlineKeyboardButton('Gabriel Traveller', callback_data='gabriel_traveller')
            item7 = types.InlineKeyboardButton('Vagabrothers', callback_data='vagabrothers')
            item8 = types.InlineKeyboardButton('Drew Binsky', callback_data='drew_binsky')
            item9 = types.InlineKeyboardButton('Eva zu Beck', callback_data='eva_zu_back')
            item10 = types.InlineKeyboardButton('The Daily Woo', callback_data='the_daily_woo')
            item11 = types.InlineKeyboardButton('Show all', callback_data='show_all_travel')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)
            bot.send_message(message.chat.id, 'Choose YouTube Channel', reply_markup=markup)

        elif message.text == 'Learning':
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton('Ted Ed', callback_data='ted_ed')
            item2 = types.InlineKeyboardButton('Crash Course', callback_data='crash_course')
            item3 = types.InlineKeyboardButton('Vsause', callback_data='vsause')
            item4 = types.InlineKeyboardButton('Khan Academy', callback_data='khan_academy')
            item5 = types.InlineKeyboardButton('Veritasium', callback_data='veritasium')
            item6 = types.InlineKeyboardButton('AsapSCIENCE', callback_data='asap_science')
            item7 = types.InlineKeyboardButton('Common Sense Education', callback_data='common_sense_edu')
            item8 = types.InlineKeyboardButton('Edutopia', callback_data='edutopia')
            item9 = types.InlineKeyboardButton('Big Think', callback_data='big_think')
            item10 = types.InlineKeyboardButton('National Geographic', callback_data='national_geographic')
            item11 = types.InlineKeyboardButton('Show all', callback_data='show_all_learning')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)
            bot.send_message(message.chat.id, 'Choose YouTube Channel', reply_markup=markup)

        elif message.text == 'Sports':
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton('ESPN | World of Sports', callback_data='espn')
            item2 = types.InlineKeyboardButton('Football Daily | Football Videos', callback_data='football_daily')
            item3 = types.InlineKeyboardButton('Red Bull', callback_data='red_bull')
            item4 = types.InlineKeyboardButton('Olympic', callback_data='olympic')
            item5 = types.InlineKeyboardButton('BT Sport | Sports Highlights', callback_data='bt_sport')
            item6 = types.InlineKeyboardButton('VICE Sports', callback_data='vice_sports')
            item7 = types.InlineKeyboardButton('NBA | NBA Highlights', callback_data='nba')
            item8 = types.InlineKeyboardButton('F2Freestylers | Ultimate Soccer Skills Channel', callback_data='f2')
            item9 = types.InlineKeyboardButton('freekickerz', callback_data='freekickerz')
            item10 = types.InlineKeyboardButton('UFC - Ultimate Fighting Championship', callback_data='ufc')
            item11 = types.InlineKeyboardButton('Show all', callback_data='show_all_sports')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)
            bot.send_message(message.chat.id, 'Choose YouTube Channel', reply_markup=markup)

        elif message.text == 'Animation':
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton('Explosm Entertainment | Animation And Comics', callback_data='explosm')
            item2 = types.InlineKeyboardButton('Walt Disney Animation Studios | Animation Channel', callback_data='disney')
            item3 = types.InlineKeyboardButton('Domics - Animator by day, animator by night', callback_data='domics')
            item4 = types.InlineKeyboardButton('Shut Up! Cartoons', callback_data='shut_up')
            item5 = types.InlineKeyboardButton('Carbot Animations', callback_data='carbot')
            item6 = types.InlineKeyboardButton('Tabbes | Funny Animation Videos', callback_data='tabbes')
            item7 = types.InlineKeyboardButton('TimTom', callback_data='timtom')
            item8 = types.InlineKeyboardButton('Daidus | Animation Videos', callback_data='daidus')
            item9 = types.InlineKeyboardButton('No Idea Animation', callback_data='no_idea')
            item10 = types.InlineKeyboardButton('Angelo Animations', callback_data='angelo')
            item11 = types.InlineKeyboardButton('Show all', callback_data='show_all_animations')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)
            bot.send_message(message.chat.id, 'Choose YouTube Channel', reply_markup=markup)

        else:
            bot.send_message(message.chat.id, 'Please, select the command from the given table')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            # 1 music channel
            if call.data == 'the_sound_you_need':
                bot.send_message(call.message.chat.id, 'The Sound You Need - '
                                                       'https://www.youtube.com/user/thesoundyouneed1')
            # 2 music channel
            elif call.data == 'electro_pose':
                bot.send_message(call.message.chat.id, 'Electro Pose - https://www.youtube.com/user/electropose1')
            # 3 music channel
            elif call.data == 'majestic_casual':
                bot.send_message(call.message.chat.id, 'Majestic Casual - https://www.youtube.com/user/majesticcasual')
            # 4 music channel
            elif call.data == 'stay_see':
                bot.send_message(call.message.chat.id, 'Stay See - https://www.youtube.com/user/stayseemusic')
            # 5 music channel
            elif call.data == 'chill_masters':
                bot.send_message(call.message.chat.id, 'Chill Masters - https://www.youtube.com/user'
                                                       '/chillmasterschannel')
            # 6 music channel
            elif call.data == 'future_house_music':
                bot.send_message(call.message.chat.id, 'Future House Music - https://www.youtube.com/channel/UCXvSeBDvzmPO05k-0RyB34w')
            # 7 music channel
            elif call.data == 'mr_deep_sense':
                bot.send_message(call.message.chat.id, 'MrDeepSense - https://www.youtube.com/user/MrDeepSense')
            # 8 music channel
            elif call.data == 'mr_revillz':
                bot.send_message(call.message.chat.id, 'MrRevillz - https://www.youtube.com/user/MrRevillz')
            # 9 music channel
            elif call.data == 'chilled_cow':
                bot.send_message(call.message.chat.id, 'Chilled Cow - https://www.youtube.com/channel/UCSJ4gkVC6NrvII8umztf0Ow')
            # 10 music channel
            elif call.data == 'mr_suicide_sheep':
                bot.send_message(call.message.chat.id, 'MrSuicideSheep - https://www.youtube.com/user/MrSuicideSheep')
            # All music channels
            elif call.data == 'show_all_music':
                bot.send_message(call.message.chat.id,
                                 'The Sound You Need - ' + 'https://www.youtube.com/user/thesoundyouneed1 \n' +
                                 'Electro Pose - https://www.youtube.com/user/electropose1\n' +
                                 'Majestic Casual - https://www.youtube.com/user/majesticcasual\n' +
                                 'Stay See - https://www.youtube.com/user/stayseemusic\n' +
                                 'Chill Masters - https://www.youtube.com/user/chillmasterschannel\n' +
                                 'Future House Music - https://www.youtube.com/channel/UCXvSeBDvzmPO05k-0RyB34w\n' +
                                 'MrDeepSense - https://www.youtube.com/user/MrDeepSense\n' +
                                 'MrRevillz - https://www.youtube.com/user/MrRevillz\n' +
                                 'Chilled Cow - https://www.youtube.com/channel/UCSJ4gkVC6NrvII8umztf0Ow\n' +
                                 'MrSuicideSheep - https://www.youtube.com/user/MrSuicideSheep')

            # 1 tech channel
            elif call.data == 'brown_lee':
                bot.send_message(call.message.chat.id,
                                 'Marques Brownlee - https://www.youtube.com/user/marquesbrownlee')
            # 2 tech channel
            elif call.data == 'ur_avg_consumer':
                bot.send_message(call.message.chat.id, 'UrAvgConsumer - https://www.youtube.com/user/UrAvgConsumer')
            # 3 tech channel
            elif call.data == 'linus_tech_lips':
                bot.send_message(call.message.chat.id, 'LinusTechLips - https://www.youtube.com/user/LinusTechTips')
            # 4 tech channel
            elif call.data == 'unbox_therapy':
                bot.send_message(call.message.chat.id, 'Unbox Therapy - https://www.youtube.com/user/unboxtherapy')
            # 5 tech channel
            elif call.data == 'austin_evans':
                bot.send_message(call.message.chat.id,
                                 'Austin Evans - https://www.youtube.com/user/duncan33303/featured')
            # 6 tech channel
            elif call.data == 'j_morrison':
                bot.send_message(call.message.chat.id,
                                 'Jonathan Morrison - https://www.youtube.com/user/tldtoday/featured')
            # 7 tech channel
            elif call.data == 'j_rettinger':
                bot.send_message(call.message.chat.id,
                                 'Jonathan Rettinger - https://www.youtube.com/channel/UCR0AnNR7sViH3TWMJl5jyxw')
            # 8 tech channel
            elif call.data == 'mr_whose_the_boss':
                bot.send_message(call.message.chat.id,
                                 'MrWhoseTheBoss - https://www.youtube.com/user/Mrwhosetheboss/videos')
            # 9 tech channel
            elif call.data == 'android_authority':
                bot.send_message(call.message.chat.id,
                                 'Android Authority - https://www.youtube.com/user/AndroidAuthority')
            # 10 tech channel
            elif call.data == 'i_justine':
                bot.send_message(call.message.chat.id, 'iJustine - https://www.youtube.com/user/ijustine')
            # all tech channels
            elif call.data == 'show_all_tech':
                bot.send_message(call.message.chat.id,
                                 'Marques Brownlee - https://www.youtube.com/user/marquesbrownlee\n' +
                                 'UrAvgConsumer - https://www.youtube.com/user/UrAvgConsumer\n' +
                                 'LinusTechLips - https://www.youtube.com/user/LinusTechTips\n' +
                                 'Unbox Therapy - https://www.youtube.com/user/unboxtherapy\n' +
                                 'Austin Evans - https://www.youtube.com/user/duncan33303/featured\n' +
                                 'Jonathan Morrison - https://www.youtube.com/user/tldtoday/featured\n' +
                                 'Jonathan Rettinger - https://www.youtube.com/channel/UCR0AnNR7sViH3TWMJl5jyxw\n' +
                                 'MrWhoseTheBoss - https://www.youtube.com/user/Mrwhosetheboss/videos\n' +
                                 'Android Authority - https://www.youtube.com/user/AndroidAuthority\n' +
                                 'iJustine - https://www.youtube.com/user/ijustine')


            # 1 travel channel
            elif call.data == 'bald_and_bankrupt':
                bot.send_message(call.message.chat.id,
                                 'Bald & Bankrupt - https://www.youtube.com/channel/UCxDZs_ltFFvn0FDHT6kmoXA')
            # 2 travel channel
            elif call.data == 'indigo_traveller':
                bot.send_message(call.message.chat.id,
                                 'Indigo Traveller - https://www.youtube.com/channel/UCXulruMI7BHj3kGyosNa0jA')
            # 3 travel channel
            elif call.data == 'kara_and_nate':
                bot.send_message(call.message.chat.id,
                                 'Kara & Nate - https://www.youtube.com/channel/UC4ijq8Cg-8zQKx8OH12dUSw')
            # 4 travel channel
            elif call.data == 'endless_adventure':
                bot.send_message(call.message.chat.id,
                                 'Endless Adventure - https://www.youtube.com/channel/UCEDrRCC0qRtPd5-sSa1hajw')
            # 5 travel channel
            elif call.data == 'fun_for_louis':
                bot.send_message(call.message.chat.id, 'FunForLouis - https://www.youtube.com/user/FunForLouis')
            # 6 travel channel
            elif call.data == 'gabriel_traveller':
                bot.send_message(call.message.chat.id, 'Gabriel Traveller - https://www.youtube.com/user/gabejedmo')
            # 7 travel channel
            elif call.data == 'vagabrothers':
                bot.send_message(call.message.chat.id, 'Vagabrothers - https://www.youtube.com/user/vagabrothers')
            # 8 travel channel
            elif call.data == 'drew_binsky':
                bot.send_message(call.message.chat.id, 'Drew Binsky - https://www.youtube.com/user/thehungrypartier')
            # 9 travel channel
            elif call.data == 'eva_zu_back':
                bot.send_message(call.message.chat.id,
                                 'Eva zu Back - https://www.youtube.com/channel/UCDTINI9skkeZNY2ZXnBqIkQ')
            # 10 travel channel
            elif call.data == 'the_daily_woo':
                bot.send_message(call.message.chat.id,
                                 'The Daily Woo - https://www.youtube.com/user/TheDailyWoo/featured')
            # all travel channels
            elif call.data == 'show_all_travel':
                bot.send_message(call.message.chat.id,
                                 'Bald & Bankrupt - https://www.youtube.com/channel/UCxDZs_ltFFvn0FDHT6kmoXA\n' +
                                 'Indigo Traveller - https://www.youtube.com/channel/UCXulruMI7BHj3kGyosNa0jA\n' +
                                 'Kara & Nate - https://www.youtube.com/channel/UC4ijq8Cg-8zQKx8OH12dUSw\n' +
                                 'Endless Adventure - https://www.youtube.com/channel/UCEDrRCC0qRtPd5-sSa1hajw\n' +
                                 'FunForLouis - https://www.youtube.com/user/FunForLouis\n' +
                                 'Gabriel Traveller - https://www.youtube.com/user/gabejedmo\n' +
                                 'Vagabrothers - https://www.youtube.com/user/vagabrothers\n' +
                                 'Drew Binsky - https://www.youtube.com/user/thehungrypartier\n' +
                                 'Eva zu Back - https://www.youtube.com/channel/UCDTINI9skkeZNY2ZXnBqIkQ\n' +
                                 'The Daily Woo - https://www.youtube.com/user/TheDailyWoo/featured')

            # 1 learning channel
            elif call.data == 'ted_ed':
                bot.send_message(call.message.chat.id, 'Ted Ed - https://www.youtube.com/user/TEDEducation')
            # 2 learning channel
            if call.data == 'crash_course':
                bot.send_message(call.message.chat.id, 'Crash Course - https://www.youtube.com/user/crashcourse')
            # 3 learning channel
            if call.data == 'vsause':
                bot.send_message(call.message.chat.id, 'Vsause - https://www.youtube.com/user/Vsauce')
            # 4 learning channel
            if call.data == 'khan_academy':
                bot.send_message(call.message.chat.id, 'Khan Academy - https://www.youtube.com/user/khanacademy')
            # 5 learning channel
            if call.data == 'Veritasium':
                bot.send_message(call.message.chat.id, 'Veritasium - https://www.youtube.com/user/1veritasium')
            # 6 learning channel
            if call.data == 'asap_science':
                bot.send_message(call.message.chat.id, 'AsapSCIENCE - https://www.youtube.com/user/AsapSCIENCE')
            # 7 learning channel
            if call.data == 'common_sense_edu':
                bot.send_message(call.message.chat.id,
                                 'Common Sense Education - https://www.youtube.com/c/CommonSenseEducators/videos')
            # 8 learning channel
            if call.data == 'edutopia':
                bot.send_message(call.message.chat.id, 'Edutopia - https://www.youtube.com/user/edutopia')
            # 9 learning channel
            if call.data == 'big_think':
                bot.send_message(call.message.chat.id, 'Big Think - https://www.youtube.com/user/bigthink')
            # 10 learning channel
            if call.data == 'national_geographic':
                bot.send_message(call.message.chat.id,
                                 'National Geographic - https://www.youtube.com/user/NationalGeographic')
            # all learning channels
            if call.data == 'show_all_learning':
                bot.send_message(call.message.chat.id, 'Ted Ed - https://www.youtube.com/user/TEDEducation\n' +
                                 'Crash Course - https://www.youtube.com/user/crashcourse\n' +
                                 'Vsause - https://www.youtube.com/user/Vsauce\n' +
                                 'Khan Academy - https://www.youtube.com/user/khanacademy\n' +
                                 'Veritasium - https://www.youtube.com/user/1veritasium\n' +
                                 'AsapSCIENCE - https://www.youtube.com/user/AsapSCIENCE\n' +
                                 'Common Sense Education - https://www.youtube.com/c/CommonSenseEducators/videos\n' +
                                 'Edutopia - https://www.youtube.com/user/edutopia\n' +
                                 'Big Think - https://www.youtube.com/user/bigthink\n' +
                                 'National Geographic - https://www.youtube.com/user/NationalGeographic')

            # 1 sports channel
            elif call.data == 'espn':
                bot.send_message(call.message.chat.id,
                                 'ESPN | World of Sports - https://www.youtube.com/user/ESPN/videos')
            # 2 sports channel
            elif call.data == 'football_daily':
                bot.send_message(call.message.chat.id,
                                 'Football Daily | Football Videos - https://www.youtube.com/user/TheFootballDaily/videos')
            # 3 sports channel
            elif call.data == 'red_bull':
                bot.send_message(call.message.chat.id, 'Red Bull - https://www.youtube.com/user/redbull/videos')
            # 4 sports channel
            elif call.data == 'olympic':
                bot.send_message(call.message.chat.id, 'Olympic - https://www.youtube.com/user/olympic/videos')
            # 5 sports channel
            elif call.data == 'bt_sport':
                bot.send_message(call.message.chat.id,
                                 'BT Sport | Sports Highlights - https://www.youtube.com/user/BTSportOfficial/videos')
            # 6 sports channel
            elif call.data == 'vice_sports':
                bot.send_message(call.message.chat.id, 'VICE Sports - https://www.youtube.com/user/NOC/videos')
            # 7 sports channel
            elif call.data == 'nba':
                bot.send_message(call.message.chat.id, 'NBA | NBA Highlights - https://www.youtube.com/user/NBA/videos')
            # 8 sports channel
            elif call.data == 'f2':
                bot.send_message(call.message.chat.id,
                                 'F2Freestylers | Ultimate Soccer Skills Channel - https://www.youtube.com/user/F2Freestylers/videos')
            # 9 sports channel
            elif call.data == 'freekickerz':
                bot.send_message(call.message.chat.id, 'freekickerz - https://www.youtube.com/user/freekickerz/videos')
            # 10 sports channel
            elif call.data == 'ufc':
                bot.send_message(call.message.chat.id,
                                 'UFC - Ultimate Fighting Championship - https://www.youtube.com/user/UFC/videos')
            # all sports channels
            elif call.data == 'show_all_sports':
                bot.send_message(call.message.chat.id,
                                 'ESPN | World of Sports - https://www.youtube.com/user/ESPN/videos\n' +
                                 'Football Daily | Football Videos - https://www.youtube.com/user/TheFootballDaily/videos\n' +
                                 'Red Bull - https://www.youtube.com/user/redbull/videos\n' +
                                 'Olympic - https://www.youtube.com/user/olympic/videos\n' +
                                 'BT Sport | Sports Highlights - https://www.youtube.com/user/BTSportOfficial/videos\n' +
                                 'VICE Sports - https://www.youtube.com/user/NOC/videos\n' +
                                 'NBA | NBA Highlights - https://www.youtube.com/user/NBA/videos\n' +
                                 'F2Freestylers | Ultimate Soccer Skills Channel - https://www.youtube.com/user/F2Freestylers/videos\n' +
                                 'freekickerz - https://www.youtube.com/user/freekickerz/videos\n' +
                                 'UFC - Ultimate Fighting Championship - https://www.youtube.com/user/UFC/videos')

            # 1 animation channel
            elif call.data == 'explosm':
                bot.send_message(call.message.chat.id,
                                 'Explosm Entertainment | Animation And Comics - https://www.youtube.com/user/ExplosmEntertainment/videos')
            # 2 animation channel
            elif call.data == 'disney':
                bot.send_message(call.message.chat.id,
                                 'Walt Disney Animation Studios | Animation Channel - https://www.youtube.com/user/disneyanimation/videos')
            # 3 animation channel
            elif call.data == 'domics':
                bot.send_message(call.message.chat.id,
                                 'Domics - Animator by day, animator by night - https://www.youtube.com/user/D0MICS/videos')
            # 4 animation channel
            elif call.data == 'shut_up':
                bot.send_message(call.message.chat.id,
                                 'Shut Up! Cartoons - https://www.youtube.com/user/ShutUpCartoons/videos')
            # 5 animation channel
            elif call.data == 'carbot':
                bot.send_message(call.message.chat.id,
                                 'CarbotAnimations - https://www.youtube.com/user/CarbotAnimations/videos')
            # 6 animation channel
            elif call.data == 'tabbes':
                bot.send_message(call.message.chat.id,
                                 'Tabbes | Funny Animation Videos - https://www.youtube.com/channel/UCDQBZcjYKP1J1Nu-Y0_D37Q/videos')
            # 7 animation channel
            elif call.data == 'timtom':
                bot.send_message(call.message.chat.id,
                                 'TimTom - https://www.youtube.com/channel/UCj6CFdE3LSddaoszxq604TQ/videos')
            # 8 animation channel
            elif call.data == 'daidus':
                bot.send_message(call.message.chat.id,
                                 'Daidus - hhttps://www.youtube.com/channel/UC2Ds30pkifFVD0CE08wF50g/videos')
            # 9 animation channel
            elif call.data == 'no_idea':
                bot.send_message(call.message.chat.id,
                                 'No Idea Animation - https://www.youtube.com/channel/UCMRbVkqlh90dMKGLJZEcNZA/videos')
            # 10 animation channel
            elif call.data == 'angelo':
                bot.send_message(call.message.chat.id,
                                 'Angelo Animations - https://www.youtube.com/c/AngeloAnimations/videos')
            # All animation channels
            elif call.data == 'show_all_animations':
                bot.send_message(call.message.chat.id,
                                 'Explosm Entertainment | Animation And Comics - https://www.youtube.com/user/ExplosmEntertainment/videos\n' +
                                 'Walt Disney Animation Studios | Animation Channel - https://www.youtube.com/user/disneyanimation/videos\n' +
                                 'Domics - Animator by day, animator by night - https://www.youtube.com/user/D0MICS/videos\n' +
                                 'Shut Up! Cartoons - https://www.youtube.com/user/ShutUpCartoons/videos\n' +
                                 'CarbotAnimations - https://www.youtube.com/user/CarbotAnimations/videos\n' +
                                 'Tabbes | Funny Animation Videos - https://www.youtube.com/channel/UCDQBZcjYKP1J1Nu-Y0_D37Q/videos\n' +
                                 'TimTom - https://www.youtube.com/channel/UCj6CFdE3LSddaoszxq604TQ/videos\n' +
                                 'Daidus - hhttps://www.youtube.com/channel/UC2Ds30pkifFVD0CE08wF50g/videos\n' +
                                 'No Idea Animation - https://www.youtube.com/channel/UCMRbVkqlh90dMKGLJZEcNZA/videos\n' +
                                 'Angelo Animations - https://www.youtube.com/c/AngeloAnimations/videos')

            else:
                bot.send_message(call.message.chat.id, 'Enjoy watching')
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Choose YouTube channel',
                                  reply_markup=None)
    except Exception as e:
        print(repr(e))


# run bot
bot.polling()
