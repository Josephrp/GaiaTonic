def config_list_from_json(json_content):
    """
    Function to load configurations from JSON content into a dictionary.
    """
    config_data = json.loads(json_content)
    return config_data