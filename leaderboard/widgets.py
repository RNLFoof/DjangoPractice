from datetime import date, timedelta

from django.forms import MultiWidget, NumberInput


class DurationSelectorWidget(MultiWidget):
    def __init__(self, attrs=None):
        at = {"style": "width: 42px","value": 0, "min": 0}
        _widgets = (
            NumberInput(attrs=at),
            NumberInput(attrs=at),
            NumberInput(attrs=at),
            NumberInput(attrs=at)
        )
        super(DurationSelectorWidget, self).__init__(_widgets, attrs)

    def decompress(self, value):
        if value:
            if " " not in value:
                d, x = 0, value
            else:
                d, x = value.split(" ")
            print(x)
            print(x.split(":"))
            h, m, s = tuple(x.split(":"))
            return [int(h), int(d), int(m), int(s)]
            # return [value.days, value.seconds // 3600, value.seconds % 3600 // 60, value.seconds % 60]
        return [0, 0, 0, 0]

    def value_from_datadict(self, data, files, name):
        l = []
        for x in range(0,4):
            l.append(self.widgets[0].value_from_datadict(data, files, f"{name}_{x}"))

        # 0, a falsey value, is an actual correct response. so. although an int shouldn't be in here anyway
        print(l)
        return timedelta(
            days=0 if l[0] in [None,""] else int(l[0]),
            hours=0 if l[1] in [None,""] else int(l[1]),
            minutes=0 if l[2] in [None,""] else int(l[2]),
            seconds=0 if l[3] in [None,""] else int(l[3])
        )

    def render(self, name, value, attrs=None, renderer=None):
        s = ""
        value = value or [0, 0, 0, 0]
        for n,w in enumerate(self.widgets):
            wname = f"{name}_{n}"
            wvalue = value[n]
            id = self.get_context(name,value,attrs)["widget"]["attrs"]["id"]
            w.attrs["id"] = f"{id}_{n}" # Give the subwidgets their own IDs because at first they don't have any
            s+=f'<label for="{w.attrs["id"]}">{"DHMS"[n]}</label>' + w.render(wname,wvalue)
        return s