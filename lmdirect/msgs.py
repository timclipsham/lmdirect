"""Local API commands for La Marzocco espresso machines."""

"""All models currently Wifi-enabled."""
MODEL_GS3_AV = "GS3 AV"
MODEL_GS3_MP = "GS3 MP"
MODEL_LM = "Linea Mini"

# Tags

from lmdirect.const import (
    CALCULATED_VALUE,
    CONTINUOUS_OFFSET,
    DRINKS_K1_OFFSET,
    DRINKS_K2_OFFSET,
    DRINKS_K3_OFFSET,
    DRINKS_K4_OFFSET,
    FLUSHING_OFFSET,
)

DATE_RECEIVED = "date_received"
POWER = "power"
POWER_MYSTERY = "power_mystery"
TEMP_COFFEE = "coffee_temp"
TEMP_STEAM = "steam_temp"
TSET_STEAM = "steam_set_temp"
TSET_COFFEE = "coffee_set_temp"
DOSE_K1 = "dose_k1"
DOSE_K2 = "dose_k2"
DOSE_K3 = "dose_k3"
DOSE_K4 = "dose_k4"
DOSE_K5 = "dose_k5"
DOSE_HOT_WATER = "dose_hot_water"
ENABLE_PREBREWING = "enable_prebrewing"
PREBREWING_TON_K1 = "prebrewing_ton_k1"
PREBREWING_TON_K2 = "prebrewing_ton_k2"
PREBREWING_TON_K3 = "prebrewing_ton_k3"
PREBREWING_TON_K4 = "prebrewing_ton_k4"
PREBREWING_TOFF_K1 = "prebrewing_toff_k1"
PREBREWING_TOFF_K2 = "prebrewing_toff_k2"
PREBREWING_TOFF_K3 = "prebrewing_toff_k3"
PREBREWING_TOFF_K4 = "prebrewing_toff_k4"
DRINKS_K1 = "drinks_k1"
DRINKS_K2 = "drinks_k2"
DRINKS_K3 = "drinks_k3"
DRINKS_K4 = "drinks_k4"
CONTINUOUS = "continuous"
TOTAL_COFFEE = "total_coffee"
HOT_WATER = "hot_water"
DRINK_MYSTERY = "drink_mystery"
TOTAL_COFFEE_ACTIVATIONS = "total_coffee_activations"
HOT_WATER_2 = "hot_water_2"
DRINKS_HOT_WATER = "drinks_hot_water"
TOTAL_FLUSHING = "total_flushing"
MACHINE_NAME = "machine_name"
FRONT_PANEL_DISPLAY = "front_panel_display"
MYSTERY_VALUES = "mystery_values"
VAL_1 = "val_1"
VAL_2 = "val_2"
VAL_3 = "val_3"
VAL_4 = "val_4"
VAL_5 = "val_5"
VAL_6 = "val_6"
VAL_7 = "val_7"
VAL_8 = "val_8"
VAL_9 = "val_9"
VAL_10 = "val_10"
VAL_11 = "val_11"
VAL_12 = "val_12"
VAL_13 = "val_13"
VAL_14 = "val_14"
VAL_15 = "val_15"
VAL_16 = "val_16"
VAL_17 = "val_17"
VAL_18 = "val_18"

HEATING_STATE = "heating_state"
STEAM_HEATER_ON = "steam_heater_on"
COFFEE_HEATER_ON = "coffee_heater_on"
HEATING_ON = "heating_on"
PUMP_ON = "pump_on"
BREW_SOLENOID_ON = "brew_solenoid_on"
HOT_WATER_SOLENOID_ON = "hot_water_solenoid_on"
BOILER_FILL_SOLENOID_ON = "boiler_fill_solenoid_on"

KEY_ACTIVE = "key_active"
CURRENT_PULSE_COUNT = "current_pulse_count"

COFFEE_HEATING_ELEMENT_HOURS = "coffee_heating_element_hours"
STEAM_HEATING_ELEMENT_HOURS = "steam_heating_element_hours"
MACHINE_RUNNING_SECONDS = "machine_running_seconds"
DAYS_SINCE_BUILT = "days_since_built"
PUMP_ON_SECONDS = "pump_on_seconds"
WATER_ON_SECONDS = "water_on_seconds"

FIRMWARE_VER = "firmware_ver"
MODULE_SER_NUM = "module_ser_num"

UPDATE_AVAILABLE = "update_available"

SUN_ON_HOUR = "sun_on_hour"
SUN_OFF_HOUR = "sun_off_hour"
MON_ON_HOUR = "mon_on_hour"
MON_OFF_HOUR = "mon_off_hour"
TUE_ON_HOUR = "tue_on_hour"
TUE_OFF_HOUR = "tue_off_hour"
WED_ON_HOUR = "wed_on_hour"
WED_OFF_HOUR = "wed_off_hour"
THU_ON_HOUR = "thu_on_hour"
THU_OFF_HOUR = "thu_off_hour"
FRI_ON_HOUR = "fri_on_hour"
FRI_OFF_HOUR = "fri_off_hour"
SAT_ON_HOUR = "sat_on_hour"
SAT_OFF_HOUR = "sat_off_hour"
SUN_ON_HOUR = "sun_on_hour"
SUN_OFF_HOUR = "sun_off_hour"
MON_ON_MIN = "mon_on_min"
MON_OFF_MIN = "mon_off_min"
TUE_ON_MIN = "tue_on_min"
TUE_OFF_MIN = "tue_off_min"
WED_ON_MIN = "wed_on_min"
WED_OFF_MIN = "wed_off_min"
THU_ON_MIN = "thu_on_min"
THU_OFF_MIN = "thu_off_min"
FRI_ON_MIN = "fri_on_min"
FRI_OFF_MIN = "fri_off_min"
SAT_ON_MIN = "sat_on_min"
SAT_OFF_MIN = "sat_off_min"
SUN_ON_MIN = "sun_on_min"
SUN_OFF_MIN = "sun_off_min"

AUTO_BITFIELD = "auto_bitfield"
GLOBAL_AUTO = "global_auto"
SUN_AUTO = "sun"
MON_AUTO = "mon"
TUE_AUTO = "tue"
WED_AUTO = "wed"
THU_AUTO = "thu"
FRI_AUTO = "fri"
SAT_AUTO = "sat"

AUTO_DAYS = [MON_AUTO, TUE_AUTO, WED_AUTO, THU_AUTO, FRI_AUTO, SAT_AUTO, SUN_AUTO]

SECOND = "second"
MINUTE = "minute"
HOUR = "hour"
DAYOFWEEK = "dayofweek"
DAY = "day"
MONTH = "month"
YEAR = "month"

FLOW_KEY = "flow_key"
FLOW_RATE = "flow_rate"
FLOW_PULSES = "flow_pulses"
FLOW_SECONDS = "flow_seconds"

WRITE_RESULT = "write_result"
MACHINE_SER_NUM = "machine_ser_num"

"""Data Types"""
TYPE_MAIN = 1
TYPE_PREBREW = 2
TYPE_AUTO_ON_OFF = 3
TYPE_COFFEE_TEMP = 4
TYPE_STEAM_TEMP = 5
TYPE_DRINK_STATS = 6

DIVIDE_KEYS = ["temp", "prebrewing_to"]
SERIAL_NUMBERS = [MACHINE_SER_NUM, MODULE_SER_NUM]

# Response Maps
class Elem:

    INT = 0
    STRING = 1

    def __init__(self, index, size=1, type=INT):
        self._index = index
        self._size = size
        self._type = type

    @property
    def index(self):
        return self._index

    @property
    def size(self):
        return self._size

    @property
    def type(self):
        return self._type


# R
# 40 1C 00 04: Message
# 03 BC: Coffee Temp (95.6C)
# 04 D8: Steam Temp (124.0C)
# B6: Check byte

TEMP_REPORT_MAP = {Elem(0, 2): TEMP_COFFEE, Elem(2, 2): TEMP_STEAM}

# R
# 40 00 00 20: Message
# 01
# 78: Version (1.20)
# 02
# 53 6E XX XX XX XX XX XX XX XX XX XX: Module serial number (SnXXXXXXXXXX)
# 00: ?? sometimes 01
# 00 00 00 00 00 00 00
# 27: 01: Power (ON)
# 01 00 00 00
# 32: 02 96: Coffee Temp (66.2C)
# 34: 03 2A: Steam Temp (81.0C)
# 70: Check byte

STATUS_MAP = {
    Elem(1): FIRMWARE_VER,
    Elem(3, 12, type=Elem.STRING): MODULE_SER_NUM,
    Elem(15): POWER_MYSTERY,
    Elem(17): KEY_ACTIVE,
    Elem(19, 2): CURRENT_PULSE_COUNT,
    # Elem(23): POWER,
    Elem(27): HEATING_STATE,
    # Elem(28, 2): TEMP_COFFEE,
    # Elem(30, 2): TEMP_STEAM,
}

HEATING_VALUES = {
    HEATING_ON: 0x10,
    COFFEE_HEATER_ON: 0x20,
    STEAM_HEATER_ON: 0x40,
    PUMP_ON: 0x01,
    BREW_SOLENOID_ON: 0x02,
    BOILER_FILL_SOLENOID_ON: 0x04,  # ??
    HOT_WATER_SOLENOID_ON: 0x08,
}

# R
# 00 00 00 1F: Preamble
# 01 00 00 02 6E 31 39
# 11: 03 C7: Coffee Temp Set (96.7C)
# 13: 04 D9: Steam Temp Set (124.1C)
# 15: 00: Prebrewing ON (off)
# 16: 00: B1 Prebrewing ON
# 17: 00: B2 Prebrewing ON
# 18: 00: B3 Prebrewing ON
# 19: 0A: B4 Prebrewing ON (1.0s)
# 20: 00: B1 Prebrewing Off
# 21: 00: B2 Prebrewing Off
# 22: 00: B3 Prebrewing Off
# 23: 00: B4 Prebrewing Off
# 24: 0078: Dose B1
# 26: 0076: Dost B2
# 28: 0078: Dose B3
# 30: 0085: Dose B4
# 32: 03E8: Dose B5
# 34: 08: Seconds hot water
# 35: Check byte

CONFIG_MAP = {
    Elem(0): POWER,
    Elem(7, 2): TSET_COFFEE,
    Elem(9, 2): TSET_STEAM,
    Elem(11): ENABLE_PREBREWING,
    Elem(12): PREBREWING_TON_K1,
    Elem(13): PREBREWING_TON_K2,
    Elem(14): PREBREWING_TON_K3,
    Elem(15): PREBREWING_TON_K4,
    Elem(16): PREBREWING_TOFF_K1,
    Elem(17): PREBREWING_TOFF_K2,
    Elem(18): PREBREWING_TOFF_K3,
    Elem(19): PREBREWING_TOFF_K4,
    Elem(20, 2): DOSE_K1,
    Elem(22, 2): DOSE_K2,
    Elem(24, 2): DOSE_K3,
    Elem(26, 2): DOSE_K4,
    Elem(28, 2): DOSE_K5,
    Elem(30): DOSE_HOT_WATER,
}

# Response to R 03 10 00 1D EB

# R
# 03 10 00 1D: Message
# 4: FE: Bitfield for auto on/off, where upper bits are the days bit 0 is auto on/off (disabled)
# 5: 06: Sunday on hour
# 6: 11: Sunday off hour (5pm)
# 7: 06: Monday on hour
# 8: 11: Monday off hour (5pm)
# 9: 06: Tuesday on hour
# 10: 11: Tuesday off hour (5pm)
# 11: 06: Wednesday on hour
# 12: 11: Wednesday off hour (5pm)
# 13: 06: Thursday on hour
# 14: 11: Thursday off hour (5pm)
# 15: 06: Friday on hour
# 16: 11: Friday off hour (5pm)
# 17: 06: Saturday on hour
# 18: 11: Saturday off hour (5pm)
# 00 00 00 00 00 00 00 00 00 00 00 00 00 00
# 2E: Check byte

AUTO_SCHED_MAP = {
    Elem(0): AUTO_BITFIELD,
    Elem(1): MON_ON_HOUR,
    Elem(2): MON_OFF_HOUR,
    Elem(3): TUE_ON_HOUR,
    Elem(4): TUE_OFF_HOUR,
    Elem(5): WED_ON_HOUR,
    Elem(6): WED_OFF_HOUR,
    Elem(7): THU_ON_HOUR,
    Elem(8): THU_OFF_HOUR,
    Elem(9): FRI_ON_HOUR,
    Elem(10): FRI_OFF_HOUR,
    Elem(11): SAT_ON_HOUR,
    Elem(12): SAT_OFF_HOUR,
    Elem(13): SUN_ON_HOUR,
    Elem(14): SUN_OFF_HOUR,
    Elem(15): MON_ON_MIN,
    Elem(16): MON_OFF_MIN,
    Elem(17): TUE_ON_MIN,
    Elem(18): TUE_OFF_MIN,
    Elem(19): WED_ON_MIN,
    Elem(20): WED_OFF_MIN,
    Elem(21): THU_ON_MIN,
    Elem(22): THU_OFF_MIN,
    Elem(23): FRI_ON_MIN,
    Elem(24): FRI_OFF_MIN,
    Elem(25): SAT_ON_MIN,
    Elem(26): SAT_OFF_MIN,
    Elem(27): SUN_ON_MIN,
    Elem(28): SUN_OFF_MIN,
}

AUTO_ENABLE_MAP = {
    Elem(0): AUTO_BITFIELD,
}

AUTO_BITFIELD_MAP = {
    0: GLOBAL_AUTO,
    1: MON_AUTO,
    2: TUE_AUTO,
    3: WED_AUTO,
    4: THU_AUTO,
    5: FRI_AUTO,
    6: SAT_AUTO,
    7: SUN_AUTO,
}

# W: Write
# 00 00 00 01 : Message
# OK: Result
# 72: Check byte

# WRITE_RESULT_MAP = {
#     Elem(0, 1, type=Elem.STRING): WRITE_RESULT,
# }

# App: R 01 00 00 11 D5
# Machine:
# R
# 01 00 00 11: Read machine serial number
# 5A: Z (?)
# XX XX XX XX XX XX XX XX 00 00 00 00 00 00 00 00: Machine serial number
# 7D: Check byte

SER_NUM_MAP = {
    Elem(1, 16, type=Elem.STRING): MACHINE_SER_NUM,
}

# R
# 03000007
# 00: Second (00)
# 05: Minute (5)
# 0A: Hour (10)
# 02: Day of week (2)
# 16: Day (22)
# 0C: Month (12)
# 14: Year (20)
# B3: Check byte

DATETIME_MAP = {
    Elem(0): SECOND,
    Elem(1): MINUTE,
    Elem(2): HOUR,
    Elem(3): DAYOFWEEK,
    Elem(4): DAY,
    Elem(5): MONTH,
    Elem(6): YEAR,
}

# R
# 0020002C
# 0000014A: Key 1 (1 espresso) Completed Drinks
# 00000096: Key 2 (2 espressos) Completed Drinks
# 000001B0: Key 3 (1 coffee) Completed Drinks
# 00000021: Key 4 (2 coffees) Completed Drinks
# 00000563: Continuous Completed Drinks
# 00000914: Total Completed Coffee Drinks (total of above)
# 00000010: Hot water activations
# 0000000A: Increments every so often (?)
# 00000ADE: Total Coffee Drink Activations
# 00000010: Hot water activations
# 00000032: Completed Hot Water

DRINK_STATS_MAP = {
    Elem(0, 4): DRINKS_K1,
    Elem(4, 4): DRINKS_K2,
    Elem(8, 4): DRINKS_K3,
    Elem(12, 4): DRINKS_K4,
    Elem(16, 4): CONTINUOUS,
    Elem(20, 4): TOTAL_COFFEE,
    Elem(24, 4): HOT_WATER,
    Elem(28, 4): DRINK_MYSTERY,
    Elem(32, 4): TOTAL_COFFEE_ACTIVATIONS,
    Elem(36, 4): HOT_WATER_2,
    Elem(40, 4): DRINKS_HOT_WATER,
    Elem(CALCULATED_VALUE): TOTAL_FLUSHING,
}

GATEWAY_DRINK_MAP = {
    -1: FLUSHING_OFFSET,
    0: DRINKS_K1_OFFSET,
    1: DRINKS_K2_OFFSET,
    2: DRINKS_K3_OFFSET,
    3: DRINKS_K4_OFFSET,
    4: CONTINUOUS_OFFSET,
}

DRINK_OFFSET_MAP = {
    TOTAL_FLUSHING: FLUSHING_OFFSET,
    DRINKS_K1: DRINKS_K1_OFFSET,
    DRINKS_K2: DRINKS_K2_OFFSET,
    DRINKS_K3: DRINKS_K3_OFFSET,
    DRINKS_K4: DRINKS_K4_OFFSET,
    CONTINUOUS: CONTINUOUS_OFFSET,
}

# Z
# 60000016
# Snxxxxxxxxxx
# 04: Key
# 01: Rate (1 = high flow rate, 0 = low flow rate) - flips from 1 to 0 as flow slows
# 0009: Seconds (upper 12 bits are whole seconds, lower 4 bits are fractional)
# 000C: Pulses
# 03B6: Coffee boiler temp
# 04D4: Steam boiler temp
# DC: Check byte

WATER_FLOW_MAP = {
    Elem(12): FLOW_KEY,
    Elem(13): FLOW_RATE,
    Elem(14, 2): FLOW_SECONDS,
    Elem(16, 2): FLOW_PULSES,
    # Elem(18, 2): TEMP_COFFEE,
    # Elem(20, 2): TEMP_STEAM,
}

# R
# 00500018 - Message
# 000001FE - Coffee heating element minutes on
# 00000189 - Steam heating element minutes on
# 00009772 - Number of seconds that the machine has been running, either coffee or hot water
# 00001CA9 - Total hours of on-time
# 00009500 - Number of seconds that the pump has been running
# 00000075 - Number of seconds that hot water has been dispensed

USAGE_MAP = {
    Elem(0, 4): COFFEE_HEATING_ELEMENT_HOURS,
    Elem(4, 4): STEAM_HEATING_ELEMENT_HOURS,
    Elem(8, 4): MACHINE_RUNNING_SECONDS,
    Elem(12, 4): DAYS_SINCE_BUILT,
    Elem(16, 4): PUMP_ON_SECONDS,
    Elem(20, 4): WATER_ON_SECONDS,
}

# 3230322E39DF46: 202.9°F
# 20: Space
# DBDB: Boiler states
# 30393A32386100: 09:28a
# 42555A5A2020202020202020: BUZZ
# 543A3037: T:07


FRONT_DISPLAY_MAP = {
    Elem(0, 33, Elem.STRING): FRONT_PANEL_DISPLAY,
}

# 03
# E7
# 02
# D8
# 04
# F8
# 09
# 5B
# 02
# C2
# 03
# 04
# 08
# 9E
# 02
# 49
# 00
# F5

MYSTERY_MAP = {
    Elem(0): VAL_1,
    Elem(1): VAL_2,
    Elem(2): VAL_3,
    Elem(3): VAL_4,
    Elem(4): VAL_5,
    Elem(5): VAL_6,
    Elem(6): VAL_7,
    Elem(7): VAL_8,
    Elem(8): VAL_9,
    Elem(9): VAL_10,
    Elem(10): VAL_11,
    Elem(11): VAL_12,
    Elem(12): VAL_13,
    Elem(13): VAL_14,
    Elem(14): VAL_15,
    Elem(15): VAL_16,
    Elem(16): VAL_17,
    Elem(17): VAL_18,
}


class Msg:
    GET_STATUS = 0
    GET_CONFIG = 1
    GET_AUTO_SCHED = 2
    SET_POWER = 3
    GET_TEMP_REPORT = 4
    GET_AUTO_ENABLE = 4
    SET_AUTO_ENABLE = 5
    GET_SER_NUM = 6
    GET_DATETIME = 7
    SET_COFFEE_TEMP = 8
    SET_STEAM_TEMP = 9
    SET_PREBREWING_ENABLE = 10
    SET_AUTO_SCHED = 11
    SET_DOSE = 12
    SET_DOSE_HOT_WATER = 13
    SET_PREBREW_TIMES = 14
    GET_DRINK_STATS = 15
    GET_WATER_FLOW = 16
    GET_USAGE_STATS = 17
    GET_FRONT_DISPLAY = 18
    GET_MYSTERY = 19

    """Auto on/off address starts at 0x11 for Monday and increments by 4 thereafter."""
    AUTO_ON_OFF_HOUR_BASE = 0x11
    AUTO_ON_OFF_MIN_BASE = 0x20

    """Dose address starts at 0x14 for the first key and increments by 2 thereafter."""
    DOSE_KEY_BASE = 0x14

    """Prebrew on address base."""
    PREBREW_ON_BASE = 0x0C

    """Prebrew off address base."""
    PREBREW_OFF_BASE = 0x10

    READ = "R"
    WRITE = "W"
    STREAM = "Z"

    RESPONSE_GOOD = "OK"

    def __init__(self, msg_type, msg, map):
        """Init command"""
        self._msg_type = msg_type
        self._msg = msg
        self._map = map

    @property
    def msg_type(self):
        """Command type"""
        return self._msg_type

    @property
    def msg(self):
        """Command type"""
        return self._msg

    @property
    def map(self):
        """Return map if we should decode, None if not"""
        return self._map


MSGS = {
    # Reads
    Msg.GET_STATUS: Msg(Msg.READ, "40000020", STATUS_MAP),
    Msg.GET_CONFIG: Msg(Msg.READ, "0000001F", CONFIG_MAP),
    Msg.GET_AUTO_SCHED: Msg(Msg.READ, "0310001D", AUTO_SCHED_MAP),
    Msg.GET_AUTO_ENABLE: Msg(Msg.READ, "03100001", AUTO_ENABLE_MAP),
    Msg.GET_TEMP_REPORT: Msg(Msg.READ, "401C0004", TEMP_REPORT_MAP),
    Msg.GET_SER_NUM: Msg(Msg.READ, "01000011", SER_NUM_MAP),
    Msg.GET_DATETIME: Msg(Msg.READ, "03000007", DATETIME_MAP),
    Msg.GET_DRINK_STATS: Msg(Msg.READ, "0020002C", DRINK_STATS_MAP),
    Msg.GET_WATER_FLOW: Msg(Msg.STREAM, "60000016", WATER_FLOW_MAP),
    Msg.GET_USAGE_STATS: Msg(Msg.READ, "00500018", USAGE_MAP),
    Msg.GET_FRONT_DISPLAY: Msg(Msg.READ, "60ED0021", FRONT_DISPLAY_MAP),
    Msg.GET_MYSTERY: Msg(Msg.READ, "60DA0012", MYSTERY_MAP),
    # Writes
    Msg.SET_POWER: Msg(Msg.WRITE, "00000001", None),
    Msg.SET_COFFEE_TEMP: Msg(Msg.WRITE, "00070002", None),
    Msg.SET_STEAM_TEMP: Msg(Msg.WRITE, "00090002", None),
    Msg.SET_PREBREWING_ENABLE: Msg(Msg.WRITE, "000B0001", None),
    Msg.SET_AUTO_SCHED: Msg(Msg.WRITE, "03100002", None),
    Msg.SET_AUTO_ENABLE: Msg(Msg.WRITE, "03100001", None),
    # Write config for keys (second byte is base + the key number and will be replaced)
    Msg.SET_DOSE: Msg(Msg.WRITE, "00140002", None),
    Msg.SET_DOSE_HOT_WATER: Msg(Msg.WRITE, "001E0001", None),
    Msg.SET_PREBREW_TIMES: Msg(Msg.WRITE, "000C0001", None),
}

# 0000:001f - Config
# 0020:004C - Drink Stats
# 0050:0068 - Usage Stats
# 0070:00AF - Unused (FF)
# 00B0:00BB - Module Serial Number
# 00C0:00CB - Module Serial Number
# 00D0:00DF - Machine Name
# 00E0:00FF - Unused (00)
# 0100:010F - Machine Serial Number
# 0110:011F -
