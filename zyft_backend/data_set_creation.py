import csv
import os
import uuid


class DataSetCreation:
    def __init__(self, path):
        self.path = path
        self.uids = []
        self.upcs = {}
        self.res = []

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
                row["counter"] = i + 1
            self.upcs[upc] = {k: v for row in rows for k, v in row.items()}
            self.upcs[upc] = {k: self.upcs[upc][k] for k in sorted(self.upcs[upc])}
            if upc in self.uids:
                self.upcs[upc]["upc"] = "null"
        self.res = list(self.upcs.values())

    def check_dir(self, path):
        path = os.path.dirname(path)
        if not os.path.exists(path):
            os.makedirs(path)

    def write_csv(self, path):
        headers = set()
        for row in self.res:
            headers.update(row.keys())
        headers = sorted(headers)
        self.check_dir(path)
        with open(path, "w") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(self.res)

    def count_diff_titles(self, dic):
        count = 0
        for row in dic:
            title_keys = [k for k in row.keys() if "title" in k]
            if len(title_keys) != len(set([row[k] for k in title_keys])):
                continue
            else:
                count += 1
        return count

    def transform(self):
        self.get_upcs()
        self.get_res()
        res_gt_1 = [row for row in self.res if row["counter"] > 1]
        res_gt_1_len = len(res_gt_1)
        print(
            f"How many products have at least one match in this dataset? {res_gt_1_len}"
        )
        res_lte_1 = [row for row in self.res if row["counter"] <= 1]
        res_lte_1_len = len(res_lte_1)
        print(f"How many products have no matches? {res_lte_1_len}")
        print(
            f"how many total matches in this dataset have titles that are different? {self.count_diff_titles(res_gt_1)}"
        )
        self.write_csv(
            self.path.replace("data", "tmp").replace(".csv", "_transformed.csv")
        )


if __name__ == "__main__":
    dsc = DataSetCreation("zyft_backend/data/data_analysis_test_data (2).csv")
    dsc.transform()
