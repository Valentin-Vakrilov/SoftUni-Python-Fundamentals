import re


number_of_barcodes = int(input())

search_pattern = r"(@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+)"

for barcode in range(number_of_barcodes):
    current_barcode = input()
    match = re.search(search_pattern, current_barcode)
    if match:
        product_group = ""
        for index in range(len(current_barcode)):
            if current_barcode[index].isdigit():
                product_group += current_barcode[index]

        if product_group == "":
            print("Product group: 00")
        else:
            print(f"Product group: {product_group}")

    else:
        print("Invalid barcode")
