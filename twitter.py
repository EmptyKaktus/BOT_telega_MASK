import telegram
import time
import feedparser


# Замените <TOKEN> на токен вашего Telegram бота
bot_token = '5702973315:AAHwwEXnVSnNK6QUfyezLVl8t48lwF2u5y4'
# Замените <CHAT_ID> на ID вашего чата с ботом
chat_id = '<1001768245860>'
# Замените <USERNAME> на имя пользователя Илона Маска на Twitter
elon_twitter_username = '<elonmusk>'

# Функция для отправки уведомления в Telegram

# Функция для отправки уведомления в Telegram
def send_telegram_message(message):
    bot = telegram.Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=message)

# Функция для получения последнего поста Илона Маска с помощью TwitRSS
def get_latest_tweet():
    url = f'https://twitrss.me/twitter_user_to_rss/?user={elon_twitter_username}'
    feed = feedparser.parse(url)
    latest_entry = feed.entries[0]
    tweet_text = latest_entry.title
    tweet_link = latest_entry.link
    return tweet_text, tweet_link

# Основной цикл программы
def main():
    last_tweet_text = None
    while True:
        # Получаем последний пост Илона Маска
        current_tweet_text, current_tweet_link = get_latest_tweet()

        # Если текст поста изменился, отправляем уведомление
        if current_tweet_text != last_tweet_text:
            send_telegram_message(f'Новый пост от Илона Маска:\n{current_tweet_link}')
            last_tweet_text = current_tweet_text

        # Пауза в программе перед следующей проверкой (например, каждые 5 минут)
        time.sleep(300)

if __name__ == '__main__':
    main()