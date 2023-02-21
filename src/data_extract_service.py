import pandas as pd

class DataExtract:
    def __init__(self) -> None:
        self.vote_results = self.load_from_raw_data("vote_results")
        self.legislators = self.load_from_raw_data("legislators")
        self.bills = self.load_from_raw_data("bills")
        self.votes = self.load_from_raw_data("votes")

    def load_from_raw_data(self, file_name: str):
        try:
            return (
                pd.read_csv(f"raw_data/{file_name}.csv").drop_duplicates().reset_index()
            )
        except FileNotFoundError:
            raise Exception(
                f"File {file_name} not found: check if the path to file is quorum_challenge/raw_data/{file_name}.csv"
            )

    def make_files(self):
        self.legislators_support_oppose_count_dict = dict()
        self.bills_dict = dict()
        for _, legislator in self.vote_results.iterrows():
            if not self.legislators_support_oppose_count_dict.get(
                legislator["legislator_id"]
            ):
                self.create_legislators_support_oppose_count_dict(legislator)
            if not self.bills_dict.get(legislator["vote_id"]):
                self.create_bills_dict(legislator)
            if legislator["vote_type"] == 1:
                self.legislators_support_oppose_count_dict[legislator["legislator_id"]][
                    "num_supported_bills"
                ] += 1
                self.bills_dict[legislator["vote_id"]]["supporter_count"] += 1
            elif legislator["vote_type"] == 2:
                self.legislators_support_oppose_count_dict[legislator["legislator_id"]][
                    "num_opposed_bills"
                ] += 1
                self.bills_dict[legislator["vote_id"]]["opposer_count"] += 1

        legislators_support_oppose_count = pd.DataFrame(
            self.legislators_support_oppose_count_dict
        ).T
        legislators_support_oppose_count.to_csv(
            "legislators_support_oppose_count.csv", index=False
        )
        bills = pd.DataFrame(self.bills_dict).T
        bills.to_csv("bills.csv", index=False)

    def create_legislators_support_oppose_count_dict(self, legislator):
        self.legislators_support_oppose_count_dict[legislator["legislator_id"]] = {
            "id": legislator["legislator_id"],
            "name": self.legislators.loc[
                self.legislators.id == legislator["legislator_id"], "name"
            ].values[0],
            "num_supported_bills": 0,
            "num_opposed_bills": 0,
        }

    def create_bills_dict(self):
        pass