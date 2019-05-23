from django.core.serializers import serialize
import json
class SerializeMixin(object):
    def serialize(self,qs):
        json_data=serialize('json',qs)
        python_data=json.loads(json_data)
        final_list=[]
        for obj in python_data:
            item=obj['fields']
            final_list.append(item)
        json_data=json.dumps(final_list)
        return json_data
