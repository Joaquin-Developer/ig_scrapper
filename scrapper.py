"Instagram scrapper"
import os
import json
from datetime import datetime
import logging
from typing import List, Tuple

import instaloader
from instaloader.exceptions import ProfileNotExistsException


logging.basicConfig(level=logging.INFO)


def get_credentials() -> Tuple[str, str]:
    "Get user/passw by envs"
    return os.getenv("IG_USERNAME"), os.getenv("IG_PASSWORD")


def get_followers(username: str) -> List[str]:
    """
    Args:
        username: user to search
    Returns:
        list: followers
    """
    user, passw = get_credentials()
    igloader = instaloader.Instaloader()
    igloader.login(user, passw)

    try:
        profile = instaloader.Profile.from_username(igloader.context, username)
    except ProfileNotExistsException:
        logging.info("Username %s nt found", username)
        return []

    return [follower.username for follower in profile.get_followers()]


def save_json_file(data: List[str]):
    actual_date = datetime.now().strftime("%Y-%m-%d_%H:%M")
    filename = f"data/ig_scrapper_{actual_date}.json"

    with open(filename, "w") as file:
        json.dump(data, file)
    logging.info("JSON File: %s", filename)


def main():
    username = "__jjjoaquin__"
    followers_list = get_followers(username)

    logging.info("Username: %s", username)

    count = len(followers_list)
    if count < 1:
        logging.warning("NO data.")
        return

    logging.info("Len: %i", count)
    save_json_file(followers_list)


if __name__ == "__main__":
    main()
