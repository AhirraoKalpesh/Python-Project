class shop:
   # bill=0
    product_list = []

    def add(self):
        n = int(input("\nEnter no of products to add: "))
        self.bill = 1

        def add1(self):
            for i in range(0, n):
                self.product_name, self.price, self.qty = input(
                    "\nenter values:").split()
                if self.product_name not in shop.product_list:
                    self.empty = [self.product_name, self.price, self.qty]
                    shop.product_list.append(self.empty)
                else:
                    print("Product already exist!")
                    add1(self)
        # shop.product_list.extend(list([self.product_name,self.price,self.qty]))
        # print(shop.product_list)
        add1(self)

    def cal(self):

        k = -1

        for i in self.product_list:
           # print(i)
            k += 1
            b = 1
            for j in range(len(i)):

                if j == 0:
                    continue
                else:
                    b = int(i[1])*int(i[2])
                    break
            shop.product_list[k].append(b)
        # print(shop.product_list)

    def same(self):
        for i in shop.product_list:
            for j in shop.product_list:
                if i[0] == j[0]:
                    i[1] = str(int(i[1]) + int(j[1]))
                    i[2] = str(int(i[2]) + int(j[2]))

                    shop.product_list.remove(j)

    def show(self):
        print(f"\nName\tPrice\tQuantity\tTotal")
        for i in shop.product_list:
            # for j in i:
            #     print(j, "\t", end=" ")
            # print()

            print(f" {i[0]}\t {i[1]}\t {i[2]}\t\t {i[3]}")

    def update(self):
        ans = 'Y'
        nm = input("\nEnter product Name:")
        for i in shop.product_list:
            if i[0] == nm:
                while(ans in 'Yy'):
                    up = int(input(
                        "\nWhat do you want to update:\n1.Product name\n2.Product Price\n3.Product Quantity\n4.Exit\n\nEnter your choice: "))
                    if up == 1:
                        pn = input("\nEnter new product name: ")
                        i[0] = pn
                    elif up == 2:
                        npp = input("\nEnter new product price: ")
                        i[1] = npp
                        i[3] = (int(i[2]) * int(i[1]))
                    elif up == 3:
                        npq = input("\nEnter new product quantity: ")
                        i[2] = npq
                        i[3] = str(int(i[2]) * int(i[1]))
                    elif up == 4:
                        break
                    else:
                        print("\n!Wrong Choice!")
                    # ans = input("Do you want to update again: ")

    def delete(self):
        self.nm = input("\nEnter product name to delete: ")
        for i in shop.product_list:
            for j in i:
                if j == self.nm:
                    shop.product_list.remove(i)
        shop.show(self)


obj = shop()
ans = 'Y'
while(ans in 'Yy'):
    print("\n1.Add Product\n2.Product Bill\n3.Update Product\n4.Delete Product\n5.Exit")
    ch = int(input("\nEnter your choice: "))
    if ch == 1:
        obj.add()
        obj.cal()
    elif ch == 2:
        obj.show()
    elif ch == 3:
        obj.update()
        obj.show()
    elif ch == 4:
        obj.delete()
    elif ch == 5:
        break
    else:
        print("wrong choice")
    # ans = input("Do u want to continue")
