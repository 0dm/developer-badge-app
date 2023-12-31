import streamlit as st
import discord
import asyncio

st.title("Discord Bot Runner")
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

    try:
        bot.run(token)
    except Exception as e:
        bot_status.error(f"Bot has encountered an error: {e}")
    finally:
        bot_status.success("The bot has run successfully!")


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
