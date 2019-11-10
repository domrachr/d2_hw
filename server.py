import os
import random
import sentry_sdk

from bottle import route, run
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://7edb02abd5754148861f5dbd5bcf7486@sentry.io/1814797",
    integrations=[BottleIntegration()]
)

# app = Bottle()

@route('/')
def index():
    html = """
<!doctype html>
<html lang="en">
  <head>
    <title>Интеграция с Sentry</title>
  </head>
  <body>
    <h1>SUCCESS</h1>
  </body>
</html>
"""
    return html

@route('/success')
def success():
    html = """
<!doctype html>
<html lang="en">
  <head>
    <title>Интеграция с Sentry</title>
  </head>
  <body>
    <h1>SUCCESS</h1>
  </body>
</html>
"""
    return html


@route('/fail')
def fail():
    raise RuntimeError("FAIL")
    return


if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)
