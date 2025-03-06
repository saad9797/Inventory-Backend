from django.db import models

class Supplier(models.Model):
    SupplierID = models.AutoField(primary_key=True)
    SupplierName = models.CharField(max_length=255)
    Contact = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)

    def __str__(self):
        return self.SupplierName

class Category(models.Model):
    CategoryID = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=255)
    Description = models.TextField()

    def __str__(self):
        return self.CategoryName

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.department_name

class PurchaseOrder(models.Model):
    PurchaseOrderID = models.AutoField(primary_key=True)
    SupplierID = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    OrderDate = models.DateField()
    Stand = models.CharField(max_length=255)
    TotalAmount = models.FloatField()

    def __str__(self):
        return f"Order {self.PurchaseOrderID}"

class Product(models.Model):
    ProductID = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=255)
    CategoryID = models.ForeignKey(Category, on_delete=models.CASCADE)
    Description = models.TextField()
    UnitPrice = models.FloatField()

    def __str__(self):
        return self.ProductName

class MRF(models.Model):
    mrf_id = models.AutoField(primary_key=True)
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    request_date = models.DateField()
    quantity_requested = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"Info {self.mrf_id}"

class PurchaseOrderDetails(models.Model):
    PurchaseOrderDetailID = models.AutoField(primary_key=True)
    PurchaseOrderID = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    CostPrice = models.FloatField()
    Subtotal = models.FloatField()

    def __str__(self):
        return f"Detail {self.PurchaseOrderDetailID}"

class Inventory(models.Model):
    InventoryID = models.AutoField(primary_key=True)
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    WarehouseLocation = models.CharField(max_length=255)

    def __str__(self):
        return f"Inventory {self.InventoryID}"