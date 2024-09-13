import os
import shutil

import git
from pyrogram import filters

from DONATE_ARMY_MUSIC import app


@app.on_message(filters.command(["downloadrepo"]))
def download_repo(_, message):
    if len(message.command) != 2:
        message.reply_text(
            "Please provide the GitHub repository URL after the command. Example: /downloadrepo Repo Url "
        )
        return

    repo_url = message.command[1]
    zip_path = download_and_zip_repo(repo_url)

    if zip_path:
        with open(zip_path, "rb") as zip_file:
            message.reply_document(zip_file)
        os.remove(zip_path)
    else:
        message.reply_text("Unable to download the specified GitHub repository.")


def download_and_zip_repo(repo_url):
    try:
        repo_name = repo_url.split("/")[-1].replace(".git", "")
        repo_path = f"{repo_name}"

        # Clone the repository
        repo = git.Repo.clone_from(repo_url, repo_path)

        # Create a zip file of the repository
        shutil.make_archive(repo_path, "zip", repo_path)

        return f"{repo_path}.zip"
    except Exception as e:
        print(f"Error downloading and zipping GitHub repository: {e}")
        return None
    finally:
        if os.path.exists(repo_path):
            shutil.rmtree(repo_path)


__MODULE__ = "Rᴇᴘᴏ"
__HELP__ = """
## Cᴏᴍᴍᴀɴᴅs Hᴇᴘ

### 1. /ᴅᴏᴡɴᴏᴀᴅʀᴇᴘᴏ
**Dᴇsᴄʀɪᴘᴛɪᴏɴ:**
Dᴏᴡɴᴏᴀᴅ ᴀɴᴅ ʀᴇᴛʀɪᴇᴠᴇ ғɪᴇs ғʀᴏᴍ ᴀ GɪᴛHᴜʙ ʀᴇᴘᴏsɪᴛᴏʀʏ.

**Usᴀɢᴇ:**
/ᴅᴏᴡɴᴏᴀᴅʀᴇᴘᴏ [Rᴇᴘᴏ_URL]

**Dᴇᴛᴀɪs:**
- Cᴏɴᴇs ᴛʜᴇ sᴘᴇᴄɪғɪᴇᴅ GɪᴛHᴜʙ ʀᴇᴘᴏsɪᴛᴏʀʏ.
- Cʀᴇᴀᴛᴇs ᴀ ᴢɪᴘ ғɪᴇ ᴏғ ᴛʜᴇ ʀᴇᴘᴏsɪᴛᴏʀʏ.
- Sᴇɴᴅs ᴛʜᴇ ᴢɪᴘ ғɪᴇ ʙᴀᴄᴋ ᴀs ᴀ ᴅᴏᴄᴜᴍᴇɴᴛ.
- Iғ ᴛʜᴇ ᴅᴏᴡɴᴏᴀᴅ ғᴀɪs, ᴀɴ ᴇʀʀᴏʀ ᴍᴇssᴀɢᴇ ᴡɪ ʙᴇ ᴅɪsᴘᴀʏᴇᴅ.

**Exᴀᴍᴘᴇs:**
- `/ᴅᴏᴡɴᴏᴀᴅʀᴇᴘᴏ ʜᴛᴛᴘs://ɢɪᴛʜᴜʙ.ᴄᴏᴍ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘᴏsɪᴛᴏʀʏ`

"""
