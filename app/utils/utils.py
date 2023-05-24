import requests


def fix_number(wpp):
    _wpp = wpp
    if len(_wpp) == 10:
        auxiliar = _wpp[2:]
        auxiliar = '9' + auxiliar
        codigo = _wpp[:2]
        _wpp = codigo + auxiliar
    elif len(_wpp) == 11:
        auxiliar = _wpp[3:]
        codigo = _wpp[:2]
        _wpp = codigo + auxiliar
    else:
        _wpp = wpp
    return _wpp


def update_lead_pipefy(idcard, idposicao):
    _request_url = "https://app.pipefy.com/queries"
    _api_token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VyIjp7ImlkIjozMDEwMjQ1MjUsImVtYWlsIjoidGlAaGF1c3ouY29tLmJyIiwiYXBwbGljYXRpb24iOjMwMDA2ODU0NH19.LGOfdmTwrMk3k9bXoRJq1MAAkCc1MdN-YTeiFH1Qe8_-plpFC0fE0khFzak9PsAeFFw3K_MWVeGD4rSR5ccU7Q"
    _idcard = idcard
    _idposicao = idposicao
    _headers = {"Authorization": _api_token}
    _mutation = 'mutation { moveCardToPhase(input:{card_id:' + _idcard + 'destination_phase_id:' + _idposicao + '}){card{current_phase{id name}}}}'
    requests.post(_request_url, json={"query": _mutation}, headers=_headers)

