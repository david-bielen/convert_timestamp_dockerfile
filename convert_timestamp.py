from datetime import datetime


def convert_timestamp(timestamp: int) -> datetime:
    try:
        return datetime.fromtimestamp(timestamp / 1000)
    except (TypeError, ValueError, OSError):
        raise ValueError(
            "Invalid input: timestamp must be a positive integer in milliseconds."
        )


if __name__ == "__main__":
    timestamp = int(input("Enter a timestamp in milliseconds: "))
    print(convert_timestamp(timestamp))
