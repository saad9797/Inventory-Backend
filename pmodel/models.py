from django.db import models

class Supplier(models.Model):
    SupplierID = models.AutoField(primary_key=True)
    SupplierName = models.CharField(max_length=255,default='Unknown')
    Contact = models.CharField(max_length=255,default='Unknown')
    Address = models.CharField(max_length=255,default='Unknown')

    def __str__(self):
        return self.SupplierName
    
class Category(models.Model):
    CategoryID = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=255,default='Unknown')
    Description = models.TextField(null=True)

    def __str__(self):
        return self.CategoryName

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=255,default='Unknown')
    email = models.EmailField(null=True)

    def __str__(self):
        return self.department_name

class PurchaseOrder(models.Model):
    PurchaseOrderID = models.AutoField(primary_key=True)
    SupplierID = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    DateRecieved = models.DateField(null=True)
    TotalAmount = models.FloatField(null=True)
    DeliveryChalanNumber = models.CharField(max_length=255,default='Unknown')

    def __str__(self):
        return f"Order {self.PurchaseOrderID}"


class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    DepartmentID = models.ForeignKey(Department, on_delete=models.CASCADE)
    Email = models.EmailField(null=True)
    Role = models.CharField(max_length=255,default='Unknown')
    Password = models.CharField(max_length=255,default='Unknown')

    def __str__(self):
        return self.UserID


class Product(models.Model):
    ProductID = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=255,default='Unknown')
    CategoryID = models.ForeignKey(Category, on_delete=models.CASCADE)
    Description = models.TextField(null=True)
    Specification = models.TextField(null=True)
    MajorHead = models.CharField(max_length=255,default='Unknown')

    def __str__(self):
        return self.ProductName

class MRF(models.Model):
    MrfID = models.AutoField(primary_key=True)
    DepartmentID = models.ForeignKey(Department, on_delete=models.CASCADE)
    request_date = models.DateField(null=True)
    recieved_date = models.DateField(null=True)
    quantity_requested = models.IntegerField(null=True)
    quantity_recieved = models.IntegerField(null=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=255,default='Unknown')
    Reference = models.CharField(max_length=255,default='Unknown')
    Purpose = models.CharField(max_length=255,default='Unknown')

    def __str__(self):
        return f"Info {self.MrfID}"

class PurchaseOrderDetails(models.Model):
    PurchaseOrderDetailID = models.AutoField(primary_key=True)
    PurchaseOrderID = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity = models.IntegerField(null=True)
    CostPrice = models.FloatField(null=True)
    Subtotal = models.FloatField(null=True)

    def __str__(self):
        return f"Detail {self.PurchaseOrderDetailID}"

class Inventory(models.Model):
    InventoryID = models.AutoField(primary_key=True)
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity = models.IntegerField(null=True)
    WarehouseLocation = models.CharField(max_length=255,default='Unknown')

    def __str__(self):
        return f"Inventory {self.InventoryID}"