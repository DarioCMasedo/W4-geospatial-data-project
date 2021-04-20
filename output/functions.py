def api(location, search, radius):
    params = dict(
        client_id='mi token1',
        client_secret='mi token2',
        v='20180323',
        ll=location,
        query='Schools',
        radius=radius,
        sortByDistance=True,
        limit=100
    )
    resp = requests.get(url=url, params=params).json()
    return resp

# Hacer un data frame
    def dataframe(frame):
        data = frame.get("response").get("groups")[0].get("items")
    return get_place_info(data)