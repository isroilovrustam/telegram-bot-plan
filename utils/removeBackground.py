import requests
import logging

url = "https://background-removal.p.rapidapi.com/remove"

# payload = {"image_url": "https://objectcut.com/assets/img/raven.jpg"}
headers = {
    "content-type": "application/x-www-form-urlencoded",
    "X-RapidAPI-Key": "4886c3a7d9msh7d5c40fca147d72p14f274jsn2843157cc7f4",
    "X-RapidAPI-Host": "background-removal.p.rapidapi.com"
}


# test payload
# payload = "image_url=https%3A%2F%2Fobjectcut.com%2Fassets%2Fimg%2Fraven.jpg"

async def remove_background(img_url):
    payload = f"image_url={img_url}"
    response = requests.request("POST", url, data=payload, headers=headers)
    logging.info(response.json()['response']['image_url'])
    return response.json()['response']['image_url']
