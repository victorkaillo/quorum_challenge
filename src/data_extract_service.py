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
legislators_dict = dict()
for _, legislator in vote_results.iterrows():
    if not legislators_dict.get(legislator['legislator_id']):
        legislators_dict[legislator['legislator_id']] = {"id": legislator['legislator_id'],"name": legislators.loc[legislators.id == legislator['legislator_id'],"name"].values[0],"num_supported_bills": set(),"num_opposed_bills": set()}
    if legislator['vote_type'] == 1:
        legislators_dict[legislator['legislator_id']]["num_supported_bills"].add(legislator['vote_id'])
    elif legislator['vote_type'] == 2:
        legislators_dict[legislator['legislator_id']]["num_opposed_bills"].add(legislator['vote_id'])
    # print(legislator['legislator_id'])