# ---- Base ----
FROM python AS base
COPY bot.py /GPT3Pitt/bot.py
COPY ai.py /GPT3Pitt/ai.py
WORKDIR /GPT3Pitt

# ---- Dependencies ----
FROM base as dependencies
COPY requirements.txt /GPT3Pitt/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# ---- Release ----
FROM dependencies AS release
CMD [ "python", "bot.py" ]
