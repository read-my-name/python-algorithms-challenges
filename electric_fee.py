accnum = input("Enter 12-digit account number: ").upper()
# Initialize variables for rates 1 through 5 to zero.
rate1 = rate2 = rate3 = rate4 = rate5 =0
# Initialize the service tax (stax) variable to zero.
stax = 0
    
while accnum != 'Q':
    elec = int(input("Enter electricity usage in Kilowatts(KW): "))
    
    # Calculate fee for usage up to 200 kWh
    rate1 = min(elec, 200) * 0.218
    
    # Calculate fee for usage between 201 and 300 kWh
    if elec > 200:
        rate2 = min(max(elec - 200, 0), 100) * 0.3340
    else:
        rate2 = 0
    
    # Calculate fee for usage between 301 and 600 kWh
    if elec > 300:
        rate3 = min(max(elec - 300, 0), 300) * 0.5160
    else:
        rate3 = 0
    
    # Calculate fee for usage between 601 and 900 kWh
    if elec > 600:
        rate4 = min(max(elec - 600, 0), 300) * 0.546
    else:
        rate4 = 0
    
    # Calculate fee for usage above 900 kWh
    if elec > 900:
        rate5 = max(elec - 900, 0) * 0.5710
    else:
        rate5 = 0

    # Calculate the total electric fee by summing up the fees from all rate tiers.
    ttlrate = rate1 + rate2 + rate3 + rate4 + rate5

    # Calculate the ICPT (Imbalance Cost Pass-Through) by multiplying the electric usage by 0.02.
    ICPT = elec * 0.02

    if elec > 600:
        # Calculate the service tax (stax) for usage above 600 kWh.
        stax = (elec - 600) * (0.5460 - 0.02) * 0.016

    # Calculate the KWYBB (Kilowatt-hour Usage-Based Billed) by multiplying the total electric fee by 0.016.
    KWTBB = ttlrate *0.016

    # Calculate the final bill by subtracting ICPT and adding service tax and KWYBB.
    finalbill = ttlrate - ICPT + stax + KWTBB

    print('Account Number: %s'%accnum)  # Print the account number.
    print('Charges: %.2f'%ttlrate)  # Print the total electric charges with 2 decimal places.
    print('ICPT(-0,02/KW): -%.2f'%ICPT)  # Print the ICPT with 2 decimal places and a negative sign.
    print('srvTax(0.06): %.2f'%stax)  # Print the service tax with 2 decimal places.
    print('KWYBB(0.16): %.2f'%KWTBB)  # Print the KWYBB with 2 decimal places.
    print('Total %.2f'%finalbill)  # Print the final bill total with 2 decimal places.


    accnum = input("Enter 12-digit account number: ").upper()

    
        
