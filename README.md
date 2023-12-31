# developer-badge-app
## an easy way to get the active developer badge on Discord
![badge](https://github.com/0dm/developer-badge-app/assets/57018940/bc64bda9-749b-466d-81f0-95732aef3aa3)


if you do not have an application already, create one at https://discord.com/developers/applications and invite the bot to your server by going to oauth2->url generator and selecting the scope "bot". 

see [here](https://support-dev.discord.com/hc/en-us/articles/10113997751447-Active-Developer-Badge) for an actual explanation.

## usage
1. go [here](https://0dm-developer-badge-app-main-bfopwq.streamlit.app) (Streamlit)
2. enter your bot's token
3. click run
4. send `/ping` to the bot
5. claim your badge [here](https://discord.com/developers/active-developer) (could take 24 hours)

### self-hosting instructions
`poetry install`

`poetry shell`

`streamlit run main.py`

### the badge
read more here: https://support-dev.discord.com/hc/en-us/articles/10113997751447-Active-Developer-Badge
