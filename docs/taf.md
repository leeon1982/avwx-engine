# TAF

A TAF (Terminal Aerodrome Forecast) is a 24-hour weather forecast for the area 5 statute miles from the reporting station. They are update once every three or six hours or when significant changes warrent an update, and the observations are valid for six hours or until the next report is issued

## class avwx.**Taf**(*station_ident: str*)

The Taf class offers an object-oriented approach to managing TAF data for a single station.

```python
>>> from avwx import Taf
>>> kjfk = Taf('KJFK')
>>> kjfk.station_info.name
'John F Kennedy International Airport'
>>> kjfk.update()
True
>>> kjfk.last_updated
datetime.datetime(2018, 3, 4, 23, 43, 26, 209644)
>>> kjfk.raw
'KJFK 042030Z 0421/0524 33016G27KT P6SM BKN045 FM051600 36016G22KT P6SM BKN040 FM052100 35013KT P6SM SCT035'
>>> len(kjfk.data.forecast)
3
>>> kjfk.data.forecast[0].flight_rules
'VFR'
>>> kjfk.translations.forecast[0].wind
'NNW-330 at 16kt gusting to 27kt'
>>> kjfk.speech
'Starting on March 4th - From 21 to 16 zulu, Winds three three zero at 16kt gusting to 27kt. Visibility greater than six miles. Broken layer at 4500ft. From 16 to 21 zulu, Winds three sixzero at 16kt gusting to 22kt. Visibility greater than six miles. Broken layer at 4000ft. From 21 to midnight zulu, Winds three five zero at 13kt. Visibility greater than six miles. Scattered clouds at 3500ft'
```

The update function can also accept a given report string if you want to override to normal fetching process.

```python
>>> from avwx import Taf
>>> zyhb = Taf('ZYHB')
>>> zyhb.station_info.city
'Hulan'
>>> report = "TAF ZYHB 082300Z 0823/0911 VRB03KT 9999 SCT018 BKN120 TX14/0907Z TN04/0921Z FM090100 09015KT 9999 -SHRA WS020/13045KT SCT018 BKN120 BECMG 0904/0906 34008KT PROB30 TEMPO 0906/0911 7000 -RA SCT020 650104 530804 RMK FCST BASED ON AUTO OBS. NXT FCST BY 090600Z"
>>> zyhb.update(report)
True
>>> zyhb.data.remarks
'RMK FCST BASED ON AUTO OBS. NXT FCST BY 090600Z'
>>> zyhb.summary[-1]
'Vis 7km, Light Rain, Scattered clouds at 2000ft, Frequent moderate turbulence in clear air from 8000ft to 12000ft, Moderate icing in clouds from 1000ft to 5000ft'
```

### **async_update**() -> *bool*

Async version of `update`

### **data**: *avwx.structs.TafData* = *None*

TafData dataclass of parsed data values and units. Parsed on update()

### **from_report**(*report: str*) -> *avwx.Taf*

Returns an updated report object based on an existing report

### **last_updated**: *datetime.datetime* = *None*

UTC Datetime object when the report was last updated

### **raw**: *str* = *None*

The unparsed report string. Fetched on update()

### **service**: *avwx.service.Service*

Service object used to fetch the report string

### **speech**: *str*

Report summary designed to be read by a text-to-speech program

### **station**: *str*

4-character ICAO station ident code the report was initialized with

### **station_info**: *avwx.Station*

Provides basic station info. Raises a BadStation exception if the station's info cannot be found

### **summary**: *[str]*

Condensed report summaries created from translations

### **translations**: *avwx.structs.TafTrans*

TafTrans dataclass of translation strings from data. Parsed on update()

### **units**: *avwx.structs.Units*

Units inferred from the station location and report contents

### **update**(*report: str = None*) -> *bool*

Updates `raw`, `data`, and `translations` by fetching and parsing the report

Can accept a report string to parse instead

Returns `True` if a new report is available, else `False`

## Taf Module

If you don't need or want the object-oriented handling provided by the Taf class, you can use the core TAF functions directly.

### avwx.taf.**parse**(*station: str, report: str*) -> (*avwx.structs.TafData, avwx.structs.Units*)

Returns TafData and Units dataclasses with parsed data and their associated units

<!-- ### avwx.taf.**parse_lines**(*lines: [str], units: avwx.structs.Units, use_na: bool = True*) -> *[dict]*

Returns a list of parsed line dictionaries -->
