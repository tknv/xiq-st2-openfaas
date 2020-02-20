import logging, requests, json, os, sys


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    data = json.loads(req)
    coming_token = os.getenv("Http_Authorization")
    logger.debug("coming_token: %s" % coming_token)
    our_token = os.getenv("auth_token")
    logger.debug("our_token: %s" % our_token)
    if not our_token in coming_token:
        sys.exit("Incoming token: %s is might be wrong."  % coming_token)
        return
    clients = len(data['data']['observations'])
    logger.debug("clients: %s" % clients)
    push_to_st2(req)
    return "Observed: %s clients" % clients


def push_to_st2(req):
    st2_host = os.getenv("st2_webhook_host")
    st2_api_key = os.getenv("api_key")
    session = requests.Session()
    session.verify = False
    logger.debug("Sending XIQ data: %s to %s" % (req, st2_host))
    response = session.post(
        st2_host, 
        data=req,
        headers={'Content-Type': 'application/json', 'St2-Api-Key': st2_api_key}
    )
    # Accept 202 for SSL cert error fallback
    if response.status_code not in [200, 202]:
        raise ValueError(
            'Request to ST2 returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )
    return response