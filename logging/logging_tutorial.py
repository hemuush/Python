from decimal import DivisionByZero
import logging

logging.basicConfig(level=logging.DEBUG,filename="logging/log.log",filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")

#Custom Logger
log = logging.getLogger(__name__)
log.info("Test the custom logger")

#Differnt level of logging
x = 5
logging.info(f"the value of x is {x}")

try:
    1/0
except ZeroDivisionError as e:
    logging.error("ZeroDivisionError",exc_info=True)

'''
try:
    1/0
except ZeroDivisionError as e:
    logging.exception("ZeroDivisionError")
'''

# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")