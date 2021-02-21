
def get_by_pk_or_pass(model_name,pk):
    data = model_name.objects.filter(pk=pk)
    if data != None and data.count() < 2:
        return data
    return None    

def get_by_slug_or_pass(model_name,slug):
    data = model_name.objects.filter(slug=slug)
    if data != None and data.count() < 2:
        return data
    return None 