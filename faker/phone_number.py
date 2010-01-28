import random

from faker.utils import numerify

formats = [
    '###-###-####',
    '(###)###-####',
    '1-###-###-####',
    '###.###.####',
    '###-###-####',
    '(###)###-####',
    '1-###-###-####',
    '###.###.####',
    '###-###-#### x###',
    '(###)###-#### x###',
    '1-###-###-#### x###',
    '###.###.#### x###',
    '###-###-#### x####',
    '(###)###-#### x####',
    '1-###-###-#### x####',
    '###.###.#### x####',
    '###-###-#### x#####',
    '(###)###-#### x#####',
    '1-###-###-#### x#####',
    '###.###.#### x#####'
]

def phone_number():
    return numerify(random.choice(formats))
