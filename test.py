import time
import food_pickup_operator as op

driver = op.init() # gk boleh ganti instance nya
op.fill_table(driver, 4)
op.start_order(driver)

op.choose_stall(driver, 1)

time.sleep(2)
op.order_menu(driver, 1, 2)

op.choose_menu(driver, 2)
op.cancel_order(driver)

op.open_cart(driver)
time.sleep(10)
op.close_cart(driver)

op.checkout(driver)

# op.search(driver, "tei")


# op.open_recommendation(driver)
# time.sleep(1)
# op.close_recommendation(driver)
