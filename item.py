class Item:
    
    def __init__(self, name, item_correct_loc_id, item_current_loc_id = None):
        self.name = name
        self.item_correct_loc_id = item_correct_loc_id
        self.item_current_loc_id = item_current_loc_id

    def __str__(self):
        return "Name - {}".format(self.name)
    
    def check_correct_item_place(self):
        if self.item_correct_loc_id == self.item_current_loc_id:
            return True
        else:
            return False