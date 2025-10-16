FROM python:3.12-slim

WORKDIR /telegram_bot

ENV SECRET_KEY='fdsafsad31251436'

RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


COPY  requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /telegram_bot/media

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

CMD ["sh", "-c", "python manage.py collectstatic --noinput && gunicorn config.wsgi:application --bind 0.0.0.0:8000"]
