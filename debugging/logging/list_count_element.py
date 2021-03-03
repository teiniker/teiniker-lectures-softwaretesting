import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s : %(message)s')
log = logging.getLogger(__name__)

def list_count_element(nums, e):
    log.debug('list_count_element({}, {})'.format(nums, e))
    count = 0
    for n in nums:
        log.debug('  for-loop: n = {}'.format(n))
        if n == e:
            log.debug('    element found, count = {}'.format(count))
            # Bug: count += count + 1
            count = count +1
    return count

numbers = [5, 2, 1, 8, 4, 3, 7, 1, 1, 4]
count = list_count_element(numbers, 1)
print('Count of elements = {}'.format(count))


