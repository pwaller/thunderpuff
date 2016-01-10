#! /usr/bin/env python3

from __future__ import print_function

import json
import sys


from collections import OrderedDict


def is_tags(what):
    if not isinstance(what, list) or len(what) == 0:
        return False

    first = what[0]
    if not isinstance(first, dict):
        return False

    if "Key" in first and "Value" in first:
        if len(first) == 2:
            return True
        if len(first) == 3 and "PropagateAtLaunch" in first:
            return True

    return False


def tag_call(items):
    class State:
        has_propagate = False

    def assign(item):
        if "PropagateAtLaunch" in item:
            State.has_propagate = True
        return "{}={}".format(item["Key"], prettify(item["Value"]))
    tags = ", ".join(assign(item) for item in items)
    propagate = ""
    if State.has_propagate:
        propagate = ",\n    PropagateAtLaunch=True"
    return "Tags({}{})".format(tags, propagate)


def prettify(what):
    if isinstance(what, dict):
        if "Ref" in what:
            # {"Ref": "Foo"} -> "Foo", i.e, a ref just goes to its name.
            return what["Ref"]
        if "Fn::Join" in what:
            return "join()"
        middle = ", ".join('"{}": {}'.format(k, prettify(v)) for k, v in what.items())
        return "{" + middle + "}"

    if isinstance(what, list):
        if is_tags(what):
            return tag_call(what)
        middle = ",\n    ".join(prettify(x) for x in what)
        return "[" + middle + "]"

    return repr(what)


def process(template):
    # template['Description']
    # template['Parameters']
    # template['Conditions']

    for name, resource in template['Resources'].items():

        properties = ""
        if "Properties" in resource:
            spacing = ",\n    "
            properties = spacing
            properties += spacing.join(
                "{}={}".format(name, prettify(value))
                for name, value in resource["Properties"].items())

        print("""{name} = t.add(\n    "{type}"{properties})""".format(
            name=name,
            type=resource["Type"],
            properties=properties,
        ))

        print()

    # template['Outputs']


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    for arg in args:
        with open(arg) as fd:
            process(json.load(fd, object_pairs_hook=OrderedDict))

if __name__ == "__main__":
    raise SystemExit(main())
