from tronx import (
	USER_NAME, 
	__python_version__, 
	__pyro_version__, 
	nora_version,
	db_status, 
	uptime, 
	USER_BIO,
)

from .variables import (
	assistant_name
}




stat_string = f"""
**Dex:** Stats

**Location:** /home/stats

**Name:** {USER_NAME}
**{assistant_name} version:** {nora_version}
**Python version:** {__python_version__}
**Pyrogram version:** {__pyro_version__}
**Database:** {db_status}
**Uptime:** {uptime()}
**User Bio:** {USER_BIO}
"""



closed_menu_string = f"""
Welcome to Tron.
This is your Helpdex, Tap on open button to get more buttons which will help you to understand & operate your userbot & assistant ( LARA )

• Menu is closed
"""
