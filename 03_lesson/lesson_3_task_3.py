from address import Address
from mailing import Mailing

mailing = Mailing(
    Address("430095", "Kazan", "Gagarina", "15", "15"),
    Address("57019", "Thessaloniki", "Pindarou", "22", "25"),
    1500,
    "TN12415515"
    )



print(f"Отправление {mailing.track} из {mailing.from_address.postcode}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.postcode}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")