import re


def match_process(data, keyword):
    data['Process_matched'] = 0
    for idx, r_data in data.iterrows():
        inform = r_data['Inform']
        for _, r_keyword in keyword.iterrows():
            if all([re.search(k, inform) for k in r_keyword['Keywords'].split(',')]):
                process_matched = r_keyword['Process']
                data.at[idx, 'Process_matched'] = process_matched
    return data
