@app.bot.on_callback_query(filters.regex("home-tab"))
@app.alert_user
async def _start(_, cb: CallbackQuery):
    await cb.edit_message_media(
        media=InputMediaPhoto(media=app.BotPic(), caption=app.home_tab_string()),
        reply_markup=InlineKeyboardMarkup([
                app.BuildKeyboard(
                    (
                        ["• Plugins •", "plugins-tab"]
                    )
                ),
                app.BuildKeyboard(
                    (
                        ["• Diskusi •", "https://t.me/ruangdiskusikami"],
                        ["• Update •", "https://t.me/ruangprojects"]
                    )
                ),
                app.BuildKeyboard(([["Close", "close-tab"]]))
        ]
        ),
    )
