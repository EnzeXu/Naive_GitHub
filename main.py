from datetime import datetime


def get_now_string():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")


if __name__ == "__main__":
    print(f"[{get_now_string()}] Hello world!")


