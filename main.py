# ==============================
# KEEP ALIVE WEB SERVER
# ==============================
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# ==============================
# DISCORD BOT IMPORTS & SETUP
# ==============================
import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import Button, View

intents = discord.Intents.default()
intents.guilds = True
intents.members = True  # 👈 Required for detecting boosts

bot = commands.Bot(command_prefix="!", intents=intents)

# ==============================
# BOT EVENTS (Login & Command Sync)
# ==============================
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

    GUILD_ID = 1384943751608275106  

    try:
        guild = discord.Object(id=GUILD_ID)
        bot.tree.copy_global_to(guild=guild)
        await bot.tree.sync(guild=guild)

        print(f"🌐 Synced commands to guild {GUILD_ID}")
    except Exception as e:
        print(f"❌ Error syncing commands: {e}")



# ==============================
# 🎮 GAMING COMMUNITY SERVER SETUP
# Creates roles and channels for gaming servers
# ==============================
@bot.tree.command(name="setup", description="Set up a gaming community server with roles and channels")
@app_commands.checks.has_permissions(administrator=True)
async def setup(interaction: discord.Interaction):
    guild = interaction.guild
    await interaction.response.send_message("🎮 Setting up your gaming community server...", ephemeral=True)

    # === Create Roles ===
    await guild.create_role(
        name="👑 Admin",
        permissions=discord.Permissions(administrator=True),
        colour=discord.Colour.red()
    )

    mod_perms = discord.Permissions()
    mod_perms.update(
        manage_messages=True,
        kick_members=True,
        mute_members=True,
        view_audit_log=True,
        manage_roles=True
    )
    await guild.create_role(
        name="🛡️ Moderator",
        permissions=mod_perms,
        colour=discord.Colour.orange()
    )

    await guild.create_role(name="🎮 Gamer", colour=discord.Colour.green())
    await guild.create_role(name="👶 Newbie", colour=discord.Colour.light_grey())

    # === Create Categories and Channels ===
    cat_info = await guild.create_category("📘 Info & Rules")
    cat_general = await guild.create_category("💬 Community")
    cat_games = await guild.create_category("🎮 Game Chat")
    cat_voice = await guild.create_category("🔊 Voice Channels")

    await guild.create_text_channel("📢│announcements", category=cat_info)
    await guild.create_text_channel("📜│rules", category=cat_info)

    await guild.create_text_channel("💬│general-chat", category=cat_general)
    await guild.create_text_channel("📸│media-sharing", category=cat_general)
    await guild.create_text_channel("🤖│bot-commands", category=cat_general)

    await guild.create_text_channel("🎮│game-chat", category=cat_games)
    await guild.create_text_channel("🕹️│lfg", category=cat_games)
    await guild.create_text_channel("🏆│highlights", category=cat_games)

    await guild.create_text_channel("🎮│Minecraft", category=cat_games)
    await guild.create_text_channel("🕹️│League of Legend", category=cat_games)
    await guild.create_text_channel("🏆│Valorant", category=cat_games)

    await guild.create_voice_channel("🔊│General VC", category=cat_voice)
    await guild.create_voice_channel("🎮│In Game", category=cat_voice)
    await guild.create_voice_channel("🎙️│Streamer Room", category=cat_voice)

    await interaction.followup.send("✅ Server setup complete with roles and gaming channels!")


# ==============================
# ⛏️ MINECRAFT SMP SERVER SETUP  
# Creates Minecraft-specific roles and channels
# ==============================
@bot.tree.command(name="smp-setup", description="Set up a Minecraft SMP server with roles and channels")
@app_commands.checks.has_permissions(administrator=True)
async def smp_setup(interaction: discord.Interaction):
    guild = interaction.guild
    await interaction.response.send_message("⛏️ Setting up your Minecraft SMP server...", ephemeral=True)

    # === Create Roles ===
    await guild.create_role(
        name="👑 Admin",
        permissions=discord.Permissions(administrator=True),
        colour=discord.Colour.red()
    )

    mod_perms = discord.Permissions()
    mod_perms.update(
        manage_messages=True,
        kick_members=True,
        mute_members=True,
        view_audit_log=True,
        manage_roles=True
    )
    await guild.create_role(
        name="🛡️ Moderator",
        permissions=mod_perms,
        colour=discord.Colour.orange()
    )

    await guild.create_role(name="🌍 Member", colour=discord.Colour.green())
    await guild.create_role(name="👶 Newbie", colour=discord.Colour.light_grey())

    # === Create Categories and Channels ===
    cat_info = await guild.create_category("📘 Server Info")
    cat_general = await guild.create_category("💬 Community")
    cat_minecraft = await guild.create_category("⛏️ Minecraft SMP")
    cat_voice = await guild.create_category("🔊 Voice Channels")

    await guild.create_text_channel("📢│announcements", category=cat_info)
    await guild.create_text_channel("📜│rules", category=cat_info)
    await guild.create_text_channel("📝│whitelist-apply", category=cat_info)

    await guild.create_text_channel("💬│general-chat", category=cat_general)
    await guild.create_text_channel("📸│screenshots", category=cat_general)
    await guild.create_text_channel("🤖│bot-commands", category=cat_general)

    await guild.create_text_channel("🗺️│server-map", category=cat_minecraft)
    await guild.create_text_channel("💰│trading-post", category=cat_minecraft)
    await guild.create_text_channel("🏠│land-claims", category=cat_minecraft)
    await guild.create_text_channel("⚔️│pvp-discussion", category=cat_minecraft)
    await guild.create_text_channel("🐉│end-raids", category=cat_minecraft)

    await guild.create_voice_channel("🔊│General VC", category=cat_voice)
    await guild.create_voice_channel("🎮│Mining Party", category=cat_voice)
    await guild.create_voice_channel("⚔️│Boss Fight", category=cat_voice)
    await guild.create_voice_channel("🎙️│Streamer Room", category=cat_voice)

    await interaction.followup.send("✅ Minecraft SMP server setup complete with roles and channels!")


# ==============================
# 🎫 TICKET SYSTEM CONFIGURATION
# Button views and role/category IDs for support
# ==============================
STAFF_ROLE_ID = 1412474000965111888  # 👈 replace with your Staff role ID
TICKET_CATEGORY_ID = 987654321098765432  # 👈 replace with your Tickets category ID
MODERATION_CATEGORY_ID = 1428793663529423051  # 👈 Moderation tickets category
INQUIRY_ROLE_1 = 1431996923493224480  # 👈 Additional role for inquiry tickets
INQUIRY_ROLE_2 = 1412007276805619794  # 👈 Additional role for inquiry tickets

# ==============================
# 📦 CRATES SYSTEM DATA
# Crate information and pricing
# ==============================
CRATES = {
    "ember": {
        "title": "EMBER CRATE - ₱10.00",
        "image": "https://your-image-link.com/cutiecat.png",
        "description": "A cute and stylish weapon/armor pack!"
    },
    "glimmer": {
        "title": "GLIMMER CRATE - ₱20.00",
        "image": "https://your-image-link.com/starlight.png",
        "description": "Shine bright with the Starlight set!"
    },
    "lumen": {
        "title": "LUMEN CRATE - ₱30.00",
        "image": "https://your-image-link.com/glow.png",
        "description": "Glowing with power and style!",
    },
    "astral": {
        "title": "ASTRAL CRATE - ₱40.00",
        "image": "https://your-image-link.com/astral.png",
        "description": "A mystical set for the magical player!",
    },
    "eclipse": {
        "title": "ECLIPSE CRATE - ₱50.00",
        "image": "https://your-image-link.com/eclipse.png",
        "description": "Dark and mysterious, perfect for the stealthy player!",
    },
    # Add more crates here
}

# Support ticket buttons (inquiries, reports, etc.)

class SupportView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Button(label="🔮 Ask Us", style=discord.ButtonStyle.success, custom_id="ticket_inquiries"))
        self.add_item(Button(label="⚔️ Player Report", style=discord.ButtonStyle.danger, custom_id="ticket_report"))
        self.add_item(Button(label="🪄 Lost Items", style=discord.ButtonStyle.secondary, custom_id="ticket_items"))
        self.add_item(Button(label="🎭 Event Claim", style=discord.ButtonStyle.primary, custom_id="ticket_events"))

# Ticket management buttons (claim/close) shown in each ticket
class TicketManageView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Button(label="🎫 Claim", style=discord.ButtonStyle.success, custom_id="claim_ticket"))
        self.add_item(Button(label="🔒 Close", style=discord.ButtonStyle.danger, custom_id="close_ticket"))

# Crate selection buttons
class CrateButtons(View):
    def __init__(self):
        super().__init__(timeout=None)  # persistent view

        # Add buttons dynamically from CRATES
        for crate_id, crate in CRATES.items():
            self.add_item(
                Button(
                    label=crate["title"].split(" - ")[0],  # show name only
                    style=discord.ButtonStyle.secondary,
                    custom_id=crate_id
                )
            )

# ==============================
# 🎫 SUPPORT COMMAND
# Shows the main support panel with ticket options
# ==============================
@bot.tree.command(name="support", description="Show The Alley Support Panel")
async def support(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🌙 WELCOME TO THE ALLEY SUPPORT",
        description=(
            "Step into the shadows of **Knockturn Alley**... 🕯️\n\n"
            "Choose a panel below to open a **ticket**. Our staff will assist you shortly.\n\n"
            "» **Event Claim** – Claim your prize\n"
            "» **Ask Us** – General questions about *The Alley SMP*\n"
            "» **Player Reports** – Report players, duels, or suspicious activities\n"
            "» **Lost Items** – Recover vanished or broken items\n"
            "*The Alley Management* 🕯️"
        ),
        color=0x8e44ad
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1409513135966257222/1411000212964638780/8acff8e587df623ec95f8313f9a88ae9.gif?ex=68b30fd9&is=68b1be59&hm=37d965e0e68b9c016ebb4f58bc42abcac9a1a779ad7610ba6e2630200a7e26cb&")

    await interaction.response.send_message(embed=embed, view=SupportView())

# ==============================
# 🔧 MAIN INTERACTION HANDLER
# Handles all button clicks (tickets, shop, applications)
# ==============================
@bot.event
async def on_interaction(interaction: discord.Interaction):
    if interaction.type == discord.InteractionType.component:
        cid = interaction.data["custom_id"]
        guild = interaction.guild
        category = discord.utils.get(guild.categories, id=1410682286273335480)

        # ===== SUPPORT TICKET CREATION =====
        if cid.startswith("ticket_"):
            # Check if user already has a ticket
            for channel in category.channels:
                if channel.name.endswith(str(interaction.user.id)):
                    await interaction.response.send_message(
                        "❗ You already have an open ticket!", ephemeral=True
                    )
                    return

            # Set up base overwrites
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(view_channel=False),
                interaction.user: discord.PermissionOverwrite(view_channel=True, send_messages=True),
                guild.get_role(STAFF_ROLE_ID): discord.PermissionOverwrite(view_channel=True, send_messages=True)
            }

            # Add extra roles for inquiry tickets
            if cid == "ticket_inquiries":
                inquiry_role_1 = guild.get_role(INQUIRY_ROLE_1)
                inquiry_role_2 = guild.get_role(INQUIRY_ROLE_2)
                if inquiry_role_1:
                    overwrites[inquiry_role_1] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
                if inquiry_role_2:
                    overwrites[inquiry_role_2] = discord.PermissionOverwrite(view_channel=True, send_messages=True)

            # Create ticket channel
            ticket_channel = await guild.create_text_channel(
                name=f"{cid}-{interaction.user.id}",
                category=category,
                overwrites=overwrites
            )

            await ticket_channel.send(
                f"👋 Welcome {interaction.user.mention}!\n"
                f"Please describe your issue. Our staff will assist you shortly.\n\n"
                f"**Ticket Type:** `{cid.replace('ticket_', '').capitalize()}`",
                view=TicketManageView()
            )

            await interaction.response.send_message(
                f"✅ Ticket created: {ticket_channel.mention}", ephemeral=True
            )

        # ===== SHOP TICKET CREATION =====
        elif cid.startswith("shop_"):
            # Check if user already has a shop ticket
            for channel in category.channels:
                if channel.name.startswith("shop_") and channel.name.endswith(str(interaction.user.id)):
                    await interaction.response.send_message(
                        "❗ You already have an open shop ticket!", ephemeral=True
                    )
                    return

            # Create shop ticket channel
            shop_channel = await guild.create_text_channel(
                name=f"{cid}-{interaction.user.id}",
                category=category,
                overwrites={
                    guild.default_role: discord.PermissionOverwrite(view_channel=False),
                    interaction.user: discord.PermissionOverwrite(view_channel=True, send_messages=True),
                    guild.get_role(STAFF_ROLE_ID): discord.PermissionOverwrite(view_channel=True, send_messages=True)
                }
            )

            shop_type = cid.replace('shop_', '').capitalize()
            await shop_channel.send(
                f"🛒 Welcome to The Alley Shop {interaction.user.mention}!\n"
                f"You've selected: **{shop_type}**\n\n"
                f"Please let our staff know what you'd like to purchase or claim.\n"
                f"Our team will process your request shortly! 🕯️",
                view=TicketManageView()
            )

            await interaction.response.send_message(
                f"✅ Shop ticket created: {shop_channel.mention}", ephemeral=True
            )

        # ===== APPLICATION TICKET CREATION =====
        elif cid.startswith("apply_"):
            # Check if user already has an application ticket
            for channel in category.channels:
                if channel.name.startswith("apply_") and channel.name.endswith(str(interaction.user.id)):
                    await interaction.response.send_message(
                        "❗ You already have an open application!", ephemeral=True
                    )
                    return

            # Create application ticket channel
            app_channel = await guild.create_text_channel(
                name=f"{cid}-{interaction.user.id}",
                category=category,
                overwrites={
                    guild.default_role: discord.PermissionOverwrite(view_channel=False),
                    interaction.user: discord.PermissionOverwrite(view_channel=True, send_messages=True),
                    guild.get_role(STAFF_ROLE_ID): discord.PermissionOverwrite(view_channel=True, send_messages=True)
                }
            )

            position = cid.replace('apply_', '').capitalize()
            await app_channel.send(
                f"📜 Welcome to The Alley Applications {interaction.user.mention}!\n"
                f"You're applying for: **{position}**\n\n"
                f"Please answer the following questions:\n"
                f"1. What's your age and timezone?\n"
                f"2. Why do you want to join The Alley staff team?\n"
                f"3. What experience do you have in this role?\n"
                f"4. How active can you be?\n\n"
                f"Our management team will review your application! 🕯️",
                view=TicketManageView()
            )

            await interaction.response.send_message(
                f"✅ Application submitted: {app_channel.mention}", ephemeral=True
            )

        # ===== TICKET CLAIM (Staff Only) =====
        elif cid == "claim_ticket":
            # Check if user has staff role
            staff_role = guild.get_role(STAFF_ROLE_ID)
            if staff_role not in interaction.user.roles:
                await interaction.response.send_message(
                    "❌ Only staff members can claim tickets!", ephemeral=True
                )
                return

            channel = interaction.channel
            # Check if already claimed
            if "claimed-by" in channel.name:
                await interaction.response.send_message(
                    "❌ This ticket has already been claimed!", ephemeral=True
                )
                return

            # Rename channel to show it's claimed
            new_name = f"{channel.name}-claimed-by-{interaction.user.display_name.lower()}"
            await channel.edit(name=new_name[:100])  # Discord channel name limit

            await interaction.response.send_message(
                f"🎫 **Ticket claimed by {interaction.user.mention}!**\n"
                f"This ticket is now being handled by staff."
            )

        # ===== TICKET CLOSE (Staff or Creator) =====
        elif cid == "close_ticket":
            # Check if user has staff role or is the ticket creator
            staff_role = guild.get_role(STAFF_ROLE_ID)
            channel_name = interaction.channel.name
            user_id = str(interaction.user.id)

            if staff_role not in interaction.user.roles and not channel_name.endswith(user_id):
                await interaction.response.send_message(
                    "❌ Only staff members or the ticket creator can close tickets!", ephemeral=True
                )
                return

            await interaction.response.send_message(
                f"🔒 **Ticket closed by {interaction.user.mention}**\n"
                f"This channel will be deleted in 5 seconds..."
            )

            # Wait 5 seconds then delete the channel
            import asyncio
            await asyncio.sleep(5)
            await interaction.channel.delete()

        # ===== CRATE SELECTION =====
        elif cid in CRATES:
            crate = CRATES[cid]

            embed = discord.Embed(
                title=crate["title"],
                description=crate["description"],
                color=discord.Color.pink()
            )
            embed.set_image(url=crate["image"])

            await interaction.response.send_message(embed=embed, ephemeral=True)

        # ===== MODERATION TICKET CREATION =====
        elif cid.startswith("mod_"):
            staff_role = guild.get_role(STAFF_ROLE_ID)
            if staff_role not in interaction.user.roles:
                await interaction.response.send_message(
                    "❌ Only staff members can create moderation tickets!", ephemeral=True
                )
                return

            mod_category = discord.utils.get(guild.categories, id=MODERATION_CATEGORY_ID)
            if mod_category is None:
                await interaction.response.send_message(
                    "❌ Moderation category not found! Please check the category ID.", ephemeral=True
                )
                return

            for channel in mod_category.channels:
                if channel.name.startswith("mod_") and channel.name.endswith(str(interaction.user.id)):
                    await interaction.response.send_message(
                        "❗ You already have an open moderation ticket!", ephemeral=True
                    )
                    return

            mod_channel = await guild.create_text_channel(
                name=f"{cid}-{interaction.user.id}",
                category=mod_category,
                overwrites={
                    guild.default_role: discord.PermissionOverwrite(view_channel=False),
                    interaction.user: discord.PermissionOverwrite(view_channel=True, send_messages=True),
                    guild.get_role(STAFF_ROLE_ID): discord.PermissionOverwrite(view_channel=True, send_messages=True)
                }
            )

            action_names = {
                "mod_warning": "⚠️ Warning",
                "mod_tempban": "⏱️ Temp Ban",
                "mod_permaban": "🔨 Perma Ban",
                "mod_promoted": "⬆️ Promoted",
                "mod_demoted": "⬇️ Demoted"
            }
            action_name = action_names.get(cid, "Moderation Action")

            mod_embed = discord.Embed(
                title=f"⚖️ {action_name} - Moderation Ticket",
                description=(
                    f"**Staff Member:** {interaction.user.mention}\n"
                    f"**Action Type:** {action_name}\n\n"
                    "Please provide the following information:\n"
                    "1. **Target Member:** Who is this action for?\n"
                    "2. **Reason:** Why is this action being taken?\n"
                    "3. **Evidence:** Any screenshots or proof (if applicable)\n"
                    "4. **Duration:** (For Temp Ban only)\n\n"
                    "*The Alley Management* 🕯️"
                ),
                color=0xe74c3c
            )
            mod_embed.set_footer(text="Staff Moderation Log | The Alley Management 🕯️")

            await mod_channel.send(embed=mod_embed, view=TicketManageView())
            await interaction.response.send_message(
                f"✅ Moderation ticket created: {mod_channel.mention}", ephemeral=True
            )

# ==============================
# 🛒 SHOP PANEL SYSTEM
# Handles shop-related purchases and claims
# ==============================
class ShopView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Button(label="🎉 Events", style=discord.ButtonStyle.primary, custom_id="shop_events"))
        self.add_item(Button(label="🚀 Booster Perks", style=discord.ButtonStyle.success, custom_id="shop_booster"))
        self.add_item(Button(label="🏆 Ranks", style=discord.ButtonStyle.secondary, custom_id="shop_ranks"))
        self.add_item(Button(label="⬆️ Upgrades", style=discord.ButtonStyle.danger, custom_id="shop_upgrades"))

# Shop command - displays purchase/claim options
@bot.tree.command(name="shop", description="Show The Alley Shop Panel")
async def shop(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🛒 THE ALLEY SHOP",
        description="Browse through The Alley Shop and claim your perks 🕯️\n\n"
                    "» **Events** – For Event Prizes or Giveaways\n"
                    "» **Booster Perks** – Claiming Booster Perks\n"
                    "» **Ranks** – For Buying Ranks w/ Perks\n"
                    "» **Upgrades** – For Rank Upgrades\n\n"
                    "*The Alley Management* 🕯️",
        color=0xf1c40f
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1409513135966257222/1411000212964638780/8acff8e587df623ec95f8313f9a88ae9.gif")
    embed.set_footer(text="The Alley Management 🕯️")

    await interaction.response.send_message(embed=embed, view=ShopView())

# ==============================
# 📜 APPLICATION PANEL SYSTEM  
# Handles staff position applications
# ==============================
class ApplicationView(View):
    def __init__(self):
        super().__init__(timeout=None)

        self.add_item(Button(label="🏗️ Builder", style=discord.ButtonStyle.success, custom_id="apply_builder"))
        self.add_item(Button(label="💻 Dev", style=discord.ButtonStyle.secondary, custom_id="apply_dev"))
        self.add_item(Button(label="🤝 Helper", style=discord.ButtonStyle.success, custom_id="apply_helper"))
        self.add_item(Button(label="🎥 Streamer", style=discord.ButtonStyle.secondary, custom_id="apply_streamer"))
        self.add_item(Button(label="📸 Media Team", style=discord.ButtonStyle.primary, custom_id="apply_media"))

# Application command - displays staff position options
@bot.tree.command(name="apply", description="Show The Alley Application Panel")
async def apply(interaction: discord.Interaction):
    embed = discord.Embed(
        title="📜 THE ALLEY APPLICATION",
        description="Interested in joining The Alley Staff Team? 🕯️\n\n"
                    "» **Builder** – Create maps & designs\n"
                    "» **Dev** – Assist with coding & bots\n"
                    "» **Helper** – Support the community\n"
                    "» **Streamer** – Promote The Alley live\n"
                    "» **Media Team** – Create content & graphics\n\n"
                    "*The Alley Management* 🕯️",
        color=0x2ecc71
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1409513135966257222/1411000212964638780/8acff8e587df623ec95f8313f9a88ae9.gif")
    embed.set_footer(text="The Alley Management 🕯️")

    await interaction.response.send_message(embed=embed, view=ApplicationView())

# ==============================
# ⚖️ MODERATION TICKET SYSTEM
# Handles staff moderation actions (warnings, bans, promotions)
# ==============================
class ModerationView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Button(label="⚠️ Warning", style=discord.ButtonStyle.secondary, custom_id="mod_warning"))
        self.add_item(Button(label="⏱️ Temp Ban", style=discord.ButtonStyle.primary, custom_id="mod_tempban"))
        self.add_item(Button(label="🔨 Perma Ban", style=discord.ButtonStyle.danger, custom_id="mod_permaban"))
        self.add_item(Button(label="⬆️ Promoted", style=discord.ButtonStyle.success, custom_id="mod_promoted"))
        self.add_item(Button(label="⬇️ Demoted", style=discord.ButtonStyle.secondary, custom_id="mod_demoted"))

@bot.tree.command(name="mod", description="Show The Alley Moderation Panel")
@app_commands.checks.has_permissions(manage_messages=True)
async def moderation(interaction: discord.Interaction):
    embed = discord.Embed(
        title="⚖️ THE ALLEY MODERATION PANEL",
        description="Staff moderation action logging system 🕯️\n\n"
                    "» **Warning** – Issue a warning to a member\n"
                    "» **Temp Ban** – Temporarily ban a member\n"
                    "» **Perma Ban** – Permanently ban a member\n"
                    "» **Promoted** – Log a staff promotion\n"
                    "» **Demoted** – Log a staff demotion\n\n"
                    "*Select an action below to create a moderation ticket.*\n"
                    "*The Alley Management* 🕯️",
        color=0xe74c3c
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1409513135966257222/1411000212964638780/8acff8e587df623ec95f8313f9a88ae9.gif")
    embed.set_footer(text="Staff Only | The Alley Management 🕯️")

    await interaction.response.send_message(embed=embed, view=ModerationView())

# ==============================
# 📦 CRATES COMMAND (Improved)
# Shows all available crates for purchase
# ==============================
@bot.tree.command(name="crates", description="View all crates available for purchase")
async def crates(interaction: discord.Interaction):
    embed = discord.Embed(
        title="📦 THE ALLEY CRATE SHOP",
        description=(
            "Unlock exclusive **cosmetics, weapons, and armor sets** from mystical crates! ✨\n\n"
            "Click a button below to preview each crate and see what treasures await you.\n"
            "💰 **Prices are shown in PHP** (₱)\n\n"
            "*Support The Alley and show off your new loot!* 🕯️"
        ),
        color=discord.Color.purple()
    )

    # Dynamically add crate info fields
    for crate_id, crate in CRATES.items():
        embed.add_field(
            name=f"🎁 {crate['title']}",
            value=f"_{crate['description']}_",
            inline=False
        )

    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1409513135966257222/1411000212964638780/8acff8e587df623ec95f8313f9a88ae9.gif")
    embed.set_footer(text="Use the buttons below to preview crates | The Alley Management 🕯️")

    await interaction.response.send_message(embed=embed, view=CrateButtons())


# ==============================
# 🚀 BOOST NOTIFICATION SYSTEM
# ==============================

BOOST_CHANNEL_ID = 123456789012345678  # 👈 Replace with your boost-log channel ID

@bot.event
async def on_member_update(before: discord.Member, after: discord.Member):
    # Detect when a user boosts the server
    if before.premium_since is None and after.premium_since is not None:
        channel = after.guild.get_channel(BOOST_CHANNEL_ID)

        if channel:
            embed = discord.Embed(
                title="🚀 Server Boost!",
                description=f"Thank you {after.mention} for boosting the server! 🎉",
                color=discord.Color.purple()
            )
            embed.set_thumbnail(url=after.display_avatar.url)
            await channel.send(embed=embed)


# ==============================
# 🚀 BOT STARTUP
# Starts the keep-alive server and runs the bot
# ==============================
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env

TOKEN = os.getenv("DISCORD_TOKEN")  # Fetch bot token from .env

if TOKEN is None or TOKEN.strip() == "":
    raise ValueError("❌ DISCORD_TOKEN not found! Make sure it's set in your .env file.")

keep_alive()  # Start Flask server
bot.run(TOKEN)
