import config
from aiogram import Bot, types, Dispatcher, executor

bot = Bot(token=config.Token)
dp = Dispatcher(bot)

btmk = types.ReplyKeyboardMarkup()
bt = types.KeyboardButton('/asks')
btmk.add(bt)

@dp.message_handler(commands=['start', 'help'])
async def statr(message: types.Message):
    await message.answer(f'Здравствуйте! Это платформа Redux GosZacup! \n Если вас есть вопросы поищите их тут написав или нажав кнопку "/asks"', reply_markup=btmk)


@dp.message_handler(commands=['asks'])
async def send_instruction(message: types.Message):
    await message.answer(f'1) администрирование контракта \n 2) аффилированное лицо - лицо \n 3) база данных поставщиков и консультантов \n 4) база данных недобросовестных поставщиков и консультантов \n 5) банковское сопровождение контракта \n 6) бенефициарный владелец \n 7) близкие родственники \n 8) близкие лица \n 9) веб-портал государственных закупок (веб-портал) \n 10) государственные или муниципальные нужды \n 11) государственные закупки \n 12) гарантийное обеспечение исполнения контракта \n 13) гарантийное обеспечение предложения поставщика \n 13) гарантийное обеспечение предложения поставщика \n 14) демпинговая цена \n 15) декларация, гарантирующая предложение поставщика \n 16) декларация, гарантирующая исполнение контракта \n 17) документация о закупке \n  18) закупающая организация \n 19) идентификационный код \n 20) консультант \n 21) консультационные услуги \n 22) контракт \n 23) предложение поставщика иликонсультанта \n 24) комиссия по закупке \n 25) критерии оценки \n 26) лот \n 27) мониторинг \n 28) национальный режим \n 29) недостоверная информация несоответствующие действительности данные, предоставленные поставщикомконсультантом в своем предложении; \n 30) общий классификатогосударственных закупок \n 31) оценка предложений процесс определения соответствия предложений поставщиков и консультантокритериям, установленным документацией о закупке; \n 32) оцененная стоимость \n 33) план закупок \n 34) поставщик \n 35) (утратил силу в соответствии с Законом Кыргызской Республики от 25 июля 2023 года № 147) \n 36) (утратил силу в соответствии с Законом Кыргызской Республики от 25 июля 2023 года № 147) \n 37) протокол \n 38) работы \n 39) рамочное соглашение \n 40) смарт-контракт \n 41) срок для предложений \n 42) срок обжалования \n 43) товары \n 44) уполномоченный банк \n 45) уполномоченный государственныйорган по государственным закупкам \n 46) услуги \n 47) устойчивые государственныезакупки \n 48) центр закупок (далее - Агент) \n 49) электронный формат закупок \n 50) электронный каталог ДЛЯ ВЫБОРА ВОПРОСА НАПИШИТЕ ЦИФРУ У ВОПРОСА')


@dp.message_handler()
async def send_ask(message: types.Message):
    if message.text == '1':
        await message.reply(f'1) администрирование контракта - процесс управления и контроля за исполнением сторонами обязательств по контракту, осуществляемый с использованием веб-портала и/или электронного каталога, обеспечивающий прозрачный, доступный и подотчетный процесс исполнения контрактов, направленный на снижение рисков, связанных с ненадлежащим исполнением или неисполнением контрактов, а также коррупционных рисков при исполнении контракта;')
    if message.text == '2':
        await message.reply(f'2) аффилированное лицо - лицо, соответствующее одному или нескольким ниже перечисленным признакам, за исключением государственных и муниципальных учреждений, где участником или учредителем является закупающая организация, и деятельность которых не противоречит законодательству о конкуренции:- лицо, оказывающее влияние на принятие решения по процедурам государственных закупок;- руководитель и работник закупающих организаций/Агента, а также их близкие родственники или близкие лица;- участник (учредитель) поставщика или консультанта, который является лицом, занимающим политическую государственную должность, политическую муниципальную должность, специальную государственную должность, и его близкие родственники или близкие лица, владеющие долей в уставном капитале поставщика или консультанта;')
    if message.text == '3':
        await message.reply(f'3) база данных поставщиков и консультантов - электронная база данных, содержащая совокупность информации о поставщиках и консультантах, участвующих в процедурах государственных закупок, интегрируемая с государственными информационными системами для раскрытия информации о поставщиках и консультантах в соответствии с законодательством о государственных закупках;')
    if message.text == '4':
        await message.reply(f'4) база данных недобросовестных поставщиков и консультантов - реестр недобросовестных поставщиков и консультантов, а также их руководителей, включенных в него за неисполнение или ненадлежащее исполнение своих обязательств по контракту и за нарушения правил участия в процедурах государственных закупок;')
    if message.text == '5':
        await message.reply(f'5) банковское сопровождение контракта - обеспечение уполномоченным банком на основании договора о банковском сопровождении проведения платежей, мониторинга расчетов, осуществляемых поставщиком и всеми привлекаемыми в ходе исполнения контракта другими лицами в рамках исполнения данного контракта, на отдельном счете, открытом в одном из уполномоченных банков, для контроля за целевым расходованием денежных средств, а также доведение результатов банковского сопровождения контрактов до сведения закупающей организации/Агента;f')
    if message.text == '6':
        await message.reply(f'6) бенефициарный владелец юридического лица - физическое лицо (физические лица), которое в конечном итоге (через цепочку владения и контроля) прямо или косвенно (через третьих лиц) владеет юридическим лицом на праве собственности или контролирует юридическое лицо, оказывает влияние на принятие им решений;')
    if message.text == '7':
        await message.reply(f'7) близкие родственники - отец и мать, усыновители, дети, в том числе усыновленные, полнородные и неполнородные братья и сестры, дедушка, бабушка, внуки;')
    if message.text == '8':
        await message.reply(f'8) близкие лица - лица, состоящие в зарегистрированном браке, в том числе лица, которые совместно проживают, но не состоят в браке, а также отчим, мачеха, пасынок, падчерица, зять, невестка;')
    if message.text == '9':
        await message.reply(f'9) веб-портал государственных закупок (веб-портал) - государственная информационная система, созданная уполномоченным государственным органом по государственным закупкам в целях обеспечения прозрачного, доступного и подотчетного процесса государственных закупок с сохранением информации сроком не менее 10 лет;')
    if message.text == '10':
        await message.reply(f'10) государственные или муниципальные нужды - потребности закупающих организаций в товарах, работах, услугах и консультационных услугах, удовлетворяемые полностью или частично за счет государственных средств;')
    if message.text == '11':
        await message.reply(f'11) государственные закупки - приобретение закупающей организацией товаров, работ, услуг и консультационных услуг методами, установленными настоящим Законом, финансируемое полностью или частично за счет государственных средств. Государственными средствами признаются:- средства республиканского, местного бюджетов для осуществления деятельности закупающими организациями;- средства специальных счетов;- средства фондов и иных юридических лиц, созданных за счет государственных средств, средств государственных органов или органов местного самоуправления;- средства, предоставляемые в качестве иностранной помощи на основании международных договоров, вступивших в силу в соответствии с законодательством Кыргызской Республики, если иные способы использования средств не предусмотрены такими соглашениями;- кредитные средства, гарантированные и обеспеченные государством;')
    if message.text == '12':
        await message.reply(f'12) гарантийное обеспечение исполнения контракта - способ обеспечения исполнения обязательств поставщиком перед закупающей организацией/Агентом по контракту - по форме, предусмотренной настоящим Законом;')
    if message.text == '13':
        await message.reply(f'13) гарантийное обеспечение предложения поставщика - способ обеспечения исполнения обязательств предложения поставщика по форме, предусмотренной настоящим Законом;')
    if message.text == '14':
        await message.reply(f'14) демпинговая цена - цена, предложенная поставщиком на работы, услуги и товары, которая является ниже запланированной стоимости предмета закупки, определенной закупающей организацией/Агентом, более чем на 20 процентов;')
    if message.text == '15':
        await message.reply(f'15) декларация, гарантирующая предложение поставщика - документ, подписанный поставщиком и представляемый в закупающую организацию/Агенту как гарантия обеспечения исполнения обязательств, указанных в предложении;')
    if message.text == '16':
        await message.reply(f'16) декларация, гарантирующая исполнение контракта - документ, подписанный поставщиком и представляемый в закупающую организацию/Агенту как способ обеспечения исполнения обязательств, предусмотренных контрактом;')
    if message.text == '17':
        await message.reply(f'17) документация о закупке - пакет документов, включая любые изменения к ним, представляемый закупающей организацией/Агентом поставщику или консультанту для подготовки ими предложения, содержащий условия, порядок проведения закупок, в том числе проект контракта;')
    if message.text == '18':
        await message.reply(f'18) закупающая организация -государственный орган, орган местного самоуправления, государственные имуниципальные учреждения, фонды и иные юридические лица, созданные за счетгосударственных средств, средств государственных органов или органов местногосамоуправления;')
    if message.text == '19':
        await message.reply(f'19) идентификационный код -набор цифр и символов, выдаваемый веб-порталом государственных закупок путемшифрования наименования поставщика в процессе проведения государственных закупокдвухпакетным способом неограниченного метода с целью исключения конфликтаинтересов и человеческого фактора, иными словами наименование поставщикавскрывается во время второго пакета двухпакетного способа;')
    if message.text == '20':
        await message.reply(f'20) консультант - физическое(индивидуальный консультант) или юридическое лицо, оказывающее консультационныеуслуги;')
    if message.text == '21':
        await message.reply(f'21) консультационные услуги -услуги интеллектуального или консультационного характера, предоставляемыеконсультантами, имеющими необходимые специализированные профессиональные знания,опыт и соответствующую квалификацию, в том числе разработка проектно-сметнойдокументации (проектирование зданий, сооружений), разработка которых неосновывается на стандартных нормах и правилах, утвержденных уполномоченнымгосударственным органом по разработке и реализации политики в сфереархитектурно-строительной деятельности;')
    if message.text == '22':
        await message.reply(f'22) контракт - договор озакупке между закупающей организацией/Агентом и поставщиком, консультантом,заключаемый по результатам процедур закупок или рамочного соглашения;')
    if message.text == '23':
        await message.reply(f'23) предложение поставщика иликонсультанта - предложение поставщика на поставку товаров, оказание услуг,осуществление работ или предложение консультанта на оказание консультационныхуслуг при проведении государственных закупок;')
    if message.text == '24':
        await message.reply(f'24) комиссия по закупке -коллегиальный орган, создаваемый закупающей организацией для выполнения функцийв соответствии с настоящим Законом;')
    if message.text == '25':
        await message.reply(f'25) критерии оценки -установленные в документации о закупке объективные критерии для определенияпобедителя закупки;')
    if message.text == '26':
        await message.reply(f'26) лот - неделимый предметзакупок, выступающий отдельным предметом закупки, оценка которого должнапроизводиться независимо от других лотов;')
    if message.text == '27':
        await message.reply(f'27) мониторинг - исследованиерынка, результаты которого используются для обеспечения эффективности иэкономичности закупок;')
    if message.text == '28':
        await message.reply(f'8) национальный режим - режимпредусматривающий допуск товаров, работ, услуг иностранного происхождения поставщиков (подрядчиков), предлагающих такие товары, выполняющих работыоказывающих услуги, к участию в государственных закупках на равных условиях товарами кыргызского происхождения, работами, услугами, соответственнвыполняемыми, оказываемыми поставщиками (подрядчиками) Кыргызской Республикиесли требование о предоставлении такого режима установлено международнымдоговорами, вступившими в силу в соответствии с законодательством КыргызскоРеспублики;')
    if message.text == '29':
        await message.reply(f'29) недостоверная информация несоответствующие действительности данные, предоставленные поставщикомконсультантом в своем предложении;')
    if message.text == '30':
        await message.reply(f'30) общий классификатогосударственных закупок - систематизированный свод наименований и кодотоваров, работ, услуг и консультационных услуг, сгруппированных по различныпризнакам, направленным для мониторинга государственных закупок, утверждаемырешением уполномоченного государственного органа по государственнызакупкам;')
    if message.text == '31':
        await message.reply(f'31) оценка предложений процесс определения соответствия предложений поставщиков и консультантокритериям, установленным документацией о закупке;')
    if message.text == '32':
        await message.reply(f'32) оцененная стоимость - ценапредложения поставщика с учетом жизненного цикла и критериев качества, указанныхв документации о закупке;')
    if message.text == '33':
        await message.reply(f'33) план закупок - документ,содержащий сведения о закупке товаров, работ, услуг и консультационных услуг,которые запланированы для обеспечения государственных нужд;')
    if message.text == '34':
        await message.reply(f'34) поставщик - любоеюридическое или физическое лицо, участвующее в процедурах закупок по поставкетоваров, работ и услуг;')
    if message.text == '35':
        await message.reply(f'35) (утратил силу в соответствии с Законом Кыргызской Республики от 25 июля 2023 года № 147)')
    if message.text == '36':
        await message.reply(f'36) (утратил силу в соответствии с Законом Кыргызской Республики от 25 июля 2023 года №147)')
    if message.text == '37':
        await message.reply(f'37) протокол - документальныйотчет, отражающий соответствующий этап процесса закупок;')
    if message.text == '38':
        await message.reply(f'38) работы - вся деятельность,связанная со строительством, реконструкцией, сносом, ремонтом или обновлениемздания, сооружения или объекта;')
    if message.text == '39':
        await message.reply(f'39) рамочное соглашение -соглашение, подписанное с одним и более поставщиками, в котором оговариваютсяусловия будущего контракта;')
    if message.text == '40':
        await message.reply(f'40) смарт-контракт - контракт вэлектронной форме, формируемый с использованием информационных технологий.Исполнение прав и обязанностей по смарт-контракту осуществляется путемсовершения действий в определенном порядке в последовательности и принаступлении обстоятельств, определенных таким контрактом;')
    if message.text == '41':
        await message.reply(f'41) срок для предложений -период со дня публикации объявления о проведении закупки до окончательного срокапредставления предложений;')
    if message.text == '42':
        await message.reply(f'42) срок обжалования - срок дляподачи жалобы и административной жалобы участниками государственных закупок,установленный настоящим Законом;')
    if message.text == '43':
        await message.reply(f'43) товары - продукты трудалюбого вида и описания, в том числе сырье, изделия, оборудование и предметы втвердом, жидком или газообразном состоянии, электрическая энергия, а такжеуслуги, сопутствующие поставкам товаров, если стоимость таких сопутствующихуслуг не превышает стоимости самих товаров;')
    if message.text == '44':
        await message.reply(f'44) уполномоченный банк - банк,в отношении которого Кабинетом Министров принято решение о включении его вперечень банков, уполномоченных осуществлять банковское сопровождениеконтрактов;')
    if message.text == '45':
        await message.reply(f'45) уполномоченный государственныйорган по государственным закупкам - уполномоченный Кабинетом Министровгосударственный орган, проводящий государственную политику в области закупоктоваров, работ, услуг и консультационных услуг;')
    if message.text == '46':
        await message.reply(f'46) услуги - любые закупки, заисключением товаров, работ и консультационных услуг, на основе степениэффективного измеряемого физического результата;')
    if message.text == '47':
        await message.reply(f'47) устойчивые государственныезакупки - процесс, при котором закупающие организации/Агент должны оценитьвыгоды не только для организации, но и для общества, с минимизацией ущербаокружающей среде. При оценке стоимости учитывается стоимость жизненного циклапродукции;')
    if message.text == '48':
        await message.reply(f'48) центр закупок (далее - Агент) -орган, на который возложена функция проведения централизованных закупок повидам товаров, работ, услуг и консультационных услуг, определяемых решениемКабинета Министров;')
    if message.text == '49':
        await message.reply(f'49) электронный формат закупок- процедура организации и проведения закупок в сети Интернет, осуществляемаяс использованием информационных систем (веб-портал) и электронных информационныхресурсов, обеспечивающая процедуру приобретения предмета закупок в режимереального времени;')
    if message.text == '50':
        await message.reply(f'50) электронный каталог -электронная торговая информационная площадка, предоставляющаясистематизированный перечень стандартных товаров, работ и услуг с указаниемтекущих цен, предлагаемых поставщиками.(В редакции Закона Кыргызской Республики от 25 июля 2023 года')
    else:
        for i in range(51):
            if message.text == i:
                await message.reply('Простите такого вопроса нет! Выберите другой!')


if __name__ == "__main__":
    executor.start_polling(dp)