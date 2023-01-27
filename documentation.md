# Documentation

## Installation
---

Clone package from github, in `your/custom/directory/` 
```sh
git clone https://github.com/alvingun01/food_operator_fyp.git
```

Go to project directory
```sh
cd project/
```

Create virtual environment
```sh
# Windows
python -m venv env 
# MacOS or Linux
python3 -m venv env 

# Windows
env\Scripts\activate.bat
# MacOS or Linux
source env/bin/activate
```

Install package
``` sh
pip install -e /your/custom/directory/food-pickup-operator
pip freeze > requirements.txt
```

## Initialization
---

``` py
import food_pickup_operator as op
driver = op.init() 
```

`driver` instance must be preserved during all processes.

## Methods
---

### Start page

- Fill table number 
  ```py
  op.fill_table(driver, <table_no>: int)
  ```
- Start order/cart
  ```py
  op.start_order(driver)
  ```

### Home page

- Choose stall
  ```py
  op.choose_stall(driver, <stall_id>: int)
  ```

### Stall page

- Choose menu
  ```py
  op.choose_menu(driver, <menu_id>: int)
  ```
  To cancel (close modal)
  ```py
  op.cancel_order(driver)
  ```
- Fill quantity
  ```py
  op.fill_quantity(driver, <quantity>: int)
  ```
- Submit order, or
  ```py
  op.submit_order(driver)
  ```
- All at once
  ```py
  op.order_menu(driver, <menu_id>: int, <quantity>: int)
  ```

### General 

- Search 
  ```py
  op.search(driver, <keyword>: int)
  ```
- Filter
  - Open filter modal
    ```py
    op.open_filter(driver)
    ```
    To cancel (close modal)
    ```py
    op.close_filter(driver)
    ```
  - Apply filter
    ```py
    op.apply_filter(driver)
    ```
- Recommendation
  ```py
  op.open_recommendation(driver)
  ```
  To cancel (close modal)
  ```py
  op.close_recommendation(driver)
  ```

