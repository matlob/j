import requests,telebot
bot = telebot.TeleBot("5268584144:AAFDsaJ5UDS8EVkSGfPizGNSICqastE7578")
import secrets
@bot.message_handler(commands=["start"])
def mes(message):
	 bot.send_message(message.chat.id,' Hello , Send User Instagram To Get Informaiton -@F_7_U .')
@bot.message_handler(func=lambda m: True)
def inf(message):
	head = {
	'HOST': "www.instagram.com",
	'KeepAlive' : 'True',
	'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
	'Cookie': 'cookie',
	'Accept' : "*/*",
	'ContentType' : "application/x-www-form-urlencoded",
	"X-Requested-With" : "XMLHttpRequest",
	"X-IG-App-ID": "936619743392459",
	"X-Instagram-AJAX" : "missing",
	"X-CSRFToken" : "missing",
	"Accept-Language" : "en-US,en;q=0.9"
	}
	cookie = secrets.token_hex(8)*2
	r = requests.session()
	target   = message.text
	url_id   = f'https://www.instagram.com/{target}/?__a=1'
	req_id   = r.get(url_id,headers=head).json()
	bio    = str(req_id['graphql']['user']['biography'])
	url   = str(req_id['graphql']['user']['external_url'])
	nam   = str(req_id['graphql']['user']['full_name'])
	idd   = str(req_id['graphql']['user']['id'])
	isp   = str(req_id['graphql']['user']['is_private'])
	isv   = str(req_id['graphql']['user']['is_verified'])
	pro   = str(req_id['graphql']['user']['profile_pic_url'])
	followers   = str(req_id['graphql']['user']['edge_followed_by']['count'])
	following   = str(req_id['graphql']['user']['edge_follow']['count'])	
	fol = (f"""š£šš¢š šŖšØšš§ : {nam}\n
	
	šš¤š”š”š¤š¬šš§šØ : {followers}

\nšš¤š”š”š¤š¬šš£š : {following}

\nšŖšØšš§šš : {idd}

\nššššššš : {isp}

\nššššššššæ : {isv}

\nš½šš : {bio}

\nššš : https://www.instagram.com/{target}""")
	bot.send_photo(message.chat.id,pro,fol)
bot.polling(True)