import random

lotto_box = list(range(1, 46))
random.shuffle(lotto_box)
use_suffle = lotto_box[:6]
use_suffle.sort()
print(use_suffle)

use_sample = random.sample(lotto_box, 6)
use_sample.sort()
print(use_sample)
