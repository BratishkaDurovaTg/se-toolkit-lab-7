import asyncio
import argparse
import sys

from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message

from config import get_settings
from handlers.commands import handle_health, handle_help, handle_labs, handle_start


def dispatch_test_command(command: str) -> str:
    if command == "/start":
        return handle_start()
    if command == "/help":
        return handle_help()
    if command == "/health":
        return handle_health()
    if command == "/labs":
        return handle_labs()
    return f"Unknown command: {command}"


router = Router()


@router.message(Command("start"))
async def start_command(message: Message) -> None:
    await message.answer(handle_start())


@router.message(Command("help"))
async def help_command(message: Message) -> None:
    await message.answer(handle_help())


@router.message(Command("health"))
async def health_command(message: Message) -> None:
    await message.answer(handle_health())


@router.message(Command("labs"))
async def labs_command(message: Message) -> None:
    await message.answer(handle_labs())


async def run_telegram_bot() -> int:
    settings = get_settings()

    if not settings.bot_token:
        print(
            "BOT_TOKEN is required for Telegram mode. Use --test or set BOT_TOKEN in .env.bot.secret.",
            file=sys.stderr,
        )
        return 1

    bot = Bot(token=settings.bot_token)
    dispatcher = Dispatcher()
    dispatcher.include_router(router)

    await dispatcher.start_polling(bot)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", help="Run a bot command without Telegram")
    args = parser.parse_args()

    if args.test is not None:
        _ = get_settings()
        print(dispatch_test_command(args.test))
        return 0

    try:
        return asyncio.run(run_telegram_bot())
    except KeyboardInterrupt:
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
