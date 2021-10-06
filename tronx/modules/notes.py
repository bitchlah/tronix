import time

from pyrogram import filters
from pyrogram.types import (
	InlineKeyboardMarkup, 
	InlineKeyboardButton, 
	Message
)

from tronx import (
	app, 
	CMD_HELP,
	Config,
	PREFIX
	)

from tronx.database.postgres import notes_sql as db

from tronx.helpers import (
	gen,
	regex,
	error,
	send_edit,
	# others 
	parse_button, 
	build_keyboard, 
	Types, 
	get_note_type, 
	fetch_note_type,
	long,
)




CMD_HELP.update(
	{"notes" : (
		"notes",
		{
		"save [note mame ] [reply to message]" : "Save A Note Of Any Type Of Media In Your Database.", 
		">" : "Get Your Note. Example: `>mynote`, Where mynote is note name and command ( >)",
		"notes" : "Get Your Saved Note List.",
		"clear" : "Delete A Note."
		}
		)
	}
)




GET_FORMAT = {
	Types.TEXT.value: app.send_message,
	Types.DOCUMENT.value: app.send_document,
	Types.PHOTO.value: app.send_photo,
	Types.VIDEO.value: app.send_video,
	Types.STICKER.value: app.send_sticker,
	Types.AUDIO.value: app.send_audio,
	Types.VOICE.value: app.send_voice,
	Types.VIDEO_NOTE.value: app.send_video_note,
	Types.ANIMATION.value: app.send_animation,
	Types.ANIMATED_STICKER.value: app.send_sticker,
	Types.CONTACT: app.send_contact
}




@app.on_message(gen("save"))
async def save_note(_, m: Message):
	if len(m.command) < 2:
		return await send_edit(m, "A note name is required with command to save notes ...", mono=True)

	note_name, text, message_type, content = get_note_type(m)
	if not note_name:
		return await send_edit(m, "A name is necessary for a note !", mono=True)

	if message_type == Types.TEXT:
		file_id = None
		teks, button = parse_button(text)
		if not teks:
			await send_edit(m, f"`{m.text}`\n\nError: There is no text in here !")

	db.save_selfnote(m.from_user.id, note_name, text, message_type, content)
	await send_edit(m, "Saved note = **[ `{}` ]**".format(note_name),parse_mode="markdown")




@app.on_message(regex(">"))
async def get_note(_, m: Message):
	reply = m.reply_to_message
	if m.text and m.text.startswith(">"):
		if len(m.text.split()) == 1:
			note = m.text.replace(">", "")
		else:
			return
		getnotes = db.get_selfnote(m.from_user.id, note)

		if not getnotes:
			return await send_edit(m, "This note does not exist !")

		msg_id = None # message.message_id
		if reply:
			mdg_id = reply.message_id
		if getnotes['type'] == Types.TEXT:
			teks, button = parse_button(getnotes.get('value'))
			button = build_keyboard(button)
			if button:
				button = InlineKeyboardMarkup(button)
			else:
				button = False
			if button:
				return await send_edit(m, "Inline button not supported in this userbot version :(")
			else:
				await send_edit(m, teks)

		elif getnotes['type'] in (Types.STICKER, Types.VOICE, Types.VIDEO_NOTE, Types.CONTACT, Types.ANIMATED_STICKER):
			await m.delete()
			try:
				if msg_id:
					await GET_FORMAT[getnotes['type']](message.chat.id, getnotes['file'], reply_to_message_id=msg_id)
				else:
					await GET_FORMAT[getnotes['type']](message.chat.id, getnotes['file'])
			except errors.exceptions.bad_request_400.BadRequest:
				msg = await app.get_messages(m.chat.id, getnotes['message_id'])
				note_name, text, message_type, content = fetch_note_type(msg)
				db.save_selfnote(m.chat.id, note, "", getnotes['type'], content, getnotes['message_id'])
				if msg_id:
					await GET_FORMAT[getnotes['type']](m.chat.id, content, reply_to_message_id=msg_id)
				else:
					await GET_FORMAT[getnotes['type']](m.chat.id, content)
		else:
			await m.delete()
			if getnotes.get('value'):
				teks, button = parse_button(getnotes.get('value'))
				button = build_keyboard(button)
				if button:
					button = InlineKeyboardMarkup(button)
				else:
					button = False
			else:
				teks = False
				button = False
			if button:
				return await send_edit(m, "Inline button not supported in this userbot version :(\nSee @tronuserbot for more information")
			else:
				try:
					if msg_id:
						await GET_FORMAT[getnotes['type']](m.chat.id, getnotes['file'], caption=teks, reply_to_message_id=msg_id)
					else:
						await GET_FORMAT[getnotes['type']](m.chat.id, getnotes['file'], caption=teks)
				except errors.exceptions.bad_request_400.BadRequest:
					msg = await app.get_messages(m.chat.id, getnotes['message_id'])
					note_name, text, message_type, content = fetch_note_type(msg)
					db.save_selfnote(m.chat.id, note, teks, getnotes['type'], content, getnotes['message_id'])
					if msg_id:
						await GET_FORMAT[getnotes['type']](m.chat.id, getnotes['file'], caption=teks, reply_to_message_id=msg_id)
					else:
						await GET_FORMAT[getnotes['type']](m.chat.id, getnotes['file'], caption=teks)
	else:
		return




@app.on_message(gen("notes"))
async def notes_list(_, m: Message):	
	getnotes = db.get_all_selfnotes(m.from_user.id)
	if not getnotes:
		return await send_edit(m, "There are no saved notes !")

	notelist = "**Notebook:**\n\n"
	for x in getnotes:
		if len(notelist) >= 1800:
			await send_edit(m, notebook)
			notelist = "**Notebook:**\n\n"
		notelist += "`>{}`\n".format(x)

	await send_edit(m, notelist)




@app.on_message(gen("clear"))
async def clear_note(client, m: Message):	
	if long(m) <= 1:
		return await send_edit(m, f"Sir, give note name after command, Ex: `{PREFIX}clear cat`")

	note = m.text.split()[1]
	getnote = db.rm_selfnote(m.from_user.id, note)
	if not getnote:
		return await send_edit(m, "This note does not exist!")
	else:
		await send_edit(m, "Deleted note = **[ `{}` ]**".format(note),parse_mode="markdown")
        
