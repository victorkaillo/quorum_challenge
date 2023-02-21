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

    def create_legislators_support_oppose_count(self):
        legislators_support_oppose_count_dict = dict()
        for _, legislator in self.vote_results.iterrows():
            if not legislators_support_oppose_count_dict.get(
                legislator["legislator_id"]
            ):
                legislators_support_oppose_count_dict[legislator["legislator_id"]] = {
                    "id": legislator["legislator_id"],
                    "name": self.legislators.loc[
                        self.legislators.id == legislator["legislator_id"], "name"
                    ].values[0],
                    "num_supported_bills": 0,
                    "num_opposed_bills": 0,
                }

            if legislator["vote_type"] == 1:
                legislators_support_oppose_count_dict[legislator["legislator_id"]][
                    "num_supported_bills"
                ] += 1
            elif legislator["vote_type"] == 2:
                legislators_support_oppose_count_dict[legislator["legislator_id"]][
                    "num_opposed_bills"
                ] += 1
        legislators_support_oppose_count = pd.DataFrame(
            legislators_support_oppose_count_dict
        ).T
        legislators_support_oppose_count.to_csv(
            "legislators_support_oppose_count.csv", index=False
        )

    def create_bills(self):
        pass