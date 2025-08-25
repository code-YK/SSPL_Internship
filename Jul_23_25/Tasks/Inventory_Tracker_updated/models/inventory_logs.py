class InventoryLog:
    def __init__(self, log_id, product_id, warehouse_id, txn_type, quantity, txn_date, total_amount):
        self.log_id = log_id
        self.product_id = product_id
        self.warehouse_id = warehouse_id
        self.txn_type = txn_type
        self.quantity = quantity
        self.txn_date = txn_date
        self.total_amount = total_amount
