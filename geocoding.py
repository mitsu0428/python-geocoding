# pip install googlemapsでpython環境にgoogleMapApi叩く準備
# GCP(GoogleCloudPlatformに登録してAPIKEYを取得しておく/毎月の無料クレジットで4万件ほど可能??※要検索)
import csv
import re
import time
import googlemaps

# csvファイル読み込み
address_list = []
with open("target.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        # 正規表現で改行や空白などがGoogleMapApiでエラーになるものはreplace
        format_text = re.sub(r"\r\n|\r|\n", "", str(row))
        format_text = re.sub(r"\s", "", format_text)
        if format_text == "":
            address_list.append(["住所不明"])
        else:
            address_list.append([format_text])
print(address_list)


# googleMapApiを叩く
googleapikey = ""
googleMap = googlemaps.Client(key=googleapikey)

convert_address = []
for address in address_list:
    location_from_google = googleMap.geocode(address[0])
    print(location_from_google)

    if location_from_google == []:
        convert_address.append(["住所不明", "住所不明", "住所不明"])
    else:
        lat_lng = location_from_google[0]["geometry"]["location"]
        latitude = lat_lng["lat"]
        longitude = lat_lng["lng"]

        key = str(latitude).replace(".", "") + str(longitude).replace(".", "")
        print(key)

        convert_address.append([key, address])

for write in convert_address:
    with open("output.csv", "a", encoding="utf-8") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(write)
