# Project-Sacred

# 🕹️ Discord Ticket & Community Bot

A **Python Discord Bot** for managing **support tickets, shop systems, applications, crates, and server moderation** for your Minecraft community server.  

Fully customizable and easy to set up for your server’s roles, channels, and ticket system.


---

## Features

### 🎫 Ticket System
- Create support, shop, application, or moderation tickets via **buttons**  
- Staff can **claim** and **close** tickets  
- **Customizable ticket content** messages and categories  

### 🛒 Shop & Crates
- Users can browse **crates** with previews  
- Purchase items, ranks, upgrades, or claim event rewards  
- Fully configurable pricing and crate content  

### 📜 Applications
- Staff position applications with predefined roles (Builder, Dev, Helper, Streamer, Media)  
- Tickets created for each application  

### ⚖️ Moderation
- Staff-only moderation tickets: warnings, temp/permanent bans, promotions, demotions  
- Logs moderation actions in a dedicated category  

### 🎮 Server Setup
- Commands to **automatically create roles and channels** for:
  - Gaming servers
  - Minecraft SMP servers  
- Predefined roles, categories, and channels for quick setup  

### 🚀 Boost Notifications
- Automatically announces server boosts in a designated channel  

### 🔧 Keep Alive
- Built-in Flask server to keep the bot alive when hosted on platforms like **Replit** or **Render**  

---

## Setup

### 1. Clone or import repository
```bash
git clone https://github.com/yourusername/the-alley-bot.git
cd the-alley-bot

```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure the bot

Edit the configuration variables directly in the code:
```bash
DISCORD_TOKEN = "your-bot-token"               # Your Discord bot token
GUILD_ID = 123456789012345678                  # Your server ID
STAFF_ROLE_ID = 123456789012345678             # Staff role for tickets
TICKET_CATEGORY_ID = 123456789012345678        # Support ticket category
MODERATION_CATEGORY_ID = 123456789012345678    # Moderation ticket category
BOOST_CHANNEL_ID = 123456789012345678          # Boost announcement channel
```

You can also customize ticket messages, crate content, shop buttons, and application roles directly in the Python code.

Note: .env is optional if your hosting provider supports secret environment variables (Replit, Render, etc.).

4. Run the bot
python main.py


Flask server runs on port 8080 to keep the bot alive on hosted platforms.
```
Commands & Panels
Command	Description
/support	Show the support ticket panel
/shop	Show the shop & crates panel
/apply	Show the staff application panel
/mod	Show the moderation panel
/crates	View all crates available for purchase
/setup	Automatically set up a gaming server (Admin only)
/smp-setup	Automatically set up a Minecraft SMP server (Admin only)
```
Deployment
🔹 Hosting on Replit

Add DISCORD_TOKEN in the Secrets/Environment variables section

Click Run to start the bot

🔹 Hosting on Render

Create a Web Service with python main.py as the start command

The bot listens on port 8080 (Flask handles keep-alive)

Add DISCORD_TOKEN and any other secrets in the Environment section

🔹 Optional Keep Alive with GitHub Actions
```
# .github/workflows/keep_alive.yml
name: Keep Bot Alive
on:
  schedule:
    - cron: "*/13 * * * *"
  workflow_dispatch:

jobs:
  ping:
    runs-on: ubuntu-latest
    steps:
      - name: Ping bot URL
        run: curl https://your-bot-url.com


Replace the URL with your public bot URL. No hardcoding in the repo is needed.
```
Customization

Ticket Messages: Edit SupportView, TicketManageView, and interaction handlers

Crates & Shop: Modify the CRATES dictionary and CrateButtons

Applications: Add/remove roles in ApplicationView and /apply command

Moderation: Add/remove actions in ModerationView

Contributing

Pull requests and suggestions are welcome!

Please follow code formatting and include comments for any new features.
