
from collections import OrderedDict

from .helper.caller_assignment import caller_assignment_name


class Template(object):

    def __init__(self, description):
        self.description = description

        self.parameters = OrderedDict()
        self.resources = OrderedDict()

    def add(self, what, **properties):
        # self.resources[]
        # Get name from assignment

        name = caller_assignment_name()
        print("Add({})".format(name))
