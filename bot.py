import os
import discord
import discord.ext
import ai

# ------------------------------- INITIALIZATION -------------------------------
bot = discord.Bot(intents=discord.Intents.all())
TOKEN = os.getenv("DISCORD_TOKEN")
warning = "\n\n*NOTICE: I am an AI that is currently being trained. My goal is to provide answers to questions, but please note that they may be incorrect. Please rate this answer with either a thumbs up or down.*"
emojis = ['\N{THUMBS UP SIGN}','\N{THUMBS DOWN SIGN}'] # Reactions to add to ai-generated messages
# ------------------------------------------------------------------------------

# Bot start
@bot.event
async def on_ready():
    print("Bot has started successfully.")
    
# Responds to new forum posts with an answer
@bot.event
async def on_thread_create(thread):
    if thread.parent.name == "questions":
        print("[LOG] New thread detected")
        await thread.join()
        question = thread.starting_message.channel.name
        answer = ai.ask(question)
        message = await thread.send(answer+warning)
        for emoji in emojis:
            await message.add_reaction(emoji)
            

bot.run(TOKEN)