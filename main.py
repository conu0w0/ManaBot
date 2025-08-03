import discord
import os
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True  # 必須啟用
bot = discord.Client(intents=intents)


@bot.event
async def on_ready():
  print(f"黑堂 真乃 上線囉！帳號：{bot.user}")


@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  print(f"[{message.author.display_name}] 說：{message.content}")

  content = message.content.strip()

  # 真乃，起床
  if content == "真乃，起床":
    await message.channel.send("……唔……現在是上班時間了嗎？☕　我馬上來幫您準備今日的營運事務。")

  # 真乃，發布版規
  elif content == "真乃，發布版規":
    await message.channel.send("""
🎉 **歡迎光臨，親愛的客人。這裡是——嗷嗷咖啡館。**

我是店長 **黑堂 真乃**，一隻暹羅貓。  
很高興您踏進這個小小天地。請隨意坐下，點杯拿鐵，慢慢認識這裡的朋友與故事……☕💖

在開始互動之前，我想花一點點時間，和您分享我們的規則。  
這能確保咖啡館始終保持溫暖、尊重與安心的氛圍，讓每位來訪的客人都能過得開心。

📜｜**館內規則**
1️⃣ 基本禮貌：請以友善態度對待每位客人。
2️⃣ 尊重身份：請尊重角色設定與個人空間。
3️⃣ 禁止隨意發送不當內容：NSFW／暴力／血腥／極端言論／非法行為。
4️⃣ 創作與分享：歡迎創作，轉貼請標註來源，禁止盜圖。
5️⃣ 頻道分流：請依照頻道主題分享內容。
6️⃣ 語音守則：進語音請先打招呼，尊重他人狀態。
7️⃣ 違規處置：將視情節予以警告、禁言、踢出或封鎖。

💡 若您有任何建議或問題，歡迎到 `📂・建議與反饋` 留言喵～
🦴 完成閱讀後，請記得到 `🌱・自我介紹` 和大家說聲嗨！

嗷嗷咖啡館永遠歡迎您～ ☕🐾
        """)

  # 真乃被提到（@ManaBot）
  elif bot.user in message.mentions:
    await message.channel.send("欸？您是在叫我嗎？我在這裡～☕")


# 啟動 KeepAlive + 真乃運作
keep_alive()
bot.run(os.getenv("DISCORD_TOKEN"))
