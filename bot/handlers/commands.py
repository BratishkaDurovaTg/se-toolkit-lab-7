def handle_start() -> str:
    return "Welcome to the LMS bot!"


def handle_help() -> str:
    return "\n".join(
        [
            "Available commands:",
            "/start - welcome message",
            "/help - list available commands",
            "/health - backend status placeholder",
            "/labs - labs list placeholder",
        ]
    )


def handle_health() -> str:
    return "Backend status: not implemented yet."


def handle_labs() -> str:
    return "Labs list: not implemented yet."
