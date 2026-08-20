ALGORITHM SmartCanteenCheckout
    // Step 1: Initialize variables
    SET totalCost = 0
    SET orderItems = EMPTY LIST
    SET systemRunning = TRUE

    // Step 2: Process items in the order
    WHILE cashier adds item DO
        INPUT itemID, itemPrice, quantity
        
        // Check stock availability
        IF checkStock(itemID) >= quantity THEN
            SET itemTotal = itemPrice * quantity
            SET totalCost = totalCost + itemTotal
            APPEND (itemID, quantity) TO orderItems
            CALL updateStock(itemID, quantity)
        ELSE
            PRINT "Warning: Item out of stock or insufficient quantity!"
        ENDIF

        INPUT choice ("Add another item? Y/N")
        IF choice == "N" THEN
            EXIT WHILE
        ENDIF
    ENDWHILE

    PRINT "Total Amount Due: PHP " + totalCost

    // Step 3: Payment Process
    REPEAT
        INPUT amountTendered
        IF amountTendered < totalCost THEN
            PRINT "Insufficient payment. Remaining balance: PHP " + (totalCost - amountTendered)
        ENDIF
    UNTIL amountTendered >= totalCost

    // Step 4: Calculate Change
    SET change = amountTendered - totalCost
    PRINT "Payment Successful!"
    PRINT "Change: PHP " + change

    // Step 5: Print Receipt
    CALL printReceipt(orderItems, totalCost, amountTendered, change)
END ALGORITHM