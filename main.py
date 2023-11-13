import disnake

from disnake.ext import commands

bot = commands.Bot(command_prefix="*", intents=disnake.Intents.all())


@bot.slash_command()
async def test(interaction: disnake.AppCmdInter):
    await interaction.send("go B")

bot.run("MTA4MzgwMDE5NTc1OTg3ODE2NA.GSkFRV.pvZj3POAeG42BgWu1RcMTYnH2btP0SO6KXlhf0")