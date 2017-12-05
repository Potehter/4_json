# Prettify JSON

Code prettifies JSON file. File has to be on local disk, output in console

# Quickstart

Filepath - is a argument in python execution command

Example of script launch on Linux, Python 3.5:

```bash

$ python pprint_json.py <path to file>

output example
{
    "features": [
        {
            "geometry": {
                "coordinates": [
                    37.39703804817934,
                    55.740999719549094
                ],
                "type": "Point"
            },
            "properties": {
                "Attributes": {
                    "Address": "улица Академика Павлова, дом 10",
                    "AdmArea": "Западный административный округ",
                    "ClarificationOfWorkingHours": null,
                    "District": "район Кунцево",
                    "IsNetObject": "да",
                    "Name": "Ароматный Мир",
                    "OperatingCompany": "Ароматный Мир",
                    "PublicPhone": [
                        {
                            "PublicPhone": "(495) 777-51-95"
                        }
                    ],
                    "TypeService": "реализация продовольственных товаров",
                    "WorkingHours": [
                        {
                            "DayOfWeek": "понедельник",
                            "Hours": "09:30-22:30"
                        },
                        {
                            "DayOfWeek": "вторник",
                            "Hours": "09:30-22:30"
                        },
                        {
                            "DayOfWeek": "среда",
                            "Hours": "09:30-22:30"
                        },
                        {
                            "DayOfWeek": "четверг",
                            "Hours": "09:30-22:30"
                        },
                        {
                            "DayOfWeek": "пятница",
                            "Hours": "09:30-22:30"
                        },
                        {
                            "DayOfWeek": "суббота",
                            "Hours": "09:30-22:30"
                        },
                        {
                            "DayOfWeek": "воскресенье",
                            "Hours": "09:30-22:30"
                        }
                    ],
                    "global_id": 14371450
                },
                "DatasetId": 1854,
                "ReleaseNumber": 2,
                "RowId": "79742784-9ef3-4543-bc98-a219a8903c18",
                "VersionNumber": 1
            },
            "type": "Feature"
        },
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
