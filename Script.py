class script(object):
    START_TXT = """<b>ππ·π΄π π±π°πππ°ππ³,</b>{},
<b>πΈ'πΌ <a href=https://t.me/{}>{}</a>,

 β πΈ π°πΌ π° πΆππ΄π°π π±π°π±π ππΈπππ΄π π΅πΎπ ππΎππ π΅πΈπ»π΄π..
 β πΉπππ π°π³π³ πΌπ΄ ππΎ ππΎππ πΆππΎππΏ π°π½π³ πΌπ°πΊπ΄ πΌπ΄ π°π³πΌπΈπ½ ππ·π΄ππ΄..
 β ππ·π΄π½ ππΎπ π²π°π½ ππ΄π΄ πΌπ πΆππ΄π°ππ½π΄ππ..π
 
 ππ ππππππ:<a href=https://t.me/themastertheblaster>β£οΈ βΞ΅cΟβΞ΅ΙΎ ΰΈ£Ξ΅Ξ΅Ι±Ξ±Ι³ β£οΈ</a></b>"""

    HELP_TXT = """<b>π·π΄π π±ππ³π³π {}
π·π΄ππ΄ πΈπ πΌπ π·π΄π»πΏ π²πΎπΌπΌπ°π½π³π.</b>"""
    ABOUT_TXT = """<b>π MΚ Nα΄α΄α΄ : <a href=https://t.me/mkvstevefilter_bot>π ΡΟΡΞ½Ρ Π½Ξ±ΡΡΞΉΠΈgΟΞΏΠΈ π</a></b>
<b>π« MΚ FΚΙͺα΄Ι΄α΄ : <a href=https://t.me/themastertheblaster>β£οΈ βΞ΅cΟβΞ΅ΙΎ ΰΈ£Ξ΅Ξ΅Ι±Ξ±Ι³ β£οΈ</a></b>
<b>π΅π· Cα΄α΄Ι΄α΄ΚΚ :  <a href=https://www.google.com/search?q=USA+&ei=Z3rKYvOXGtS34t4Pp6mEgAU&ved=0ahUKEwiz5_KR4e34AhXUm9gFHacUAVAQ4dUDCA4&uact=5&oq=USA+&gs_lcp=Cgdnd3Mtd2l6EAMyBwgAELEDEEMyCggAELEDEIMBEEMyBAgAEEMyCggAELEDEIMBEEMyBAgAEEMyBggAEAoQQzIECAAQQzIGCAAQChBDMgQIABBDMgcIABCxAxBDOgcIABBHELADOgcIABCwAxBDOgoIABDkAhCwAxgBOg8ILhDUAhDIAxCwAxBDGAI6DAguEMgDELADEEMYAjoHCC4QsQMQQzoKCC4QxwEQ0QMQQzoHCC4Q1AIQQzoOCAAQgAQQsQMQgwEQyQM6BAguEEM6FAgAEOoCELQCEIoDELcDENQDEOUCOhEILhCABBCxAxCDARDHARDRAzoLCAAQgAQQsQMQgwE6DgguELEDEIMBEMcBENEDOgsILhCABBCxAxCDAToNCC4QsQMQgwEQ1AIQQzoKCC4QxwEQowIQQzoKCC4QsQMQgwEQQ0oECEEYAEoECEYYAVCFCljAHGD_OmgCcAF4A4AB3ASIAd8dkgEHMi0yLjUtNpgBAKABAbABCsgBEMABAdoBBggBEAEYCdoBBggCEAEYCA&sclient=gws-wiz#>USA</a></b>
<b>π Lα΄Ι΄Ι’α΄α΄Ι’α΄ : <a href=https://en.wikipedia.org/wiki/English_language>EΙ΄Ι’ΚΙͺsΚ</a></b>
<b>π½ Sα΄α΄α΄α΄ : <a href=https://www.google.com/search?q=texas&ei=uozKYoTTHvjNseMP9P-Y6A0&gs_ssp=eJzj4tDP1TcwT4rPMWD0Yi1JrUgsBgAqsgUX&oq=texas&gs_lcp=Cgdnd3Mtd2l6EAEYADIICC4QsQMQkQIyBAgAEEMyBAgAEEMyCgguELEDENQCEEMyCgguELEDEIMBEEMyDQguELEDEIMBENQCEEMyDggAEIAEELEDEIMBEMkDMhEILhCABBCxAxCDARDHARDRAzIOCC4QgAQQsQMQgwEQ1AIyCwgAEIAEELEDEIMBOgcIABBHELADOgcIABCwAxBDOgcIABCxAxBDOgUIABCABDoKCAAQ6gIQtAIQQzoKCAAQsQMQgwEQQzoQCC4QsQMQgwEQxwEQ0QMQQzoICAAQsQMQgwE6BwguELEDEEM6DAgAELEDEIMBEAoQQzoRCC4QgAQQsQMQgwEQxwEQrwFKBAhBGABKBAhGGABQ1gpYxyhgiDtoAnABeAOAAdYBiAHEEZIBBjAuMTUuMZgBAKABAbABCsgBCsABAQ&sclient=gws-wiz#>Tα΄xα΄s</a></b>
<b>πͺ΄ Bα΄ΚΙ΄ : <a href=https://www.google.com/search?q=hawkins+city&ei=1ozKYvWeL8KUseMPkNefwAc&gs_ssp=eJzj4tTP1TcwNEhONjRg9OLJSCzPzswrVkjOLKkEAFl_B7w&oq=haw&gs_lcp=Cgdnd3Mtd2l6EAEYAzIHCC4QsQMQQzIQCC4QsQMQgwEQxwEQowIQQzIECAAQQzIKCC4QsQMQgwEQQzIHCC4Q1AIQQzIECAAQQzIECAAQQzIECAAQQzILCC4QgAQQsQMQ1AIyBwguENQCEEM6BwgAEEcQsAM6BwgAELADEEM6CggAEOQCELADGAE6DQgAEOQCELADEMkDGAE6DwguENQCEMgDELADEEMYAjoMCC4QyAMQsAMQQxgCOgoILhDHARDRAxBDOgoIABCxAxCDARBDOgcIABCxAxBDOg4IABCABBCxAxCDARDJAzoECC4QQzoNCC4Q1AIQ6gIQtAIQQzoKCC4Q6gIQtAIQQzoLCAAQgAQQsQMQgwE6CggAELEDEIMBEAo6CAgAELEDEIMBOhEILhCABBCxAxCDARDHARCjAjoICC4QsQMQgwE6CgguEMcBEKMCEENKBAhBGABKBAhGGAFQrQtYjR9ghTdoAnABeAOAAdkBiAH1B5IBBTAuNi4xmAEAoAEBsAEKyAEQwAEB2gEGCAEQARgJ2gEGCAIQARgI&sclient=gws-wiz#>Hα΄α΄‘α΄ΙͺΙ΄s</a></b>
<b>β€οΈβπ₯ MΚ Lα΄α΄ α΄Κ : <a href=https://www.google.com/search?q=nancy+wheeler&ei=Ro3KYqShHe-hseMP5ZuS2Ak&oq=NAn&gs_lcp=Cgdnd3Mtd2l6EAMYADIFCAAQkQIyBQgAEJECMgQILhBDMgcILhDUAhBDMgQILhBDMgQIABBDMgoILhDHARCjAhBDMg4ILhCABBCxAxCDARDUAjIICC4QgAQQsQMyCwguEIAEELEDEIMBOgcIABBHELADOgcIABCwAxBDOgoIABDkAhCwAxgBOgwILhDIAxCwAxBDGAI6EgguEMcBEKMCEMgDELADEEMYAjoKCC4QsQMQgwEQQzoECAAQAzoFCAAQgAQ6CgguEOoCELQCEEM6CggAEOoCELQCEEM6DQguENQCEOoCELQCEEM6EAguELEDEIMBEMcBENEDEEM6CwgAEIAEELEDEIMBOggIABCxAxCDAToICC4Q1AIQkQJKBAhBGABKBAhGGAFQ7QZYxBtgpTJoAnABeASAAfkCiAH3D5IBBzAuMS42LjGYAQCgAQGwAQrIARPAAQHaAQYIARABGAnaAQYIAhABGAg&sclient=gws-wiz>Nα΄Ι΄α΄Κ WΚα΄α΄Κα΄Κ</a></b>
<b>π’ MΚ O??Ιͺα΄α΄  : <a href=https://t.me/Mkv_blasters>MKV BΚα΄sα΄α΄Κs </a></b>
<b>π¨βπ« MΚ Sα΄Κα΄α΄Κ : <a href=https://www.google.com/search?q=hawkins+high+school&oq=hawkins+hi&aqs=chrome.0.0i131i433i512j69i57j0i512l7.6697j0j9&client=ms-android-samsung-ss&sourceid=chrome-mobile&ie=UTF-8#imgrc=KF1BErh5KE74eM>Hα΄α΄‘α΄ΙͺΙ΄s HΙͺΙ’Κ Sα΄Κα΄α΄Κ</a></b>"""
    DONATION_TXT = """<b>ππ¨π¨π€π’ππ¬ & ππ¦π¨π¨π­π‘π’ππ¬</b> 

βΊβΊ <b>ππ¨π§ππ­π’π¨π§</b>

βͺΌ <b>ππ¨π? πππ§ ππ?π² ππ ππ§π² ππ¨π¨π€π’π (π¨π«) ππ¦π¨π¨π­π‘π’π π³. 
<b>βββββββββα Payment Methods αβββββββββ
β? ππΌπΌπ΄πΉπ²π£π?π
β? π£π?πππΊ
β? π£π΅πΌπ»π²π£π²
β? π£π?ππ£π?πΉ
_ππ¨π§π­πππ­ ππ ππ¨π« ππ§π¨π° πππ¨π?π­ ππ‘π πππ²π¦ππ§π­ ππ§ππ¨_
ββββββββββββα <a href=https://t.me/themastertheblaster><b>β£οΈ βΞ΅cΟβΞ΅ΙΎ ΰΈ£Ξ΅Ξ΅Ι±Ξ±Ι³ β£οΈ</b></a> αββββββββββββ

βΊβΊ <b>πππ’π ππ«π¨π¦π¨π­π’π¨π§</b>

βͺΌ <b>ππ¨π§π­πππ­ ππ ππ’π­π‘ ππ¨π? ππ¨π§π­ππ§π­ ππ‘π’ππ‘ ππ¨π? πππ§π­ ππ¨ ππ«π¨π¦π¨π­π . 
<b>βββββββββα Payment Methods αβββββββββ
β? ππΌπΌπ΄πΉπ²π£π?π
β? π£π?πππΊ
β? π£π΅πΌπ»π²π£π²
β? π£π?ππ£π?πΉ
_ππ¨π§π­πππ­ ππ ππ’π­π‘ ππ¨π?π« ππ¨π§π­ππ§π­ ππ§π ππ§π¨π° πππ¨π?π­ ππ‘π πππ²π¦ππ§π­ ππ§ππ¨_
ββββββββββββα <a href=https://t.me/themastertheblaster><b>β£οΈ βΞ΅cΟβΞ΅ΙΎ ΰΈ£Ξ΅Ξ΅Ι±Ξ±Ι³ β£οΈ</b></a> αββββββββββββ"""
    PROMOTION_TXT = """<b>γ πππ’π ππ«π¨π¦π¨π­π’π¨π§ γ</b>

βͺΌ <b>ππ¨π§π­πππ­ ππ ππ’π­π‘ ππ¨π? ππ¨π§π­ππ§π­ ππ‘π’ππ‘ ππ¨π? πππ§π­ ππ¨ ππ«π¨π¦π¨π­π . 
<b>βββββββββα Payment Methods αβββββββββ
β? ππΌπΌπ΄πΉπ²π£π?π
β? π£π?πππΊ
β? π£π΅πΌπ»π²π£π²
β? π£π?ππ£π?πΉ
_ππ¨π§π­πππ­ ππ ππ’π­π‘ ππ¨π?π« ππ¨π§π­ππ§π­ ππ§π ππ§π¨π° πππ¨π?π­ ππ‘π πππ²π¦ππ§π­ ππ§ππ¨_
ββββββββββββα <a href=https://t.me/themastertheblaster><b>β£οΈ βΞ΅cΟβΞ΅ΙΎ ΰΈ£Ξ΅Ξ΅Ι±Ξ±Ι³ β£οΈ</b></a> αββββββββββββ""" 
    FILE_TXT = """β€ πππ₯π©: ππ’π₯π ππ­π¨π«π ππ¨ππ?π₯π../

<b>π±π πππΈπ½πΆ ππ·πΈπ πΌπΎπ³ππ»π΄ ππΎπ π²π°π½ πππΎππ΄ π΅πΈπ»π΄π πΈπ½ πΌπ π³π°ππ°π±π°ππ΄ π°π½π³ πΈ ππΈπ»π» πΆπΈππ΄ ππΎπ π° πΏπ΄ππΌπ°π½π΄π½π π»πΈπ½πΊ  ππΎ π°π²π²π΄ππ ππ·π΄ ππ°ππ΄π³ π΅πΈπ»π΄π.πΈπ΅ ππΎπ ππ°π½π ππΎ π°π³π³ π΅πΈπ»π΄π π΅ππΎπΌ π° πΏππ±π»πΈπ² π²π·π°π½π½π΄π» ππ΄π½π³ ππ·π΄ π΅πΈπ»π π»πΈπ½πΊ πΎπ½π»π  πΎπ ππΎπ ππ°π½π ππΎ π°π³π³ π΅πΈπ»π΄π π΅ππΎπΌ π°  πΏππΈππ°ππ΄ π²π·π°π½π½π΄π» ππΎπ πΌπππ πΌπ°πΊπ΄ πΌπ΄ π°π³πΌπΈπ½ πΎπ½ ππ·π΄ π²π·π°π½π½π΄π» ππΎ π°π²π²π΄ππ π΅πΈπ»π΄π...//</b>

βͺΌ ππ¨π¦π¦ππ§ππ¬ ππ§π ππ¬ππ π βΊ

βͺ /plink βΊβΊ <b>ππ΄πΏπ»π ππΎ π°π½π πΌπ΄π³πΈπ° ππΎ πΆπ΄π π»πΈπ½πΊ.</b>
βͺ /pbatch βΊβΊ <b>πππ΄ ππΎππ πΌπ΄π³πΈπ° π»πΈπ½πΊ ππΈππ· ππ·πΈπ π²πΎπΌπΌπ°π½π³.</b>
βͺ /batch βΊβΊ <b>ππΎ π²ππ΄π°ππ΄ π»πΈπ½πΊ π΅πΎπ πΌππ»ππΈπΏπ»π΄ π΅πΈπ»π΄π.</b>

βͺΌ ππ±ππ¦π©π₯π βΊ

<code>/batch https://t.me/Mkv_blasters/3 https://t.me/Mkv_blasters/8</code>

π²ππ΄π³πΈππ βΊβΊ <a href=https://t.me/Mkv_bots><b>πΌπΊπ π±πΎππ</b></a>"""
    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- Give a user details
β’/whois :-give a user full details"""
    FUN_TXT ="""<b>Gα΄α΄α΄s</b> 
    
<b>β‘ πΉπππ ππΎπΌπ΄ πΊπΈπ½π³ πΎπ΅ π΅ππ½ ππ·πΈπ½πΆ'π β‘</b>
 
π£. /dice - ππΎπ»π΄ ππ·π΄ π³πΈπ²π΄ 
π€. /Throw ππ /Dart - ππΎ πΌπ°πΊπ΄ π³π°ππ 
3. /Runs - ππΎπΌπ΄ ππ°π½π³πΎπΌ π³πΈπ°π»πΎπΆππ΄π 
4. /Goal or /Shoot - ππΎ πΌπ°πΊπ΄ π° πΆπΎπ°π» πΎπ ππ·πΎπΎπ
5. /luck or /cownd - ππΏπΈπ½ π°π½π³ πππ ππΎππ π»ππ²πΊ"""
    DEPLOY_TXT = """<b>π·πΎπ ππΎ π±π΄ πΌπ π±π΄ππ π΅ππΈπ΄π½π³..?</b> 
  
<b>β? Tutorial βΊβΊ</b> <i><b>https://youtube.com/channel/UCdk53DCXKoKOKgKeohUEnmA</b></i>

<b>πΈπ΅ ππΎπ ππ°π½π ππΎ π±π΄ πΌπ π±π΄ππ π΅ππΈπ΄π½π³ π²πΎπ½ππ°π²π <a href=https://t.me/themastertheblaster>β£οΈ βΞ΅cΟβΞ΅ΙΎ ΰΈ£Ξ΅Ξ΅Ι±Ξ±Ι³ β£οΈ</a></b>

<b>ππ·π°ππ΄ π°π½π³ πππ±ππ²ππΈπ±π΄</b>
π²ππ΄π³πΈππ βΊβΊ <a href=https://t.me/Mkv_bots><b>πΌπΊπ π±πΎππ</b></a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and <b>ΡΟΡΞ½Ρ</b>  will respond whenever a keyword is found the message

<b>NOTE:</b>
1. <b>ΡΟΡΞ½Ρ</b> should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
β’ /filter - <code>add a filter in chat</code>
β’ /filters - <code>list all the filters of a chat</code>
β’ /del - <code>delete a specific filter in chat</code>
β’ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    SONG_TXT = """<b>ππΎπ½πΆ π³πΎππ½π»πΎπ°π³ πΌπΎπ³ππ»π΄</b>

<b>ππΎπ½πΆ π³πΎππ½π»πΎπ°π³ πΌπΎπ³ππ»π΄, π΅πΎπ ππ·πΎππ΄ ππ·πΎ π»πΎππ΄ πΌπππΈπ². ππΎπ π²π°π½ πππ΄ ππ·πΈπ π΅π΄π°πππ΄ π΅πΎπ π³πΎππ½π»πΎπ°π³ π°π½π ππΎπ½πΆ ππΈππ· πππΏπ΄π π΅π°ππ ππΏπ΄π΄π³.ππΎππΊπ πΎπ½π»π πΎπ½ πΆππΎππΏπ../</b>

<b>π²πΎπΌπΌπ°π½π³π</b>

βΊβΊ  /song ππΎπ½πΆ π½π°πΌπ΄ 

ππΎππΊπ πΎπ½π»π πΎπ½ πΆππΎππΏ

π²ππ΄π³πΈππ :- <a href=https://t.me/mkv_bots>πΌπΊπ π±πΎππ</a>"""
    PIN_TXT ="""<b>PIN MODULE</b>
<b>πΏπΈπ½ π° πΌπ΄πππ°πΆπ΄../</b>

<b>π°π»π» ππ·π΄ πΏπΈπ½ ππ΄π»π°ππ΄π³ π²πΎπΌπΌπ°π½π³π π²π°π½ π±π΄ π΅πΎππ½π³ π·π΄ππ΄::</b>

<b>ππ²πΎπΌπΌπ°π½π³π π°π½π³ πππ°πΆπ΄π</b>

β /pin :- ππΎ πΏπΈπ½ ππ·π΄ πΌπ΄πππ°πΆπ΄ πΎπ½ ππΎππ π²π·π°ππ
β /unpin :- ππΎ ππ½πΏπΈπ½ ππ·π΄ π²ππππ΄π΄π½π πΏπΈπ½π½π΄π³ πΌπ΄ππ°π°πΆπ΄"""
    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>

β’ /paste [text] - paste the given text on Pasty

<b>NOTE:</b>

β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""
    TTS_TXT = """Help: <b> TTS π€ module:</b>

Translate text to speech

<b>Commands and Usage:</b>

β’ /tts <text> : convert text to speech

<b>NOTE:</b>

β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ IMDb can translate texts to 200+ languages."""
    PINGS_TXT ="""<b>π Ping:</b>

Helps you to know your ping πΆπΌββοΈ

<b>Commands:</b>

β’ /alive - To check you are alive.
β’ /help - To get help.
β’ /ping - To get your ping.
β’ /repo - Source Code.
β’ /channel - Channel Details.
β’ /steve - Bot Link.
<b>πΉUsageπΉ :</b>

β’ This commands can be used in pms and groups
β’ This commands can be used buy everyone in the groups and bots pm
β’ Share us for more features"""
    TELE_TXT = """<b>β«οΈHELP: TelegraphβͺοΈ</b>

Do as you wish with telegra.ph module!

</b>USAGE:</b>

π€§ /telegraph - Send me Picture or Vide Under (5MB)

<b>NOTE:</b>

β’ This Command Is Available in goups and pms
β’ This Command Can be used by everyone"""

    PRIVATEBOT_TXT = """<b>π³πΎ ππΎπ ππ°π½π ππΎ π±π΄ πΌπ π±π΄ππ π΅ππΈπ΄π½π³</b>
<b>βΊβΊ π³πΎ ππΎπ ππ°π½π ππΎ π±π΄ πΌπ π±π΄ππ π΅ππΈπ΄π½π³ π»πΈπΊπ΄ β£οΈ βΞ΅cΟβΞ΅ΙΎ ΰΈ£Ξ΅Ξ΅Ι±Ξ±Ι³ β£οΈ</b>
<b>βΊβΊ ππΈππ· π°π»π» ππΎππ π²ππ΄π³πΈππ</b>
<b>βΊβΊ ππΈππ· ππΎππ πΎππ½π΄πππ·πΈπΏ</b>
<b>βΊβΊ π²πΎπ½ππ°π²π πΌπ΄ <a href=https://t.me/themastertheblaster>β£οΈ βΞ΅cΟβΞ΅ΙΎ ΰΈ£Ξ΅Ξ΅Ι±Ξ±Ι³ β£οΈ</a></b>"""

    JSON_TXT ="""<b>JSON:</b>

Bot returns json for all replied messages with /json

<b>Features:</b>

Message Editting JSON
Pm Support
Group Support

<b>Note:</b>

Everyone can use this command , if spaming happens bot will automatically ban you from the group."""
    PURGE_TXT = """<b>Purge</b>
    
Delete A Lot Of Messages From Groups! 
    
 <b>ADMIN</b> 

β /purge :- Delete All Messages From The Replied To Message, To The Current Message"""
    BUTTON_TXT = """Help: <b>Buttons</b>

-<b>ΡΟΡΞ½Ρ</b> Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. <b>ΡΟΡΞ½Ρ</b> supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/mkv_blasters)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """<b>π°πππΎ π΅πΈπ»ππ΄π πΎπ½/πΎπ΅π΅ πΌπΎπ³ππ»π΄..</b>

<b>π°πππΎ π΅πΈπ»ππ΄π πΈπ ππ·π΄ π΅π΄π°ππππ΄ ππΎ π΅πΈπ»ππ΄π π°π½π³ ππ°ππ΄  ππ·π΄ π΅πΈπ»π΄π π°πππΎπΌπ°ππΈπ²π°π»π»π π΅ππΎπΌ π²π·π°π½π½π΄π» ππΎ πΆππΎππΏ. ππΎπ π²π°π½ πππ΄ ππ·π΄ π΅πΎπ»π»πΎππΈπ½πΆ π²πΎπΌπΌπ°π½π³π ππΎ πΎπ½ π°π½π³ πΎπ΅π΅ ππ·π΄ π°πππΎπ΅πΈπ»ππ΄π πΈπ½ ππΎππ πΆππΎππΏ.../</b>

<b>π²πΎπΌπΌπ°π½π³π :-
<b>βΊβΊ /autofilter on - π΄π½π°π±π»π΄ π°πππΎ π΅πΈπ»ππ΄π πΈπ½ ππ·π΄ πΆππΎππΏπ.</b>
<b>βΊβΊ /autofilter off - π³πΈππ°π±π»π΄π³ π°πππΎ π΅πΈπ»ππ΄π πΈπ½ ππ·π΄ πΆππΎππΏπ.</b>
<b>βΊβΊ /set_template - ππ΄π π²ππππΎπΌ πΈπΌπ³π± ππ΄πΌπΏπ»π°ππ΄ π΅πΎπ π°πππΎ π΅πΈπ»ππ΄π.</b>
<b>βΊβΊ /get_template - πΆπ΄π π²ππππ΄π½π πΈπΌπ³π± ππ΄πΌπΏπ»π°ππ΄ πΎπ΅ π°πππΎ π΅πΈπ»ππ΄π.</b>

<b>π²ππ΄π³πΈππ :- <a href=https://t.me/mkv_bots>πΌπΊπ π±πΎππ</a></b>"""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
β’ /connect  - <code>connect a particular chat to your PM</code>
β’ /disconnect  - <code>disconnect from a chat</code>
β’ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of <b>ΡΟΡΞ½Ρ</b> 

<b>Commands and Usage:</b>
β’ /id - <code>get id of a specifed user.</code>
β’ /info  - <code>get information about a user.</code>
β’ /imdb  - <code>get the film information from IMDb source.</code>
β’ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
β’ /logs - <code>to get the rescent errors</code>
β’ /stats - <code>to get status of files in db.</code>
β’ /delete - <code>to delete a specific file from db.</code>
β’ /users - <code>to get list of my users and ids.</code>
β’ /chats - <code>to get list of the my chats and ids </code>
β’ /leave  - <code>to leave from a chat.</code>
β’ /disable  -  <code>do disable a chat.</code>
β’ /ban_user  - <code>to ban a user.</code>
β’ /unban_user  - <code>to unban a user.</code>
β’ /channel - <code>to get list of total connected channels</code>
β’ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b>π Tα΄α΄α΄Κ FΙͺΚα΄s : <code>{}</code></b>
<b>π€ Tα΄α΄α΄Κ Usα΄Κs : <code>{}</code></b>
<b>πͺ© Tα΄α΄α΄Κ CΚα΄α΄s : <code>{}</code></b>
<b>πΎ Usα΄α΄ Sα΄α΄Κα΄Ι’α΄ : <code>{}</code> πΌπ±</b>
<b>π FΚα΄α΄ Sα΄α΄Κα΄Ι’α΄  : <code>{}</code> πΌπ±</b>"""
    LOG_TEXT_G = """<b>#Nα΄α΄‘ GΚα΄α΄α΄</b>
    
<b>πͺ© GΚα΄α΄α΄ βͺΌ {}(<code>{}</code>)</b>
<b>π€ Tα΄α΄α΄Κ Mα΄α΄Κα΄Κs βͺΌ <code>{}</code></b>
<b>π― Aα΄α΄α΄α΄ BΚ βͺΌ {}</b>
"""
    LOG_TEXT_P = """<b>#Nα΄α΄‘ Usα΄Κ</b>
    
<b>πͺͺ Iα΄ - <code>{}</code></b>
<b>π? Nα΄α΄α΄ - {}</b>
"""
    REPORT_TXT = """β€ πππ₯π©: Rα΄α΄α΄Κα΄ β οΈ

ππππ πππππππ πππππ π’ππ ππ ππππππ π πππππππ ππ π ππππ ππ πππ ππππππ ππ πππ ππππππππππ πππππ. π³ππ'π ππππππ ππππ πππππππ.

β€ ππ¨π¦π¦ππ§ππ¬ ππ§π ππ¬ππ π:

βͺ/report ππ @admins - π³π ππΎππππ πΊ πππΎπ ππ πππΎ πΊπ½ππππ (ππΎπππ ππ πΊ ππΎπππΊππΎ)."""

    CORONA_TXT = """β€ πππ₯π©: π’ππππ½

ππππ π²ππππππ πππππ π’ππ ππ ππππ  πππππ’ πππππππππππ πππππ πππππ 

β€ ππ¨π¦π¦ππ§ππ¬ ππ§π ππ¬ππ π:

βͺ /covid - πππΎ ππππ πΌππππΊππ½ ππππ ππππ πΌππππππ ππΊππΎ ππ ππΎπ πΌππππ½πΎ πππΏππππΊππππ

βπ€ππΊππππΎ:
<code>/covid π¨ππ½ππΊ</code>"""

    URLSHORT_TXT = """β€ πππ₯π©: π΄ππ πππππππΎπ

ππππ πππππππ πππππ π’ππ ππ πππππ π πππ 

β€ ππ¨π¦π¦ππ§ππ¬ ππ§π ππ¬ππ π:

βͺ /short: πππΎ ππππ πΌππππΊππ½ ππππ ππππ ππππ ππ ππΎπ ππππππΎπ½ πππππ

βπ€ππΊππππΎ:
<code>/short https://youtube.com/channel/UCdk53DCXKoKOKgKeohUEnmA</code>"""

    VIDEO_TXT ="""π·π΄π»πΏ ππΎπ ππΎ π³πΎππ½π»πΎπ°π³ ππΈπ³π΄πΎ π΅ππΎπΌ ππΎππππ±π΄.

β’ ππ΄π’π¨π¦
π π°πΆ ππ’π― ππ°πΈπ―π­π°π’π₯ ππ―πΊ ππͺπ₯π¦π° ππ³π°π? π π°πΆπ΅πΆπ£π¦

ππ€π¬ ππ€ ππ¨π
β’ ππΊπ±π¦ /video or /mp4 ππ―π₯ (https://youtube.com/channel/UCdk53DCXKoKOKgKeohUEnmA)
β’ ππΉπ’π?π±π­π¦:
<code>/mp4 https://youtube.com/channel/UCdk53DCXKoKOKgKeohUEnmA</code>
<code>/video https://youtube.com/channel/UCdk53DCXKoKOKgKeohUEnmA</code>"""

    ZOMBIES_TXT = """π·π΄π»πΏ ππΎπ ππΎ πΊπΈπ²πΊ πππ΄ππ

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
β’ /inkick - command with required arguments and i will kick members from group.
β’ /instatus - to check current status of chat member from group.
β’ /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
β’ /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
β’ /dkick - to kick deleted accounts."""

    IMAGE_TXT = """β€ πππ₯π©: Iα΄α΄Ι’α΄

ππππ πππππππ πππππ π’ππ ππ ππππ πππππ ππππ’ ππππππ’ 

β€ ππ¨π¦π¦ππ§ππ¬ ππ§π ππ¬ππ π:

βͺ π©πππ ππΎππ½ ππΎ πΊ πππΊππΎ ππ πΎπ½ππ β¨

π¬πΊπ½πΎ π»π <a href=https://t.me/Mkv_bots>πΌπΊπ π±πΎππ</a>"""

    STICKER_TXT = """ππΎπ π²π°π½ πππ΄ ππ·πΈπ πΌπΎπ³ππ»π΄ ππΎ π΅πΈπ½π³ π°π½π πππΈπ²πΊπ΄ππ πΈπ³.
β’ πππππ
To Get Sticker ID
 
  β­ ππ€π¬ ππ€ ππ¨π
 
β Reply To Any Sticker [/stickerid]"""

    YTTHUMB_TXT = """π·π΄π»πΏπ ππΎ π³πΎππ½π»πΎπ°π³ π°π½π ππΎππππ±π΄ ππΈπ³π΄πΎ ππ·ππΌπ±π½π°πΈπ»
    
β­ππ€π¬ ππ€ ππ¨π
ππΊπ±π¦ /ytthumb ππ―π₯ ππͺπ₯π¦π° ππͺπ―π¬

β’ ππΉπ’π?π±π­π¦
<code>/ytthumb https://youtube.com/channel/UCdk53DCXKoKOKgKeohUEnmA</code>"""

    ABOOK_TXT = """β€ πππ₯π©: π ππ½πππ»πππ

πππ πππ πππππππ π πΏπ³π΅ ππππ ππ π πππππ ππππ π πππ ππππ πππππππ β―

β€ ππ¨π¦π¦ππ§ππ¬ ππ§π ππ¬ππ π:

βͺ /audiobook: π±πΎπππ ππππ πΌππππΊππ½ ππ πΊππ π―π£π₯ ππ ππΎππΎππΊππΎ πππΎ πΊππ½ππ"""

    GTRANS_TXT = """β€ πππ₯π©: π¦πππππΎ π³ππΊππππΊππΎπ

ππππ πππππππ πππππ π’ππ ππ πππππππππ π πππ‘π ππ πΊππ πππππππππ π’ππ π πππ. ππππ πππππππ π ππππ ππ ππππ ππ πππ πππππ β―

β€ ππ¨π¦π¦ππ§ππ¬ ππ§π ππ¬ππ π:

βͺ/tr - π³π πππΊππππΊππΎπ ππΎπππ ππ πΊ πππΎπΌππΏπΌ ππΊππππΊππΎ

β€ π­πππΎ:
πΆππππΎ πππππ /tr πππ ππππππ½ πππΎπΌππΏπ πππΎ ππΊππππΊππΎ πΌππ½πΎ

βπ€ππΊππππΎ: /ππ ππ
β’ πΎπ = π€ππππππ
β’ ππ = π¬πΊππΊππΊππΊπ
β’ ππ = π§πππ½π"""

    RESTRIC_TXT = """β€ πππ₯π©: Mα΄α΄α΄ π«

πππππ πππ πππ ππππππππ π πππππ πππππ πππ πππ ππ ππππππ πππππ πππππ ππππ πππππππππππ’.

βͺ/ban: π³π π»πΊπ πΊ πππΎπ πΏπππ πππΎ πππππ.
βͺ/unban: π³π πππ»πΊπ πΊ πππΎπ ππ πππΎ πππππ.
βͺ/tban: π³π ππΎπππππΊππππ π»πΊπ πΊ πππΎπ.
βͺ/mute: π³π ππππΎ πΊ πππΎπ ππ πππΎ πππππ.
βͺ/unmute: π³π ππππππΎ πΊ πππΎπ ππ πππΎ πππππ.
βͺ/tmute: π³π ππΎπππππΊππππ ππππΎ πΊ πππΎπ.

β€ π­πππΎ:
πΆππππΎ πππππ /tmute ππ /tban πππ ππππππ½ πππΎπΌππΏπ πππΎ ππππΎ πππππ.

βπ€ππΊππππΎ: /ππ»πΊπ 2π½ ππ /πππππΎ 2π½.
πΈππ πΌπΊπ πππΎ ππΊπππΎπ: π/π/π½. 
 β’ π = ππππππΎπ
 β’ π = πππππ
 β’ π½ = π½πΊππ"""
    CREATOR_REQUIRED = """β<b>You have To Be The Group Creator To Do That.</b>"""
      
    INPUT_REQUIRED = "β **Arguments Required**"
      
    KICKED = """βοΈ Successfully Kicked {} Members According To The Arguments Provided."""
      
    START_KICK = """π? Removing Inactive Members This May Take A While..."""
      
    ADMIN_REQUIRED = """β<b>ΰ΄ΰ΄¨ΰ΅ΰ΄¨ΰ΅ Admin ΰ΄ΰ΄ΰ΅ΰ΄ΰ΄€ΰ΅ΰ΄€ ΰ΄Έΰ΅ΰ΄₯ΰ΄²ΰ΄€ΰ΅ΰ΄€ΰ΅ ΰ΄ΰ΄Ύΰ΅» ΰ΄¨ΰ΄Ώΰ΄ΰ΅ΰ΄ΰ΄Ώΰ΄²ΰ΅ΰ΄² ΰ΄ͺΰ΅ΰ΄ΰ΅ΰ΄΅ΰ΄Ύ Bii..Add Me Again with all admin rights.</b>"""
      
    DKICK = """βοΈ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """<b>ΰ΄ΰ΄ͺΰ΅ΰ΄ͺΰ΅ ΰ΄ΰ΄²ΰ΅ΰ΄²ΰ΄Ύΰ΄ ΰ΄ΰ΄ΰ΄Ώΰ΄ΰ΅ΰ΄ΰ΅ΰ΄?ΰ΄Ύΰ΄±ΰ΅ΰ΄±ΰ΄Ώ ΰ΄€ΰ΄°ΰ΄Ύΰ΄...</b>"""
      
    STATUS = """{}\n<b>Chat Member Status</b>**\n\n```<i>Recently``` - {}\n```Within Week``` - {}\n```Within Month``` - {}\n```Long Time Ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}</i>
"""
