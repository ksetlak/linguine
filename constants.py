import locale

help_text = """
This utility converts .json files containing l18n dictionaries to spreadsheets convenient for editing and the other
way around.

The idea is to allow non-technical people to collaborate on translations without the need for them to install any
additional software and work with what they have. 

Find out more: <link>
"""  # TODO: Add a link to the README.md once it's hosted.

locale_list = [f(loc) for loc in locale.windows_locale.items() for f in (
    lambda x: x[1],
    lambda x: x[1].split("_")[0]
)]
locale_list = list(set(locale_list))
locale_list.sort()

spreadsheet_mimetypes = [
    'application/vnd.ms-excel',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    # 'application/vnd.oasis.opendocument.spreadsheet'  # TODO: Implement!
]