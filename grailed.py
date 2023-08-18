import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
import json
import os

config = { "DiscordWebHook" : "", "Brand" : []}

def SendWebHook(title, url, price, currency, size, brand, photo, WHook):
    webhook = DiscordWebhook(rate_limit_retry=True, url=WHook)
    embed = DiscordEmbed(title= 'New Product Found!', description= "**[" + title + ']' + "(" + url + ")**", color='0db7d8')  # Colore in formato esadecimale
    embed.add_embed_field(name='Prezzo:', value= price + ' ' + currency, inline=True)
    embed.add_embed_field(name='Taglia:', value= size, inline=True)
    embed.add_embed_field(name='Brand:', value= brand, inline=True)
    embed.set_thumbnail(url=photo)
    webhook.add_embed(embed)
    response = webhook.execute()

def CheckConfig(fname, defdata):
    if os.path.exists(fname) and os.path.getsize(fname) > 0:
        with open(fname, "r") as file:
            data = json.load(file)
        if data['DiscordWebHook'] == "" or data['Brand'] == []: 
            data = defdata
            with open(fname, "w") as file:
                json.dump(data, file, indent=4) 
                input('Please fill the Config.json file!')
                exit()
    else:
        data = defdata
        with open(fname, "w") as file:
            json.dump(data, file, indent=4) 
            input('Please fill the Config.json file!')
            exit()
    return data

def CheckList():
    data = { "ids" : []}
    if os.path.exists('List.json'):
        with open('List.json', "r") as file:
            data = json.load(file)
    else:
        with open('List.json', "w") as file:
            json.dump(data, file, indent=4) 
    return data

if __name__ == "__main__":

    config = CheckConfig("Config.json", config)

            
    while True:
        headers = {
            'Accept': '/',
            'Accept-Language': 'it-IT,it;q=0.9',
            'x-emb-st': '1692363393696',
            'X-Algolia-Application-Id': 'MNRWEFSS2Q',
            'User-Agent': 'iOS (16.5.1); Algolia for Swift (8.13.3)',
            'X-Algolia-API-Key': 'bc9ee1c014521ccf312525a4ef324a16',
            'Connection': 'keep-alive',
            'x-emb-id': 'E3E9A27141D1465B886AA188A6C3A506',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        for brand in config['Brand']:
            
            data = '{"analytics":true,"enableABTest":true,"filters":"(strata:grailed OR strata:hype OR strata:basic OR strata:sartorial) AND price_i>=0 AND (marketplace: grailed)","personalizationImpact":99,"query":"' + brand + '","hitsPerPage":200,"enablePersonalization":true,"clickAnalytics":true,"userToken":"1381231","page":0,"getRankingInfo":true}'
            response = eval((requests.post('https://mnrwefss2q-dsn.algolia.net/1/indexes/Listing_production/query', headers=headers, data=data).text).replace('true', 'True').replace('false', 'False').replace('null', 'None'))['hits']
            response = { x : x for x in response if x['id'] not in CheckList()['ids']} 
            for item in response:
                with open('List.json', "w") as file:
                    data = json.load(file)
                    data['ids'].append(item['id'])
                    json.dump(data, file, indent=4)
                product_url = 'https://www.grailed.com/' + (requests.get('https://www.grailed.com/api/listings/' + str(item['id']), headers=headers).json()['data']['pretty_path'])
                SendWebHook(item['title'], product_url, str(item['price']), item['currency'], item['size'], item['designer_names'], item['retina_cover_photo']['url'], config['DiscordWebHook'])
