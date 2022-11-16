class Strings(object):
    def close_tab_string(self):
        text = "📍Welcome to ALBY PYROBOT📍\n"
        text += "Silahkan klik Tombol dibawah untuk mengetahui fitur dan cara mengoperasikan ALBY PYROBOT\n"
        text += "\n\n• Menu Ditutup"

        return text


    def home_tab_string(self):
        text = "🏠 **Home**\n\n"
        text += "📍 **ALBY-Userbot Inline Menu** 📍"

        return text


    def plugin_tab_string(self):
        text = "📍 **ALBY-Userbot Inline Menu** 📍\n\n"
        text += f"🔖 **Plugins:** `{len(self.CMD_HELP)}`"

        return text


    def restart_tab_string(self, process: str=None):
        text = "**Dex:** Settings\n\n"
        text += "**Location:** /home/settings/restart bot\n"
        text += f"**Process:** {process}"

        return text


    def settings_tab_string(self):
        text = "**Dex:** Settings\n\n"
        text += "**Location:** /home/settings"

        return text


    def shutdown_tab_string(self, process: str=None):
        text = "**Dex:** Settings\n\n"
        text += "**Location:** /home/settings/shutdown\n"
        text += f"**Process:** {process}"

        return text
 

    def stats_tab_string(self):
        text = "**Dex:** Stats\n"
        text += "**Location:** /home/stats\n\n"
        text += f"**Name:** {self.UserName()}\n"
        text += f"**{self.BotName()} version:** {self.assistant_version}\n"
        text += f"**Python version:** {self.python_version}\n"
        text += f"**Pyrogram version:** {self.pyrogram_version}\n"
        text += f"**Database:** {self.db_status()}\n"
        text += f"**Uptime:** {self.uptime()}\n"
        text += f"**User Bio:** {self.UserBio()}\n"

        return text


    def update_tab_string(self):
        text = "Not implemented yet."

        return text


    def ialive_tab_string(self):
        text = f"**⛊  Inline Status:**\n\n"
        text += f"**⟐** {self.USER_BIO}\n\n"
        text += f"**⟜ Owner**: [{self.name}](https://t.me/{self.username})\n"
        text += f"**⟜ Tron:** `{self.userbot_version}`\n"
        text += f"**⟜ Python:** `{self.python_version}`\n"
        text += f"**⟜ Pyrogram:** `{self.pyrogram_version}`\n"
        text += f"**⟜ uptime:** `{self.uptime()}`\n"

        return text



    def pmpermit_tab_string(self):
        text = "Not implemented yet."

        return text
