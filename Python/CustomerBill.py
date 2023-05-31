class Bill:

    items_stock = {"hplaptops":20,"delllaptops":15,"domsartkit":35,
                   "samsunga34":16,"iphone72":9,"sugar(5kg)":48,
                   "titanwatch":5}
    items_amount = {"hplaptops":54990,"delllaptops":43999,"domsartkit":198,
                   "samsunga34":29999,"iphone72":109990,"sugar(5kg)":150,
                   "titanwatch":2199}
    tax = 0.18
    discount = 0.075
    bill_id = 0

    def __init__(s,name,id,date):
        s.name = name
        Bill.bill_id += 1
        s.__bill_id = Bill.bill_id
        s.id = id
        s.date = date
        s.items = dict()
    
    def bill_detail(s):
        print(f"This Bill {s.__bill_id} was generated {s.date} for {s.id}")

    def generate(s):
        cost = 0
        for x in s.items:
            if s.items[x] <= Bill.items_stock[x]:
                Bill.items_stock[x] -= s.items[x]
                cost += Bill.items_amount[x]*s.items[x]
            else:
                return -1
        cost -= cost*Bill.discount
        cost += cost*Bill.tax
        return round(cost)
    
class Customer:

    __id = 230000
    def __init__(s,name):
        s.name = name
        s.id = Customer.__id + 1
        Customer.__id += 1
        s.cust_bill = Bill(s.name,Customer.__id,"01.06.2023")
    
    def purchase(s):
        while True:
            for i in Bill.items_stock:
                print(i,end=', ')
            print("\n>---Enter -1 to exit---<")
            ch = input("Enter your product as same given above: ").lower()
            if ch == '-1':
                break
            qua = int(input("Enter the quantity: "))
            s.cust_bill.items[ch] = qua
        cost = s.cust_bill.generate()
        if cost == -1:
            print("Error! Bill cannot be generated")
        else:
            print("You have to Pay: Rs",cost)
    
    def get_details(s):
        print("}--Detail of the customer---{")
        print("Name:",s.name,"\nId:",s.id)
        s.cust_bill.bill_detail()

c = Customer(input("Enter Customer name: "))
c.purchase()
c.get_details()
