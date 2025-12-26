from loader import bot

# Импорт handlers
import handlers.menu
import handlers.qr
import handlers.news
import handlers.faq
import handlers.voice
import handlers.email
import handlers.donate
import handlers.common_features
import handlers.premium_features

if __name__ == '__main__':
    try:
        print("🚀 Запуск бота...")
        bot.remove_webhook()
        bot.infinity_polling()
    except KeyboardInterrupt:
        print("\n⏹️  Бот остановлен")
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        raise
