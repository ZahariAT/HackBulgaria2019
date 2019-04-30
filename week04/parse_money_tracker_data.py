class RowsToList:
    @staticmethod
    def rows_to_list(all_user_data):
        lst = []
        with open(all_user_data, 'r') as f:
            for row in f.readlines():
                lst.append(row)
        return lst

if __name__ == '__main__':
    print(RowsToList.rows_to_list("money_tracker.txt"))