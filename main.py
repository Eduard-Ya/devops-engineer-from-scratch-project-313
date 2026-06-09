import os
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from flask import Flask


sentry_dsn = os.getenv("SENTRY_DSN")
if sentry_dsn:
    sentry_sdk.init(
        dsn=sentry_dsn,
        integrations=[FlaskIntegration()],
        traces_sample_rate=1.0,
        environment=os.getenv("ENVIRONMENT", "production")
    )

app = Flask(__name__)


@app.route('/ping')
def ping():
    return 'pong'


@app.route('/')
def root():
    return {"message": "Hello, World!"}


if __name__ == '__main__':
    port = int(os.getenv("PORT", 8080))
    app.run(host='0.0.0.0', port=port)