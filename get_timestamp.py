from datetime import datetime


def get_current_timestamp_in_millieseconds() -> int:
    return int(datetime.now().timestamp() * 1000)


if __name__ == "__main__":
    print(
        f"The current timestamp in millieseconds: {get_current_timestamp_in_millieseconds()}."
    )
