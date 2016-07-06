import meetup_api_client


def get_client():
    name, config = meetup_api_client.app.get_config()
    return meetup_api_client.app.get_client(config)

if __name__ == '__main__':
    meetup_client = get_client()
