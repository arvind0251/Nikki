#  Copyright (c) 2025 AshokShau
#  Licensed under the GNU AGPL v3.0: https://www.gnu.org/licenses/agpl-3.0.html
#  Part of the TgMusicBot project. All rights reserved where applicable.

from typing import Literal
from pytdbot import types
from ._config import config

# ─────────────────────
# Close Button
# ─────────────────────
CLOSE_BTN = types.InlineKeyboardButton(
    text="Cʟᴏsᴇ", type=types.InlineKeyboardButtonTypeCallback(b"vcplay_close")
)

# ─────────────────────
# Safe URL Button Helper
# ─────────────────────
def safe_url_button(text: str, url: str):
    """Return a valid InlineKeyboardButton only if URL is valid."""
    if not url or not url.startswith("http"):
        return None
    return types.InlineKeyboardButton(text=text, type=types.InlineKeyboardButtonTypeUrl(url))

# ─────────────────────
# Control Buttons (Play/Pause/Stop/Resume)
# ─────────────────────
def control_buttons(mode: Literal["play", "pause", "resume"]) -> types.ReplyMarkupInlineKeyboard:
    def btn(text: str, name: str) -> types.InlineKeyboardButton:
        return types.InlineKeyboardButton(
            text=text,
            type=types.InlineKeyboardButtonTypeCallback(f"play_{name}".encode()),
        )

    skip_btn = btn("‣‣I", "skip")
    stop_btn = btn("▢", "stop")
    pause_btn = btn("II", "pause")
    resume_btn = btn("▷", "resume")

    layouts = {
        "play": [[skip_btn, stop_btn, pause_btn, resume_btn], [CLOSE_BTN]],
        "pause": [[skip_btn, stop_btn, resume_btn], [CLOSE_BTN]],
        "resume": [[skip_btn, stop_btn, pause_btn], [CLOSE_BTN]],
    }

    return types.ReplyMarkupInlineKeyboard(layouts.get(mode, [[CLOSE_BTN]]))

# ─────────────────────
# Static Buttons
# ─────────────────────
CHANNEL_BTN = safe_url_button("ᴜᴘᴅᴀᴛᴇꜱ", config.SUPPORT_CHANNEL)
GROUP_BTN = safe_url_button("ꜱᴜᴘᴘᴏʀᴛ", config.SUPPORT_GROUP)

HELP_BTN = types.InlineKeyboardButton(
    text="Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅꜱ", type=types.InlineKeyboardButtonTypeCallback(b"help_all")
)
USER_BTN = types.InlineKeyboardButton(
    text="Uꜱᴇʀ Cᴏᴍᴍᴀɴᴅꜱ", type=types.InlineKeyboardButtonTypeCallback(b"help_user")
)
ADMIN_BTN = types.InlineKeyboardButton(
    text="Aᴅᴍɪɴ Cᴏᴍᴍᴀɴᴅꜱ", type=types.InlineKeyboardButtonTypeCallback(b"help_admin")
)
OWNER_BTN = types.InlineKeyboardButton(
    text="Oᴡɴᴇʀ Cᴏᴍᴍᴀɴᴅꜱ", type=types.InlineKeyboardButtonTypeCallback(b"help_owner")
)
DEVS_BTN = types.InlineKeyboardButton(
    text="Dᴇᴠꜱ Cᴏᴍᴍᴀɴᴅꜱ", type=types.InlineKeyboardButtonTypeCallback(b"help_devs")
)
HOME_BTN = types.InlineKeyboardButton(
    text="Hᴏᴍᴇ", type=types.InlineKeyboardButtonTypeCallback(b"help_back")
)

# ─────────────────────
# Support Button Keyboard
# ─────────────────────
def build_support_buttons():
    rows = []
    row1 = [btn for btn in (CHANNEL_BTN, GROUP_BTN) if btn]
    if row1:
        rows.append(row1)
    rows.append([CLOSE_BTN])
    return types.ReplyMarkupInlineKeyboard(rows)

SupportButton = build_support_buttons()

# ─────────────────────
# Help Menus
# ─────────────────────
HelpMenu = types.ReplyMarkupInlineKeyboard(
    [
        [USER_BTN, ADMIN_BTN],
        [OWNER_BTN, DEVS_BTN],
        [CLOSE_BTN, HOME_BTN],
    ]
)

BackHelpMenu = types.ReplyMarkupInlineKeyboard([[HELP_BTN, HOME_BTN], [CLOSE_BTN]])

# ─────────────────────
# Dynamic Add Me Button
# ─────────────────────
def add_me_markup(username: str) -> types.ReplyMarkupInlineKeyboard:
    """
    Returns an inline keyboard with a button to add the bot to a group
    and support buttons.
    """
    if not username:
        username = "YourBotUsername"  # fallback if bot has no username

    rows = [
        [
            types.InlineKeyboardButton(
                text="Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                type=types.InlineKeyboardButtonTypeUrl(
                    f"https://t.me/{username}?startgroup=true"
                ),
            )
        ],
        [HELP_BTN],
    ]

    row2 = [btn for btn in (CHANNEL_BTN, GROUP_BTN) if btn]
    if row2:
        rows.append(row2)

    return types.ReplyMarkupInlineKeyboard(rows)
