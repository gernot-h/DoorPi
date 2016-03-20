# -*- coding: utf-8 -*-

from main import DOORPI

DOCUMENTATION = dict(
    text_description=_("%s text_description" % __name__),
    actions=[],
    events=[],
    configuration=[
        dict(json_path='/resources/event_handler/event_log/type', type='string', default='sqllite', mandatory=False,
             description=_('%s configuration event_log type description' % __name__)),
        dict(json_path='/resources/event_handler/event_log/connection_string', type='string', mandatory=False,
             default='!BASE_PATH!/conf/event_log.db',
             description=_('%s configuration event_log connection_string description' % __name__)),
    ],
    libraries=dict(
        threading=DOORPI.libraries['threading'].copy(),
        inspect=DOORPI.libraries['inspect'].copy(),
        sqlite3=dict(
            mandatory=True,
            text_warning=_("library sqlite3 text_warning"),
            text_description=_("library sqlite3 text_description"),
            text_installation=_("library sqlite3 text_description"),
            auto_install=dict(standard=True),
            text_test=_("library global text_test pre") +
                      _("<code> import sqlite3</code>") +
                      _("library global text_test post"),
            text_configuration=_("library sqlite3 text_configuration"),
            configuration=[],
            text_links={
                _("docs.python.org"): _("library sqlite3 text_links %s" % DOORPI.CONST.USED_PYTHON_VERSION)
            }
        )
    ),
    test=[]
)

DOCUMENTATION["test"].append(DOCUMENTATION["libraries"].keys())
extended_base_events = DOORPI.CONST.HANDLER_BASE_EVENTS[:]
event_parameters = []
for single_parameter in ['year', 'month', 'day', 'hour', 'minute', 'second']:
    event_parameters.append(dict(
        name=single_parameter,
        type="int",
        description=_("current value for %s" % single_parameter)
    ))

for single_event in DOORPI.CONST.HANDLER_BASE_EVENTS:
    extended_base_events.append("%sEvenNumber" % single_event)
    extended_base_events.append("%sUnevenNumber" % single_event)

for single_event in extended_base_events + ["OnTimeTick"]:
    DOCUMENTATION["events"].append(dict(
        name=single_event,
        description=_("%s event description %s" % (__name__, single_event)),
        parameter=event_parameters
    ))

for single_minute in DOORPI.CONST.MINUTE_RANGE:
    DOCUMENTATION["events"].append(dict(
        name="OnTimeMinute%s" % single_minute,
        description=_("%s event description OnTimeMinute%s" % (__name__, single_minute)),
        parameter=event_parameters
    ))
for single_hour in DOORPI.CONST.HOUR_RANGE:
    DOCUMENTATION["events"].append(dict(
        name="OnTimeHour%s" % single_hour,
        description=_("%s event description OnTimeHour%s" % (__name__, single_hour)),
        parameter=event_parameters
    ))