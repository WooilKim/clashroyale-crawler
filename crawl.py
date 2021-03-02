import pandas as pd
import requests
import numpy as np


def find_top_2(season, weak_cnt):
    url = 'https://royaleapi.com/clan/LGLCJ029/war/analytics'

    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    r = requests.get(url, headers=header)

    dfs = pd.read_html(r.text)[0]
    # print(dfs)
    # print(dfs.headers)
    dfs['this_weak_sum'] = 0

    for w in range(1, weak_cnt + 1):
        dfs[f'{season} - {w}'] = dfs[f'{season} - {w}'].replace(np.nan, 0)
        dfs['this_weak_sum'] += dfs[f'{season} - {w}']

    # dfs.sort_values(by='this_weak_sum').head(5)
    print(dfs.sort_values(by='this_weak_sum', ascending=False)[['Player', 'this_weak_sum']].head(5).to_string(
        index=False))


if __name__ == '__main__':
    find_top_2(69, 4)
