import requests
import json
import os
import pandas as pd
import time

base_url = "https://shopee.tw/api/v2/item/get_ratings"

def main():
    # Read the Excel file
    df = pd.read_excel('Shoppee_Ratings (1).xlsx')
    ids = []

    for i in df['url']:
        if i.split('/')[-2].isdigit():
            shop_id = i.split('/')[-2]
        else:
            shop_id = i.split('/')[-1].split('.')[-2]
        
        product_id = i.split('/')[-1].split('.')[-1]
        ids.append([product_id, shop_id])

    print(len(ids))


    os.mkdir("/home/anand/shopee/data")

    for i in range(50):
        product_id, shop_id = ids[i]
        # Define the URL

        for j in range(5):
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

            # Make the GET request
            response = requests.get(base_url, params=params)


            if j == 0:
                path = f"/home/anand/shopee/data/{i}"
                os.mkdir(path)

            # Check if the request was successful
            if response.status_code == 200:
                # Parse the JSON response
                data = response.json()
                # print(data)

                print("No: ", i)
                print("ProductId: ", product_id)
                print("Rating: ", j+1)
                if data['data']['ratings']:
                    print("No of Ratings: ", len(data['data']['ratings']))
                else:
                    print("No of Ratings: ", 0)
                print("")
                print("")

                # Save to a JSON file
                with open(f"data/{i}/{j+1}response.json", "w") as f:
                    json.dump([data], f)

                if data['data']['has_more']:
                    loopForPagination(product_id, data, len(data['data']['ratings']), i, j)
            else:
                print(f"Failed to get data from the endpoint. Status code: {response.status_code}, message: {response.message}")


def loopForPagination(product_id, data, offset, i, j):
    count = 1
    while data['data']['has_more']:
        params = {
            'exclude_filter': 1,
            'filter': 0,
            'filter_size': 0,
            'flag': 1,
            'fold_filter': 0,
            'itemid': product_id,
            'limit': 6,
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

        with open(f"data/{i}/{j+1}response.json", "a+") as f:
            f.seek(0,2)
            f.seek(f.tell()-1, 0)
            f.truncate()
            f.write(',')
            json.dump(data, f)
            f.write(']')

        if data['data']['ratings']:
            offset += len(data['data']['ratings'])

start = time.time()
main()
end = time.time()
print("Time taken =", end-start)