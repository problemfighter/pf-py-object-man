import inspect


class CopyObject:

    def get_all_fields(self, klass_object):
        klass_props = []
        if klass_object:
            for props in inspect.getmembers(klass_object):
                pass
        return klass_props

    def copy(self, source, destination):
        self.get_all_fields(destination)
        pass