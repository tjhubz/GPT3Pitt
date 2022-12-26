# ---- Base ----
FROM python:slim AS base
COPY bot.py /GPT3Pitt/bot.py
COPY config.json /GPT3Pitt/config.json
WORKDIR /GPT3Pitt

# ---- Dependencies ----
FROM base as dependencies
COPY requirements.txt /GPT3Pitt/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# ---- Release ----
FROM dependencies AS release
CMD [ "python", "bot.py" ]
