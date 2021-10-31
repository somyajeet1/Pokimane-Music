
import io
import os

from pyrogram import filters
from tswift import Song

from pyrogram import Client as pbot




# Lel, Didn't Get Time To Make New One So Used Plugin Made br @mrconfused and @sandy1709 dont edit credits


@pbot.on_message(filters.command(["lyric", "lyrics"]))
async def _(client, message):
    lel = await message.reply("Searching For Lyrics Wait krr.....")
    query = message.text
    if not query:
        await lel.edit("`What I am Supposed to find `")
        return

    song = ""
    song = Song.find_song(query)
    if song:
        if song.lyrics:
            reply = song.format()
        else:
            reply = "Couldn't find any lyrics for that song! jaa noob google pr search kr B*** itna parisan kyu kr raha hai try `.glyrics`"
    else:
        reply = "lyrics not found! try with artist name along with song if still doesnt work try `.glyrics` jaa noob google pr search kr **** mujhae kyu parisan kr raha hai LOL"

    if len(reply) > 4095:
        with io.BytesIO(str.encode(reply)) as out_file:
            out_file.name = "lyrics.text"
            await client.send_document(
                message.chat.id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=query,
                reply_to_msg_id=message.message_id,
            )
            await lel.delete()
    else:
        await lel.edit(reply)  # edit or reply
