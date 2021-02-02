import discord
import regex
import keys.privatekey as ps
import random


class FishBot(discord.Client):
    # einloggen
    async def on_ready(self):
        print("ready")

    # bei Nachricht
    async def on_message(self, message):
        if message.author == client.user:
            return

        pattern = """.*[Ii]['`´"]?[Mm] ([^,\.\n\r]+)"""
        match = regex.match(pattern, message.content)

        greetings = ["Hi, ", "Hey, ", "Howdy, "]

        if match:
            await message.channel.send(random.choice(greetings) +
                                       match[1] + ", I'm dad.")


if __name__ == "__main__":
    client = FishBot()
    client.run(ps.privatekey())
