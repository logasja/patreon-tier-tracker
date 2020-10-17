import json
from requests_html import HTMLSession
from requests import post
import asyncio

with open('config.json') as config_file:
  config = json.load(config_file)


def getRemainingSlots():
  session = HTMLSession()

  url = "https://www.patreon.com/{0}".format(config['account'])

  resp = session.get(url)

  alljson = resp.html.search('Object.assign(window.patreon.bootstrap, {});')

  datajson = json.loads(alljson[0])["campaign"]["included"]

  datajson = list(filter(lambda x: True if ('title' in x['attributes']) and (config['tier'] in x['attributes']['title']) else False, datajson))

  if (datajson):
    return datajson[0]['attributes']['remaining']
  else:
    raise Exception("Could not find a teir by that name")

def notify(message):
  report = {}
  report['value1'] = message
  post("https://maker.ifttt.com/trigger/{0}/with/key/{1}".format(config['ifttt_event'], config['ifttt_key']), data=report)

async def worker():
  while True:
    slots = getRemainingSlots()

    if slots > 0:
      notify("{0} has {1} slot(s) available in the {2} tier!".format(config['account'], slots, config['tier']))

    # Waits ten minutes before re-running
    await asyncio.sleep(60 * 10)

if __name__ == "__main__":
  notify("The loop is starting!")
  loop = asyncio.get_event_loop()
  try:
    asyncio.ensure_future(worker())
    loop.run_forever()
  except KeyboardInterrupt:
    pass
  finally:
    print("Closing")
    notify("The loop has stopped!")
    loop.close()