import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s : %(message)s')
log = logging.getLogger(__name__)

def list_count_element(nums, element):
    log.debug(f"list_count_element({nums}, {element})")
    counter = 0
    for n in nums:
        log.debug(f"  for-loop: n = {n}")
        if n == element:
            log.debug(f"    element found, counter = {counter}")
            # Bug: count += count + 1
            counter += 1
    return counter

numbers = [5, 2, 1, 8, 4, 3, 7, 1, 1, 4]
count = list_count_element(numbers, 1)
print(f"Count of elements = {count}")
assert count == 3
