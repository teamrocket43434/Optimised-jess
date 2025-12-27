"""Help commands"""
import discord
from discord.ext import commands
from config import EMBED_COLOR, BOT_PREFIX

class Help(commands.Cog):
    """Help and information commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help", aliases=["h"])
    async def help_command(self, ctx, category: str = None):
        """Show help information

        Categories: collection, category, hunt, settings, prediction, starboard, owner, all
        """
        prefix = BOT_PREFIX[0]  # Use first prefix for examples

        # Check if user is owner
        is_owner = await self.bot.is_owner(ctx.author)

        if not category:
            # Main help embed
            embed = discord.Embed(
                title="📚 Poketwo Helper Bot - Help",
                description=f"Use `{prefix}help <category>` for detailed information about a category\nUse `{prefix}help all` to see all commands at once",
                color=EMBED_COLOR
            )

            embed.add_field(
                name="📦 Collection",
                value=f"`{prefix}help collection` - Manage your Pokemon collection",
                inline=False
            )

            embed.add_field(
                name="🗂️ Category",
                value=f"`{prefix}help category` - Bulk collection management with categories",
                inline=False
            )

            embed.add_field(
                name="✨ Shiny Hunt",
                value=f"`{prefix}help hunt` - Set up shiny hunting",
                inline=False
            )

            embed.add_field(
                name="⚙️ Settings",
                value=f"`{prefix}help settings` - Configure bot settings",
                inline=False
            )

            embed.add_field(
                name="🔮 Prediction",
                value=f"`{prefix}help prediction` - Manual Pokemon prediction",
                inline=False
            )

            embed.add_field(
                name="⭐ Starboard",
                value=f"`{prefix}help starboard` - Configure starboard channels",
                inline=False
            )

            if is_owner:
                embed.add_field(
                    name="👑 Owner",
                    value=f"`{prefix}help owner` - Bot owner commands",
                    inline=False
                )

            embed.add_field(
                name="ℹ️ About",
                value=f"`{prefix}about` - Bot information and stats",
                inline=False
            )

            embed.add_field(
                name="🏓 Ping",
                value=f"`{prefix}ping` - Check bot latency",
                inline=False
            )

            embed.set_footer(text=f"Bot Prefix: {', '.join(BOT_PREFIX)}")

            await ctx.reply(embed=embed, mention_author=False)
            return

        category = category.lower()

        # Collection category
        if category in ["collection", "cl", "collect"]:
            embed = discord.Embed(
                title="📦 Collection Commands",
                description="Manage your Pokemon collection for this server. Get pinged when Pokemon you collect spawn!",
                color=EMBED_COLOR
            )

            embed.add_field(
                name=f"`{prefix}cl add <pokemon>`",
                value=(
                    "Add Pokemon to your collection\n"
                    f"**Aliases:** `{prefix}collection add`\n"
                    f"**Examples:**\n"
                    f"• `{prefix}cl add Pikachu`\n"
                    f"• `{prefix}cl add Pikachu, Charizard, Mewtwo`\n"
                    f"• `{prefix}cl add Furfrou all` (adds all Furfrou variants)"
                ),
                inline=False
            )

            embed.add_field(
                name=f"`{prefix}cl remove <pokemon>`",
                value=(
                    "Remove Pokemon from your collection\n"
                    f"**Aliases:** `{prefix}collection remove`\n"
                    f"**Example:** `{prefix}cl remove Pikachu`"
                ),
                inline=False
            )

            embed.add_field(
                name=f"`{prefix}cl list`",
                value=(
                    "View your collection in a paginated embed with buttons\n"
                    f"**Aliases:** `{prefix}collection list`"
                ),
                inline=False
            )

            embed.add_field(
                name=f"`{prefix}cl raw`",
                value=(
                    "View your collection as comma-separated text (sends as .txt file if large)\n"
                    f"**Aliases:** `{prefix}collection raw`"
                ),
                inline=False
            )

            embed.add_field(
                name=f"`{prefix}cl clear`",
                value=(
                    "⚠️ Clear your entire collection\n"
                    f"**Aliases:** `{prefix}collection clear`"
                ),
                inline=False
            )

            embed.add_field(
                name="💡 How It Works",
                value=(
                    "• When a Pokemon you collect spawns, you get pinged!\n"
                    "• If you add `Furfrou`, you get pinged for all Furfrou variants\n"
                    "• If you add `Furfrou all`, all variants are explicitly added to your collection"
                ),
                inline=False
            )

        # Category commands
        elif category in ["category", "cat", "categories"]:
            embed = discord.Embed(
                title="🗂️ Category Commands",
                description="Bulk collection management with categories. Admins create categories, users add them to their collection!",
                color=EMBED_COLOR
            )

            embed.add_field(
                name=f"`{prefix}cat add <categories>`",
                value=(
                    "Add Pokemon from categories to your collection\n"
                    f"**Aliases:** `{prefix}category add`\n"
                    f"**Examples:**\n"
                    f"• `{prefix}cat add Rares`\n"
                    f"• `{prefix}cat add Rares, Regionals, Gigantamax`"
                ),
                inline=False
            )

            embed.add_field(
                name=f"`{prefix}cat remove <categories>`",
                value=(
                    "Remove Pokemon from categories from your collection\n"
                    f"**Aliases:** `{prefix}category remove`\n"
                    f"**Example:** `{prefix}cat remove Rares`"
                ),
                inline=False
            )

            embed.add_field(
                name=f"`{prefix}cat list`",
                value=(
                    "View all server categories with Pokemon counts\n"
                    f"**Aliases:** `{prefix}category list`"
                ),
                inline=False
            )

            embed.add_field(
                name=f"`{prefix}cat info <name>`",
                value=(
                    "View Pokemon in a specific category (paginated)\n"
                    f"**Aliases:** `{prefix}category info`\n"
                    f"**Example:** `{prefix}cat info Rares`"
                ),
                inline=False
            )

            embed.add_field(
                name="📝 Admin Commands",
                value=(
                    f"`{prefix}cat create <name> <pokemon>` - Create a category\n"
                    f"**Example:** `{prefix}cat create Rares articuno, moltres, zapdos`\n\n"
                    f"`{prefix}cat edit <name> <pokemon>` - Edit a category (replaces all Pokemon)\n"
                    f"**Example:** `{prefix}cat edit Rares marshadow, lugia`\n\n"
                    f"`{prefix}cat delete <name>` - Delete a category\n"
                    f"**Example:** `{prefix}cat delete Rares`"
                ),
                inline=False
            )

            embed.add_field(
                name="💡 How It Works",
                value=(
                    "• Admins create categories with Pokemon lists\n"
                    "• Users can add entire categories to their collection at once\n"
                    "• Supports 'all' variants (e.g., `arceus all`, `furfrou all`)\n"
                    "• Category names are case-insensitive and can have spaces"
                ),
                inline=False
            )

        # Shiny Hunt category
        elif category in ["hunt", "sh", "shiny"]:
            embed = discord.Embed(
                title="✨ Shiny Hunt Commands",
                description="Set up shiny hunting to get pinged when your target Pokemon spawns!",
                color=EMBED_COLOR
            )

            embed.add_field(
                name=f"`{prefix}sh`",
                value=(
                    "Check your current shiny hunt\n"
                    f"**Aliases:** `{prefix}hunt`, `{prefix}shinyhunt`"
                ),
                inline=False
            )

            embed.add_field(
                name=f"`{prefix}sh <pokemon>`",
                value=(
                    "Start hunting a Pokemon\n"
                    f"**Aliases:** `{prefix}hunt <pokemon>`, `{prefix}shinyhunt <pokemon>`\n"
                    f"**Examples:**\n"
                    f"• `{prefix}sh Pikachu`\n"
                    f"• `{prefix}sh Furfrou all` (hunt all Furfrou variants)"
                ),
                inline=False
            )

            embed.add_field(
                name=f"`{prefix}sh clear`",
                value=(
                    "Stop hunting (also accepts `none` or `stop`)\n"
                    f"**Aliases:** `{prefix}hunt clear`, `{prefix}shinyhunt clear`"
                ),
                inline=False
            )

            embed.add_field(
                name="💡 Note",
                value="You can hunt one Pokemon (or all its variants) at a time per server!",
                inline=False
            )

        # Settings category
        elif category in ["settings", "setting", "config", "afk"]:
            embed = discord.Embed(
                title="⚙️ Settings Commands",
                description="Configure bot settings for your server and personal preferences",
                color=EMBED_COLOR
            )

            embed.add_field(
                name="👤 User Settings",
                value="",
                inline=False
            )

            embed.add_field(
                name=f"`{prefix}afk`",
                value=(
                    "Toggle collection and shiny hunt pings using interactive buttons\n"
                    f"**Aliases:** `{prefix}away`\n"
                    "🟢 **Green** = Pings ON (you'll be pinged)\n"
                    "🔴 **Red** = Pings OFF (you won't be pinged)\n"
                    "*AFK status is global across all servers*"
                ),
                inline=False
            )

            embed.add_field(
                name="🛠️ Server Settings",
                value="",
                inline=False
            )

            embed.add_field(
                name=f"`{prefix}server-settings`",
                value=(
                    "View all current server settings\n"
                    f"**Aliases:** `{prefix}ss`, `{prefix}settings`, `{prefix}serversettings`"
                ),
                inline=False
            )

            embed.add_field(
                name="📝 Admin Commands",
                value="",
                inline=False
            )

            embed.add_field(
                name=f"`{prefix}rare-role @role`",
                value=(
                    "Set role to ping for rare Pokemon (Legendary/Mythical/Ultra Beast)\n"
                    f"**Aliases:** `{prefix}rr`, `{prefix}rarerole`\n"
                    f"**Example:** `{prefix}rare-role @Rare Hunters`\n"
                    f"Use `{prefix}rare-role none` to clear"
                ),
                inline=False
            )

            embed.add_field(
                name=f"`{prefix}regional-role @role`",
                value=(
                    "Set role to ping for regional Pokemon\n"
                    f"**Aliases:** `{prefix}regrole`, `{prefix}regional`, `{prefix}regionrole`\n"
                    f"**Example:** `{prefix}regional-role @Regional`\n"
                    f"Use `{prefix}regional-role none` to clear"
                ),
                inline=False
            )

            embed.add_field(
                name=f"`{prefix}only-pings`",
                value=(
                    "Toggle only-pings mode (only send predictions when there are pings)\n"
                    f"**Aliases:** `{prefix}op`, `{prefix}onlypings`\n"
                    f"**Examples:**\n"
                    f"• `{prefix}only-pings` - View current status\n"
                    f"• `{prefix}only-pings true` - Enable\n"
                    f"• `{prefix}only-pings false` - Disable"
                ),
                inline=False
            )

        # Prediction category
        elif category in ["prediction", "predict", "pred"]:
            embed = discord.Embed(
                title="🔮 Prediction Commands",
                description="Manually predict Pokemon from images or view auto-detection info",
                color=EMBED_COLOR
            )

            embed.add_field(
                name=f"`{prefix}predict <image_url>`",
                value=(
                    "Predict Pokemon from image URL\n"
                    f"**Aliases:** `{prefix}pred`, `{prefix}p`\n"
                    f"**Example:** `{prefix}predict https://...`"
                ),
                inline=False
            )

            embed.add_field(
                name=f"`{prefix}predict` (reply to message)",
                value=(
                    "Reply to a message with an image to predict it\n"
                    f"**Example:** Reply to image with `{prefix}predict`"
                ),
                inline=False
            )

            embed.add_field(
                name="🤖 Auto-Detection",
                value=(
                    "The bot automatically predicts Poketwo spawns and pings:\n"
                    "• **Shiny hunters** hunting that Pokemon\n"
                    "• **Collectors** who have collected that Pokemon\n"
                    "• **Rare/Regional roles** if applicable"
                ),
                inline=False
            )

            embed.add_field(
                name="📊 Dual Model System",
                value=(
                    "Bot uses two AI models for accuracy:\n"
                    "• **Primary model** (224x224) - Fast predictions\n"
                    "• **Secondary model** (336x224) - Used for low confidence cases\n"
                    "Predictions with ≥90% confidence are posted automatically"
                ),
                inline=False
            )

        # Starboard category
        elif category in ["starboard", "star", "log"]:
            embed = discord.Embed(
                title="⭐ Starboard Commands",
                description="Configure automatic logging of rare catches, hatches, and unboxes to dedicated channels",
                color=EMBED_COLOR
            )

            embed.add_field(
                name=f"`{prefix}starboard-settings`",
                value=(
                    "View current starboard channel configuration"
                ),
                inline=False
            )

            embed.add_field(
                name="📺 Channel Configuration (Admin Only)",
                value="",
                inline=False
            )

            embed.add_field(
                name="Starboard For All",
                value=(
                    f"`{prefix}starboard-all #channel` - All catches, hatches, unboxes\n"
                    f"Use `none` instead of #channel to remove"
                ),
                inline=False
            )

            embed.add_field(
                name="General Channels",
                value=(
                    f"`{prefix}starboard-catch #channel` - All catches\n"
                    f"`{prefix}starboard-egg #channel` - All egg hatches\n"
                    f"`{prefix}starboard-unbox #channel` - All box openings\n"
                    f"Use `none` instead of #channel to remove"
                ),
                inline=False
            )

            embed.add_field(
                name="Specific Criteria Channels",
                value=(
                    f"`{prefix}starboard-shiny #channel` - Shiny catches/hatches/unboxes\n"
                    f"`{prefix}starboard-gigantamax #channel` - Gigantamax catches/hatches/unboxes\n"
                    f"`{prefix}starboard-highiv #channel` - High IV (≥90%)\n"
                    f"`{prefix}starboard-lowiv #channel` - Low IV (≤10%)\n"
                    f"`{prefix}starboard-missingno #channel` - MissingNo catches\n"
                    f"Use `none` instead of #channel to remove"
                ),
                inline=False
            )

            embed.add_field(
                name="🔍 Manual Checking (Admin Only)",
                value=(
                    f"`{prefix}catchcheck` - Manually check a catch message\n"
                    f"`{prefix}eggcheck` - Manually check an egg hatch\n"
                    f"`{prefix}unboxcheck` - Manually check a box opening\n"
                    "Use by replying to a message or providing message ID"
                ),
                inline=False
            )

            embed.add_field(
                name="📋 What Gets Logged?",
                value=(
                    "• **Shiny** catches/hatches/unboxes\n"
                    "• **Gigantamax** catches/hatches/unboxes\n"
                    "• **High IV** (≥90%) or **Low IV** (≤10%)\n"
                    "• **MissingNo** catches\n"
                    "• **Combinations** (e.g., Shiny + High IV)\n\n"
                    "Note: A Pokemon meeting multiple criteria will be sent to multiple channels!"
                ),
                inline=False
            )

        # Owner commands
        elif category in ["owner", "admin", "botowner"]:
            if not is_owner:
                await ctx.reply("❌ This category is only available to the bot owner.", mention_author=False)
                return

            embed = discord.Embed(
                title="👑 Owner Commands",
                description="Bot owner only commands for global settings",
                color=0xFFD700  # Gold color
            )

            embed.add_field(
                name=f"`{prefix}set-low-prediction-channel #channel`",
                value=(
                    "Set global channel for low confidence predictions (< 90%)\n"
                    f"**Aliases:** `{prefix}setlowpred`, `{prefix}lowpredchannel`\n"
                    f"**Example:** `{prefix}set-low-prediction-channel #low-predictions`"
                ),
                inline=False
            )

            embed.add_field(
                name=f"`{prefix}set-secondary-model-channel #channel`",
                value=(
                    "Set global channel for secondary model logs\n"
                    f"**Aliases:** `{prefix}setsecondary`, `{prefix}secondarychannel`\n"
                    f"**Example:** `{prefix}set-secondary-model-channel #secondary-logs`\n"
                    "Logs when secondary model (336x224) is used for predictions"
                ),
                inline=False
            )

            embed.add_field(
                name=f"`{prefix}starboard-set-global-catch #channel`",
                value=(
                    "Set global catch starboard channel (across all servers)\n"
                    f"**Aliases:** `{prefix}sbsetglobalcatch`"
                ),
                inline=False
            )

            embed.add_field(
                name=f"`{prefix}starboard-set-global-egg #channel`",
                value=(
                    "Set global egg starboard channel (across all servers)\n"
                    f"**Aliases:** `{prefix}sbsetglobalegg`"
                ),
                inline=False
            )

            embed.add_field(
                name=f"`{prefix}starboard-set-global-unbox #channel`",
                value=(
                    "Set global unbox starboard channel (across all servers)\n"
                    f"**Aliases:** `{prefix}sbsetglobalunbox`"
                ),
                inline=False
            )

        # All commands
        elif category in ["all", "commands"]:
            embed = discord.Embed(
                title="📚 All Commands",
                description="Complete list of all bot commands",
                color=EMBED_COLOR
            )

            embed.add_field(
                name="📦 Collection",
                value=(
                    f"`{prefix}cl add` • `{prefix}cl remove` • `{prefix}cl list`\n"
                    f"`{prefix}cl raw` • `{prefix}cl clear`"
                ),
                inline=False
            )

            embed.add_field(
                name="🗂️ Category",
                value=(
                    f"`{prefix}cat add` • `{prefix}cat remove` • `{prefix}cat list` • `{prefix}cat info`\n"
                    f"**Admin:** `{prefix}cat create` • `{prefix}cat edit` • `{prefix}cat delete`"
                ),
                inline=False
            )

            embed.add_field(
                name="✨ Shiny Hunt",
                value=f"`{prefix}sh` • `{prefix}sh <pokemon>` • `{prefix}sh clear`",
                inline=False
            )

            embed.add_field(
                name="⚙️ Settings",
                value=(
                    f"`{prefix}afk` • `{prefix}server-settings`\n"
                    f"**Admin:** `{prefix}rare-role` • `{prefix}regional-role` • `{prefix}only-pings`"
                ),
                inline=False
            )

            embed.add_field(
                name="🔮 Prediction",
                value=f"`{prefix}predict`",
                inline=False
            )

            embed.add_field(
                name="⭐ Starboard Settings",
                value=(
                    f"`{prefix}starboard-settings` • `{prefix}starboard-all`\n"
                    f"`{prefix}starboard-catch/egg/unbox`\n"
                    f"`{prefix}starboard-shiny/gigantamax/highiv/lowiv/missingno`"
                ),
                inline=False
            )

            embed.add_field(
                name="🔍 Starboard Manual Check",
                value=f"`{prefix}catchcheck` • `{prefix}eggcheck` • `{prefix}unboxcheck`",
                inline=False
            )

            if is_owner:
                embed.add_field(
                    name="👑 Owner",
                    value=(
                        f"`{prefix}set-low-prediction-channel`\n"
                        f"`{prefix}set-secondary-model-channel`\n"
                        f"`{prefix}starboard-set-global-catch/egg/unbox`"
                    ),
                    inline=False
                )

            embed.add_field(
                name="ℹ️ Info",
                value=f"`{prefix}help` • `{prefix}about` • `{prefix}ping`",
                inline=False
            )

        else:
            await ctx.reply(
                f"❌ Unknown category: `{category}`\n"
                f"Available categories: `collection`, `category`, `hunt`, `settings`, `prediction`, `starboard`, {'`owner`, ' if is_owner else ''}`all`\n"
                f"Use `{prefix}help` to see the main help menu.",
                mention_author=False
            )
            return

        embed.set_footer(text=f"Bot Prefix: {', '.join(BOT_PREFIX)}")
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command(name="about")
    async def about_command(self, ctx):
        """Show bot information and statistics"""
        prefix = BOT_PREFIX[0]

        embed = discord.Embed(
            title="ℹ️ About Pokemon Helper Bot",
            description="A comprehensive Pokemon collection and prediction bot for Poketwo",
            color=EMBED_COLOR
        )

        embed.add_field(
            name="✨ Key Features",
            value=(
                "• 📦 **Collection Management** - Track and get pinged for Pokemon you collect\n"
                "• 🗂️ **Category System** - Bulk add Pokemon to collection\n"
                "• ✨ **Shiny Hunting** - Get notified when your hunt target spawns\n"
                "• 🔮 **Dual Model Prediction** - Automatically identifies Poketwo spawns\n"
                "• ⭐ **Starboard Logging** - Log rare catches, hatches, and unboxes\n"
                "• 🎯 **Smart Pings** - Collectors, hunters, and role-based pings\n"
                "• 🔕 **AFK Mode** - Disable pings when you're away"
            ),
            inline=False
        )

        embed.add_field(
            name="📊 Statistics",
            value=(
                f"**Servers:** {len(self.bot.guilds)}\n"
                f"**Users:** {sum(g.member_count for g in self.bot.guilds)}\n"
                f"**Commands:** {len(self.bot.commands)}"
            ),
            inline=True
        )

        embed.add_field(
            name="⚙️ Technical",
            value=(
                f"**Prefix:** {', '.join(BOT_PREFIX)}\n"
                f"**Library:** discord.py\n"
                f"**Database:** MongoDB\n"
                f"**AI Models:** Dual CNN (224x224 + 336x224)"
            ),
            inline=True
        )

        embed.add_field(
            name="🚀 Getting Started",
            value=f"Use `{prefix}help` to see all available commands and features!",
            inline=False
        )

        embed.add_field(
            name="🔗 Quick Links",
            value=(
                f"• `{prefix}help collection` - Set up your collection\n"
                f"• `{prefix}help category` - Bulk collection management\n"
                f"• `{prefix}help starboard` - Configure starboard logging\n"
                f"• `{prefix}afk` - Manage your ping preferences"
            ),
            inline=False
        )

        embed.set_footer(text=f"Made with ❤️ for the Poketwo community")

        await ctx.reply(embed=embed, mention_author=False)

    @commands.command(name="ping", aliases=["latency", "pong"])
    async def ping_command(self, ctx):
        """Check bot's latency"""
        import time

        # Measure API latency
        api_latency = round(self.bot.latency * 1000)

        # Measure response time
        start = time.perf_counter()
        message = await ctx.reply("🏓 Pinging...", mention_author=False)
        end = time.perf_counter()
        response_time = round((end - start) * 1000)

        # Update with full info
        embed = discord.Embed(
            title="🏓 Pong!",
            color=EMBED_COLOR
        )

        embed.add_field(name="API Latency", value=f"{api_latency}ms", inline=True)
        embed.add_field(name="Response Time", value=f"{response_time}ms", inline=True)

        # Status indicator
        if api_latency < 100:
            status = "🟢 Excellent"
        elif api_latency < 200:
            status = "🟡 Good"
        elif api_latency < 300:
            status = "🟠 Fair"
        else:
            status = "🔴 Poor"

        embed.add_field(name="Status", value=status, inline=True)
        embed.set_footer(text=f"Requested by {ctx.author.display_name}")

        await message.edit(content=None, embed=embed)

    @commands.command(name="commands", aliases=["cmds"])
    async def commands_command(self, ctx):
        """Quick alias to show all commands"""
        await ctx.invoke(self.help_command, category="all")

async def setup(bot):
    await bot.add_cog(Help(bot))
