import attr
from .resource import 


@attr.s
class NetworkResource(InfoResource):
    target = attr.ib()
    addresses = attr.ib(default={},
                        validator=attr.validators.instance_of(dict))

    def __attrs_post_init__(self):
        pass

    def get_if_addr(self, adr):
        """Returns the address for the specified interface"""
        return self.addresses[adr] #pylint: disable=unsubscriptable-object
