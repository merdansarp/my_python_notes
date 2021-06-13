from datetime import datetime

class MessageFormatter:
    def success(self, message):
        now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        return f"[{now}] -> {message}"


class MessageWriter:
    def __init__(self):
        self.message_formatter = MessageFormatter()

    def write(self, message):
        print(self.message_formatter.success(message))


def main():
    message_writer = MessageWriter()
    message_writer.write("Joy Division Concert at Concert Hall")


if __name__ == "__main__":
    main()