import time
from zillow_data import ZillowData
from google_form import FillGoogleForm

z_data = ZillowData()
g_form = FillGoogleForm()

g_form.open_form()
time.sleep(5)

for item in range(0, len(z_data.property_prices)):
    time.sleep(2)
    g_form.fill_address(z_data.property_addrs[item])
    time.sleep(1)
    g_form.fill_price(z_data.property_prices[item])
    time.sleep(1)
    g_form.fill_link(z_data.property_links[item])
    time.sleep(1)
    g_form.submit_entry()
    time.sleep(1)
    g_form.new_entry()

g_form.driver.quit()
