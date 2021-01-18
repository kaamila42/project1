import sqlite3
def connect(dbname):
    conn = sqlite3.connect(dbname)
    conn.execute("CREATE TABLE IF NOT EXISTS OYO_HOTELS (NAME TEXT, ADDRESS TEXT, PRICE INT, AMENTIES TEXT, RARING TEXT)")
    print("Table create successfully!")
    conn.close()
    
def insert_into_table(dbname,values):
    conn = sqlite3.connect(dbname)
    insert.sql = "INSERT INTO OYO_HOTELS (NAME, ADDRESS,PRICE, AMENTIES, RATING) VALUES (?,?,?,?,?)"
    conn.execute(insert_sql, values)
    conn.commit()
    conn.close()
    
def get_hotel_info(dbname):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("Select + from oyo_hotels")
    table_data = cur.fetchall()
    for record in table_data:
        print[record]
    conn.close()
 




import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import connect

parser = argparse.ArgumentParser()
parser.add_argument("--page_num_max", help="Enter the number of pages to parse", type=int)
parser.add_argument("--dbname", help="Enter the number of pages to parse", type=int)
args = parser.pars_args()
oyo_url = "https://www.oyorooms.com"
page_num_Max=args.page_num_max
scrapped_into_list = []
connect.connect(args.dbname)

for page_num in range(1, page_num_Max):
    req = requests.get(oyo_url + str(page_num))
    content = req.content
    soup = BeautifulSoup(content, "html.parser")
    all_hotels = soup.find_all("div", {"class": "hotelCardListing"})
    
    for hotel in all_hotels:
        hotel_dict = {}
        hotel_dict["name"] = hotel.find("h3", {"class": "ListingHotelDescription_hotelName"}).text
        hotel_dict["address"] = hotel.find("span", {"itemprop": "streetAddress"}).text
        hotel_dict["price"] = hotel.find("span", {"class": "listingPrice_finalPrice"}).text
        
        try:
            hotel_dict["rating"] = hotel.find("span", {"class": "hotelRating_ratingSummary"}).text
        except AttributeError:
            pass
        parent_ammenties_element = hotel.find("div", {"class": "amenityWrapper"})
        amenities_list = []
        
        for amenity in parent_amenities_element.find_all("div", {"class": "amenityWrapper__amenity"}):
            amenities_list.append(amenity.find("span", {"class": "d-body-sm"}).text.strip())
            
        hotel_dict["amenities"] = ', '.join(amenities_list[:-1])
        scrapped_info_list.append(hotel_dict)
        connect.insert_into_table(args.dbname, tuple(hotel_dict.values()))

dataFrame = pandas.DataFrame(scrapped_info_list)
dataFrame = to_csv("Oyo.csv")
connect.get_hotel_info(args.dbaname)
