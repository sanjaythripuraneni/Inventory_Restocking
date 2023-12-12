import unittest
import datetime
from code import InventoryRestockingSystem
class TestInventoryRestockingSystem(unittest.TestCase):
    def setUp(self):
        self.inventory_system = InventoryRestockingSystem()
    
    def test_add_item(self):
        self.inventory_system.add_item(1, "Item A", 10, 5.0, 20, "Supplier X")
        self.assertTrue(1 in self.inventory_system.inventory)
    
    def test_update_item_quantity(self):
        self.inventory_system.add_item(2, "Item B", 5, 8.0, 15, "Supplier Y")
        self.inventory_system.update_item_quantity(2, 3)
        self.assertEqual(self.inventory_system.inventory[2]['quantity'], 8)
    
    def test_set_reorder_point(self):
        self.inventory_system.add_item(3, "Item C", 15, 10.0, 25, "Supplier Z")
        self.inventory_system.set_reorder_point(3, 30)
        self.assertEqual(self.inventory_system.reorder_points[3], 30)

    def test_generate_restock_alerts(self):
        self.inventory_system.add_item(4, "Item D", 5, 5.0, 10, "Supplier A")
        alerts = self.inventory_system.generate_restock_alerts()
        self.assertTrue(4 in alerts)
    
    def test_create_purchase_order(self):
        self.inventory_system.add_item(5, "Item E", 8, 6.0, 12, "Supplier B")
        self.inventory_system.create_purchase_order(5, 10)
        self.assertEqual(len(self.inventory_system.purchase_orders), 1)
    
    def test_receive_inventory(self):
        self.inventory_system.add_item(6, "Item F", 12, 7.0, 18, "Supplier C")
        self.inventory_system.receive_inventory(6, 5, "Supplier C")
        self.assertEqual(self.inventory_system.inventory[6]['quantity'], 17)
    
    def test_calculate_restocking_costs(self):
        self.inventory_system.add_item(7, "Item G", 20, 4.0, 30, "Supplier D")
        self.inventory_system.create_purchase_order(7, 15)
        cost = self.inventory_system.calculate_restocking_costs()
        self.assertEqual(cost, 60.0)
    
    def test_set_preferred_supplier(self):
        self.inventory_system.add_item(8, "Item H", 10, 5.0, 15, "Supplier E")
        self.inventory_system.set_preferred_supplier(8, "Supplier F")
        self.assertEqual(self.inventory_system.inventory[8]['supplier'], "Supplier F")

    def test_export_restocking_reports(self):
        self.inventory_system.add_item(9, "Item I", 6, 8.0, 12, "Supplier G")
        self.inventory_system.receive_inventory(9, 4, "Supplier G")
        self.inventory_system.export_restocking_reports("restocking_report.txt")
        # Check if the file 'restocking_report.txt' exists
        
    def test_add_supplier(self):
        self.inventory_system.add_supplier(1, "Supplier A", "Contact Info A")
        self.assertTrue(1 in self.inventory_system.supplier_info)
    
    def test_view_supplier_info(self):
        self.inventory_system.add_supplier(2, "Supplier B", "Contact Info B")
        info = self.inventory_system.view_supplier_info(2)
        self.assertEqual(info['name'], "Supplier B")
    
    def test_track_purchase_history(self):
        self.inventory_system.add_item(10, "Item J", 8, 5.0, 12, "Supplier H")
        self.inventory_system.create_purchase_order(10, 6)
        history = self.inventory_system.track_purchase_history(10)
        self.assertEqual(len(history), 1)
    
    def test_calculate_total_inventory_value(self):
        self.inventory_system.add_item(12, "Item L", 10, 8.0, 15, "Supplier J")
        total_value = self.inventory_system.calculate_total_inventory_value()
        self.assertEqual(total_value, 80.0)
    
    def test_set_preferred_suppliers(self):
        self.inventory_system.add_item(13, "Item M", 5, 6.0, 10, "Supplier K")
        self.inventory_system.set_preferred_suppliers(13, ["Supplier K", "Supplier L"])
        self.assertEqual(self.inventory_system.inventory[13]['preferred_suppliers'], ["Supplier K", "Supplier L"])
    
    def test_generate_restocking_summary_report(self):
        self.inventory_system.add_item(14, "Item N", 10, 7.0, 15, "Supplier M")
        self.inventory_system.receive_inventory(14, 5, "Supplier M")
        report = self.inventory_system.generate_restocking_summary_report()
        self.assertTrue(14 in report)
    
    def test_set_supplier_contact_info(self):
        self.inventory_system.add_supplier(3, "Supplier C", "Contact Info C")
        self.inventory_system.set_supplier_contact_info(3, "New Contact Info C")
        self.assertEqual(self.inventory_system.supplier_info[3]['contact_info'], "New Contact Info C")
    
    def test_create_return_request(self):
        self.inventory_system.add_item(15, "Item O", 8, 5.0, 12, "Supplier N")
        request = self.inventory_system.create_return_request(15, 3, "Defective Item")
        self.assertIsNotNone(request)
    
    def test_process_return_request(self):
        self.inventory_system.add_item(16, "Item P", 10, 6.0, 15, "Supplier O")
        request = self.inventory_system.create_return_request(16, 2, "Wrong Item")
        print('request:',request)
        response = self.inventory_system.process_return_request(request['request_id'])
        print('response:',response)
        self.assertEqual(response, "Return request processed successfully.")
    
    def test_set_discount(self):
        self.inventory_system.add_item(17, "Item Q", 10, 8.0, 15, "Supplier P")
        self.inventory_system.set_discount(17, 10)
        self.assertEqual(self.inventory_system.inventory[17]['discount_percentage'], 10)
    
    def test_calculate_discounted_price(self):
        self.inventory_system.add_item(18, "Item R", 10, 8.0, 15, "Supplier Q")
        self.inventory_system.set_discount(18, 15)
        discounted_price = self.inventory_system.calculate_discounted_price(18)
        self.assertEqual(discounted_price, 6.8)
    
    def test_view_low_inventory_items(self):
        self.inventory_system.add_item(19, "Item S", 5, 5.0, 10, "Supplier R")
        low_inventory = self.inventory_system.view_low_inventory_items(7)
        self.assertTrue(19 in low_inventory)
    
    def test_set_expiry_date(self):
        self.inventory_system.add_item(20, "Item T", 10, 6.0, 15, "Supplier S")
        expiry_date = datetime.datetime(2023, 12, 31)
        self.inventory_system.set_expiry_date(20, expiry_date)
        self.assertEqual(self.inventory_system.inventory[20]['expiry_date'], expiry_date)
    
    def test_check_item_expiry_status(self):
        self.inventory_system.add_item(21, "Item U", 10, 6.0, 15, "Supplier T")
        expiry_date = datetime.datetime(2022, 12, 31)
        self.inventory_system.set_expiry_date(21, expiry_date)
        status = self.inventory_system.check_item_expiry_status(21)
        self.assertEqual(status, "Expired")
    
    def test_calculate_reorder_quantity(self):
        self.inventory_system.add_item(22, "Item V", 5, 6.0, 10, "Supplier U")
        self.inventory_system.set_reorder_point(22, 8)
        reorder_quantity = self.inventory_system.calculate_reorder_quantity(22)
        self.assertEqual(reorder_quantity, 3)
    
if __name__ == '__main__':
    unittest.main()
