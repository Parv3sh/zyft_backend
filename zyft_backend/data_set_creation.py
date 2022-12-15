import csv
import os
import uuid


class DataTransformer:
    def __init__(self, path):
        self.path = path
        self.uids = []
        self.upcs = {}

    def get_upcs(self):
        with open(self.path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                upc = row["upc"]
                if upc == "null":
                    upc = str(uuid.uuid4())
                    self.uids.append(upc)
                if upc not in self.upcs:
                    self.upcs[upc] = []
                self.upcs[upc].append(row)

    def get_res(self):
        res = []
        for upc, rows in self.upcs.items():
            for i, row in enumerate(rows):
                for k, v in list(row.items()):
                    if i == 0 and k == "upc":
                        continue
                    if i != 0 and k == "upc":
                        del row[k]
                        continue
                    row[f"{k}_{i+1}"] = v
                    del row[k]
        for upc, rows in self.upcs.items():
            self.upcs[upc] = {k: v for row in rows for k, v in row.items()}
            self.upcs[upc] = {k: self.upcs[upc][k] for k in sorted(self.upcs[upc])}
            if upc in self.uids:
                self.upcs[upc]["upc"] = "null"
        res = list(self.upcs.values())
        return res

    def check_dir(self, path):
        path = os.path.dirname(path)
        if not os.path.exists(path):
            os.makedirs(path)

    def write_csv(self, path, res):
        headers = set()
        for row in res:
            headers.update(row.keys())
        headers = sorted(headers)
        self.check_dir(path)
        with open(path, "w") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(res)

    def transform(self):
        self.get_upcs()
        res = self.get_res()
        self.write_csv("zyft_backend/tmp/transformed.csv", res)


if __name__ == "__main__":
    dt = DataTransformer("zyft_backend/data/data_analysis_test_data (2).csv")
    dt.transform()
