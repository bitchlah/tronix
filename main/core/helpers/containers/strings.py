class Strings(object):
    def close_tab_string(self):
        text = "πWelcome to ALBY PYROBOTπ\n"
        text += "Silahkan klik Tombol dibawah untuk mengetahui fitur dan cara mengoperasikan ALBY PYROBOT\n"
        text += "\n\nβ’ Menu Ditutup"

        return text


    def home_tab_string(self):
        text = "π  **Home**\n\n"
        text += "π **ALBY-Userbot Inline Menu** π"

        return text


    def plugin_tab_string(self):
        text = "π **ALBY-Userbot Inline Menu** π\n\n"
        text += f"π **Plugins:** `{len(self.CMD_HELP)}`"

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
        text = f"**β  Inline Status:**\n\n"
        text += f"**β** {self.USER_BIO}\n\n"
        text += f"**β Owner**: [{self.name}](https://t.me/{self.username})\n"
        text += f"**β Tron:** `{self.userbot_version}`\n"
        text += f"**β Python:** `{self.python_version}`\n"
        text += f"**β Pyrogram:** `{self.pyrogram_version}`\n"
        text += f"**β uptime:** `{self.uptime()}`\n"

        return text



    def pmpermit_tab_string(self):
        text = "Not implemented yet."

        return text
