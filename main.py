import streamlit as st
import discord
import asyncio

st.title("developer-badge-app")
token = st.text_input("Enter your bot token")

bot_status = st.empty()  # Placeholder for bot status message


def run_bot(token):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    bot = discord.Bot()

    @bot.slash_command()
    async def ping(ctx):
        embed = discord.Embed(description=(f"Pong!"), colour=discord.Colour.purple())
        await ctx.respond(embed=embed)
        await bot.close()
        loop.stop()

    @bot.event
    async def on_ready():
        bot_status.info(f"Logged in as {bot.user.name}#{bot.user.discriminator}")
        await bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching, name="for /ping"
            )
        )

    try:
        bot.run(token)
    except Exception as e:
        bot_status.error(f"Bot has encountered an error: {e}")
    finally:
        bot_status.success("The bot has run successfully!")
        st.write(
            "You can claim your active developer badge [here](https://discord.com/developers/active-developer)"
        )


def disable():
    st.session_state.disabled = True


if "disabled" not in st.session_state:
    st.session_state.disabled = False

if st.button("Run Bot", on_click=disable, disabled=st.session_state.disabled):
    if token:
        bot_status.warning("Bot is running...")
        run_bot(token)
    else:
        st.error("Please enter a bot token")
