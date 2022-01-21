from django.template.defaulttags import register

@register.inclusion_tag("app/components/test.html")
def test_component(echo):
    return {
        "echo": echo
    }

@register.inclusion_tag("app/components/login_button.html")
def login_button():
    return {}

@register.inclusion_tag("app/components/logout_button.html")
def logout_button():
    return {}

@register.inclusion_tag("app/components/schedule_card.html")
def schedule_card(schedule):
    return {
        "schedule": schedule 
    }   

@register.inclusion_tag("app/components/timeslot_card.html")
def timeslot_card(date, timeslots):
    return {
        "date": date,
        "timeslots": timeslots
    }   