from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class OrderField(models.PositiveIntegerField):
    def __init__(self, for_fields=None, *args, **kwargs):
        self.for_fields = for_fields
        super().__init__(*args, **kwargs)
    
    def pre_save(self, model_instance, add):
        print(f"Model instance is here: {model_instance}")
        if getattr(model_instance, self.attname) is None:
            # no current value
            try:
                qs = self.model.objects.all()
                if self.for_fields:
                    # filter by objects with the same field values
                    # for the fields in for_fields
                    query = {field: getattr(model_instance, field) for field in self.for_fields}
                    print(f"This is query: {query}")
                    qs = qs.filter(**query)
                    print(f"It's qs here: {qs}")
                # get the order of the last item
                last_item = qs.latest(self.attname)
                print(f"This is last item: {last_item}")
                value = last_item.order + 1
                print(f"This is value: {value}")
            except ObjectDoesNotExist:
                value = 0
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super().pre_save(model_instance, add)