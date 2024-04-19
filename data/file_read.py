import json


class Record:
    def __init__(self, id, money, address):
        self.id = id
        self.money = money
        self.address = address

    def __str__(self):
        return f"id={self.id}, money={self.money}, address={self.address}"



class ReadJsonFile:
    def __init__(self, path):
        self.path = path

    def read_file(self) -> list[Record]:
        res = open(self.path, "r", encoding="UTF-8")
        all_list: list[Record] = []
        for item in res.readlines():
            try:
                json_item = json.loads(item)
                record = Record(json_item["id"], json_item["money"], json_item["address"])
                all_list.append(record)
            except Exception as e:
                print(e)

        res.close()

        return all_list
