import meetup_api_client
import logging


def set_root_loglevel(level):
    logging.getLogger().setLevel(level)

def get_client():
    name, config = meetup_api_client.app.get_config()
    return meetup_api_client.app.get_client(config)


if __name__ == '__main__':
    set_root_loglevel(logging.DEBUG)
    meetup_client = get_client()
    j_result = meetup_client.get_photos()
