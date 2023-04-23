import __main__
import os
from os import path
import json
import platform


class Pytimelinejs:

    def __init__(self):
        self.title = ""
        self.subtitle = ""
        self.mediatitre = ""
        self.events = []



    def _parse_date(self, date):
        date = str(date).split("/")
        if len(date) == 1:
            return {"year": date[0]}
        elif len(date) == 2:
            return {"month": date[0], "year": date[1]}
        elif len(date) == 3:
            return {"day": date[0], "month": date[1], "year": date[2]}
        else:
            raise ValueError("Date invalide")

    def titre(self, titre, sous_titre="", media_titre=""):
        self.title = titre
        self.subtitle = sous_titre
        self.mediatitre = media_titre

    def date(self, date, titre, description="", media_url=""):
        self.events.append({
            "start_date": self._parse_date(date),
            "text": {
                "headline": titre,
                "text": description
            },
            "media":{
                "url": media_url
            }
        })

    def periode(self, date_debut, date_fin, titre, description="", media_url=""):
        self.events.append({
            "start_date": self._parse_date(date_debut),
            "end_date": self._parse_date(date_fin),
            "text": {
                "headline": titre,
                "text": description
            },
            "media": {
                "url": media_url
            }
        })

    def generer(self):
        JSON = {
            "title": {
                "text": {
                    "headline": self.title,
                    "text": self.subtitle
                },
                "media": {
                    "url": self.mediatitre
                }
            },
            "events": self.events
        }
        OPTIONS = {
            "scale_factor": 1,
            "language": "fr"
        }
        output = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{TITLE}</title>
    <link title="timeline-styles" rel="stylesheet" href="https://cdn.knightlab.com/libs/timeline3/latest/css/timeline.css">
    <script src="https://cdn.knightlab.com/libs/timeline3/latest/js/timeline.js"></script>
</head>
<body>
    <div id='timeline-embed' style="width: 100%; height: 600px"></div>
    <script type="text/javascript">
        timeline = new TL.Timeline('timeline-embed', {JSON}, {OPTIONS});
    </script>
</body>
</html>""".format(TITLE=self.title, JSON=json.dumps(JSON, indent=4), OPTIONS=json.dumps(OPTIONS, indent=4))
        filename = path.splitext(path.basename(__main__.__file__))[0] + ".html"
        with open(filename, "w") as file:
            file.write(output)
        # could be "linux", "linux2", "linux3", ...
        if platform.system() ==  "linux":
         # linux
         os.system('xdg-open ' + filename)
        elif platform.system() == "Darwin":
            # MAC OS X
            os.system('open ' + path.abspath(filename))
        elif os.name == "nt":
            # Windows, Cygwin, etc. (either 32-bit or 64-bit)
            os.system('xdg-open ' + filename) 
        
                

pytimelinejs = Pytimelinejs()

for f in [f for f in dir(Pytimelinejs) if not f.startswith('_')]:
    globals()[f] = getattr(pytimelinejs, f)
