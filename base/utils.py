from typing import Dict, Any

import requests


def get_headers_from_investing_screener() -> Dict[str, Any]:
    """
    Get cookies from investing.com stock screener page
    """
    
    url = "https://cn.investing.com/stock-screener/?sp=country::6|sector::a|industry::16|equityType::a|exchange::a%3Ceq_market_cap;1"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    }
    res = requests.get(url, headers=headers)
    p = res.cookies.get_dict()
    

    return headers
