import requests
import json
import os
import pandas as pd
import time
from urllib.parse import urlparse

base_url = "https://shopee.tw/api/v4/item/get_ratings"

def create_folder(url, i):
    a = urlparse(url)
    folder_name = os.path.basename(a.path+i)
    print(folder_name)
    folder_name = folder_name[:12]
    path = os.path.join(os.getcwd(), "data", folder_name)
    try: 
        os.makedirs(path, exist_ok=True) 
        print("Directory '%s' created successfully" % folder_name) 
    except OSError as error: 
        print("Directory '%s' can not be created" % folder_name) 
    return path


def main():
    df = pd.read_excel('Shoppee_Ratings.xlsx')
    ids = []
    for i in df['url']:
        if i.split('/')[-2].isdigit():
            shop_id = i.split('/')[-2]
        else:
            shop_id = i.split('/')[-1].split('.')[-2]

        product_id = i.split('/')[-1].split('.')[-1]
        ids.append([product_id, shop_id])

    # print(len(ids))
    curr_dir = os.getcwd()
    path = os.path.join(curr_dir, "data")
    os.makedirs(path, exist_ok=True)

    for i in range(10):
        product_id, shop_id = ids[i]

        for j in range(1):
            params = {
                'exclude_filter': 1,
                'filter': 0,
                'filter_size': 0,
                'flag': 1,
                'fold_filter': 0,
                'itemid': product_id,
                'limit': 59,
                'offset': 0,
                'relevant_reviews': 'false',
                'request_source': 2,
                'shopid': shop_id,
                'tag_filter': '',
                'type': j+1,
                'variation_filters': '',
            }

            response = requests.get(base_url, params=params)
            url = response.url
            # print(url)

            if j == 0:
                folder_path = create_folder(url, str(i))
            
            if response.status_code == 200:
                data = response.json()           

                print("No: ", i)
                print("ProductId: ", product_id)
                print("Rating: ", j+1)
                if data['data']['ratings']:
                    print("No of Ratings: ", len(data['data']['ratings']))
                else:
                    print("No of Ratings: ", 0)
                print("")
                print("")
                    
                with open(os.path.join(folder_path, "response.json"), "w", encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)

                if data['data']['has_more']:
                    loopForPagination(product_id, data, len(
                        data['data']['ratings']), i, j, folder_path)
            else:
                print(
                    f"Failed to get data from the endpoint. Status code: {response.status_code}, message: {response.message}")


def loopForPagination(product_id, data, offset, i, j, folder_path):
    count = 1
    while data['data']['has_more']:
        params = {
            'exclude_filter': 1,
            'filter': 0,
            'filter_size': 0,
            'flag': 1,
            'fold_filter': 0,
            'itemid': product_id,
            'limit': 59,
            'offset': offset,
            'relevant_reviews': 'false',
            'request_source': 2,
            'shopid': 9241878,
            'tag_filter': '',
            'type': j+1,
            'variation_filters': '',
        }
        response = requests.get(base_url, params=params)

        data = response.json()

        print("Paginating")
        print("No: ", i)
        print("ProductId: ", product_id)
        print("Rating: ", j+1)
        if data['data']['ratings']:
            print("No of Ratings: ", len(data['data']['ratings']))
        else:
            print("No of Ratings: ", 0)
        print()
        print()

        file_path = os.path.join(folder_path, str(j+1), "response.json")
        data_list = []
        if os.path.exists(file_path):
            with open(file_path, "r", encoding='utf-8') as f:
                data_list = json.load(f)
        else:
            data_list = []
        data_list.append(data)
        with open(file_path, "w+", encoding='utf-8') as f:
            json.dump(data_list, f, ensure_ascii=False, indent=4)

        if data['data']['ratings']:
            offset += len(data['data']['ratings'])


start = time.time()
main()
end = time.time()
print("Time taken =", end-start)
