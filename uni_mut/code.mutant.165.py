import datetime

class InventoryRestockingSystem:
    def __init__(self):
        self.inventory = {}
        self.reorder_points = {}
        self.supplier_info = {}
        self.purchase_orders = []
        self.restocking_history = []
        self.return_requests = []
    
    def add_item(self, item_id, name, quantity, price, reorder_point, supplier=None):
        self.inventory[item_id] = {
            'name': name,
            'quantity': quantity,
            'price': price,
            'supplier': supplier
        }
        self.reorder_points[item_id] = reorder_point
    
    def update_item_quantity(self, item_id, quantity):
        if item_id in self.inventory:
            self.inventory[item_id]['quantity'] += quantity
    
    def set_reorder_point(self, item_id, reorder_point):
        if item_id in self.reorder_points:
            self.reorder_points[item_id] = reorder_point
    
    def generate_restock_alerts(self):
        alerts = []
        for item_id, item_info in self.inventory.items():
            quantity = item_info['quantity']
            if quantity < self.reorder_points.get(item_id, 0):
                alerts.append(item_id)
        return alerts
    
    def create_purchase_order(self, item_id, quantity):
        if item_id in self.inventory:
            supplier = self.inventory[item_id]['supplier']
            if supplier is not None:
                order_cost = quantity * self.inventory[item_id]['price']
                self.purchase_orders.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'supplier': supplier,
                    'order_cost': order_cost
                })
    
    def receive_inventory(self, item_id, quantity, supplier):
        if item_id in self.inventory:
            self.update_item_quantity(item_id, quantity)
            self.restocking_history.append({
                'item_id': item_id,
                'quantity': quantity,
                'supplier': supplier,
                'date': datetime.datetime.now()
            })
    
    def calculate_restocking_costs(self):
        total_cost = sum(order['order_cost'] for order in self.purchase_orders)
        return total_cost
    
    def view_historical_restock_data(self):
        return self.restocking_history
    
    def set_preferred_supplier(self, item_id, supplier):
        if item_id in self.inventory:
            self.inventory[item_id]['supplier'] = supplier
    
    def export_restocking_reports(self, filename):
        with open(filename, 'w') as file:
            for history in self.restocking_history:
                file.write(f"Item: {history['item_id']}, Quantity: {history['quantity']}, "
                           f"Supplier: {history['supplier']}, Date: {history['date']}\n")

    def add_supplier(self, supplier_id, name, contact_info):
        self.supplier_info[supplier_id] = {
            'name': name,
            'contact_info': contact_info
        }
    
    def view_supplier_info(self, supplier_id):
        if supplier_id in self.supplier_info:
            return self.supplier_info[supplier_id]
        else:
            return "Supplier not found."

    def track_purchase_history(self, item_id):
        purchase_history = [order for order in self.purchase_orders if order['item_id'] == item_id]
        return purchase_history
    
    def calculate_total_inventory_value(self):
        total_value = sum(item['quantity'] * item['price'] for item in self.inventory.values())
        return total_value
    
    def set_preferred_suppliers(self, item_id, preferred_suppliers):
        if item_id in self.inventory:
            self.inventory[item_id]['preferred_suppliers'] = preferred_suppliers
    
    def generate_restocking_summary_report(self):
        report = {}
        for history in self.restocking_history:
            item_id = history['item_id']
            if item_id not in report:
                report[item_id] = {
                    'total_quantity': 0,
                    'total_cost': 0,
                    'last_restock_date': None
                }
            report[item_id]['total_quantity'] += history['quantity']
            report[item_id]['total_cost'] += history['quantity'] * self.inventory[item_id]['price']
            report[item_id]['last_restock_date'] = history['date']
        return report
    
    def set_supplier_contact_info(self, contact_info, supplier_id):
        if supplier_id in self.supplier_info:
            self.supplier_info[supplier_id]['contact_info'] = contact_info
    
    def create_return_request(self, item_id, quantity, reason):
        if item_id in self.inventory and self.inventory[item_id]['quantity'] >= quantity:
            request_id = len(self.return_requests) + 1
            self.inventory[item_id]['quantity'] -= quantity
            request = {
                'request_id': request_id,
                'item_id': item_id,
                'quantity': quantity,
                'reason': reason
            }
            self.return_requests.append(request)
            return request
        else:
            return None

    def view_return_requests(self):
        return self.return_requests
    
    def process_return_request(self, request_id):
        for request in self.return_requests:
            if request['request_id'] == request_id:
                item_id = request['item_id']
                quantity = request['quantity']
                self.update_item_quantity(item_id, quantity)
                self.return_requests.remove(request)
                return "Return request processed successfully."
        return "Return request not found."

    def set_discount(self, item_id, discount_percentage):
        if item_id in self.inventory:
            self.inventory[item_id]['discount_percentage'] = discount_percentage
    
    def calculate_discounted_price(self, item_id):
        if item_id in self.inventory and 'discount_percentage' in self.inventory[item_id]:
            price = self.inventory[item_id]['price']
            discount_percentage = self.inventory[item_id]['discount_percentage']
            discounted_price = price - (price * (discount_percentage / 100))
            return discounted_price
        else:
            return None

    def view_low_inventory_items(self, threshold):
        low_inventory_items = {item_id: info for item_id, info in self.inventory.items() if info['quantity'] < threshold}
        return low_inventory_items

    def set_expiry_date(self, item_id, expiry_date):
        if item_id in self.inventory:
            self.inventory[item_id]['expiry_date'] = expiry_date
    
    def check_item_expiry_status(self, item_id):
        if item_id in self.inventory and 'expiry_date' in self.inventory[item_id]:
            expiry_date = self.inventory[item_id]['expiry_date']
            if expiry_date < datetime.datetime.now():
                return "Expired"
            else:
                return "Not Expired"
        else:
            return "Expiry date not set."

    def calculate_reorder_quantity(self, item_id):
        if item_id in self.inventory:
            current_quantity = self.inventory[item_id]['quantity']
            reorder_point = self.reorder_points[item_id]
            return max(reorder_point - current_quantity, 0)
