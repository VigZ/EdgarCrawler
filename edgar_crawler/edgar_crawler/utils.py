def generate_url(base_url, param_list):
    for key in param_list:
        base_url += key + "=" + param_list[key] + "&"
    return base_url
