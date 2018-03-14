import json
import requests

url = 'https://lwcal.scu.edu/live/calendar/view/week/date/20170610?user_tz=America%2FDetroit&syntax=%3Cwidget%20type%3D%22events_calendar%22%3E%3Carg%20id%3D%22modular%22%3Etrue%3C%2Farg%3E%3Carg%20id%3D%22hide_repeats%22%3Etrue%3C%2Farg%3E%3Carg%20id%3D%22exclude_tag%22%3Eprivate%3C%2Farg%3E%3Carg%20id%3D%22mini_cal_heat_map%22%3Etrue%3C%2Farg%3E%3Carg%20id%3D%22thumb_width%22%3E200%3C%2Farg%3E%3Carg%20id%3D%22thumb_height%22%3E200%3C%2Farg%3E%3C%2Fwidget%3E'

response = requests.get(url)
data = json.loads(response.content)

print data

print data["events"].keys()
# Data: [u'20170610', u'20170604', u'20170605', u'20170606', u'20170607', u'20170608', u'20170609']
# There are 7 dates data that you can get from the json like shown above.

# for example you can print titles like follows (by parsing the json)
for i in data["events"].keys():
    print data["events"][i][0]['title']