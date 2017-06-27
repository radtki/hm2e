#!/usr/bin/env python3

from datetime import datetime

now = datetime.now()
year = now.year
nextyear = year + 1
ALLOWED_YEARS = [year, nextyear]
doy = datetime.today().timetuple().tm_yday


def getDayOfYear(year, month, day):
    """Return the day of year (number) for a given date."""
    return datetime(year, month, day).timetuple().tm_yday


def getSeasonForDate(year, month, day):
    """Return the season for a given date."""
    check = datetime(year, month, day)
    if check.year not in ALLOWED_YEARS:
        return

    doy = check.timetuple().tm_yday

    if doy in SEASONS[check.year]['NEBENSAISON']:
        return 'NEBENSAISON'
    elif doy in SEASONS[check.year]['VORSAISON']:
        return 'VORSAISON'
    else:
        return 'HAUPTSAISON'


def getPriceForDay(year, month, day, room=None):
    """Return the price for a given day."""
    if year not in ALLOWED_YEARS:
        return

    check = datetime(year, month, day)
    wday = check.isoweekday()
    week = WEEK[wday]

    if room:
        try:
            return {room: PRICES[room][getSeasonForDate(year, month, day)][week]}
        except KeyError:
            return {}
    else:
        return {
            'SINGLE': PRICES['SINGLE'][getSeasonForDate(year, month, day)][week],
            'DOUBLE': PRICES['DOUBLE'][getSeasonForDate(year, month, day)][week],
            'FAMILY': PRICES['FAMILY'][getSeasonForDate(year, month, day)][week]
            }


WEEK = {
    'Monday': 'WEEK',
    'Tuesday': 'WEEK',
    'Wednesday': 'WEEK',
    'Thursday': 'WEEK',
    'Friday': 'WEEKEND',
    'Saturday': 'WEEKEND',
    'Sunday': 'WEEKEND',
    1: 'WEEK',
    2: 'WEEK',
    3: 'WEEK',
    4: 'WEEK',
    5: 'WEEKEND',
    6: 'WEEKEND',
    7: 'WEEKEND'
    }

SEASONS = {
    year: {
        'NEBENSAISON': range(getDayOfYear(year, 4, 1), getDayOfYear(year, 9, 15)),
        'VORSAISON': range(getDayOfYear(year, 9, 16), getDayOfYear(year, 12, 19))
    },
    nextyear: {
        'NEBENSAISON': range(getDayOfYear(nextyear, 4, 1), getDayOfYear(nextyear, 9, 15)),
        'VORSAISON': range(getDayOfYear(nextyear, 9, 16), getDayOfYear(nextyear, 12, 19))
    }
}

PRICES = {
    'DOUBLE': {
        'HAUPTSAISON': {'WEEK': [180, 200], 'WEEKEND': [198, 218]},
        'NEBENSAISON': {'WEEK': [160, 180], 'WEEKEND': [176, 196]},
        'VORSAISON': {'WEEK': [140, 160], 'WEEKEND': [154, 174]},
        'RackRate': {'WEEK': [200, 220], 'WEEKEND': [220, 240]}
        },
    'SINGLE': {
        'HAUPTSAISON': {'WEEK': [144, 164], 'WEEKEND': [162, 182]},
        'NEBENSAISON': {'WEEK': [128, 148], 'WEEKEND': [144, 164]},
        'VORSAISON': {'WEEK': [112, 132], 'WEEKEND': [126, 146]},
        'RackRate': {'WEEK': [160, 180], 'WEEKEND': [180, 200]}
        },
    'FAMILY': {
        'HAUPTSAISON': {'WEEK': [225, 245], 'WEEKEND': [270, 290]},
        'NEBENSAISON': {'WEEK': [200, 220], 'WEEKEND': [240, 260]},
        'VORSAISON': {'WEEK': [175, 195], 'WEEKEND': [210, 230]},
        'RackRate': {'WEEK': [250, 270], 'WEEKEND': [300, 320]}
        }
    }

# Tests, to be replaced by unit/integration tests
print(getSeasonForDate(2016, 1, 20), '== None')
print(getPriceForDay(2016, 1, 20))
print(getSeasonForDate(2017, 1, 20), '== HAUPTSAISON')
print(getPriceForDay(2017, 1, 20))
print(getSeasonForDate(2017, 4, 20), '== NEBENSAISON')
print(getPriceForDay(2017, 4, 20))
print(getPriceForDay(2017, 4, 20, 'SCHNULLI'))
print(getPriceForDay(2017, 4, 20, 'DOUBLE'))
print(getPriceForDay(2017, 4, 20, 'FAMILY'))
print(getSeasonForDate(2017, 11, 20), '== VORSAISON')
print(getPriceForDay(2017, 11, 20))
print(getSeasonForDate(2017, 12, 20), '== HAUPTSAISON')
print(getPriceForDay(2017, 12, 20))
print(getSeasonForDate(2018, 1, 20), '== HAUPTSAISON')
print(getPriceForDay(2018, 1, 20))
print(getSeasonForDate(2018, 4, 20), '== NEBENSAISON')
print(getPriceForDay(2018, 4, 20))
print(getSeasonForDate(2018, 11, 20), '== VORSAISON')
print(getPriceForDay(2018, 11, 20))
print(getSeasonForDate(2018, 12, 20), '== HAUPTSAISON')
print(getPriceForDay(2018, 12, 20))
print(getSeasonForDate(2019, 12, 20), '== None')
print(getPriceForDay(2019, 12, 20))
